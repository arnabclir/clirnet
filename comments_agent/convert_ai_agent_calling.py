#!/usr/bin/env python3
"""Convert AI Agent Calling Excel file to TOON format."""

import pandas as pd
from pathlib import Path
from toon import encode

excel_path = r"D:\writing\clirnet\comments_agent\AI Agent Calling.xlsx"
output_path = r"D:\writing\clirnet\comments_agent\ai_agent_calling_toon.txt"

excel_file = Path(excel_path)
if not excel_file.exists():
    print(f"Error: File not found: {excel_path}")
    exit(1)

# Read Excel file
df = pd.read_excel(excel_file)

print(f"Original columns: {list(df.columns)}")
print(f"Original shape: {df.shape}")

# Remove completely empty rows
df = df.dropna(how='all')

# Remove unnamed columns (likely empty)
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

print(f"Cleaned columns: {list(df.columns)}")
print(f"Cleaned shape: {df.shape}")

# Convert to dict structure for TOON
records = df.to_dict(orient='records')

# Clean up NaN values
cleaned_records = []
for record in records:
    cleaned = {k: (None if pd.isna(v) else v) for k, v in record.items()}
    cleaned_records.append(cleaned)

data = {"AI_Agent_Calling": cleaned_records}

# Encode to TOON format
print("\nEncoding to TOON format...")
toon_str = encode(data)

# Write to output file
output_file = Path(output_path)
output_file.write_text(toon_str, encoding="utf-8")

print(f"[SUCCESS] Converted to TOON format")
print(f"[SUCCESS] Output saved to: {output_path}")
print(f"[SUCCESS] File size: {output_file.stat().st_size} bytes")
