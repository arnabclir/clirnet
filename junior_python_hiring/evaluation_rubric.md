# DSPy Assignment Evaluation Rubric

## Total: 100 Points

---

## 1. Code Quality & Implementation (30 points)

### 1.1 DSPy Framework Usage (12 points)
- **Correct DSPy Signatures (4 pts)**
  - 4: Properly defined `ExtractEntities`, `DeduplicateEntities`, and `ExtractRelations` signatures with correct field types
  - 3: Minor issues with field descriptions or types
  - 2: Missing one signature or significant type errors
  - 1: Multiple signature issues
  - 0: Incorrect or missing signatures

- **Predictor Implementation (4 pts)**
  - 4: Correct use of `dspy.Predict()` and `dspy.ChainOfThought()` where appropriate
  - 3: Uses predictors but suboptimal choices (e.g., ChainOfThought everywhere)
  - 2: Incorrect predictor usage or missing ChainOfThought
  - 1: Major implementation errors
  - 0: No proper predictor implementation

- **LLM Configuration (4 pts)**
  - 4: Proper `dspy.settings.configure()` with correct API setup
  - 3: Working configuration with minor issues
  - 2: Configuration works but has hardcoded values or poor practices
  - 1: Configuration issues that partially work
  - 0: No configuration or completely broken

### 1.2 Web Scraping Implementation (6 points)
- **Scraping Logic (3 pts)**
  - 3: Robust scraping with error handling, appropriate headers, timeout
  - 2: Working scraper with some error handling
  - 1: Basic scraping that works but fragile
  - 0: Broken or missing scraping logic

- **Text Processing (3 pts)**
  - 3: Proper text extraction, cleaning, and length limiting (5000 chars as shown in reference)
  - 2: Works but may include noise or improper text selection
  - 1: Minimal processing, lots of irrelevant content
  - 0: No text processing

### 1.3 Error Handling & Robustness (6 points)
- **Exception Handling (3 pts)**
  - 3: Comprehensive try-except blocks for scraping, entity extraction, and relations
  - 2: Some error handling but incomplete
  - 1: Minimal error handling
  - 0: No error handling, code crashes on errors

- **Edge Case Handling (3 pts)**
  - 3: Handles empty entities, failed scrapes, confidence issues gracefully
  - 2: Handles some edge cases
  - 1: Minimal edge case consideration
  - 0: No edge case handling

### 1.4 Code Organization & Style (6 points)
- **Code Structure (3 pts)**
  - 3: Well-organized, logical flow, reusable functions
  - 2: Mostly organized with minor issues
  - 1: Poor organization, hard to follow
  - 0: Chaotic, no structure

- **Comments & Documentation (3 pts)**
  - 3: Clear comments explaining key steps, well-documented
  - 2: Some comments but could be better
  - 1: Minimal comments
  - 0: No comments or documentation

---

## 2. DSPy Concepts Understanding (25 points)

### 2.1 Confidence Loop Implementation (10 points)
- **Deduplication Confidence Loop (5 pts)**
  - 5: Proper while loop checking confidence >= 0.9 (or ~0.91), retries on low confidence
  - 4: Confidence loop exists but threshold slightly off
  - 3: Loop exists but implementation has issues
  - 2: Attempts loop but doesn't work correctly
  - 1: Minimal attempt at confidence checking
  - 0: No confidence loop

- **Relation Extraction Confidence Loop (5 pts)**
  - 5: Proper confidence loop for relation extraction before generating Mermaid
  - 4: Loop exists with minor issues
  - 3: Partial implementation
  - 2: Attempted but flawed
  - 1: Minimal attempt
  - 0: No confidence loop for relations

### 2.2 Entity Deduplication Logic (8 points)
- **Batch Processing (4 pts)**
  - 4: Implements batching (e.g., batch_size=10) for efficient deduplication
  - 3: Batching exists but suboptimal size
  - 2: No batching but attempts deduplication
  - 1: Minimal deduplication effort
  - 0: No deduplication logic

- **Deduplication Quality (4 pts)**
  - 4: Successfully deduplicates similar entities (e.g., "intercrop", "intercrops" → 1 entity)
  - 3: Mostly deduplicates but some duplicates remain
  - 2: Minimal deduplication, many duplicates
  - 1: Deduplication doesn't work well
  - 0: No effective deduplication

### 2.3 Structured Output Validation (7 points)
- **Pydantic Models (4 pts)**
  - 4: Proper `BaseModel` classes with `Field` descriptions for all entities
  - 3: Models exist but missing some fields or descriptions
  - 2: Basic models without proper Field usage
  - 1: Attempted but poorly implemented
  - 0: No Pydantic models

- **Output Validation (3 pts)**
  - 3: Validates outputs, filters invalid entities (e.g., length checks <= 40 chars)
  - 2: Some validation
  - 1: Minimal validation
  - 0: No validation

---

## 3. Deliverables Completeness (25 points)

### 3.1 Mermaid Diagrams (12 points)
- **All 10 Diagrams Present (3 pts)**
  - 3: All 10 mermaid files exist (mermaid_1.md to mermaid_10.md)
  - 2: 8-9 files present
  - 1: 6-7 files present
  - 0: < 6 files

- **Valid Mermaid Syntax (5 pts)**
  - 5: All diagrams have valid syntax (flowchart LR, proper arrows, labels)
  - 4: 1-2 diagrams have minor syntax issues
  - 3: 3-4 diagrams have issues
  - 2: 5-6 diagrams have issues
  - 1: Most diagrams have syntax errors
  - 0: Invalid syntax throughout

