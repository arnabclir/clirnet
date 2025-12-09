# Comments Agent - TOON Format Conversion

## Overview

This directory contains utilities to convert Excel data into TOON format, optimized for efficient Large Language Model (LLM) consumption.

## Files

- **`comments_last_3_months 1.xlsx`** - Source Excel file containing medical wiki article comments
- **`comments_toon.txt`** - Generated TOON format file (188 KB)
- **`excel_to_toon.py`** - Main conversion script
- **`remove_description_column.py`** - Utility script to remove columns from Excel

## Data Structure

The Excel file contains the following columns:
- `type_id` - Article ID
- `type` - Content type (e.g., "medwiki")
- `title` - Article title
- `user_master_id` - User identifier
- `comment` - User comment text
- `added_on` - Timestamp

Total: **1,112 rows** × **6 columns**

## TOON Format

**TOON** (Token-Oriented Object Notation) is a compact data serialization format optimized for LLM prompting. It achieves **30-60% token reduction** compared to JSON for equivalent data.

### Key Benefits

- Minimizes tokens by declaring field names once, not per row
- Comma-separated values for tabular data
- Indentation-based structure
- Designed specifically for LLM input efficiency

### Format Example

```
Sheet1[1112,]{type_id,type,title,user_master_id,comment,added_on}:
  35952,medwiki,"A Clinician's Guide to CBC Interpretation","Very useful in day to day practice","2025-11-07T11:37:30"
  35774,medwiki,"A Clinical Look at the Treatment of Vertigo","7 .","2025-11-07T09:27:44"
  ...
```

## Usage

### Convert Excel to TOON

```bash
python excel_to_toon.py
```

Output will be saved to `comments_toon.txt`

### Remove Columns from Excel

```bash
python remove_description_column.py
```

This utility removes the `description` column, significantly reducing file size and token usage.

## File Size Comparison

| Format | Size | Tokens | Reduction |
|--------|------|--------|-----------|
| Excel (with description) | 3.86 MB | High | - |
| TOON (without description) | 188 KB | ~2000 | 95% smaller |

## Requirements

```
pandas>=1.3.0
python-toon>=0.1.3
```

### Installation

```bash
pip install pandas
pip install git+https://github.com/xaviviro/python-toon.git
```

## Use Cases

- Sending structured data to LLMs for analysis
- Batch processing of medical article comments
- Cost optimization for API calls (fewer tokens = lower cost)
- Efficient data storage for archival

## References

- [TOON Format Specification](https://github.com/toon-format/spec)
- [python-toon Library](https://github.com/xaviviro/python-toon)
- Token-Oriented Object Notation (TOON): JSON alternative reducing token usage by 30-60%
