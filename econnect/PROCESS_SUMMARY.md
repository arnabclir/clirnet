# Content Data Processing Summary

## What Was Done

This process extracts content data from two JSON files and joins them into a unified CSV.

### Step 1: Extract Content from JSON
- **Source:** `data_content_project.json`
- **Extraction:** Parsed the JSON structure and extracted all content items from the `project_contents` array
- **Fields extracted:**
  - `content_id` - New unique content identifier (44736-49686)
  - `content_old_id` - Legacy content identifier (8611-35763) - **used for joining with metrics**
  - `content_name` - Content title
  - `content_description` - Full content description
- **Output:** `content_data.csv` (124 records)

### Step 2: Extract Views/Reads from JSON
- **Source:** `data_content_views_reads.json`
- **Extraction:** Parsed the JSON array and extracted metrics for each content item
- **Fields extracted:**
  - `type_id` - Content type identifier (maps to content_id)
  - `views` - View count metrics
  - `reads` - Read count metrics
  - `date_Data` - Date information (comma-separated values)
- **Output:** `data_content_views_reads.csv` (124 records)

### Step 3: Join Both Datasets
- **Source 1:** `content_data.csv` (124 records)
- **Source 2:** `data_content_views_reads.csv` (124 records)
- **Join Type:** Full Outer Join on `content_old_id`
- **Join Key Mapping:**
  - `type_id` in views/reads → `content_old_id` in content data
  - Both use the legacy content ID system (8611-35763)
- **Output:** `content_data_joined.csv` (124 records total)
  - 124 records with complete data (content + views/reads)
  - 0 records with missing data (100% match rate)

**Why this join key?**
- `content_id` is the new ID system (44736-49686) - used for current platform
- `content_old_id` is the legacy ID system (8611-35763) - matches `type_id` in metrics

## Files Generated

1. **extract_content_to_csv.py** - Extracts content data from JSON (standalone)
2. **extract_views_reads_to_csv.py** - Extracts views/reads data from JSON (standalone)
3. **join_csvs.py** - Joins the two CSVs (standalone)
4. **run_all.py** - Master script that runs everything in one command

## Output Files

- `content_data.csv` - Content data extracted from data_content_project.json
  - Includes both `content_id` (new) and `content_old_id` (legacy for joining)
- `data_content_views_reads.csv` - Views/reads data extracted from data_content_views_reads.json
  - Contains `type_id` which maps to `content_old_id`
- `content_data_joined.csv` - Final joined dataset with complete content and metrics
  - 124 records with full data (title, description, views, reads, dates)

## Running Going Forward

Simply execute:
```bash
python run_all.py
```

This will automatically:
1. Extract content from `data_content_project.json` → `content_data.csv`
2. Extract views/reads from `data_content_views_reads.json` → `data_content_views_reads.csv`
3. Join both CSVs → `content_data_joined.csv`
4. Display a detailed summary of the process

**Note:** Both source JSON files must exist in the same directory as run_all.py
