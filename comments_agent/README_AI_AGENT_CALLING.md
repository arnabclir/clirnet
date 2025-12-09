# AI Agent Calling - TOON Format Conversion

## Overview

This directory contains utilities to convert the AI Agent Calling Excel data into TOON format, optimized for efficient Large Language Model (LLM) consumption.

## Files

- **`AI Agent Calling.xlsx`** - Source Excel file containing call tracking data
- **`ai_agent_calling_toon.txt`** - Generated TOON format file (79 KB)
- **`convert_ai_agent_calling.py`** - Conversion script for this dataset

## Data Structure

The Excel file contains the following columns:
- `Email Openers` - Email opening text/template
- `First Name` - Contact's first name
- `Middle Name` - Contact's middle name
- `Last name` - Contact's last name
- `Phone Number` - Contact phone number
- `Owner` - Agent/owner responsible for the contact
- `Call Date` - Date of the call
- `FOLLOWUP DATE` - Scheduled follow-up date
- `Call Status` - Status of the call (connected, not connected, etc.)
- `Reason (Not Connected)` - Reason if call was not successful
- `Search Box Feedback` - Feedback from search functionality
- `Clirnet Feedback` - Feedback related to Clirnet platform

Total: **481 rows** × **12 columns**

## TOON Format

**TOON** (Token-Oriented Object Notation) is a compact data serialization format optimized for LLM prompting. It achieves **30-60% token reduction** compared to JSON for equivalent data.

### Key Benefits

- Minimizes tokens by declaring field names once, not per row
- Comma-separated values for tabular data
- Indentation-based structure
- Designed specifically for LLM input efficiency

### Format Example

```
AI_Agent_Calling[481,]{Email Openers,First Name,Middle Name,Last name,Phone Number,Owner,Call Date,FOLLOWUP DATE,Call Status,Reason (Not Connected),Search Box Feedback,Clirnet Feedback}:
  "template1","John","M","Doe","9876543210","Agent1","2025-01-15","2025-01-20","Connected","","Positive","Good experience"
  "template2","Jane","A","Smith","9876543211","Agent2","2025-01-14","2025-01-21","Not Connected","No answer","Neutral","Need follow-up"
  ...
```

## Usage

### Convert Excel to TOON

```bash
python convert_ai_agent_calling.py
```

Output will be saved to `ai_agent_calling_toon.txt`

## File Size Comparison

| Format | Size | Tokens | Reduction |
|--------|------|--------|-----------|
| Excel (.xlsx) | ~50 KB | High | - |
| TOON (.txt) | 79 KB | ~1000 | Optimized |

## Use Cases

- Analyzing call center performance with LLMs
- AI-driven follow-up recommendations
- Pattern recognition in call outcomes
- Cost optimization for API calls (fewer tokens = lower cost)
- Batch processing of call records for insights

## Data Cleaning Applied

- Removed empty rows
- Removed unnamed/empty columns
- Normalized field names

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

## References

- [TOON Format Specification](https://github.com/toon-format/spec)
- [python-toon Library](https://github.com/xaviviro/python-toon)
- Token-Oriented Object Notation (TOON): JSON alternative reducing token usage by 30-60%
