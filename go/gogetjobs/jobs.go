package main

import (
	"context"
	"encoding/json"
	"log"
	"os"
	"strings"
	"sync"
	"time"

	"github.com/briandowns/spinner"
	"github.com/chromedp/chromedp"
	"github.com/fatih/color"
)

type Job struct {
	Source              string `json:"source"` // Website source identifier
	Link                string `json:"link"`
	CompanyLogo         string `json:"companyLogo"`
	Position            string `json:"position"`
	CompanyName         string `json:"companyName"`
	Location            string `json:"location"`
	JobType             string `json:"jobType"`
	DatePosted          string `json:"datePosted"`
	ApplicationDeadline string `json:"applicationDeadline"`
	Category            string `json:"category"`
}

type ScrapeConfig struct {
	URL          string
	WaitSelector string
	ScrapeJS     string
	SourceName   string
}

var (
	green  = color.New(color.FgGreen).SprintFunc()
	yellow = color.New(color.FgYellow).SprintFunc()
	red    = color.New(color.FgRed).SprintFunc()
)

var websites = []ScrapeConfig{
	{
		SourceName:   "careersmw",
		URL:          "https://careersmw.com/",
		WaitSelector: ".job_listings",
		ScrapeJS: `
			(async () => {
				await new Promise((resolve) => {
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

				return Array.from(document.querySelectorAll('li')).map((listingElement) => {
					const link = listingElement.querySelector('a')?.href || 'N/A';
					const companyLogo = listingElement.querySelector('.company_logo')?.src || 'N/A';
					const position = listingElement.querySelector('.position')?.innerText?.trim() || 'N/A';
					const companyName = listingElement.querySelector('.company')?.innerText?.trim() || 'N/A';
					const location = listingElement.querySelector('.location')?.innerText?.trim() || 'N/A';
					const jobType = listingElement.querySelector('.job-type')?.innerText?.trim() || 'N/A';
					const datePosted = listingElement.querySelector('time')?.getAttribute('datetime') || 'N/A';
					const applicationDeadline = listingElement.querySelector('.application-deadline')?.innerText?.trim().replace('Closes:', '').trim() || 'N/A';

					return {
						link,
						companyLogo,
						position,
						companyName,
						location,
						jobType,
						datePosted,
						applicationDeadline
					};
				}).filter(j => j.link !== 'N/A' && j.companyLogo !== 'N/A');
			})()`,
	},
	{
		SourceName:  "jobsearchmalawi",
		URL:         "https://jobsearchmalawi.com/",
		WaitSelector: "ul.job-listings li",
		ScrapeJS: `
			Array.from(document.querySelectorAll('ul.job-listings li')).map(el => ({
				link: el.querySelector('a')?.href || 'N/A',
				companyLogo: el.querySelector('.company-logo img')?.src || 'N/A',
				position: el.querySelector('.job-title')?.innerText?.trim() || 'N/A',
				companyName: el.querySelector('.company-name')?.innerText?.trim() || 'N/A',
				location: el.querySelector('.job-location')?.innerText?.trim() || 'N/A',
				jobType: el.querySelector('.job-type')?.innerText?.trim() || 'N/A',
				datePosted: el.querySelector('.post-date')?.getAttribute('datetime') || 'N/A',
				applicationDeadline: el.querySelector('.deadline')?.innerText?.trim() || 'N/A'
			})).filter(j => j.link !== 'N/A')`,
	},
	{
		SourceName:   "ntchito",
		URL:          "https://ntchito.com/jobs-in-malawi/",
		WaitSelector: ".job_listings",
		ScrapeJS: `
			Array.from(document.querySelectorAll("article")).map((listingElement) => {
				const link = listingElement.querySelector("a")?.href || "N/A";
				const companyLogo = listingElement.querySelector(".company_logo")?.src || "N/A";
				const position = listingElement.querySelector(".entry-title")?.innerText?.trim() || "N/A";
				const companyName = listingElement.querySelector(".company-name")?.innerText?.trim() || "N/A";
				const location = listingElement.querySelector(".google_map_link")?.innerText?.trim() || "N/A";
				const jobType = listingElement.querySelector(".job-type")?.innerText?.trim() || "N/A";
				const datePosted = listingElement.querySelector(".date time")?.getAttribute("datetime") || "N/A";
				const applicationDeadline = listingElement.querySelector(".application-deadline")?.innerText?.trim().replace("Closes:", "").trim() || "N/A";
				
				return {
					link,
					companyLogo,
					position,
					companyName,
					location,
					jobType,
					datePosted,
					applicationDeadline
				};
			}).filter(j => j.link !== 'N/A' && j.companyLogo !== 'N/A')`,
	},
}

