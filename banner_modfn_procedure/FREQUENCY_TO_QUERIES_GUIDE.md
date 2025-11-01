# Banner Procedure: From Frequency Requirement to SQL Queries

A quick reference showing how banner insertion frequency requirements drive the entire data transformation procedure.

---

## The Flow Chart

```
┌──────────────────────────────────────────────────────────────┐
│ STEP 1: Frequency Requirement                               │
│ "Insert 3 banners on Apr 25, 26, 27"                       │
└────────────────────┬─────────────────────────────────────────┘
                     │
                     ▼
┌──────────────────────────────────────────────────────────────┐
│ STEP 2: Identify Target Dates                               │
│ • Target Date 1: 2025-04-25 (1st banner)                   │
│ • Target Date 2: 2025-04-26 (2nd banner)                   │
│ • Target Date 3: 2025-04-27 (3rd banner)                   │
└────────────────────┬─────────────────────────────────────────┘
                     │
                     ▼
┌──────────────────────────────────────────────────────────────┐
│ STEP 3: Analyze Raw Data & Map Dates                        │
│ Raw data spans 2025-04-01 to 2025-04-28                    │
│                                                              │
│ How to split into 3 phases?                                │
│ → Look at record volume per day                            │
│ → Split to roughly equal buckets OR by logical groups      │
│                                                              │
│ Result:                                                     │
│ • Phase 1 → 2025-04-01 to 21 maps to target 2025-04-25    │
│ • Phase 2 → 2025-04-22 to 24 maps to target 2025-04-26    │
│ • Phase 3 → 2025-04-25 to 28 maps to target 2025-04-27    │
└────────────────────┬─────────────────────────────────────────┘
                     │
                     ▼
┌──────────────────────────────────────────────────────────────┐
│ STEP 4: Generate SQL Queries                                │
│                                                              │
│ Query 1: UPDATE WHERE timestamp BETWEEN 2025-04-01 AND 21  │
│          SET timestamp = 2025-04-25, logName = ...         │
│                                                              │
│ Query 2: UPDATE WHERE timestamp BETWEEN 2025-04-22 AND 24  │
│          SET timestamp = 2025-04-26, logName = ...         │
│                                                              │
│ Query 3: UPDATE WHERE timestamp BETWEEN 2025-04-25 AND 28  │
│          SET timestamp = 2025-04-27, logName = ...         │
│                                                              │
│ Queries 4-7: Update JSON fields (start_time, end_time, etc)│
│                                                              │
│ Query 8: INSERT filtered records to production table       │
└──────────────────────────────────────────────────────────────┘
```

---

## Decision Points: Frequency → Date Mapping

When you have a frequency requirement, answer these questions to determine your date mappings:

### Question 1: How Many Banners?
```
Frequency requirement tells you the number of target dates
Example: "3 banners daily" → You need 3 target dates
Example: "1 banner every 2 days" → You need multiple target dates across the time period
```

### Question 2: What Dates Should They Appear?
```
The dates when banners should be inserted into production
Example: 2025-04-25, 2025-04-26, 2025-04-27
These become your TARGET_DATE_PHASE1, PHASE2, PHASE3, etc.
```

### Question 3: How Much Raw Data for Each Banner?
```
This depends on your raw data distribution and how you want to split it.

Option A: Split by volume
- Divide total records equally among banners
- If you have 10M records and 3 banners → ~3.3M per banner

Option B: Split by time periods
- Assign continuous date ranges to each banner
- Phase 1: Apr 1-21 (21 days)
- Phase 2: Apr 22-24 (3 days)
- Phase 3: Apr 25-28 (4 days)

Option C: Split by logical groups
- Group by campaign event, hour of day, user segment, etc.
- Whatever makes sense for your use case
```

### Question 4: What Are the Source Date Ranges?
```
Once you've decided how to split the data, identify the
DATE(timestamp) ranges in the staging table that correspond
to each banner's portion.

These become your:
- [SOURCE_START_DATE_PHASE1] / [SOURCE_END_DATE_PHASE1]
- [SOURCE_START_DATE_PHASE2] / [SOURCE_END_DATE_PHASE2]
- [SOURCE_START_DATE_PHASE3] / [SOURCE_END_DATE_PHASE3]
```

---

## Example: Working Through a New Frequency Requirement

### Requirement Given:
```
"We need to insert 5 distinct banners over the next 5 days,
starting Apr 25. Each banner should show aggregated requests
from different time slices of the past month."
```

### Step 1: How Many Banners?
```
Answer: 5 banners (for 5 days)
```

### Step 2: What Dates?
```
Answer:
- Target Date Phase 1: 2025-04-25
- Target Date Phase 2: 2025-04-26
- Target Date Phase 3: 2025-04-27
- Target Date Phase 4: 2025-04-28
- Target Date Phase 5: 2025-04-29
```

### Step 3: How Much Raw Data Each?
```
We have requests from 2025-03-26 to 2025-04-24 (30 days of data)

Split 30 days across 5 banners = 6 days per banner

Answer:
- Phase 1: Mar 26-31 (6 days)
- Phase 2: Apr 1-6 (6 days)
- Phase 3: Apr 7-12 (6 days)
- Phase 4: Apr 13-18 (6 days)
- Phase 5: Apr 19-24 (6 days)
```

### Step 4: Source Date Ranges
```
Answer:
[SOURCE_START_DATE_PHASE1] = 2025-03-26
[SOURCE_END_DATE_PHASE1] = 2025-03-31

[SOURCE_START_DATE_PHASE2] = 2025-04-01
[SOURCE_END_DATE_PHASE2] = 2025-04-06

[SOURCE_START_DATE_PHASE3] = 2025-04-07
[SOURCE_END_DATE_PHASE3] = 2025-04-12

[SOURCE_START_DATE_PHASE4] = 2025-04-13
[SOURCE_END_DATE_PHASE4] = 2025-04-18

[SOURCE_START_DATE_PHASE5] = 2025-04-19
[SOURCE_END_DATE_PHASE5] = 2025-04-24
```

### Step 5: Fill Template
```
Now use NEXT_RUN_TEMPLATE.md and substitute all your
bracketed values with the answers above, then run the queries.
```

---

## Quick Decision Tree

```
START: Got a frequency requirement?
       ↓
   1. Extract target dates
       ↓
   2. Determine: How to split raw data?
       ├─ By volume? → Calculate records per banner
       ├─ By time? → Assign date ranges
       └─ By logic? → Identify grouping criteria
       ↓
   3. Identify source date ranges for each split
       ↓
   4. Document in template (BEFORE writing SQL)
       ↓
   5. Run NEXT_RUN_TEMPLATE.md with your values
       ↓
   DONE
```

---

## Common Frequency Patterns

### Pattern 1: Daily Banners
```
Requirement: "1 banner per day for 7 days"
→ 7 target dates (one per day)
→ Divide 30 days of raw data into 7 phases
→ ~4 days of raw data per banner
```

### Pattern 2: Rotating Banners
```
Requirement: "3 rotating banners, repeat every 3 days for 30 days"
→ 3 distinct target dates (repeated)
→ All banners show the same 3 dates
→ Divide raw data equally among 3 phases
```

### Pattern 3: Frequency Ramp-Up
```
Requirement: "Start with 1 banner daily, increase to 2 after week 1, then 3 after week 2"
→ Variable number of target dates
→ Different number of phases for different time periods
→ More complex date range mapping
```

### Pattern 4: Single Banner Event
```
Requirement: "One special banner on Apr 25 only"
→ 1 target date
→ All raw data maps to this one target
→ 1 phase, all records get timestamp = 2025-04-25
```
