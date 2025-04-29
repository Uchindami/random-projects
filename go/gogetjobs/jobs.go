package main

import (
	"context"
	"encoding/json"
	"log"
	"os"
	"strings"
	"time"

	"github.com/chromedp/chromedp"
)

type Job struct {
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

func GetJobsFromCareersMW() ([]Job, error) {
	// Create context with timeout
	ctx, cancel := chromedp.NewContext(
		context.Background(),
		chromedp.WithLogf(log.Printf), // Optional logging
	)
	defer cancel()
	ctx, cancel = context.WithTimeout(ctx, 30*time.Second)
	defer cancel()

	var listings []Job

	// Define chromedp tasks
	err := chromedp.Run(ctx,
		chromedp.Navigate("https://careersmw.com/"),
		chromedp.WaitVisible(`ul.job_listings li`, chromedp.ByQuery),
		chromedp.Evaluate(`
			(() => {
				const listings = [];
				const elements = document.querySelectorAll('ul.job_listings li');
				
				for (const el of elements) {
					const linkEl = el.querySelector('a');
					const logoEl = el.querySelector('.company_logo');
					const positionEl = el.querySelector('.position h3');
					const companyEl = el.querySelector('.company strong');
					const locationEl = el.querySelector('.location');
					const jobTypeEl = el.querySelector('.job-type');
					const dateEl = el.querySelector('.date time');
					const deadlineEl = el.querySelector('.application-deadline');

					const link = linkEl ? linkEl.href : 'N/A';
					const logo = logoEl ? logoEl.src : 'N/A';
					
					if (logo === 'N/A' || link === 'N/A') continue;

					listings.push({
						link: link,
						companyLogo: logo,
						position: positionEl ? positionEl.innerText.trim() : 'N/A',
						companyName: companyEl ? companyEl.innerText.trim() : 'N/A',
						location: locationEl ? locationEl.innerText.trim() : 'N/A',
						jobType: jobTypeEl ? jobTypeEl.innerText.trim() : 'N/A',
						datePosted: dateEl ? dateEl.getAttribute('datetime') : 'N/A',
						applicationDeadline: deadlineEl ? 
							deadlineEl.innerText.trim().replace('Closes:', '').trim() : 'N/A'
					});
				}
				return listings;
			})()
		`, &listings),
	)

	if err != nil {
		return nil, err
	}

	// Categorize jobs
	for i := range listings {
		listings[i].Category = categorizeJob(listings[i])
	}

	return listings, nil
}

// Implement your categorization logic based on job details
func categorizeJob(job Job) string {
	// Example categorization logic
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

func main() {
	jobs, err := GetJobsFromCareersMW()
	if err != nil {
		log.Fatalf("Failed to get jobs: %v", err)
	}
	file, err := os.Create("jobs.json")
	if err != nil {
		log.Fatalf("Failed to create JSON file: %v", err)
	}
	defer file.Close()
	enc := json.NewEncoder(file)
	enc.SetIndent("", "  ")
	if err := enc.Encode(jobs); err != nil {
		log.Fatalf("Failed to encode jobs to JSON: %v", err)
	}
	log.Println("Jobs written to jobs.json")
}
