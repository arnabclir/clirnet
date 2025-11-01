# Banner Modification Procedure - Summary & Design Guide

## 0. REQUIREMENTS GATHERING - START HERE

### Critical First Step: Determine Banner Insertion Frequency Requirements

**This procedure is driven by ONE KEY REQUIREMENT: How many banners need to be inserted into the `banner_call_data` table, and at what frequency?**

Before writing any SQL queries, you must answer these questions:

1. **What is the banner insertion frequency?**
   - Example: "We need 3 banners inserted per day"
   - Example: "We need 1 banner every 2 days"
   - Example: "We need 5 banners total: daily for first week, then every 2 days"

2. **For each frequency slot, what date should the banners show?**
   - Example: If inserting 3 banners daily from 2025-04-25 to 2025-04-27:
     - Slot 1: 2025-04-25 (covers requests from 2025-04-01 to 2025-04-21)
     - Slot 2: 2025-04-26 (covers requests from 2025-04-22 to 2025-04-24)
     - Slot 3: 2025-04-27 (covers requests from 2025-04-25 to 2025-04-28)

3. **What date ranges in the raw data map to each frequency slot?**
   - This is where you identify which source dates go into which target date bucket

### How Frequency Requirements Drive the Procedure

```
REQUIREMENT: "Insert 3 banners daily for dates Apr 25-27"
                          ↓
        TRANSLATES TO: 3 target dates (2025-04-25, 26, 27)
                          ↓
        WHICH MEANS: 3 phases/groupings of source data
                          ↓
        WHICH DETERMINES: 3 sets of date range mappings in the queries
```

**Example from Banner 5902:**
- **Frequency Requirement**: 3 banners on dates 2025-04-25, 2025-04-26, 2025-04-27
- **Phase 1 (2025-04-25)**: Source records from 2025-04-01 to 2025-04-21 + 'add-report-prod-server' log
- **Phase 2 (2025-04-26)**: Source records from 2025-04-22 to 2025-04-24
- **Phase 3 (2025-04-27)**: Source records from 2025-04-25 to 2025-04-28

---

## 1. PROCEDURE SUMMARY

### Purpose
Modify historical banner campaign data by updating timestamps, log names, and JSON payload fields, then migrate the corrected data to production at the frequency specified in the requirements.

### What It Does
The procedure takes raw request data and transforms it through 7 sequential steps:

| Step | Action | Input | Output |
|------|--------|-------|--------|
| 1 | Update main timestamp & logName (Phase 1) | Date range: 2025-04-01 to 2025-04-21 | Records with new date 2025-04-25 |
| 2 | Update timestamp & logName (Phase 1 Alt) | logName = 'add-report-prod-server' | Records rebadged as 2025-04-25 |
| 3 | Update timestamp & logName (Phase 2) | Date range: 2025-04-22 to 2025-04-24 | Records with new date 2025-04-26 |
| 4 | Update timestamp & logName (Phase 3) | Date range: 2025-04-25 to 2025-04-28 | Records with new date 2025-04-27 |
| 5 | Update start_time JSON field | logName = 'H_5902_distinct_2025-04-25' | Timestamp formatted in JSON |
| 6 | Update end_time JSON field | logNames: 2025-04-25/26/27 variants | end_time = start_time + 5 seconds |
| 7 | Update timestamp_get JSON field | logNames: 2025-04-25/26/27 variants | Unix timestamp of start_time |
| 8 | Update banner_id | All records | banner_id set to '5902' |
| 9 | Insert to production | Filtered records | Move to `clirnetapp.banner_data.banner_call_data` |

### Data Flow
```
clirnet-dev.request_edit.H_5902_distinct_data (staging table)
         ↓ (8 transformation steps)
         ↓
clirnetapp.banner_data.banner_call_data (production table)
```

### Key Parameters for Next Time
- **Source Table**: `clirnet-dev.request_edit.H_5902_distinct_data`
- **Target Table**: `clirnetapp.banner_data.banner_call_data`
- **Banner ID**: 5902
- **Target Dates**: 2025-04-25, 2025-04-26, 2025-04-27
- **Date Groups**:
  - Ph1: 2025-04-01 to 2025-04-21 → map to 2025-04-25
  - Ph1 Alt: 'add-report-prod-server' → map to 2025-04-25
  - Ph2: 2025-04-22 to 2025-04-24 → map to 2025-04-26
  - Ph3: 2025-04-25 to 2025-04-28 → map to 2025-04-27

