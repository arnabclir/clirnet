#!/usr/bin/env python3
"""
Convert Excel file to TOON format for efficient LLM consumption.
Uses the official python-toon library.

TOON: Token-Oriented Object Notation - reduces LLM tokens by 30-60% vs JSON
Reference: https://github.com/xaviviro/python-toon
"""

import pandas as pd
import sys
from pathlib import Path
from toon import encode


def excel_to_toon(excel_path: str, output_path: str) -> None:
    """
    Convert Excel file to TOON format using the python-toon library.

    Process:
    1. Read Excel file(s)
    2. Convert each sheet to a dict
    3. Encode to TOON using the official library
    4. Write to output file
    """

    # Read Excel file
    excel_file = Path(excel_path)
    if not excel_file.exists():
        print(f"Error: File not found: {excel_path}")
        sys.exit(1)

    # Read all sheets
    xls = pd.ExcelFile(excel_file)
    print(f"Found sheets: {xls.sheet_names}")

    # Convert all sheets to a dictionary structure
    data = {}

    for sheet_name in xls.sheet_names:
        df = pd.read_excel(excel_file, sheet_name=sheet_name)

        # Remove completely empty rows
        df = df.dropna(how='all')

        # Convert DataFrame to list of dicts (more natural for TOON)
        records = df.to_dict(orient='records')

        # Clean up NaN values
        cleaned_records = []
        for record in records:
            cleaned = {k: (None if pd.isna(v) else v) for k, v in record.items()}
            cleaned_records.append(cleaned)

        data[sheet_name] = cleaned_records
        print(f"  Sheet '{sheet_name}': {len(cleaned_records)} rows x {len(df.columns)} columns")

    # Encode to TOON format
    print("\nEncoding to TOON format...")
    toon_str = encode(data)

    # Write to output file
    output_file = Path(output_path)
    output_file.write_text(toon_str, encoding="utf-8")

    print(f"[SUCCESS] Converted to TOON format")
    print(f"[SUCCESS] Output saved to: {output_path}")
    print(f"[SUCCESS] File size: {output_file.stat().st_size} bytes")


if __name__ == "__main__":
    excel_path = r"D:\writing\clirnet\comments_agent\comments_last_3_months 1.xlsx"
    output_path = r"D:\writing\clirnet\comments_agent\comments_toon.txt"

    excel_to_toon(excel_path, output_path)
