import csv

with open('../job_postings.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader, 1):
        if len(row) > 2:
            print(f"Line {i}: {row}")
