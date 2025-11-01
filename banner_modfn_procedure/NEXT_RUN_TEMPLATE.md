# Banner Procedure - Next Run Template

## BEFORE YOU START: Determine Your Requirements

**Do not use this template until you have answered these questions:**

### 1. What is the Banner Insertion Frequency Requirement?
```
Example answers:
- "3 banners on 2025-04-25, 2025-04-26, 2025-04-27"
- "1 banner every other day for 2 weeks"
- "Daily banners from Apr 25 to May 5"

YOUR REQUIREMENT:
_________________________________________________________________
```

### 2. What Date Ranges in the Raw Data Map to Each Banner Date?
```
Fill in your mapping:

PHASE 1 (Target Date: ________________)
  Source date range: ________________ to ________________
  OR special log name: ________________
  Expected records: ~__________

PHASE 2 (Target Date: ________________)
  Source date range: ________________ to ________________
  Expected records: ~__________

PHASE 3 (Target Date: ________________)
  Source date range: ________________ to ________________
  Expected records: ~__________

[Add more phases if needed]
```

### 3. How Many Total Banners Will Be Inserted?
```
Total banners = number of target dates above
YOUR ANSWER: __________ banners
```

Once you have this information documented, proceed to the SQL template below.

---

## SQL QUERY TEMPLATE

Use this template for the next banner modification. Fill in the bracketed values based on your requirements above.

---

## STEP 1: Update Timestamp & LogName (Phase 1 - Primary)
```sql
UPDATE `[SOURCE_TABLE]`
SET
  timestamp = TIMESTAMP(DATETIME('[TARGET_DATE_PHASE1]', TIME(timestamp))),
  logName = 'H_[BANNER_ID]_distinct_[TARGET_DATE_PHASE1]'
WHERE DATE(timestamp) BETWEEN '[SOURCE_START_DATE_PHASE1_PRIMARY]' AND '[SOURCE_END_DATE_PHASE1_PRIMARY]'
```

---

## STEP 2: Update Timestamp & LogName (Phase 1 - Alternative)
```sql
UPDATE `[SOURCE_TABLE]`
SET
  timestamp = TIMESTAMP(DATETIME('[TARGET_DATE_PHASE1]', TIME(timestamp))),
  logName = 'H_[BANNER_ID]_distinct_[TARGET_DATE_PHASE1]'
WHERE logName = '[SPECIAL_LOG_NAME]'
```

---

## STEP 3: Update Timestamp & LogName (Phase 2)
```sql
UPDATE `[SOURCE_TABLE]`
SET
  timestamp = TIMESTAMP(DATETIME('[TARGET_DATE_PHASE2]', TIME(timestamp))),
  logName = 'H_[BANNER_ID]_distinct_[TARGET_DATE_PHASE2]'
WHERE
  DATE(timestamp) BETWEEN '[SOURCE_START_DATE_PHASE2]' AND '[SOURCE_END_DATE_PHASE2]'
  AND logName NOT IN ('H_[BANNER_ID]_distinct_[TARGET_DATE_PHASE1]')
```

---

## STEP 4: Update Timestamp & LogName (Phase 3)
```sql
UPDATE `[SOURCE_TABLE]`
SET
  timestamp = TIMESTAMP(DATETIME('[TARGET_DATE_PHASE3]', TIME(timestamp))),
  logName = 'H_[BANNER_ID]_distinct_[TARGET_DATE_PHASE3]'
WHERE
  DATE(timestamp) BETWEEN '[SOURCE_START_DATE_PHASE3]' AND '[SOURCE_END_DATE_PHASE3]'
  AND logName NOT IN ('H_[BANNER_ID]_distinct_[TARGET_DATE_PHASE1]', 'H_[BANNER_ID]_distinct_[TARGET_DATE_PHASE2]')
```

---

## STEP 5: Update start_time JSON Field
```sql
UPDATE `[SOURCE_TABLE]`
SET
  jsonPayload.start_time = FORMAT_TIMESTAMP('%Y-%m-%d %H:%M:%S', TIMESTAMP(DATETIME('[TARGET_DATE_PHASE1]', TIME(TIMESTAMP(jsonPayload.start_time)))))
WHERE logName = 'H_[BANNER_ID]_distinct_[TARGET_DATE_PHASE1]'
```

---

## STEP 6: Update end_time JSON Field
```sql
UPDATE `[SOURCE_TABLE]`
SET
  jsonPayload.end_time = FORMAT_TIMESTAMP('%Y-%m-%d %H:%M:%S', TIMESTAMP_ADD(TIMESTAMP(jsonPayload.start_time), INTERVAL 5 SECOND))
WHERE logName IN (
  'H_[BANNER_ID]_distinct_[TARGET_DATE_PHASE1]',
  'H_[BANNER_ID]_distinct_[TARGET_DATE_PHASE2]',
  'H_[BANNER_ID]_distinct_[TARGET_DATE_PHASE3]'
)
```

---

