package main

import (
    "context"
    "encoding/json"
    "fmt"
    "log"
    "time"

    "github.com/chromedp/chromedp"
)

// Job represents a single job listing.
type Job struct {
    Link                string `json:"link"`
    CompanyLogo         string `json:"companyLogo"`
    Position            string `json:"position"`
    CompanyName         string `json:"companyName"`
    Location            string `json:"location"`
    JobType             string `json:"jobType"`
    DatePosted          string `json:"datePosted"`
    ApplicationDeadline string `json:"applicationDeadline"`
}

func GetFirstJobFromNchito(ctx context.Context) (*Job, error) {
    // new browser context
    ctx, cancel := chromedp.NewContext(ctx)
    defer cancel()
    // shorter timeout so failures come fast
    ctx, cancel = context.WithTimeout(ctx, 15*time.Second)
    defer cancel()

    var jsResult string
    js := `(function() {
        const el = document.querySelector('ul.job_listings li');
        if (!el) return JSON.stringify([]);
        const job = {
            link: el.querySelector('a')?.href || 'N/A',
            companyLogo: el.querySelector('.company_logo')?.src || 'N/A',
            position: el.querySelector('.position h3')?.innerText?.trim() || 'N/A',
            companyName: el.querySelector('.company strong')?.innerText?.trim() || 'N/A',
            location: el.querySelector('.location')?.innerText?.trim() || 'N/A',
            jobType: el.querySelector('.job-type')?.innerText?.trim() || 'N/A',
            datePosted: el.querySelector('.date time')?.getAttribute('datetime') || 'N/A',
            applicationDeadline: el.querySelector('.application-deadline')?.innerText
                ?.trim().replace('Closes:', '').trim() || 'N/A'
        };
        // only return one element
        return JSON.stringify([job]);
    })();`

    if err := chromedp.Run(ctx,
        chromedp.Navigate("https://ntchito.com/jobs-in-malawi/"),
        chromedp.WaitVisible(`ul.job_listings li`, chromedp.ByQuery),
        chromedp.Evaluate(js, &jsResult),
    ); err != nil {
        return nil, err
    }

    // Parse into slice—should have 0 or 1 elements
    var jobs []Job
    if err := json.Unmarshal([]byte(jsResult), &jobs); err != nil {
        return nil, err
    }
    if len(jobs) == 0 {
        return nil, fmt.Errorf("no job found")
    }
    return &jobs[0], nil
}

func main() {
    ctx := context.Background()
    job, err := GetFirstJobFromNchito(ctx)
    if err != nil {
        log.Fatalf("failed to get first job: %v", err)
    }

    // Print it so you can eyeball the result
    out, _ := json.MarshalIndent(job, "", "  ")
    fmt.Println(string(out))
}
