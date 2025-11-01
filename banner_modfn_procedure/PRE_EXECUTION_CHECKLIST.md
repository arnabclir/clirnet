# Banner Modification Procedure - Pre-Execution Checklist

## 🎯 CRITICAL: Complete ALL items before proceeding with banner procedure

This checklist ensures successful execution of the banner modification procedure. Work through each section sequentially.

---

## 📋 SECTION 1: REQUIREMENTS GATHERING

### 1.1 Frequency Requirement Definition
- [ ] **Banner insertion frequency documented**: How many banners, at what frequency?
  - [ ] Example: "3 banners inserted per day"
  - [ ] Example: "1 banner every 2 days" 
  - [ ] Example: "5 banners total: daily for first week, then every 2 days"

- [ ] **Target dates identified**: List exact dates banners should appear in production
  - [ ] Date 1: _______________
  - [ ] Date 2: _______________
  - [ ] Date 3: _______________
  - [ ] Add additional dates as needed: _______________

- [ ] **Total banner count confirmed**: _____ banners total

### 1.2 Banner Campaign Details
- [ ] **Banner ID confirmed**: _______________ (e.g., 5902)
- [ ] **Banner name/description documented**: _______________
- [ ] **Campaign objective understood**: _______________

---

## 📊 SECTION 2: DATA ANALYSIS & DATE MAPPING

### 2.1 Source Data Investigation
- [ ] **Source table identified**: 
  - [ ] Current: `clirnet-dev.request_edit.H_[BANNER_ID]_distinct_data`
  - [ ] Or custom: _______________

- [ ] **Raw data date range confirmed**:
  - [ ] Earliest timestamp: _______________
  - [ ] Latest timestamp: _______________
  - [ ] Total time span: _____ days

- [ ] **Record volume analysis completed**:
  - [ ] Total records in source: _____ records
  - [ ] Records per day analysis: _______________
  - [ ] Special log names identified: _______________

### 2.2 Date Range Mapping Strategy
- [ ] **Phase 1 mapping decided**:
  - [ ] Source date range: _______ to _______
  - [ ] Special log names (if any): _______________
  - [ ] Target date: _______
  - [ ] Expected records: ~_______

- [ ] **Phase 2 mapping decided** (if applicable):
  - [ ] Source date range: _______ to _______
  - [ ] Target date: _______
  - [ ] Expected records: ~_______

- [ ] **Phase 3 mapping decided** (if applicable):
  - [ ] Source date range: _______ to _______
  - [ ] Target date: _______
  - [ ] Expected records: ~_______

- [ ] **Additional phases mapped** (if applicable):
  - [ ] Phase 4: _______ to _______ → _______
  - [ ] Phase 5: _______ to _______ → _______

### 2.3 Validation of Date Mappings
- [ ] **No gaps in source data**: All source dates accounted for
- [ ] **No overlaps between phases**: Date ranges don't conflict
- [ ] **Logical grouping makes sense**: Data split follows business logic
- [ ] **Record count estimates documented**: Per phase expectations recorded

---

## 🗄️ SECTION 3: DATABASE PREPARATION

### 3.1 Environment Setup
- [ ] **Target production table confirmed**: `clirnetapp.banner_data.banner_call_data`
- [ ] **Development environment access verified**: Can access `clirnet-dev.request_edit`
- [ ] **Production environment access verified**: Can write to `clirnetapp.banner_data`
- [ ] **Required permissions confirmed**: SELECT, UPDATE, INSERT privileges

### 3.2 Data Backup & Safety
- [ ] **Source table backup created**: 
  - [ ] Backup method: _______________
  - [ ] Backup location: _______________
  - [ ] Backup verified: _______________

- [ ] **Production table snapshot taken** (if needed):
  - [ ] Snapshot method: _______________
  - [ ] Restore plan documented: _______________

### 3.3 Pre-existing Data Check
- [ ] **No duplicate banner IDs in production**:
  ```sql
  SELECT banner_id, COUNT(*) as count 
  FROM `clirnetapp.banner_data.banner_call_data` 
  WHERE banner_id = '[YOUR_BANNER_ID]' 
  GROUP BY banner_id
  ```
  - [ ] Query executed: _______________
  - [ ] Result: _____ existing records found (should be 0)

---

## 🔧 SECTION 4: SQL QUERY PREPARATION

### 4.1 Template Customization
- [ ] **NEXT_RUN_TEMPLATE.md reviewed**: All variables understood
- [ ] **All [BRACKETED_VALUES] identified**: Complete list created
- [ ] **Date ranges substituted**: All date variables filled in
- [ ] **Banner ID substituted**: All references to [BANNER_ID] updated

### 4.2 Query Validation
- [ ] **Query 1 prepared**: Phase 1 timestamp & logName update
- [ ] **Query 2 prepared**: Phase 1 alternative timestamp & logName update  
- [ ] **Query 3 prepared**: Phase 2 timestamp & logName update
- [ ] **Query 4 prepared**: Phase 3 timestamp & logName update
- [ ] **Query 5 prepared**: start_time JSON field update
- [ ] **Query 6 prepared**: end_time JSON field update
- [ ] **Query 7 prepared**: timestamp_get JSON field update
- [ ] **Query 8 prepared**: banner_id update
- [ ] **Query 9 prepared**: Production table insert

### 4.3 WHERE Clause Logic Verified
- [ ] **Date range boundaries correct**: Inclusive/exclusive as intended
- [ ] **logName exclusions appropriate**: Later phases exclude earlier phase names
- [ ] **Special case handling**: Alternative logName queries included if needed

---

## 🧪 SECTION 5: TESTING & VALIDATION

