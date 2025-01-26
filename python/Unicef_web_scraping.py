import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuration
URL = "https://www.crisisgroup.org/crisiswatch/database?location%5B%5D=122&location%5B%5D=161&location%5B%5D=119&location%5B%5D=58&location%5B%5D=3985&crisis_state=&created=-3+months&from_month=1&from_year=2025&to_month=1&to_year=2025"
OUTPUT_FILE = "data.json"
WAIT_TIMEOUT = 10


def initialize_driver():
    """Initialize and return the Selenium WebDriver."""
    return webdriver.Chrome()


def extract_data(database_element):
    """Extract data from the database element."""
    data = []
    for group in database_element.find_elements(By.CLASS_NAME, "c-crisiswatch-entry"):
        try:
            # Extract country name
            country_name = group.find_element(By.TAG_NAME, "h3").text

            # Extract month and year
            month_year = group.find_element(By.TAG_NAME, "time").text

            # Extract title and paragraph content
            for entry in group.find_elements(By.CLASS_NAME, "o-crisis-states__detail"):
                title = entry.find_element(By.TAG_NAME, "strong").text
                paragraphs = entry.find_elements(By.TAG_NAME, "p")
                paragraph_texts = [
                    p.text for p in paragraphs if p.text != title]
                paragraph = " ".join(paragraph_texts)

                # Append extracted data
                data.append({
                    "Country name": country_name,
                    "Month and year": month_year,
                    "Bolded title": title,
                    "Paragraph content": paragraph
                })
        except Exception as e:
            print(f"Error extracting data from a group: {e}")
    return data


def save_to_json(data, file_path):
    """Save extracted data to a JSON file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
        print(f"Data successfully saved to {file_path}")
    except Exception as e:
        print(f"Error saving data to JSON: {e}")


def main():
    """Main function to execute the script."""
    driver = None
    try:
        # Initialize WebDriver
        driver = initialize_driver()
        driver.get(URL)

        # Wait for the database element to load
        wait = WebDriverWait(driver, WAIT_TIMEOUT)
        database_element = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "cw-database")))

        # Extract data
        data = extract_data(database_element)

        # Save data to JSON
        save_to_json(data, OUTPUT_FILE)

        # Print extracted data
        for item in data:
            print(item)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the WebDriver
        if driver:
            driver.quit()


if __name__ == "__main__":
    main()
