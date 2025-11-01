# Banner Procedure - Quick Execution Reference

## 🚀 EXECUTION SEQUENCE (In Order)

### STEP 1: Backup Source Table
```sql
CREATE TABLE `[SOURCE_TABLE]_backup_[TIMESTAMP]` AS SELECT * FROM `[SOURCE_TABLE]`;
```

### STEP 2: Phase 1 Timestamp & LogName Update (Primary)
```sql
UPDATE `[SOURCE_TABLE]`
SET timestamp = TIMESTAMP(DATETIME('[TARGET_DATE_PHASE1]', TIME(timestamp))),
    logName = 'H_[BANNER_ID]_distinct_[TARGET_DATE_PHASE1]'
WHERE DATE(timestamp) BETWEEN '[SOURCE_START_DATE_PHASE1]' AND '[SOURCE_END_DATE_PHASE1]';
```

### STEP 3: Phase 1 Timestamp & LogName Update (Alternative)
```sql
UPDATE `[SOURCE_TABLE]`
SET timestamp = TIMESTAMP(DATETIME('[TARGET_DATE_PHASE1]', TIME(timestamp))),
    logName = 'H_[BANNER_ID]_distinct_[TARGET_DATE_PHASE1]'
WHERE logName = '[SPECIAL_LOG_NAME]';
```

### STEP 4: Phase 2 Timestamp & LogName Update
```sql
UPDATE `[SOURCE_TABLE]`
SET timestamp = TIMESTAMP(DATETIME('[TARGET_DATE_PHASE2]', TIME(timestamp))),
    logName = 'H_[BANNER_ID]_distinct_[TARGET_DATE_PHASE2]'
WHERE DATE(timestamp) BETWEEN '[SOURCE_START_DATE_PHASE2]' AND '[SOURCE_END_DATE_PHASE2]'
  AND logName NOT IN ('H_[BANNER_ID]_distinct_[TARGET_DATE_PHASE1]');
```

### STEP 5: Phase 3 Timestamp & LogName Update
```sql
UPDATE `[SOURCE_TABLE]`
SET timestamp = TIMESTAMP(DATETIME('[TARGET_DATE_PHASE3]', TIME(timestamp))),
    logName = 'H_[BANNER_ID]_distinct_[TARGET_DATE_PHASE3]'
WHERE DATE(timestamp) BETWEEN '[SOURCE_START_DATE_PHASE3]' AND '[SOURCE_END_DATE_PHASE3]'
  AND logName NOT IN ('H_[BANNER_ID]_distinct_[TARGET_DATE_PHASE1]', 'H_[BANNER_ID]_distinct_[TARGET_DATE_PHASE2]');
```

### STEP 6: Update start_time JSON Field
```sql
UPDATE `[SOURCE_TABLE]`
SET jsonPayload.start_time = FORMAT_TIMESTAMP('%Y-%m-%d %H:%M:%S', TIMESTAMP(DATETIME('[TARGET_DATE_PHASE1]', TIME(TIMESTAMP(jsonPayload.start_time)))))
WHERE logName = 'H_[BANNER_ID]_distinct_[TARGET_DATE_PHASE1]';
```

### STEP 7: Update end_time JSON Field
```sql
UPDATE `[SOURCE_TABLE]`
SET jsonPayload.end_time = FORMAT_TIMESTAMP('%Y-%m-%d %H:%M:%S', TIMESTAMP_ADD(TIMESTAMP(jsonPayload.start_time), INTERVAL 5 SECOND))
WHERE logName IN ('H_[BANNER_ID]_distinct_[TARGET_DATE_PHASE1]', 'H_[BANNER_ID]_distinct_[TARGET_DATE_PHASE2]', 'H_[BANNER_ID]_distinct_[TARGET_DATE_PHASE3]');
```

### STEP 8: Update timestamp_get JSON Field
```sql
UPDATE `[SOURCE_TABLE]`
SET jsonPayload.timestamp_get = UNIX_SECONDS(TIMESTAMP(jsonPayload.start_time))
WHERE logName IN ('H_[BANNER_ID]_distinct_[TARGET_DATE_PHASE1]', 'H_[BANNER_ID]_distinct_[TARGET_DATE_PHASE2]', 'H_[BANNER_ID]_distinct_[TARGET_DATE_PHASE3]');
```

### STEP 9: Update banner_id
```sql
UPDATE `[SOURCE_TABLE]`
SET jsonPayload.banner_id = '[BANNER_ID]'
WHERE 1<>0;
```

