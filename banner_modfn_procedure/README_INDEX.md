# Banner Modification Procedure - Documentation Index

## 🎯 Overview

This folder contains complete documentation for the **Banner Modification Procedure** - a data transformation process that modifies historical banner campaign data by updating timestamps, log names, and JSON payload fields, then migrates the corrected data to production at specified frequencies.

### What This Procedure Does
- Transforms raw request data into banner campaign data
- Updates timestamps to target dates based on frequency requirements
- Modifies log names and JSON payload fields
- Migrates processed data to production banner tables
- Handles multi-phase data splitting based on business requirements

### Key Use Cases
- Historical data correction for banner campaigns
- Frequency-based data aggregation (e.g., "3 banners per day")
- Campaign performance analysis with corrected timestamps
- Production data migration from staging to live tables

---

## 📚 Document Reading Guide

### 🆕 **First Time? Start Here**
1. **Read**: [`PROCEDURE_SUMMARY.md`](PROCEDURE_SUMMARY.md) - Complete understanding of the procedure
2. **Review**: [`FREQUENCY_TO_QUERIES_GUIDE.md`](FREQUENCY_TO_QUERIES_GUIDE.md) - How requirements drive the process
3. **Use**: [`PRE_EXECUTION_CHECKLIST.md`](PRE_EXECUTION_CHECKLIST.md) - Step-by-step preparation checklist

### 🔄 **Need to Run the Procedure?**
1. **Complete**: [`PRE_EXECUTION_CHECKLIST.md`](PRE_EXECUTION_CHECKLIST.md) - All preparation tasks
2. **Reference**: [`QUICK_EXECUTION_REFERENCE.md`](QUICK_EXECUTION_REFERENCE.md) - Fast execution guide
3. **Customize**: [`NEXT_RUN_TEMPLATE.md`](NEXT_RUN_TEMPLATE.md) - SQL template with variables

### 📋 **Need the Actual SQL?**
1. **Example**: [`banner_procedure.md`](banner_procedure.md) - Real executed SQL queries (Banner 5902)
2. **Template**: [`NEXT_RUN_TEMPLATE.md`](NEXT_RUN_TEMPLATE.md) - Customizable template for new runs

---

## 📁 File Directory & Usage

| File | Purpose | When to Use | Key Content |
|------|---------|-------------|-------------|
| **`README_INDEX.md`** *(this file)* | Navigation & overview | Always start here | Folder structure, reading guide, quick reference |
| **[`PROCEDURE_SUMMARY.md`](PROCEDURE_SUMMARY.md)** | Complete procedure understanding | First time or deep dive | 7-step process, data flow, requirements gathering, design guide |
| **[`FREQUENCY_TO_QUERIES_GUIDE.md`](FREQUENCY_TO_QUERIES_GUIDE.md)** | Requirement-to-SQL mapping | Understanding how frequency drives queries | Decision trees, common patterns, examples |
| **[`PRE_EXECUTION_CHECKLIST.md`](PRE_EXECUTION_CHECKLIST.md)** | Comprehensive preparation checklist | Before every execution | 7 sections: requirements, data analysis, database prep, testing, validation |
| **[`QUICK_EXECUTION_REFERENCE.md`](QUICK_EXECUTION_REFERENCE.md)** | Fast execution during procedure | During actual execution | 10-step sequence, validation queries, rollback procedures |
| **[`NEXT_RUN_TEMPLATE.md`](NEXT_RUN_TEMPLATE.md)** | SQL template for new runs | When setting up new banner campaign | Customizable queries with variable placeholders |
| **[`banner_procedure.md`](banner_procedure.md)** | Real SQL example (Banner 5902) | Reference for actual query syntax | Executed SQL with specific dates and logic |

---

## 🚀 Quick Start for Different Scenarios

### Scenario 1: "I need to understand what this procedure does"
```
READ ORDER:
1. README_INDEX.md (this file) ← You are here
2. PROCEDURE_SUMMARY.md (Section 1: Procedure Summary)
3. FREQUENCY_TO_QUERIES_GUIDE.md (Flow Chart section)
```

### Scenario 2: "I need to run this procedure tomorrow"
```
PREPARATION ORDER:
1. PRE_EXECUTION_CHECKLIST.md (Complete ALL sections)
2. FREQUENCY_TO_QUERIES_GUIDE.md (Determine your date mappings)
3. NEXT_RUN_TEMPLATE.md (Fill in your specific variables)
4. QUICK_EXECUTION_REFERENCE.md (Keep open during execution)
```

### Scenario 3: "I have a new banner ID and need to customize the SQL"
```
CUSTOMIZATION ORDER:
1. NEXT_RUN_TEMPLATE.md (Start with this template)
2. FREQUENCY_TO_QUERIES_GUIDE.md (Map your frequency requirements)
3. banner_procedure.md (Reference actual query syntax)
4. PRE_EXECUTION_CHECKLIST.md (Validate everything)
```

### Scenario 4: "Something went wrong during execution"
```
TROUBLESHOOTING ORDER:
1. QUICK_EXECUTION_REFERENCE.md (Emergency Rollback section)
2. PRE_EXECUTION_CHECKLIST.md (Section 6: Rollback plan)
3. PROCEDURE_SUMMARY.md (Common Pitfalls section)
```

