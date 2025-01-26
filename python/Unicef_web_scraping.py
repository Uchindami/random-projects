import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the webdriver (e.g., Chrome)
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get("https://www.crisisgroup.org/crisiswatch/database?location%5B%5D=122&location%5B%5D=161&location%5B%5D=119&location%5B%5D=58&location%5B%5D=3985&crisis_state=&created=-3+months&from_month=1&from_year=2025&to_month=1&to_year=2025")

# Wait for the target element to be loaded
wait = WebDriverWait(driver, 10)
database_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cw-database")))

# Extract the data in the 
data = []
for group in database_element.find_elements(By.CLASS_NAME, "c-crisiswatch-entry"):
    # a. Country name
    country_name = group.find_element(By.TAG_NAME, "h3").text

    # b. Month and year
    month_year = group.find_element(By.TAG_NAME, "time").text

    # c. Bolded title and d. Paragraph content
    for entry in group.find_elements(By.CLASS_NAME, "o-crisis-states__detail"):
        title = entry.find_element(By.TAG_NAME, "strong").text
        
        paragraphs = entry.find_elements(By.TAG_NAME, "p")
        paragraph_texts = [p.text for p in paragraphs if p.text != title] 
        paragraph = " ".join(paragraph_texts)

    data.append({
        "Country name": country_name,
        "Month and year": month_year,
        "Bolded title:": title,
        "Paragraph content under each heading": paragraph 
    })

# Save the extracted data to a JSON file
with open('data.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)
    
# Print the extracted data
for item in data:
    print(item)

# Close the webdriver
driver.quit()