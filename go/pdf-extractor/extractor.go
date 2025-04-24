package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"mime/multipart"
	"net/http"
	"os"
	"path/filepath"
	"strings"
	"sync"

	"github.com/ledongthuc/pdf"
	docx "github.com/nguyenthenguyen/docx"
)

const (
	ocrSpaceAPIKey = "K85543186088957"
	ocrSpaceAPIURL = "https://api.ocr.space/parse/image"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: extractor <input-file>")
		os.Exit(1)
	}
	inputPath := os.Args[1]

	if !fileExists(inputPath) {
		fmt.Printf("Error: File '%s' does not exist\n", inputPath)
		os.Exit(1)
	}

	ext := strings.ToLower(filepath.Ext(inputPath))
	var text string
	var err error

	switch ext {
	case ".pdf":
		text, err = extractTextFromPDF(inputPath)
	case ".docx":
		text, err = extractTextFromDOCX(inputPath)
	case ".txt":
		text, err = extractTextFromTXT(inputPath)
	default:
		fmt.Printf("Error: Unsupported file format '%s'\n", ext)
		os.Exit(1)
	}

	if err != nil {
		fmt.Printf("Error extracting text: %v\n", err)
		os.Exit(1)
	}

	txtPath := strings.TrimSuffix(inputPath, filepath.Ext(inputPath)) + ".txt"
	if err := os.WriteFile(txtPath, []byte(text), 0644); err != nil {
		fmt.Printf("Error writing to output file: %v\n", err)
		os.Exit(1)
	}

	fmt.Printf("Text successfully extracted and saved to '%s'\n", txtPath)
}

// extractTextFromPDF tries standard extraction first, falls back to OCR if needed
func extractTextFromPDF(path string) (string, error) {
	// First try standard text extraction
	normalText, err := extractTextFromPDFNormal(path)
	if err != nil {
		return "", fmt.Errorf("PDF extraction failed: %v", err)
	}

	// If too little text is found, use OCR
	if len(normalText) < 100 {
		ocrText, ocrErr := extractTextWithOCRSpace(path)
		if ocrErr != nil {
			return normalText, fmt.Errorf("standard extraction returned minimal text, OCR also failed: %v", ocrErr)
		}
		return ocrText, nil
	}

	return normalText, nil
}

// extractTextFromPDFNormal extracts text from text-based PDFs
func extractTextFromPDFNormal(path string) (string, error) {
	f, r, err := pdf.Open(path)
	if err != nil {
		return "", err
	}
	defer f.Close()

	var textBuilder strings.Builder
	totalPages := r.NumPage()

	var wg sync.WaitGroup
	results := make(chan string, totalPages)

	for pageIndex := 1; pageIndex <= totalPages; pageIndex++ {
		wg.Add(1)
		go func(page int) {
			defer wg.Done()
			p := r.Page(page)
			if p.V.IsNull() {
				return
			}

			pageText, err := p.GetPlainText(nil)
			if err != nil {
				return
			}

			results <- fmt.Sprintf("--- Page %d ---\n%s", page, pageText)
		}(pageIndex)
	}

	go func() {
		wg.Wait()
		close(results)
	}()

	for res := range results {
		textBuilder.WriteString(res + "\n\n")
	}

	return textBuilder.String(), nil
}

// extractTextWithOCRSpace uses OCR.Space API for image-based PDFs
func extractTextWithOCRSpace(path string) (string, error) {
	file, err := os.Open(path)
	if err != nil {
		return "", fmt.Errorf("failed to open file: %v", err)
	}
	defer file.Close()

	// Prepare multipart form request
	body := &bytes.Buffer{}
	writer := multipart.NewWriter(body)
	part, err := writer.CreateFormFile("file", filepath.Base(path))
	if err != nil {
		return "", fmt.Errorf("failed to create form file: %v", err)
	}
	_, err = io.Copy(part, file)
	if err != nil {
		return "", fmt.Errorf("failed to copy file data: %v", err)
	}
	writer.Close()

	// Create HTTP request
	req, err := http.NewRequest("POST", ocrSpaceAPIURL, body)
	if err != nil {
		return "", fmt.Errorf("failed to create request: %v", err)
	}
	req.Header.Set("Content-Type", writer.FormDataContentType())
	req.Header.Set("apikey", ocrSpaceAPIKey)

	// Send request
	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		return "", fmt.Errorf("API request failed: %v", err)
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return "", fmt.Errorf("API returned non-200 status: %d", resp.StatusCode)
	}

	// Parse response
	var result struct {
		ParsedResults []struct {
			ParsedText string `json:"ParsedText"`
		} `json:"ParsedResults"`
	}
	if err := json.NewDecoder(resp.Body).Decode(&result); err != nil {
		return "", fmt.Errorf("failed to decode API response: %v", err)
	}

	if len(result.ParsedResults) == 0 {
		return "", fmt.Errorf("no text found in OCR result")
	}

	return result.ParsedResults[0].ParsedText, nil
}

// Existing helper functions remain unchanged
func extractTextFromDOCX(path string) (string, error) {
	doc, err := docx.ReadDocxFile(path)
	if err != nil {
		return "", err
	}
	defer doc.Close()
	return doc.Editable().GetContent(), nil
}

func extractTextFromTXT(path string) (string, error) {
	content, err := os.ReadFile(path)
	if err != nil {
		return "", err
	}
	return string(content), nil
}

func fileExists(path string) bool {
	_, err := os.Stat(path)
	return !os.IsNotExist(err)
}