---

## 🎯 Core Concepts Explained

### **Banner ID**
- Unique identifier for the banner campaign (e.g., 5902)
- Used throughout log names and JSON payloads
- Must be consistent across all transformations

### **Frequency Requirements** 
- Business requirement defining how many banners and when
- Example: "3 banners on Apr 25, 26, 27"
- Drives all subsequent date mapping decisions

### **Date Mapping Strategy**
- How raw data date ranges map to target banner dates
- Critical step that determines all WHERE clauses in SQL
- Must be decided BEFORE writing any queries

### **Phases**
-分组 of data transformation steps
- Phase 1, 2, 3... each mapping different source data to different target dates
- Prevent overlapping updates through logName exclusions

### **Source vs Target Tables**
- **Source**: `clirnet-dev.request_edit.H_[BANNER_ID]_distinct_data` (staging)
- **Target**: `clirnetapp.banner_data.banner_call_data` (production)

---

## 📊 Data Flow Overview

```
Raw Request Data (Source Table)
         ↓ (7 transformation steps)
         ↓
Transformed Banner Data (Source Table)
         ↓ (1 migration step)
         ↓
Production Banner Data (Target Table)
```

### The 7 Transformation Steps:
1. **Phase 1**: Update timestamp & logName (primary source dates)
2. **Phase 1 Alt**: Update timestamp & logName (alternative source)
3. **Phase 2**: Update timestamp & logName (next source dates)
4. **Phase 3**: Update timestamp & logName (final source dates)
5. **JSON start_time**: Format timestamp in JSON payload
6. **JSON end_time**: Calculate end_time = start_time + 5 seconds
7. **JSON timestamp_get**: Convert to Unix timestamp
8. **Banner ID**: Set all records to target banner ID
9. **Production Insert**: Move filtered records to live table

---

## 🔍 Key Decision Points

### **Frequency Analysis**
- How many banners? → Determines number of target dates
- What dates? → Becomes TARGET_DATE_PHASE1, PHASE2, etc.
- How to split data? → Determines source date ranges

### **Date Range Mapping**
- Option A: Split by time periods (consecutive date ranges)
- Option B: Split by volume (equal record counts)
- Option C: Split by logical groups (campaign events, segments)

### **Quality Assurance**
- Backup source data before any transformations
- Validate record counts after each step
- Test with small dataset before full execution
- Verify no duplicate banner IDs in production

---

## ⚡ Quick Reference

### **Essential Variables** (Always fill these first)
```
[BANNER_ID] = 5902 (or your campaign ID)
[SOURCE_TABLE] = clirnet-dev.request_edit.H_[BANNER_ID]_distinct_data
[TARGET_TABLE] = clirnetapp.banner_data.banner_call_data
[TARGET_DATE_PHASE1] = 2025-04-25 (or your first target date)
[TARGET_DATE_PHASE2] = 2025-04-26 (or your second target date)
[TARGET_DATE_PHASE3] = 2025-04-27 (or your third target date)
```

### **Critical Success Factors**
✅ Requirements gathered (frequency, dates, mapping strategy)  
✅ Source data analyzed (date ranges, record volumes)  
✅ Database access confirmed (dev and production)  
✅ Backup procedures in place  
✅ Validation queries prepared  
✅ Team coordination completed  

### **Common Pitfalls**
❌ Running queries without understanding date mappings  
❌ Skipping source data backup  
❌ Not validating record counts after transformations  
❌ Running production insert twice (creates duplicates)  
❌ Missing WHERE clause exclusions in later phases  

---

## 🆘 Getting Help

### **Self-Service**
1. **Procedure unclear?** → Read [`PROCEDURE_SUMMARY.md`](PROCEDURE_SUMMARY.md) Section 1
2. **Don't know your date mappings?** → Use [`FREQUENCY_TO_QUERIES_GUIDE.md`](FREQUENCY_TO_QUERIES_GUIDE.md)
3. **SQL syntax questions?** → Reference [`banner_procedure.md`](banner_procedure.md)
4. **New banner campaign?** → Start with [`NEXT_RUN_TEMPLATE.md`](NEXT_RUN_TEMPLATE.md)

### **Escalation Contacts**
- **Database Team**: ________________
- **Application Team**: ________________  
- **Project Lead**: ________________

### **Version Information**
- **Current Version**: Banner 5902 (April 2025)
- **Template Version**: v2.0
- **Last Updated**: December 2024

---

## 📞 Support Resources

| Need | Resource | Priority |
|------|----------|----------|
| Complete understanding | PROCEDURE_SUMMARY.md | High |
| Execution preparation | PRE_EXECUTION_CHECKLIST.md | Critical |
| During execution | QUICK_EXECUTION_REFERENCE.md | Critical |
| Customization | NEXT_RUN_TEMPLATE.md | High |
| Real example | banner_procedure.md | Medium |
| Decision making | FREQUENCY_TO_QUERIES_GUIDE.md | High |

---

**🎯 Remember**: This procedure transforms historical data - precision and verification at each step is crucial for data integrity. When in doubt, rollback and reassess.