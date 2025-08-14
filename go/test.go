package main

import (
	"encoding/json"
	"errors"
	"fmt"
	"os"
)

const (
	currentJobsFile  = "./current_jobs.json"
	previousJobsFile = "./previous_jobs.json"
	newJobsFile      = "./new_jobs.json"
	nodeScriptPath   = "E:/code/random-projects/javascript/web-scrapping/index.mjs"
)
func createJobKey(job Job) string {
	return fmt.Sprintf("%s|%s|%s",
		job["position"],
		job["companyName"],
		job["link"])
}
type Job map[string]interface{}

func readJobsFile(filename string) ([]Job, error) {
	data, err := os.ReadFile(filename)
	if err != nil {
		return nil, err
	}

	var jobs []Job
	if err := json.Unmarshal(data, &jobs); err != nil {
		return nil, fmt.Errorf("error parsing %s: %v", filename, err)
	}
	return jobs, nil
}

func writeJobsFile(filename string, jobs []Job) error {
	data, err := json.MarshalIndent(jobs, "", "  ")
	if err != nil {
		return fmt.Errorf("error marshaling jobs: %v", err)
	}
	return os.WriteFile(filename, data, 0644)
}

// findNewJobs compares current jobs with previous and returns the new ones
func findNewJobs(currentJobs, previousJobs []Job) []Job {
	existingJobs := make(map[string]bool)
	for _, job := range previousJobs {
		existingJobs[createJobKey(job)] = true
	}

	var newJobs []Job
	for _, job := range currentJobs {
		if !existingJobs[createJobKey(job)] {
			newJobs = append(newJobs, job)
		}
	}
	return newJobs
}
func processJobs(currentPath, previousPath, newPath string) error {
	currentJobs, err := readJobsFile(currentPath)
	if err != nil {
		return fmt.Errorf("error reading current jobs: %v", err)
	}

	previousJobs, err := readJobsFile(previousPath)
	if errors.Is(err, os.ErrNotExist) {
		// First run - treat all as new
		if err := writeJobsFile(previousPath, currentJobs); err != nil {
			return fmt.Errorf("error writing initial previous jobs: %v", err)
		}
		if err := writeJobsFile(newPath, currentJobs); err != nil {
			return fmt.Errorf("error writing new jobs: %v", err)
		}
		fmt.Println("First run: all jobs are new.")
		return nil
	} else if err != nil {
		return fmt.Errorf("error reading previous jobs: %v", err)
	}

	newJobs := findNewJobs(currentJobs, previousJobs)
	if len(newJobs) == 0 {
		fmt.Println("No new jobs found.")
		return nil
	}

	if err := writeJobsFile(newPath, newJobs); err != nil {
		return fmt.Errorf("error writing new jobs: %v", err)
	}

	fmt.Printf("Found %d new jobs.\n", len(newJobs))
	return nil
}

func main() {
	err := processJobs(currentJobsFile, previousJobsFile, newJobsFile)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error: %v\n", err)
		os.Exit(1)
	}
}