---

## 2. REPEATABLE PROCESS DESIGN

### A. Pre-Execution Checklist
Before running the procedure, verify:
- [ ] **REQUIREMENTS GATHERED**: Frequency requirement documented (how many banners, at what frequency)
- [ ] **TARGET DATES DEFINED**: List of dates banners should appear in production (e.g., 2025-04-25, 26, 27)
- [ ] **DATE MAPPINGS CREATED**: Mapped which source date ranges feed into each target date
- [ ] Correct banner ID (currently: 5902)
- [ ] Correct source table (currently: `clirnet-dev.request_edit.H_5902_distinct_data`)
- [ ] Correct target table (currently: `clirnetapp.banner_data.banner_call_data`)
- [ ] Backup of staging table created
- [ ] Test run completed on dev environment
- [ ] All date ranges in WHERE clauses are inclusive/exclusive as intended

### B. How to Determine Date Ranges from Frequency Requirements

This is the critical translation step that determines all your SQL queries.

**Step 1: Understand the Requirement**
```
EXAMPLE REQUIREMENT:
"The banner campaign should show 3 distinct banners across Apr 25-27,
with each day showing a different 'batch' of aggregated user requests"
```

**Step 2: Identify Target Dates**
```
From requirement: We need 3 banners on these dates:
- Target Date 1: 2025-04-25
- Target Date 2: 2025-04-26
- Target Date 3: 2025-04-27
```

**Step 3: Analyze Raw Data Distribution**
```
Inspect what date ranges exist in the staging table:
SELECT DATE(timestamp) as date, COUNT(*) as count
FROM staging_table
GROUP BY DATE(timestamp)
ORDER BY date
```

**Step 4: Map Source Dates → Target Dates**
```
Raw data has requests from 2025-04-01 to 2025-04-28

Frequency requirement splits into 3 buckets:
┌─────────────────────────────────────────┐
│ Target Date: 2025-04-25                │
│ Maps from source: 2025-04-01 to 21     │ (21 days of data)
├─────────────────────────────────────────┤
│ Target Date: 2025-04-26                │
│ Maps from source: 2025-04-22 to 24     │ (3 days of data)
├─────────────────────────────────────────┤
│ Target Date: 2025-04-27                │
│ Maps from source: 2025-04-25 to 28     │ (4 days of data)
└─────────────────────────────────────────┘
```

**Step 5: Create Date Mapping Document**
```
Fill this in BEFORE writing any SQL:

PHASE 1 (Target: 2025-04-25):
  Primary source:   DATE(timestamp) BETWEEN '2025-04-01' AND '2025-04-21'
  Alternative:      logName = 'add-report-prod-server'
  Records expected: ~X,XXX

PHASE 2 (Target: 2025-04-26):
  Source:           DATE(timestamp) BETWEEN '2025-04-22' AND '2025-04-24'
  Records expected: ~X,XXX

PHASE 3 (Target: 2025-04-27):
  Source:           DATE(timestamp) BETWEEN '2025-04-25' AND '2025-04-28'
  Records expected: ~X,XXX

TOTAL RECORDS EXPECTED: ~X,XXX
```

---

### C. Execution Workflow

#### Phase 1: Timestamp & LogName Updates (4 queries)
```
Query 1: Update records where DATE(timestamp) BETWEEN [START_DATE_1] AND [END_DATE_1]
         → Set timestamp to [TARGET_DATE_1]
         → Set logName to 'H_5902_distinct_[TARGET_DATE_1]'

Query 2: Update records where logName = '[SPECIAL_LOG_NAME]'
         → Set timestamp to [TARGET_DATE_1]
         → Set logName to 'H_5902_distinct_[TARGET_DATE_1]'

Query 3: Update records where DATE(timestamp) BETWEEN [START_DATE_2] AND [END_DATE_2]
         AND logName NOT IN ([EXCLUDED_LOG_NAMES])
         → Set timestamp to [TARGET_DATE_2]
         → Set logName to 'H_5902_distinct_[TARGET_DATE_2]'

Query 4: Update records where DATE(timestamp) BETWEEN [START_DATE_3] AND [END_DATE_3]
         AND logName NOT IN ([EXCLUDED_LOG_NAMES])
         → Set timestamp to [TARGET_DATE_3]
         → Set logName to 'H_5902_distinct_[TARGET_DATE_3]'
```