### 5.1 Test Environment Setup
- [ ] **Test queries ready**: All 9 queries tested on dev environment
- [ ] **Test data validation queries prepared**: Record count checks ready
- [ ] **Rollback plan documented**: Steps to revert if issues occur

### 5.2 Dry Run Validation
- [ ] **Record count pre-transformation**: 
  ```sql
  SELECT logName, COUNT(*) as count 
  FROM `[SOURCE_TABLE]` 
  WHERE DATE(timestamp) BETWEEN '[START_DATE]' AND '[END_DATE]'
  GROUP BY logName
  ```
- [ ] **Single record test completed**: 1 record transformation verified
- [ ] **JSON field formatting test**: start_time, end_time, timestamp_get formats correct
- [ ] **Banner ID assignment test**: banner_id properly set to target value

### 5.3 Expected Results Documented
- [ ] **Post-transformation record counts per phase**: 
  - [ ] Phase 1 expected: _____ records
  - [ ] Phase 2 expected: _____ records  
  - [ ] Phase 3 expected: _____ records
  - [ ] Total expected: _____ records

- [ ] **Expected logName patterns**:
  - [ ] Phase 1: H_[BANNER_ID]_distinct_[TARGET_DATE_1]
  - [ ] Phase 2: H_[BANNER_ID]_distinct_[TARGET_DATE_2]
  - [ ] Phase 3: H_[BANNER_ID]_distinct_[TARGET_DATE_3]

- [ ] **Expected timestamp patterns**:
  - [ ] All Phase 1 records: [TARGET_DATE_1] (same date)
  - [ ] All Phase 2 records: [TARGET_DATE_2] (same date)
  - [ ] All Phase 3 records: [TARGET_DATE_3] (same date)

---

## ⚡ SECTION 6: EXECUTION READINESS

### 6.1 Timeline & Coordination
- [ ] **Execution window scheduled**: 
  - [ ] Start time: _______________
  - [ ] Estimated duration: _____ minutes
  - [ ] End time: _______________

- [ ] **Stakeholders notified**: 
  - [ ] Database team informed: _______________
  - [ ] Application team informed: _______________
  - [ ] Business stakeholders informed: _______________

- [ ] **Rollback window confirmed**: If issues, can rollback within _____ minutes

### 6.2 Final Pre-Run Checklist
- [ ] **All queries copy-paste ready**: No manual typing during execution
- [ ] **Validation queries ready**: Ready to run after each step
- [ ] **Backup verified**: Can restore source table if needed
- [ ] **Team access confirmed**: All required personnel available
- [ ] **Documentation updated**: This checklist completed

---

## 📊 SECTION 7: VALIDATION QUERIES (Ready to Execute)

### 7.1 Pre-Execution Record Counts
```sql
-- Source table record counts by date range
SELECT 
  DATE(timestamp) as source_date,
  COUNT(*) as record_count
FROM `[SOURCE_TABLE]`
WHERE DATE(timestamp) BETWEEN '[START_DATE]' AND '[END_DATE]'
GROUP BY DATE(timestamp)
ORDER BY source_date;
```

### 7.2 Production Table Pre-Check
```sql
-- Current production records for this banner ID
SELECT 
  DATE(timestamp) as prod_date,
  COUNT(*) as record_count
FROM `[TARGET_TABLE]`
WHERE jsonPayload.banner_id = '[BANNER_ID]'
GROUP BY DATE(timestamp)
ORDER BY prod_date;
```

### 7.3 Post-Execution Validation Queries
```sql
-- Verify transformation success
SELECT 
  logName,
  COUNT(*) as record_count,
  MIN(timestamp) as earliest_timestamp,
  MAX(timestamp) as latest_timestamp
FROM `[SOURCE_TABLE]`
WHERE logName LIKE 'H_[BANNER_ID]_distinct_%'
GROUP BY logName
ORDER BY logName;

-- Verify production insert
SELECT 
  DATE(timestamp) as prod_date,
  jsonPayload.banner_id,
  COUNT(*) as record_count
FROM `[TARGET_TABLE]`
WHERE jsonPayload.banner_id = '[BANNER_ID]'
GROUP BY DATE(timestamp), jsonPayload.banner_id
ORDER BY prod_date;
```

---

## 🚨 CRITICAL SUCCESS FACTORS

### Before You Start:
1. **NEVER run queries without understanding date mappings** - This determines everything
2. **Always backup source data** - Transformations cannot be undone
3. **Test with small dataset first** - Validate logic before full execution
4. **Verify no duplicate banner IDs** - Production data integrity is critical
5. **Document all date ranges** - Future you will thank present you

### Common Pitfalls to Avoid:
- [ ] ❌ Running queries out of order
- [ ] ❌ Missing WHERE clause exclusions (logName NOT IN)
- [ ] ❌ Incorrect date range boundaries
- [ ] ❌ Not validating JSON field updates
- [ ] ❌ Inserting duplicate records to production

---

## 📝 COMPLETION SIGN-OFF

- [ ] **All checklist items completed**: _____ of _____ items
- [ ] **Requirements documented and reviewed**: _______________
- [ ] **Queries tested and validated**: _______________
- [ ] **Backup and rollback plan confirmed**: _______________
- [ ] **Team ready for execution**: _______________

**Ready to proceed with banner modification procedure** ☐ YES ☐ NO

---

## 📞 EMERGENCY CONTACTS & RESOURCES

- **Database Team**: _______________
- **Application Team**: _______________  
- **Project Lead**: _______________
- **Rollback Specialist**: _______________

- **Previous successful execution**: Reference PROCEDURE_SUMMARY.md
- **SQL template**: NEXT_RUN_TEMPLATE.md
- **Frequency guidance**: FREQUENCY_TO_QUERIES_GUIDE.md

---

**Remember**: This procedure transforms historical data - precision and verification at each step is crucial for data integrity.