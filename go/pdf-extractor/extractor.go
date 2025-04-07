package main

import (
	"fmt"
	"os"
	"path/filepath"
	"strings"

	"github.com/ledongthuc/pdf"
)

func main() {
	// Fixed input PDF path - change this to your PDF file path
	pdfPath := "./Resume-StatClerk.pdf"
	
	// Output text file path (same name as PDF but with .txt extension)
	txtPath := strings.TrimSuffix(pdfPath, filepath.Ext(pdfPath)) + ".txt"
	
	// Check if file exists and has .pdf extension
	if !fileExists(pdfPath) {
		fmt.Printf("Error: File '%s' does not exist\n", pdfPath)
		os.Exit(1)
	}
	
	if filepath.Ext(strings.ToLower(pdfPath)) != ".pdf" {
		fmt.Printf("Error: File '%s' is not a PDF file\n", pdfPath)
		os.Exit(1)
	}

	text, err := extractTextFromPDF(pdfPath)
	if err != nil {
		fmt.Printf("Error extracting text: %v\n", err)
		os.Exit(1)
	}

	// Write text to output file
	err = os.WriteFile(txtPath, []byte(text), 0644)
	if err != nil {
		fmt.Printf("Error writing to output file: %v\n", err)
		os.Exit(1)
	}

	fmt.Printf("Text successfully extracted from '%s' and saved to '%s'\n", pdfPath, txtPath)
}

func extractTextFromPDF(path string) (string, error) {
	f, r, err := pdf.Open(path)
	if err != nil {
		return "", err
	}
	defer f.Close()

	var textBuilder strings.Builder
	
	// Get total number of pages
	totalPages := r.NumPage()
	
	// Extract text from each page
	for pageIndex := 1; pageIndex <= totalPages; pageIndex++ {
		p := r.Page(pageIndex)
		if p.V.IsNull() {
			continue
		}
		
		text, err := p.GetPlainText(nil)
		if err != nil {
			return "", err
		}
		
		textBuilder.WriteString(fmt.Sprintf("--- Page %d ---\n", pageIndex))
		textBuilder.WriteString(text)
		textBuilder.WriteString("\n\n")
	}
	
	return textBuilder.String(), nil
}

// Helper function to check if file exists
func fileExists(path string) bool {
	_, err := os.Stat(path)
	return !os.IsNotExist(err)
}