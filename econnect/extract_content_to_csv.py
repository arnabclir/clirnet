import json
import csv
from pathlib import Path

# Read the JSON file
with open('data_content_project.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Extract content information
contents = []
for project in data.get('data', []):
    for project_content in project.get('project_contents', []):
        for content in project_content.get('fetch_with_contents', []):
            content_entry = {
                'content_id': content.get('content_id', ''),
                'content_old_id': content.get('content_old_id', ''),
                'content_name': content.get('content_title', ''),
                'content_description': content.get('content_description', '')
            }
            contents.append(content_entry)

# Write to CSV
output_path = 'content_data.csv'
with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['content_id', 'content_old_id', 'content_name', 'content_description']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(contents)

print(f"CSV created: {output_path}")
print(f"Total records: {len(contents)}")