## STEP 7: Update timestamp_get JSON Field
```sql
UPDATE `[SOURCE_TABLE]`
SET
  jsonPayload.timestamp_get = UNIX_SECONDS(TIMESTAMP(jsonPayload.start_time))
WHERE logName IN (
  'H_[BANNER_ID]_distinct_[TARGET_DATE_PHASE1]',
  'H_[BANNER_ID]_distinct_[TARGET_DATE_PHASE2]',
  'H_[BANNER_ID]_distinct_[TARGET_DATE_PHASE3]'
)
```

---

## STEP 8: Update banner_id
```sql
UPDATE `[SOURCE_TABLE]`
SET jsonPayload.banner_id = '[BANNER_ID]'
WHERE 1<>0
```

---

## STEP 9: Insert to Production Table
```sql
INSERT INTO `[TARGET_TABLE]`
SELECT * FROM `[SOURCE_TABLE]`
WHERE logName IN (
  'H_[BANNER_ID]_distinct_[TARGET_DATE_PHASE1]',
  'H_[BANNER_ID]_distinct_[TARGET_DATE_PHASE2]',
  'H_[BANNER_ID]_distinct_[TARGET_DATE_PHASE3]',
  'H_[BANNER_ID]_distinct_[TARGET_DATE_PHASE2]_ph2',
  'H_[BANNER_ID]_distinct_[TARGET_DATE_PHASE3]_ph2',
  'H_[BANNER_ID]_distinct_[ADDITIONAL_DATE_1]_ph2'
)
```

---

## Variable Reference Guide

| Variable | Source | Example | Notes |
|----------|--------|---------|-------|
| `[BANNER_ID]` | Project specification | 5902 | The campaign banner ID |
| `[SOURCE_TABLE]` | Project specification | clirnet-dev.request_edit.H_5902_distinct_data | Staging table with raw data |
| `[TARGET_TABLE]` | Project specification | clirnetapp.banner_data.banner_call_data | Production table |
| `[TARGET_DATE_PHASE1]` | **From requirement** (frequency need) | 2025-04-25 | Date all phase 1 records should show in production |
| `[TARGET_DATE_PHASE2]` | **From requirement** (frequency need) | 2025-04-26 | Date all phase 2 records should show in production |
| `[TARGET_DATE_PHASE3]` | **From requirement** (frequency need) | 2025-04-27 | Date all phase 3 records should show in production |
| `[SOURCE_START_DATE_PHASE1_PRIMARY]` | **From requirement** (date mapping) | 2025-04-01 | Earliest source date to map to phase 1 target date |
| `[SOURCE_END_DATE_PHASE1_PRIMARY]` | **From requirement** (date mapping) | 2025-04-21 | Latest source date to map to phase 1 target date |
| `[SPECIAL_LOG_NAME]` | **From requirement** (alternate mapping) | add-report-prod-server | Alternative source filter for phase 1 data |
| `[SOURCE_START_DATE_PHASE2]` | **From requirement** (date mapping) | 2025-04-22 | Earliest source date to map to phase 2 target date |
| `[SOURCE_END_DATE_PHASE2]` | **From requirement** (date mapping) | 2025-04-24 | Latest source date to map to phase 2 target date |
| `[SOURCE_START_DATE_PHASE3]` | **From requirement** (date mapping) | 2025-04-25 | Earliest source date to map to phase 3 target date |
| `[SOURCE_END_DATE_PHASE3]` | **From requirement** (date mapping) | 2025-04-28 | Latest source date to map to phase 3 target date |

**KEY INSIGHT**: Most variables marked "From requirement" come from the frequency need mapping you determined at the top of this template. Always fill in that requirements section first.

---

## Pre-Execution Validation

Before running any queries:

1. **Count records by phase in staging table:**
   ```sql
   SELECT logName, COUNT(*) as count FROM `[SOURCE_TABLE]` GROUP BY logName ORDER BY logName
   ```

2. **Verify no duplicate banner_ids already exist in production:**
   ```sql
   SELECT banner_id, COUNT(*) as count FROM `[TARGET_TABLE]` WHERE banner_id = '[BANNER_ID]' GROUP BY banner_id
   ```

3. **Test a single record transformation first:**
   ```sql
   SELECT * FROM `[SOURCE_TABLE]` LIMIT 1
   ```

---

## Post-Execution Validation

After all queries complete:

1. **Verify record counts match:**
   ```sql
   SELECT COUNT(*) as staging_count FROM `[SOURCE_TABLE]` WHERE logName LIKE 'H_[BANNER_ID]_distinct_%'
   SELECT COUNT(*) as production_count FROM `[TARGET_TABLE]` WHERE banner_id = '[BANNER_ID]'
   ```

2. **Sample data check:**
   ```sql
   SELECT * FROM `[TARGET_TABLE]` WHERE banner_id = '[BANNER_ID]' LIMIT 5
   ```

3. **Verify timestamp formats are correct:**
   ```sql
   SELECT DISTINCT
     jsonPayload.start_time,
     jsonPayload.end_time,
     jsonPayload.timestamp_get
   FROM `[TARGET_TABLE]`
   WHERE banner_id = '[BANNER_ID]'
   LIMIT 10
   ```
