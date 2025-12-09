#!/usr/bin/env python3
"""Remove the description column from the Excel file."""

import pandas as pd
from pathlib import Path

excel_path = r"D:\writing\clirnet\comments_agent\comments_last_3_months 1.xlsx"
excel_file = Path(excel_path)

print(f"Reading Excel file: {excel_path}")
df = pd.read_excel(excel_file)

print(f"Original columns: {list(df.columns)}")
print(f"Original shape: {df.shape}")

# Remove the description column
df = df.drop(columns=['description'])

print(f"New columns: {list(df.columns)}")
print(f"New shape: {df.shape}")

# Save back to Excel
df.to_excel(excel_file, index=False, sheet_name='Sheet1')
print(f"[SUCCESS] Updated Excel file saved")
