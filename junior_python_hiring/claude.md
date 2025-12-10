# Junior Python Hiring - Candidate Evaluation Instructions

This document contains instructions for Claude to automatically evaluate DSPy assignment submissions.

---

## When Asked to "Evaluate Candidates" or "Review Submissions"

Follow this systematic workflow:

### Step 1: Check Already-Evaluated Candidates

Read `candidate_tracking.md` and identify:
- Which candidates have already been evaluated (Status != "Pending")
- Their scores and evaluation details
- Create a list of evaluated candidate names for reference

### Step 2: Find Unevaluated Submission Folders

1. List all directories in `D:\writing\clirnet\junior_python_hiring\`
2. Identify folders that appear to be candidate submissions (typically formatted as `firstname_lastname_assignment` or similar)
3. Exclude:
   - Already evaluated candidates from Step 1
   - System folders
   - The assignment reference materials
4. Create a list of unevaluated candidates to process

### Step 3: Evaluate Each Candidate Using the Rubric

For each unevaluated candidate folder:

#### 3.1 Initial Validation (Quick Check - 5 min)
- **Extract candidate name** from folder name
- **Verify deliverables exist**:
  - Count Mermaid diagram files (should be 10: mermaid_1.md to mermaid_10.md)
  - Check for CSV file (Output.csv, tags.csv, or similar)
  - Check for code file (.py, .ipynb, or notebook file)
- **Document missing deliverables** - if critical items missing, note as auto-fail
- **Update deliverables checklist** in tracking document

#### 3.2 Code Review (15 min)

Read the code file and evaluate against `evaluation_rubric.md` criteria:

**DSPy Framework Usage (12 pts)**:
- Check for proper Signatures: `ExtractEntities`, `DeduplicateEntities`, `ExtractRelations`
- Verify Predictor usage: `dspy.Predict()` and `dspy.ChainOfThought()`
- Check LLM configuration: `dspy.settings.configure()`

**Web Scraping (6 pts)**:
- Review scraping logic, error handling, headers, timeout
- Check text processing, cleaning, length limiting

**Error Handling (6 pts)**:
- Look for try-except blocks around scraping, entity extraction, relations
- Check edge case handling (empty entities, failed scrapes, etc.)

**Code Organization (6 pts)**:
- Assess structure, function usage, readability
- Evaluate comments and documentation quality

**CRITICAL - Confidence Loops (10 pts)**:
- **Deduplication loop**: Must have while loop checking `confidence >= 0.9` (or ~0.91)
- **Relation extraction loop**: Must have confidence loop before Mermaid generation
- This is a KEY DIFFERENTIATOR - no confidence loop = significant point deduction

**Deduplication Logic (8 pts)**:
- Check for batch processing (batch_size parameter)
- Assess deduplication quality

**Pydantic & Validation (7 pts)**:
- Verify BaseModel classes with Field descriptions
- Check for output validation (length checks, filtering)

**Production Readiness (5 pts)**:
- Dependencies properly listed
- API key handling (env variables, not hardcoded)
- Directory creation with os.makedirs
- File naming conventions followed

#### 3.3 Deliverables Quality Assessment (10 min)

**Mermaid Diagrams (12 pts)**:
- Count: All 10 present? (3 pts)
- Syntax: Valid flowchart syntax? Check 2-3 samples (5 pts)
- Entity compliance: Do nodes come from deduplicated list? Sample 2-3 diagrams (4 pts)
  - Look for "external" entities not in the entity list (common issue)

**CSV Quality (8 pts)**:
- Structure: Has columns `link`, `tag`, `tag_type`? (3 pts)
- Completeness: All 10 URLs represented? (3 pts)
- Duplicates: Check for duplicate tags per URL (2 pts)

**Notebook Execution (5 pts)**:
- Assess if code appears runnable (3 pts)
- Check execution flow and organization (2 pts)

#### 3.4 Data Quality Spot-Check (10 min)

**Entity Quality (7 pts)**:
- Sample 2-3 URLs from CSV
- Check if entities are relevant to content (4 pts)
- Verify entity types are accurate (Drug, Disease, Concept, etc.) (3 pts)

**Relationship Quality (5 pts)**:
- Sample 2-3 Mermaid diagrams
- Check if relations make semantic sense (subject-predicate-object) (3 pts)
- Verify predicates are clear and properly trimmed (2 pts)

**Graph Utility (3 pts)**:
- Assess readability and informativeness (2 pts)
- Check complexity (not too sparse or dense) (1 pt)

#### 3.5 Calculate Scores and Document (10 min)

- **Sum all category scores** to get total out of 100
- **Calculate percentage** for each category
- **Assign grade**: A (90-100), B (75-89), C (60-74), D/F (<60)
- **Determine Pass/Fail**: Pass if ≥60, Fail if <60
- **Document findings**:
  - List 3-5 key strengths with specific examples
  - List 3-5 areas for improvement with specific examples
  - Note any critical issues (auto-fail criteria)
  - Write recommendation (Strong Hire / Hire / Maybe / No Hire)
  - Add detailed notes/comments explaining the evaluation

### Step 4: Update candidate_tracking.md

For each evaluated candidate:

#### 4.1 Update Summary Table
- Add/update row with: Candidate Name, Submission Date, "Evaluated" status, Total Score, Grade, Pass/Fail, Reviewer (Claude), Review Date

#### 4.2 Create/Update Detailed Evaluation Section
- If template section exists for the candidate, fill it out completely
- If not, add a new detailed evaluation section with:
  - All category scores filled in
  - Deliverables checklist completed (checked/unchecked)
  - Key strengths (3-5 bullet points with examples)
  - Areas for improvement (3-5 bullet points with examples)
  - Critical issues if any
  - Recommendation checkbox marked
  - Detailed notes/comments

#### 4.3 Update Statistics Section
Calculate and update:
- **Total Candidates Evaluated**: Count of all evaluated candidates
- **Average Score**: Mean of all scores
- **Highest/Lowest Score**: Track extremes
- **Pass/Fail Distribution**: Count and percentage
- **Grade Distribution**: Count by grade band (A/B/C/D-F)
- **Common Issues Found**: List recurring problems across candidates (top 3-5)
- **Common Strengths Observed**: List recurring strengths (top 3-5)

---

## Additional Tasks to Perform

### Automated Quality Checks

When evaluating, automatically flag:

1. **Critical Auto-Fail Issues**:
   - Missing deliverables (< 6 Mermaid files, no CSV, no code)
   - No confidence loop implementation
   - Hardcoded API keys (security risk)
   - Code completely non-functional

2. **Red Flags** (major point deductions):
   - No error handling at all
   - Invalid Mermaid syntax throughout
   - CSV with many duplicates per URL
   - Entities in Mermaid not from deduplicated list
   - No Pydantic models

3. **Quality Indicators** (bonus consideration):
   - Excellent code documentation
   - Robust error handling
   - Clean, reusable function structure
   - High-quality entity extraction
   - Meaningful knowledge graphs

### Comparative Analysis

After evaluating multiple candidates:
- Rank candidates by total score
- Identify standout candidates (top 20%)
- Note consistent strengths/weaknesses across cohort
- Suggest interview priorities based on scores and fit

### Submission Metadata Extraction

For each candidate, attempt to extract:
- Submission timestamp (from file modification dates)
- Code complexity metrics (number of functions, lines of code)
- Deliverable completeness percentage
- Any README or documentation provided

---

## Evaluation Best Practices

### Consistency
- Apply the rubric uniformly across all candidates
- Use the same spot-checking approach (sample 2-3 items)
- Don't let evaluation order bias scoring (early vs. late candidates)

### Objectivity
- Focus on rubric criteria, not subjective preferences
- Document specific examples for all assessments
- Separate "nice to have" from "must have"

### Context Awareness
- This is a **junior position** - some gaps are expected
- Emphasize **learning potential** and **concept understanding** over perfection
- **Production readiness** (error handling, confidence loops) is more important than code elegance

### Thoroughness
- Actually read the code, don't just skim
- Check multiple samples (not just first Mermaid diagram)
- Verify claims (if code says it handles errors, check if it actually does)

### Feedback Quality
- Provide **actionable** areas for improvement
- Give **specific examples** from their submission
- Balance critique with recognition of strengths
- Frame feedback constructively for junior developers

---

## Output Format

When evaluation is complete, provide:

1. **Summary Report**:
   ```
   Evaluated X candidates:
   - [Name 1]: Score/100 (Grade) - Recommendation
   - [Name 2]: Score/100 (Grade) - Recommendation
   ...
   
   Top candidates: [Names]
   Recommended for interview: [Names]
   ```

2. **Confirmation**:
   - "candidate_tracking.md has been updated with detailed evaluations"
   - "Statistics section updated with current cohort data"

3. **Key Insights**:
   - Common strengths across submissions
   - Common issues to address
   - Any standout submissions worth highlighting

---

## Error Handling

If issues arise during evaluation:

- **Missing files**: Document in Critical Issues, apply appropriate point deductions
- **Unreadable code**: Note in evaluation, score based on what's available
- **Ambiguous folder structure**: Ask user for clarification before proceeding
- **Incomplete evaluation_rubric.md or candidate_tracking.md**: Alert user and request files

---

## Time Estimates

- **Per candidate**: ~40-45 minutes
- **For 5 candidates**: ~3-4 hours
- **For 10 candidates**: ~6-8 hours

Plan accordingly and provide progress updates.

---

## candidate_tracking.md Document Format

The `candidate_tracking.md` file follows a specific structure for consistency and navigation. When updating this document, maintain the following format:

### Document Structure Overview

```
# Junior Python Developer - DSPy Assignment Candidate Tracking