- **Entity Compliance (4 pts)**
  - 4: All nodes in diagrams come from deduplicated entity list (strict enforcement)
  - 3: Minor violations (1-2 external entities per diagram)
  - 2: Moderate violations (3-5 external entities)
  - 1: Many entities not from deduplicated list
  - 0: No entity list enforcement

### 3.2 CSV Output (8 points)
- **Correct Structure (3 pts)**
  - 3: CSV has exactly 3 columns: link, tag, tag_type
  - 2: Correct columns but formatting issues
  - 1: Missing columns or wrong names
  - 0: Incorrect structure

- **Data Completeness (3 pts)**
  - 3: All 10 URLs represented with their deduplicated entities
  - 2: 8-9 URLs covered
  - 1: 6-7 URLs covered
  - 0: < 6 URLs

- **No Duplicates per URL (2 pts)**
  - 2: No duplicate tag entries for the same URL
  - 1: Few duplicates (< 5)
  - 0: Many duplicates

### 3.3 Colab Notebook (5 points)
- **Runnable Code (3 pts)**
  - 3: Notebook runs end-to-end without errors
  - 2: Runs with minor manual fixes
  - 1: Requires significant debugging
  - 0: Doesn't run

- **Clear Execution Flow (2 pts)**
  - 2: Logical cell organization, clear outputs shown
  - 1: Disorganized but functional
  - 0: Chaotic or no clear flow

---

## 4. Data Quality & Accuracy (15 points)

### 4.1 Entity Extraction Quality (7 points)
- **Entity Relevance (4 pts)**
  - 4: Extracted entities are highly relevant to content (concepts, drugs, people, etc.)
  - 3: Mostly relevant with some noise
  - 2: Many irrelevant entities
  - 1: Poor entity quality
  - 0: Garbage entities

- **Entity Type Accuracy (3 pts)**
  - 3: `attr_type` correctly identifies semantic types (Drug, Disease, Concept, Person, etc.)
  - 2: Mostly correct with some errors
  - 1: Many type errors
  - 0: Incorrect or missing types

### 4.2 Relationship Quality (5 points)
- **Meaningful Relations (3 pts)**
  - 3: Extracted relations make semantic sense (subject-predicate-object)
  - 2: Mostly meaningful with some odd relations
  - 1: Many nonsensical relations
  - 0: Poor relation quality

- **Predicate Labels (2 pts)**
  - 2: Clear, descriptive predicates trimmed to max 40 chars
  - 1: Predicates exist but unclear or too long
  - 0: Poor predicate quality

### 4.3 Mermaid Graph Utility (3 points)
- **Graph Readability (2 pts)**
  - 2: Diagrams are readable, informative, useful for understanding content
  - 1: Readable but limited value
  - 0: Unreadable or useless

- **Graph Complexity (1 pt)**
  - 1: Appropriate number of nodes/edges (not too sparse or dense)
  - 0: Too simple or overwhelmingly complex

---

## 5. Production Readiness & Best Practices (5 points)

### 5.1 Environment Setup (2 points)
- **Dependencies (1 pt)**
  - 1: Proper pip install commands for all required packages
  - 0: Missing or incorrect dependencies

- **API Key Handling (1 pt)**
  - 1: Uses environment variables or secure key handling
  - 0: Hardcoded keys or insecure practices

### 5.2 Output File Management (2 points)
- **Directory Creation (1 pt)**
  - 1: Creates output directories (os.makedirs) with exist_ok=True
  - 0: No directory management

- **File Naming Convention (1 pt)**
  - 1: Follows naming convention (mermaid_{i}.md, Output.csv/tags.csv)
  - 0: Incorrect naming

### 5.3 Code Reusability (1 point)
- **Functions vs Inline Code (1 pt)**
  - 1: Key logic wrapped in reusable functions
  - 0: All inline code, no functions

---

## Scoring Guidelines

### Grade Bands:
- **90-100 (A)**: Excellent - Strong candidate, hire
- **75-89 (B)**: Good - Solid understanding, consider for next round
- **60-74 (C)**: Average - Some gaps, borderline
- **Below 60 (D/F)**: Weak - Significant issues, likely reject

### Critical Must-Haves (Auto-Fail if Missing):
- All 10 Mermaid diagrams present
- CSV with all 10 URLs
- Runnable code (even if needs minor fixes)
- Evidence of confidence loop implementation

---

## Evaluation Process

1. **Quick Check** (5 min):
   - Count Mermaid files (must be 10)
   - Check CSV exists and has 3 columns
   - Verify notebook file present

2. **Code Review** (15 min):
   - Read through implementation
   - Check for confidence loops, error handling
   - Verify DSPy usage patterns

3. **Testing** (10 min):
   - Validate Mermaid syntax (paste into [Mermaid Live Editor](https://mermaid.live))
   - Check CSV for duplicates, completeness
   - Spot-check entity quality

4. **Scoring** (10 min):
   - Fill out each rubric section
   - Calculate total score
   - Write summary comments

**Total Evaluation Time**: ~40 minutes per candidate

---

## Notes for Evaluators

- **Context Matters**: Assignment emphasizes production-readiness, not just getting results
- **DSPy Understanding**: Key differentiator is proper use of confidence loops and Pydantic validation
- **Quality over Quantity**: Better to have 10 good diagrams than 10 diagrams with garbage entities
- **Red Flags**:
  - No confidence loops (shows didn't understand core concept)
  - No error handling (code will break in production)
  - Hardcoded API keys (security risk)
  - Duplicate entities in CSV (failed deduplication)
  - Invalid Mermaid syntax (didn't test deliverables)
