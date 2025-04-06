package main

import (
	"fmt"
	"net/http"
	"os"
	"strings"

	"golang.org/x/net/html"
)

func extractText(n *html.Node) string {
	if n.Type == html.TextNode {
		return n.Data
	}
	var sb strings.Builder
	for c := n.FirstChild; c != nil; c = c.NextSibling {
		sb.WriteString(extractText(c))
	}
	return sb.String()
}

func findMainContentNode(n *html.Node, tags []string) *html.Node {
	var match *html.Node
	var f func(*html.Node)
	f = func(n *html.Node) {
		if n.Type == html.ElementNode {
			for _, tag := range tags {
				if n.Data == tag {
					match = n
					return
				}
			}
		}
		for c := n.FirstChild; c != nil && match == nil; c = c.NextSibling {
			f(c)
		}
	}
	f(n)
	return match
}

func findLargestTextDiv(n *html.Node) *html.Node {
	var best *html.Node
	maxLen := 0

	var f func(*html.Node)
	f = func(n *html.Node) {
		if n.Type == html.ElementNode && n.Data == "div" {
			text := strings.TrimSpace(extractText(n))
			if len(text) > maxLen {
				maxLen = len(text)
				best = n
			}
		}
		for c := n.FirstChild; c != nil; c = c.NextSibling {
			f(c)
		}
	}
	f(n)
	return best
}

func extractMainTextFromURL(url string) (string, error) {
	resp, err := http.Get(url)
	if err != nil {
		return "", err
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return "", fmt.Errorf("HTTP Error: %s", resp.Status)
	}

	doc, err := html.Parse(resp.Body)
	if err != nil {
		return "", err
	}

	mainTags := []string{"main", "article"}
	mainNode := findMainContentNode(doc, mainTags)

	if mainNode == nil {
		mainNode = findLargestTextDiv(doc)
	}

	if mainNode == nil {
		return "", fmt.Errorf("could not find main content")
	}

	text := strings.TrimSpace(extractText(mainNode))
	return text, nil
}

func main() {
	url := "https://jobsearchmalawi.com/job/sales-analyst-2/" // Replace with your desired URL
	text, err := extractMainTextFromURL(url)
	if err != nil {
		fmt.Fprintln(os.Stderr, "Error:", err)
		os.Exit(1)
	}

	fileName := "output.txt"
	err = os.WriteFile(fileName, []byte(text), 0644)
	if err != nil {
		fmt.Fprintln(os.Stderr, "Failed to write to file:", err)
		os.Exit(1)
	}

	fmt.Println("Main content saved to", fileName)
}