> **Last Updated**: YYYY-MM-DD | **Document Owner**: AVP of Product, CLIRNET

---

## Table of Contents
[Clickable links to all sections]

## Executive Summary
[Quick stats table + key insight]

## Candidate Rankings
[Rankings by score and by submission date]

## Evaluation Statistics
[Distribution charts, grade breakdown, score statistics]

## Common Issues & Strengths
[Summary tables with rates]

## Detailed Evaluations
### ✅ Passing Candidates
[Full evaluations for passing candidates]
### ❌ Failing Candidates
[Condensed evaluations for failing candidates]

## Scoring Reference
[Grade bands, category weights, auto-fail criteria]

## Evaluation Workflow
[Process diagram and guidelines]
```

### Section Templates

#### Executive Summary Table

```markdown
| Metric | Value |
|--------|-------|
| **Total Evaluated** | X candidates |
| **Pass Rate** | X% (X passed) |
| **Average Score** | X/100 |
| **Top Performer** | Name (Score/100) |
| **Recommended for Interview** | Name1, Name2, Name3 |
```

#### Candidate Rankings Table

```markdown
| Rank | Candidate | Score | Grade | Status | Recommendation |
|:----:|-----------|:-----:|:-----:|:------:|----------------|
| 1 | [Name](#candidate-name) | **XX** | X | ✅ Pass | Recommendation |
| 2 | [Name](#candidate-name) | **XX** | X | ❌ Fail | Recommendation |
```

#### Passing Candidate Evaluation Template

```markdown
### Candidate: [Name]

| Field | Value |
|-------|-------|
| **Score** | **XX/100** (Grade: X) |
| **Status** | ✅ **PASS** / ❌ **FAIL** |
| **Recommendation** | Hire / Maybe / No Hire |
| **Submitted** | YYYY-MM-DD |
| **Reviewed** | YYYY-MM-DD |

#### Category Scores

| Category | Score | Max | % |
|----------|:-----:|:---:|:-:|
| Code Quality & Implementation | XX | 30 | XX% |
| DSPy Concepts Understanding | XX | 25 | XX% |
| Deliverables Completeness | XX | 25 | XX% |
| Data Quality & Accuracy | XX | 15 | XX% |
| Production Readiness | XX | 5 | XX% |

#### Detailed Breakdown

- DSPy Framework Usage: X/12 (notes)
- Web Scraping: X/6 (notes)
- Error Handling: X/6 (notes)
- Code Organization: X/6 (notes)
- Confidence Loops: X/10 (notes)
- Deduplication Logic: X/8 (notes)
- Pydantic & Validation: X/7 (notes)
- Mermaid Diagrams: X/12 (notes)
- CSV Quality: X/8 (notes)

#### Deliverables

- [x] / [ ] 10 Mermaid diagrams
- [x] / [ ] CSV file with correct structure
- [x] / [ ] Colab notebook
- [x] / [ ] Code runs without errors
- [x] / [ ] All 10 URLs processed

#### Key Strengths

1. **Strength 1** - Specific example
2. **Strength 2** - Specific example
...

#### Areas for Improvement

- **Issue 1** - Details
- **Issue 2** - Details
...

#### Notes

```
Detailed evaluation notes in code block format.
```

[↑ Back to Top](#table-of-contents) | [↑ Back to Rankings](#candidate-rankings)
```

#### Failing Candidate Evaluation Template (Condensed)

```markdown
### Candidate: [Name]

| Field | Value |
|-------|-------|
| **Score** | **XX/100** (Grade: F) |
| **Status** | ❌ **FAIL** |
| **Recommendation** | No Hire - Reject with feedback |
| **Submitted** | YYYY-MM-DD |
| **Reviewed** | YYYY-MM-DD |

#### Category Scores

| Category | Score | Max | % |
|----------|:-----:|:---:|:-:|
| Code Quality & Implementation | XX | 30 | XX% |
| DSPy Concepts Understanding | XX | 25 | XX% |
| Deliverables Completeness | XX | 25 | XX% |
| Data Quality & Accuracy | XX | 15 | XX% |
| Production Readiness | XX | 5 | XX% |

#### Critical Issues

- **AUTO-FAIL: Issue 1**
- **AUTO-FAIL: Issue 2**
- **CRITICAL: Issue 3**

#### Summary

Brief 2-3 sentence summary of why the candidate failed.

[↑ Back to Top](#table-of-contents) | [↑ Back to Rankings](#candidate-rankings)
```

#### Statistics Section Format

```markdown
## Evaluation Statistics

### Overall Distribution

```
Pass (≥60):  ███████░░░░░░░░░░░░░░░░░░░░░░░  X candidates (XX%)
Fail (<60):  ███████████████████████████████  X candidates (XX%)
```

### Grade Breakdown

| Grade | Range | Count | Candidates |
|:-----:|:-----:|:-----:|------------|
| **A** | 90-100 | X | Names |
| **B** | 75-89 | X | Names |
| **C** | 60-74 | X | Names |
| **D/F** | <60 | X | Names |

### Score Statistics

| Metric | Value |
|--------|:-----:|
| Average | XX/100 |
| Median | XX/100 |
| Highest | XX/100 |
| Lowest | XX/100 |
```

#### Common Issues Table Format

```markdown
### 🔴 Common Issues Found

| Issue | Affected | Rate |
|-------|:--------:|:----:|
| **Issue description** | X/Y | XX% |

### 🟢 Common Strengths Observed

| Strength | Achieved | Rate |
|----------|:--------:|:----:|
| **Strength description** | X/Y | XX% |
```

### Navigation Elements

Always include these navigation aids:

1. **Table of Contents** at the top with anchor links
2. **"Back to Top" links** after each major section: `[↑ Back to Top](#table-of-contents)`
3. **"Back to Rankings" links** after each candidate evaluation: `[↑ Back to Rankings](#candidate-rankings)`
4. **Anchor-linked candidate names** in rankings table pointing to detailed evaluations

### Formatting Guidelines

1. **Tables**: Center numeric columns using `:-----:` alignment
2. **Status indicators**: Use ✅ for Pass, ❌ for Fail
3. **Scores**: Bold the score in rankings (`**82**`)
4. **Critical issues**: Prefix with `**AUTO-FAIL:**` or `**CRITICAL:**`
5. **Notes sections**: Use code blocks (```) for detailed evaluation notes
6. **Horizontal rules**: Use `---` to separate major sections
7. **Last Updated**: Always update the timestamp in header and footer

### Maintenance Tasks

When adding new evaluations:

1. Add candidate to Rankings table (both by score and by date)
2. Add detailed evaluation in appropriate section (Passing or Failing)
3. Update Executive Summary metrics
4. Update Statistics section (counts, averages, distributions)
5. Update Common Issues & Strengths if new patterns emerge
6. Update Last Updated timestamp

---

*This workflow ensures systematic, fair, and thorough evaluation of all DSPy assignment submissions.*
