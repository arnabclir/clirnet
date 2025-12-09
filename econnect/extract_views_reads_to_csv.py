import json
import csv

def extract_views_reads_from_json():
    """Extract views/reads data from data_content_views_reads.json"""

    with open('data_content_views_reads.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Extract views/reads information
    views_reads = []
    for item in data.get('data', []):
        entry = {
            'type_id': item.get('type_id', ''),
            'views': item.get('views', ''),
            'reads': item.get('reads', ''),
            'date_Data': item.get('date_Data', '')
        }
        views_reads.append(entry)

    # Write to CSV
    output_path = 'data_content_views_reads.csv'
    with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['type_id', 'views', 'reads', 'date_Data']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(views_reads)

    return len(views_reads)

if __name__ == '__main__':
    count = extract_views_reads_from_json()
    print(f"Extracted {count} views/reads records from JSON")