#### Phase 2: JSON Payload Updates (3 queries)
```
Query 5: Update start_time for specific logName batch
         FORMULA: FORMAT_TIMESTAMP('%Y-%m-%d %H:%M:%S', TIMESTAMP(DATETIME('[TARGET_DATE]', TIME(TIMESTAMP(jsonPayload.start_time)))))

Query 6: Update end_time for all transformed records
         FORMULA: start_time + INTERVAL 5 SECOND

Query 7: Update timestamp_get for all transformed records
         FORMULA: UNIX_SECONDS(TIMESTAMP(jsonPayload.start_time))
```

#### Phase 3: Banner ID Update (1 query)
```
Query 8: Set banner_id = '[BANNER_ID]' for all records
```

#### Phase 4: Production Migration (1 query)
```
Query 9: INSERT INTO production table
         SELECT FROM staging table WHERE logName IN ([FINAL_LOG_NAMES])
```

### D. Variable Template for Next Iteration

Create a configuration file with these variables:

```yaml
BANNER_CONFIG:
  banner_id: 5902
  source_table: "clirnet-dev.request_edit.H_5902_distinct_data"
  target_table: "clirnetapp.banner_data.banner_call_data"

DATE_MAPPINGS:
  phase_1_primary:
    source_date_range: ["2025-04-01", "2025-04-21"]
    target_date: "2025-04-25"
    logname_suffix: "2025-04-25"

  phase_1_alternative:
    source_log_name: "add-report-prod-server"
    target_date: "2025-04-25"
    logname_suffix: "2025-04-25"

  phase_2:
    source_date_range: ["2025-04-22", "2025-04-24"]
    target_date: "2025-04-26"
    logname_suffix: "2025-04-26"
    exclude_lognames: ["H_5902_distinct_2025-04-25"]

  phase_3:
    source_date_range: ["2025-04-25", "2025-04-28"]
    target_date: "2025-04-27"
    logname_suffix: "2025-04-27"
    exclude_lognames: ["H_5902_distinct_2025-04-25", "H_5902_distinct_2025-04-26"]

FINAL_INSERT:
  lognames_to_insert:
    - "H_5902_distinct_2025-04-25"
    - "H_5902_distinct_2025-04-26"
    - "H_5902_distinct_2025-04-27"
    - "H_5902_distinct_2025-04-28_ph2"
    - "H_5902_distinct_2025-04-29_ph2"
    - "H_5902_distinct_2025-04-30_ph2"
```

### E. Common Pitfalls & Solutions

| Pitfall | Cause | Solution |
|---------|-------|----------|
| Records updated multiple times | Running queries out of order | Run queries sequentially; use logName exclusions in later queries |
| Missing data in final insert | Wrong logName in WHERE clause | Verify logName format matches transformation output |
| Timestamp format errors | Inconsistent DATETIME formatting | Always use ISO format 'YYYY-MM-DD' |
| End_time calculation wrong | Using wrong source field | Always calculate from `jsonPayload.start_time` |
| Duplicate records in production | Running insert query twice | Add `WHERE NOT EXISTS` or truncate staging after insert |

### F. Quick Reference Checklist for Next Run

```
□ 1. Backup source table
□ 2. Run Query Set 1 (4 timestamp/logName updates)
□ 3. Run Query Set 2 (start_time JSON update)
□ 4. Run Query Set 3 (end_time JSON update)
□ 5. Run Query Set 4 (timestamp_get JSON update)
□ 6. Run Query Set 5 (banner_id update)
□ 7. Verify record counts match expectations
□ 8. Run Query Set 6 (INSERT to production)
□ 9. Validate data in production table
□ 10. Delete from staging (optional cleanup)
```

---

## 3. AUTOMATION SUGGESTION

For future improvements, consider automating this with:
- **Python script** using BigQuery client to parameterize the procedure
- **dbt (data build tool)** to manage the transformations as reusable models
- **Scheduled Cloud Function** to run on a timer with configurable variables
