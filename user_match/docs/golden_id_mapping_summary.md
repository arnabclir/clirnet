# Golden ID Mapping and Data Standardization Summary

**Date:** December 20, 2025
**Source File:** `UM_CL_email.csv`
**Target File:** `T-Bact UID Data_Golden ID mapped.xlsm`
**Output File:** `T-Bact UID Data_Golden ID mapped_Updated.xlsm`

## Objective
The goal was to populate the `Golden ID` column in specific Excel sheets by matching `user_master_id` or `UID` against a master mapping file, while ensuring data consistency and correcting mixed datatypes.

## Steps Taken

### 1. Data Analysis & Preparation
- Analyzed `UM_CL_email.csv` to establish a priority-based mapping for `Golden ID`.
- **Priority Logic:** Numeric IDs were preferred over email IDs.
    1. `NUM ID` (Highest Priority)
    2. `NUM ID_B`
    3. `MAIL ID` (Lowest Priority)
- Standardized mapping keys to **integers** to ensure robust matching across different formats (string vs. numeric).

### 2. Data Standardization (Excel)
- Identified mixed datatypes in the `user_master_id` and `UID` columns across the workbook.
- Corrected **14,659 cells** in the `Content_ TBact` sheet where IDs were stored as the string `'Null'` or as numeric strings.
- Standardized all matching IDs to **Excel Integer** format to maintain database compatibility and precision.

### 3. Golden ID Population
- Iterated through the target sheets and populated the `Golden ID` column:
    - **`Banner_Unique_UID`**: Matched `user_master_id`.
    - **`Content Unique UID `**: Matched `UID`.
- Used the `openpyxl` library with `keep_vba=True` to ensure any existing VBA macros in the `.xlsm` file were preserved.

## Final Statistics

| Sheet Name | Action | Total Rows | Matches | Fixes (Types) |
| :--- | :--- | :--- | :--- | :--- |
| **Banner_Unique_UID** | Populated Golden ID | 51,957 | 8,079 | 0 |
| **Content Unique UID** | Populated Golden ID | 17,090 | 2,985 | 0 |
| **Content_ TBact** | Type Correction | 184,908 | N/A | 14,659 |

## Technical Details
- **Script used:** `scripts/standardize_types_and_match.py` (Temporary)
- **Tooling:** Python with `pandas` for initial analysis and `openpyxl` for high-fidelity Excel manipulation.
- **Validation:** Cell-level type checking was performed on the output file to confirm that all IDs are now stored as integers and all Golden IDs are correctly mapped.

---
*This document was generated automatically following the completion of the data mapping task.*