func main() {
	log.SetOutput(os.Stdout)
	log.Println(yellow("🚀 Starting job scraper..."))

	jobs, err := ScrapeAllJobs()
	if err != nil {
		log.Fatal(red("❌ Error:"), err)
	}

	jsonData, _ := json.MarshalIndent(jobs, "", "  ")
	log.Printf(green("\n✅ Successfully scraped %d jobs from %d websites!\n"), len(jobs), len(websites))
	log.Println(yellow("📄 JSON output:"))
	log.Println(string(jsonData))
}

func ScrapeAllJobs() ([]Job, error) {
	ctx, cancel := chromedp.NewContext(context.Background())
	defer cancel()

	var wg sync.WaitGroup
	results := make(chan []Job)
	errChan := make(chan error)

	// Shared browser context
	browserCtx, cancelBrowser := chromedp.NewContext(ctx)
	defer cancelBrowser()

	if err := chromedp.Run(browserCtx); err != nil {
		return nil, err
	}

	for _, site := range websites {
		wg.Add(1)
		go func(config ScrapeConfig) {
			defer wg.Done()

			// Create spinner for this website
			s := spinner.New(spinner.CharSets[14], 100*time.Millisecond)
			s.Prefix = yellow(" ⌛ ") + color.BlueString(config.SourceName+" ")
			s.Start()

			// Create tab context
			tabCtx, cancelTab := chromedp.NewContext(browserCtx)
			defer cancelTab()

			// Scrape with progress
			s.Suffix = yellow(" Scraping jobs...")
			jobs, err := scrapeSite(tabCtx, config)

			// Handle spinner state
			if err != nil {
				s.FinalMSG = red("❌ ") + config.SourceName + ": " + err.Error() + "\n"
				errChan <- err
			} else {
				s.FinalMSG = green("✅ ") + config.SourceName +
					color.CyanString(" (%d jobs)\n", len(jobs))
				results <- jobs
			}
			s.Stop()
		}(site)
	}

	go func() {
		wg.Wait()
		close(results)
		close(errChan)
	}()

	var combinedJobs []Job
	for jobs := range results {
		combinedJobs = append(combinedJobs, jobs...)
	}

	select {
	case err := <-errChan:
		return nil, err
	default:
		return combinedJobs, nil
	}
}

func scrapeSite(ctx context.Context, config ScrapeConfig) ([]Job, error) {
	ctx, cancel := context.WithTimeout(ctx, 30*time.Second)
	defer cancel()

	var rawJobs []Job
	err := chromedp.Run(ctx,
		chromedp.Navigate(config.URL),
		chromedp.WaitVisible(config.WaitSelector, chromedp.ByQuery),
		chromedp.Evaluate(config.ScrapeJS, &rawJobs),
	)

	if err != nil {
		return nil, err
	}

	// Process results
	for i := range rawJobs {
		rawJobs[i].Source = config.SourceName
		rawJobs[i].Category = categorizeJob(rawJobs[i])
	}

	return rawJobs, nil
}

func categorizeJob(job Job) string {
	switch {
	case strings.Contains(strings.ToLower(job.Position), "manager"):
		return "Management"
	case strings.Contains(strings.ToLower(job.JobType), "remote"):
		return "Remote"
	case strings.Contains(strings.ToLower(job.JobType), "full-time"):
		return "Full-Time"
	default:
		return "General"
	}
}
