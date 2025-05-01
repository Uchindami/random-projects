package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/briandowns/spinner"
	"github.com/chromedp/cdproto/cdp"
	"github.com/chromedp/chromedp"
	"github.com/sirupsen/logrus"
)

type JobListing struct {
	Source             string `json:"source"`
	Link               string `json:"link"`
	CompanyLogo        string `json:"company_logo"`
	Position           string `json:"position"`
	CompanyName        string `json:"company_name"`
	Location           string `json:"location"`
	JobType            string `json:"job_type"`
	DatePosted         string `json:"date_posted"`
	ApplicationDeadline string `json:"application_deadline"`
}

type SiteConfig struct {
	Name         string
	URL          string
	ListSelector string
	Selectors    map[string]string
	LoadStrategy string
	Button       string
	MaxAttempts  int
}

var (
	log = logrus.New()
	sites = []SiteConfig{
		{
			Name:         "careersmw",
			URL:          "https://careersmw.com/",
			ListSelector: "li",
			Selectors: map[string]string{
				"link":         "a",
				"company_logo": ".company_logo",
				"position":     ".position",
				"company":      ".company",
				"location":     ".location",
				"job_type":     ".job-type",
				"date":         "time",
				"deadline":     ".application-deadline",
			},
			LoadStrategy: "full-scroll",
		},
		{
			Name:         "ntchito",
			URL:          "https://ntchito.com/jobs-in-malawi/",
			ListSelector: "article",
			Selectors: map[string]string{
				"link":         "a",
				"company_logo": ".company_logo",
				"position":     ".entry-title",
				"company":      ".company-name",
				"location":     ".google_map_link",
				"job_type":     ".job-type",
				"date":         ".date time",
				"deadline":     ".application-deadline",
			},
			LoadStrategy: "partial-scroll",
		},
		{
			Name:         "jobsearchmalawi",
			URL:          "https://jobsearchmalawi.com/",
			ListSelector: "li",
			Selectors: map[string]string{
				"link":         "a",
				"company_logo": ".company_logo",
				"position":     ".position",
				"company":      ".company",
				"location":     ".location",
				"job_type":     ".job-type",
				"date":         "time",
				"deadline":     ".application-deadline",
			},
			LoadStrategy: "load-more",
			Button:       "a.load_more_jobs",
			MaxAttempts:  2,
		},
	}
)

func init() {
	log.SetFormatter(&logrus.TextFormatter{
		FullTimestamp:   true,
		TimestampFormat: "2006-01-02 15:04:05",
	})
}

func main() {
	ctx, cancel := chromedp.NewContext(context.Background())
	defer cancel()

	combinedResults := make(map[string][]JobListing)

	for _, site := range sites {
		s := spinner.New(spinner.CharSets[14], 100*time.Millisecond)
		s.Prefix = fmt.Sprintf("Scraping %s ", site.Name)
		s.Start()

		log.WithField("site", site.Name).Info("Starting scrape")
		
		listings, err := scrapeSite(ctx, site)
		if err != nil {
			s.Stop()
			log.WithError(err).Errorf("Failed to scrape %s", site.Name)
			continue
		}

		s.Stop()
		log.WithField("count", len(listings)).Infof("Completed %s scrape", site.Name)
		combinedResults[site.Name] = listings
	}

	filename := fmt.Sprintf("jobs_%s.json", time.Now().Format("20060102_150405"))
	if err := saveResults(combinedResults, filename); err != nil {
		log.WithError(err).Error("Failed to save results")
		return
	}

	log.WithField("filename", filename).Info("Saved combined results")
}

func scrapeSite(ctx context.Context, config SiteConfig) ([]JobListing, error) {
	var listings []JobListing
	var nodes []*cdp.Node

	err := chromedp.Run(ctx,
		chromedp.Navigate(config.URL),
		chromedp.WaitReady(config.ListSelector, chromedp.ByQuery),
		loadContentStrategy(config),
		chromedp.Nodes(config.ListSelector, &nodes, chromedp.ByQueryAll),
		chromedp.ActionFunc(func(ctx context.Context) error {
			for _, node := range nodes {
				listing, err := extractListing(ctx, node, config)
				if err == nil && listing.Link != "" {
					listings = append(listings, *listing)
				}
			}
			return nil
		}),
	)

	return listings, err
}

