import json
import re
from pathlib import Path


def clean_text(text):
    # Remove special characters except spaces and hyphens
    cleaned = re.sub(r'[^a-zA-Z0-9\s-]', '', str(text))
    # Convert to lowercase
    cleaned = cleaned.lower()
    # Remove extra whitespace
    cleaned = ' '.join(cleaned.split())
    # Remove leading/trailing hyphens
    cleaned = cleaned.strip('-')
    return cleaned


def clean_job_data(raw_data):
    cleaned_data = []
    for entry in raw_data:
        # Skip if fields are missing or N/A
        if not all(key in entry for key in ["position", "companyName"]):
            continue
        if entry["position"] == "N/A" or entry["companyName"] == "N/A":
            continue

        # Clean fields
        position = clean_text(entry["position"])
        company = clean_text(entry["companyName"])

        # Skip if empty after cleaning
        if position and company:
            cleaned_data.append({"position": position, "companyName": company})

    return cleaned_data


def main():
    # Read raw data
    raw_path = Path("./job_search_malawi.json")
    with open(raw_path, "r", encoding="utf-8") as f:
        raw_data = json.load(f)

    # Clean data
    cleaned_data = clean_job_data(raw_data)

    # Save cleaned data
    output_path = Path("./cleaned_jobs.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(cleaned_data, f, indent=2)

    print(f"✅ Cleaned data saved to {output_path}")


if __name__ == "__main__":
    main()
