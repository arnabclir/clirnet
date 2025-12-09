#!/usr/bin/env python3
"""
Master script to extract content data from JSON files and join them.

This script:
1. Extracts content from data_content_project.json
2. Extracts views/reads from data_content_views_reads.json
3. Joins both datasets into a single unified CSV
"""

import json
import csv
import pandas as pd
from pathlib import Path

def extract_content_from_json():
    """Extract content data from data_content_project.json"""
    print("Step 1: Extracting content from JSON...")

    with open('data_content_project.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

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

    print(f"  - Extracted {len(contents)} content records")
    print(f"  - Saved to: {output_path}")
    return len(contents)

def extract_views_reads_from_json():
    """Extract views/reads data from data_content_views_reads.json"""
    print("Step 2: Extracting views/reads from JSON...")

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

    print(f"  - Extracted {len(views_reads)} views/reads records")
    print(f"  - Saved to: {output_path}")
    return len(views_reads)

def join_csvs():
    """Join content_data.csv with data_content_views_reads.csv"""
    print("\nStep 3: Joining CSVs...")

    # Read content_data.csv normally
    content_data = pd.read_csv('content_data.csv')

    # Read views_reads.csv with only the first 4 columns
    views_reads = pd.read_csv('data_content_views_reads.csv',
                              usecols=['type_id', 'views', 'reads', 'date_Data'])

    # Rename type_id to content_old_id for joining
    views_reads = views_reads.rename(columns={'type_id': 'content_old_id'})

    # Perform a full outer join on content_old_id (type_id maps to content_old_id)
    joined = pd.merge(
        content_data,
        views_reads,
        on='content_old_id',
        how='outer'
    )

    # Sort by content_old_id for better readability
    joined = joined.sort_values('content_old_id', na_position='last')

    # Save the joined file
    output_path = 'content_data_joined.csv'
    joined.to_csv(output_path, index=False, encoding='utf-8')

    # Calculate stats
    both = joined[(joined['content_name'].notna()) & (joined['views'].notna())]
    only_content = joined[(joined['content_name'].notna()) & (joined['views'].isna())]
    only_views = joined[(joined['content_name'].isna()) & (joined['views'].notna())]

    print(f"  - Content records: {len(content_data)}")
    print(f"  - Views/reads records: {len(views_reads)}")
    print(f"  - Joined records: {len(joined)}")
    print(f"    * With both data: {len(both)}")
    print(f"    * Content only: {len(only_content)}")
    print(f"    * Views/reads only: {len(only_views)}")
    print(f"  - Saved to: {output_path}")

    return len(joined)

def main():
    """Run the complete process"""
    print("=" * 60)
    print("Content Data Processing Pipeline")
    print("=" * 60)

    try:
        content_count = extract_content_from_json()
        views_reads_count = extract_views_reads_from_json()
        total_count = join_csvs()

        print("\n" + "=" * 60)
        print("SUCCESS: Processing complete!")
        print("=" * 60)
        print(f"Final output file: content_data_joined.csv ({total_count} records)")
        print("\nFor details, see PROCESS_SUMMARY.md")

    except FileNotFoundError as e:
        print(f"ERROR: Required file not found: {e}")
        print("Make sure these files exist in the current directory:")
        print("  - data_content_project.json")
        print("  - data_content_views_reads.json")
        return 1
    except Exception as e:
        print(f"ERROR: {e}")
        return 1

    return 0

if __name__ == '__main__':
    exit(main())