func loadContentStrategy(config SiteConfig) chromedp.Action {
	switch config.LoadStrategy {
	case "full-scroll":
		return fullScroll()
	case "partial-scroll":
		return partialScroll()
	case "load-more":
		return handleLoadMore(config)
	default:
		return nil
	}
}

func fullScroll() chromedp.Action {
	return chromedp.EvaluateAsDevTools(`
		new Promise((resolve) => {
			let lastHeight = document.body.scrollHeight;
			const interval = setInterval(() => {
				window.scrollTo(0, document.body.scrollHeight);
				setTimeout(() => {
					const newHeight = document.body.scrollHeight;
					if (newHeight === lastHeight) {
						clearInterval(interval);
						resolve();
					} else {
						lastHeight = newHeight;
					}
				}, 500);
			}, 500);
		});
	`, nil)
}

func partialScroll() chromedp.Action {
	return chromedp.EvaluateAsDevTools(
		`window.scrollTo(0, document.body.scrollHeight * 0.25);`, 
		nil,
	)
}

func handleLoadMore(config SiteConfig) chromedp.Action {
	return chromedp.ActionFunc(func(ctx context.Context) error {
		attempts := 0
		var prevCount int

		// Get initial count of listings
		if err := chromedp.Run(ctx,
			chromedp.Evaluate(fmt.Sprintf(`document.querySelectorAll('%s').length`, config.ListSelector), &prevCount),
		); err != nil {
			return err
		}

		for attempts < config.MaxAttempts {
			// Attempt to click the "Load More" button
			clickCtx, cancel := context.WithTimeout(ctx, 5*time.Second)
			err := chromedp.Run(clickCtx,
				chromedp.WaitVisible(config.Button, chromedp.ByQuery),
				chromedp.Click(config.Button, chromedp.ByQuery),
			)
			cancel()

			if err != nil {
				// If button not found or click failed, increment attempts
				attempts++
				continue
			}

			// Wait for content to load and scroll
			if err := chromedp.Run(ctx,
				chromedp.Sleep(2*time.Second),
				fullScroll(),
			); err != nil {
				return err
			}

			// Get new count of listings
			var currentCount int
			if err := chromedp.Run(ctx,
				chromedp.Evaluate(fmt.Sprintf(`document.querySelectorAll('%s').length`, config.ListSelector), &currentCount),
			); err != nil {
				return err
			}

			if currentCount > prevCount {
				prevCount = currentCount
				attempts = 0 // Reset attempts as new content was loaded
			} else {
				attempts++
			}
		}

		return nil
	})
}

func extractListing(ctx context.Context, node *cdp.Node, config SiteConfig) (*JobListing, error) {
	listing := &JobListing{Source: config.Name}

	getValue := func(selector, attr string) string {
		var res string
		err := chromedp.Run(ctx,
			chromedp.AttributeValue(selector, attr, &res, nil, chromedp.ByQuery, chromedp.FromNode(node)),
		)
		if err == nil && res != "" {
			return res
		}

		err = chromedp.Run(ctx,
			chromedp.Text(selector, &res, chromedp.ByQuery, chromedp.FromNode(node)),
		)
		if err == nil {
			return res
		}

		return ""
	}

	listing.Link = getValue(config.Selectors["link"], "href")
	listing.CompanyLogo = getValue(config.Selectors["company_logo"], "src")
	listing.Position = getValue(config.Selectors["position"], "")
	listing.CompanyName = getValue(config.Selectors["company"], "")
	listing.Location = getValue(config.Selectors["location"], "")
	listing.JobType = getValue(config.Selectors["job_type"], "")
	listing.DatePosted = getValue(config.Selectors["date"], "datetime")
	listing.ApplicationDeadline = getValue(config.Selectors["deadline"], "")

	if listing.Link == "" || listing.CompanyLogo == "" {
		return nil, fmt.Errorf("invalid listing")
	}

	return listing, nil
}

func saveResults(results interface{}, filename string) error {
	file, err := os.Create(filename)
	if err != nil {
		return err
	}
	defer file.Close()

	encoder := json.NewEncoder(file)
	encoder.SetIndent("", "  ")
	return encoder.Encode(results)
}