### STEP 10: Insert to Production
```sql
INSERT INTO `[TARGET_TABLE]`
SELECT * FROM `[SOURCE_TABLE]`
WHERE logName IN ('H_[BANNER_ID]_distinct_[TARGET_DATE_PHASE1]', 'H_[BANNER_ID]_distinct_[TARGET_DATE_PHASE2]', 'H_[BANNER_ID]_distinct_[TARGET_DATE_PHASE3]');
```

---

## ⚡ VALIDATION QUERIES (Run After Each Step)

### After Steps 2-5 (Timestamp Updates):
```sql
SELECT logName, COUNT(*) as count 
FROM `[SOURCE_TABLE]` 
WHERE logName LIKE 'H_[BANNER_ID]_distinct_%' 
GROUP BY logName 
ORDER BY logName;
```

### After Steps 6-8 (JSON Updates):
```sql
SELECT DISTINCT
  jsonPayload.start_time,
  jsonPayload.end_time,
  jsonPayload.timestamp_get,
  logName
FROM `[SOURCE_TABLE]`
WHERE logName LIKE 'H_[BANNER_ID]_distinct_%'
LIMIT 5;
```

### After Step 9 (Banner ID):
```sql
SELECT DISTINCT jsonPayload.banner_id, COUNT(*) as count
FROM `[SOURCE_TABLE]`
WHERE logName LIKE 'H_[BANNER_ID]_distinct_%'
GROUP BY jsonPayload.banner_id;
```

### Final Validation (After Step 10):
```sql
-- Verify production insert
SELECT DATE(timestamp) as prod_date, COUNT(*) as count
FROM `[TARGET_TABLE]`
WHERE jsonPayload.banner_id = '[BANNER_ID]'
GROUP BY DATE(timestamp)
ORDER BY prod_date;
```

---

## 🎯 CRITICAL VARIABLES (Fill Before Starting)

| Variable | Value |
|----------|-------|
| `[BANNER_ID]` | _______________ |
| `[SOURCE_TABLE]` | _______________ |
| `[TARGET_TABLE]` | _______________ |
| `[TARGET_DATE_PHASE1]` | _______________ |
| `[TARGET_DATE_PHASE2]` | _______________ |
| `[TARGET_DATE_PHASE3]` | _______________ |
| `[SOURCE_START_DATE_PHASE1]` | _______________ |
| `[SOURCE_END_DATE_PHASE1]` | _______________ |
| `[SOURCE_START_DATE_PHASE2]` | _______________ |
| `[SOURCE_END_DATE_PHASE2]` | _______________ |
| `[SOURCE_START_DATE_PHASE3]` | _______________ |
| `[SOURCE_END_DATE_PHASE3]` | _______________ |
| `[SPECIAL_LOG_NAME]` | _______________ |

---

## ⚠️ EMERGENCY ROLLBACK

### If Something Goes Wrong:
```sql
-- Restore from backup
DROP TABLE `[SOURCE_TABLE]`;
CREATE TABLE `[SOURCE_TABLE]` AS SELECT * FROM `[SOURCE_TABLE]_backup_[TIMESTAMP]`;

-- Remove from production (if already inserted)
DELETE FROM `[TARGET_TABLE]` 
WHERE jsonPayload.banner_id = '[BANNER_ID]';
```

---

## 🚨 COMMON MISTAKES TO AVOID

1. **❌ Don't skip the backup** - Always create backup first
2. **❌ Don't run queries out of order** - Follow sequence exactly
3. **❌ Don't forget WHERE exclusions** - Later phases exclude earlier logNames
4. **❌ Don't skip validation** - Check record counts after each step
5. **❌ Don't run insert twice** - Will create duplicates in production

---

## 📊 EXPECTED RESULTS

| Phase | Expected Records | logName Pattern | Target Date |
|-------|-----------------|-----------------|-------------|
| Phase 1 | ~_______ | H_[BANNER_ID]_distinct_[TARGET_DATE_PHASE1] | [TARGET_DATE_PHASE1] |
| Phase 2 | ~_______ | H_[BANNER_ID]_distinct_[TARGET_DATE_PHASE2] | [TARGET_DATE_PHASE2] |
| Phase 3 | ~_______ | H_[BANNER_ID]_distinct_[TARGET_DATE_PHASE3] | [TARGET_DATE_PHASE3] |

**Total Expected: ~_______ records**

---

## ✅ PRE-RUN CHECKLIST (2 minutes)

- [ ] All variables filled in above
- [ ] Source table backup created
- [ ] No existing records with this banner_id in production
- [ ] All queries copied and ready
- [ ] Team notified and ready

**Go Time** ☐ YES ☐ NO

---

## 📞 ESCALATION CONTACTS

- **Database Team**: _______________
- **Project Lead**: _______________
- **Rollback Specialist**: _______________

**Remember**: Data integrity is everything. When in doubt, rollback and reassess.