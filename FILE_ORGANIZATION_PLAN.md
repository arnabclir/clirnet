# CLIRNET MLOps - File Organization Plan

**Date:** 2025-12-28
**Status:** Proposed
**Total Files Analyzed:** ~292 files across ~68 directories

---

## Executive Summary

The current directory structure contains mixed-purpose files including research, documentation, scripts, hiring materials, client projects, and technical reviews. This plan proposes a structured reorganization to improve navigability, maintainability, and team collaboration.

---

## Current State Analysis

### Directory Structure Overview

```
clirnet/
├── banner_modfn_procedure/        # Banner modification procedures (9 docs)
├── bloom-filter-use-cases/        # Research/analysis docs (3 files)
├── calculators/                   # Idea doc (empty)
├── client project/                # MICE client work (5 docs)
├── comments_agent/                # AI agent project (11 files incl. Python/Excel)
├── Dec Tech Review Preparation/   # Meeting notes & reviews (12 files)
├── econnect/                      # ETL scripts & data (10 files)
├── gemma_dspy/                    # Python project with uv (5 files)
├── junior_python_hiring/          # Hiring evaluations (~50+ candidate folders)
├── medwiki_facts_extractor/       # Python project (16 files)
├── PoC-Repo/                      # Analysis doc (1 file)
├── template_issue/                # Implementation plans (4 files)
├── user_match/                    # Project with scripts/docs
├── vm_comparison/                 # Infrastructure comparison (2 files)
├── backend_tasklist.md            # Root level doc
├── to-do-list.md                  # Root level doc
└── claude.md                      # Project instructions
```

### Identified Issues

1. **Inconsistent naming conventions** (spaces, mixed cases)
2. **Mixed file types** at root level (should be in subdirectories)
3. **No clear separation** between active projects, archives, and references
4. **Client work mixed** with internal projects
5. **Hiring materials not isolated** from production code
6. **No dedicated areas** for: research, documentation, scripts, data

---

## Proposed Organization Structure

```
clirnet/
│
├── README.md                              # Main repository README
├── CLAUDE.md                              # AI assistant instructions (keep at root)
├── .gitignore                             # Existing (keep)
│
├── 01_active_projects/                    # Current/ongoing development work
│   ├── banner_automation/                 # From: banner_modfn_procedure/
│   │   ├── procedures/
│   │   ├── automation_scripts/
│   │   └── documentation/
│   ├── comments_agent/                    # Move from root
│   │   ├── src/
│   │   ├── data/
│   │   └── docs/
│   ├── medwiki_facts_extractor/          # Move from root
│   │   ├── src/
│   │   ├── tests/
│   │   ├── data/
│   │   └── docs/
│   ├── user_match/                        # Move from root
│   │   ├── scripts/
│   │   ├── docs/
│   │   ├── reference/
│   │   └── sample_data/
│   └── gemma_dspy/                        # Move from root
│       ├── src/
│       └── tests/
│
├── 02_client_projects/                    # All client-facing work
│   ├── MICE/                              # From: client project/MICE/
│   │   ├── documentation/
│   │   ├── legal/
│   │   └── requirements/
│   └── econnect/                          # Move from root
│       ├── src/
│       ├── data/
│       └── output/
│
├── 03_research_analysis/                  # Research, PoCs, technical analysis
│   ├── bloom_filter/                      # From: bloom-filter-use-cases/
│   ├── vm_infrastructure/                 # From: vm_comparison/
│   ├── poc/                               # From: PoC-Repo/
│   └── calculators/                       # Move from root
│
├── 04_documentation/                      # Meeting notes, reviews, plans
│   ├── tech_reviews/                      # From: Dec Tech Review Preparation/
│   │   ├── 2024-10/
│   │   ├── 2024-11/
│   │   └── 2024-12/
│   ├── implementation_plans/              # From: template_issue/
│   └── backend/
│       └── tasklist.md                    # From: backend_tasklist.md
│
├── 05_hiring/                             # All hiring-related materials
│   ├── junior_python_2024/                # From: junior_python_hiring/
│   │   ├── candidates/
│   │   │   ├── evaluated/
│   │   │   ├── pending/
│   │   │   └── selected/
│   │   ├── assignments/
│   │   └── evaluation_criteria/
│   └── templates/
│
├── 06_archives/                           # Completed/inactive projects
│   └── [projects no longer active]
│
└── 07_shared_resources/                   # Common utilities, templates
    ├── python_templates/
    ├── documentation_templates/
    └── scripts/
```

---

## Categorization Logic

### 01_active_projects/
**Criteria:** Currently maintained, has active development, production code

| Source Directory | Destination | Rationale |
|-----------------|-------------|-----------|
| `banner_modfn_procedure/` | `banner_automation/` | Active automation work |
| `comments_agent/` | `comments_agent/` | Active AI agent project |
| `medwiki_facts_extractor/` | `medwiki_facts_extractor/` | Active extraction pipeline |
| `user_match/` | `user_match/` | Active matching system |
| `gemma_dspy/` | `gemma_dspy/` | Active ML experimentation |

### 02_client_projects/
**Criteria:** Billable work, external stakeholders, client deliverables

| Source Directory | Destination | Rationale |
|-----------------|-------------|-----------|
| `client project/MICE/` | `MICE/` | Client-specific work |
| `econnect/` | `econnect/` | Client data pipeline |

### 03_research_analysis/
**Criteria:** Exploratory work, technical investigations, PoCs

| Source Directory | Destination | Rationale |
|-----------------|-------------|-----------|
| `bloom-filter-use-cases/` | `bloom_filter/` | Technical research |
| `vm_comparison/` | `vm_infrastructure/` | Infrastructure analysis |
| `PoC-Repo/` | `poc/` | Proof of concept work |
| `calculators/` | `calculators/` | Research ideas |

### 04_documentation/
**Criteria:** Meeting notes, reviews, plans, non-code documentation

| Source Directory | Destination | Rationale |
|-----------------|-------------|-----------|
| `Dec Tech Review Preparation/` | `tech_reviews/` | Meeting materials by date |
| `template_issue/` | `implementation_plans/` | Strategic planning docs |
| `backend_tasklist.md` | `backend/tasklist.md` | Team-specific tasks |

### 05_hiring/
**Criteria:** All recruiting, candidate evaluation, interview materials

| Source Directory | Destination | Rationale |
|-----------------|-------------|-----------|
| `junior_python_hiring/` | `junior_python_2024/` | Organized by position/year |

---

## Standardization Guidelines

### Directory Naming
- Use **snake_case** for all directories
- No spaces in names (use underscores)
- Prefix with numbers for ordering (01_, 02_, etc.)
- Use descriptive, self-explanatory names

### File Naming
- Python: `snake_case.py`
- Documentation: `Title_Case.md` or `snake_case.md` (be consistent)
- Data: `descriptive_name_YYYY-MM-DD.ext`
- Scripts: `verb_noun.py` (e.g., `extract_data.py`)

### Project Structure Template
Each active project should follow:
```
project_name/
├── src/                    # Source code
├── tests/                  # Test files
├── data/                   # Input data (gitignored if large)
├── output/                 # Generated output (gitignored)
├── docs/                   # Project documentation
├── scripts/                # Utility scripts
├── README.md               # Project overview
└── pyproject.toml          # If using uv
```

---

## Migration Steps

### Phase 1: Preparation (No file changes)
1. [ ] Review this plan with MLOps team
2. [ ] Identify any files not covered in analysis
3. [ ] Get approval for proposed structure
4. [ ] Create backup of current state (git tag)

### Phase 2: Create New Structure
1. [ ] Create numbered directory structure (01_ to 07_)
2. [ ] Create subdirectories within each category
3. [ ] Set up proper .gitignore for data/ and output/ folders
4. [ ] Create README.md in each major directory

### Phase 3: Move Files (By category)
1. [ ] Move `client project/MICE/` → `02_client_projects/MICE/`
2. [ ] Move `econnect/` → `02_client_projects/econnect/`
3. [ ] Move `junior_python_hiring/` → `05_hiring/junior_python_2024/`
4. [ ] Move `Dec Tech Review Preparation/` → `04_documentation/tech_reviews/2024-12/`
5. [ ] Move `banner_modfn_procedure/` → `01_active_projects/banner_automation/`
6. [ ] Move `comments_agent/` → `01_active_projects/comments_agent/`
7. [ ] Move `medwiki_facts_extractor/` → `01_active_projects/`
8. [ ] Move `gemma_dspy/` → `01_active_projects/`
9. [ ] Move `user_match/` → `01_active_projects/`
10. [ ] Move research items → `03_research_analysis/`
11. [ ] Move remaining docs → `04_documentation/`

### Phase 4: Cleanup
1. [ ] Rename directories to snake_case
2. [ ] Standardize file naming within projects
3. [ ] Remove empty directories
4. [ ] Update any path references in code
5. [ ] Create main README.md at root

### Phase 5: Verification
1. [ ] Verify all files are accounted for
2. [ ] Test that scripts still work with new paths
3. [ ] Update documentation with new structure
4. [ ] Commit changes with descriptive message

---

## Handling Special Cases

### Large Data Files
- CSV/JSON files over 1MB should be in project-specific `data/` folders
- Ensure `.gitignore` excludes:
  - `*.csv` (except sample data)
  - `*.xlsx` (unless template/reference)
  - `output/` directories

### Candidate Submissions
- Structure: `05_hiring/junior_python_2024/candidates/evaluated/{candidate_name}/`
- Keep evaluation rubrics separate from submissions
- Archive old hiring drives by year

### Client Work
- Isolate completely from internal projects
- Use client name as directory name
- Keep legal/docs in clearly marked subdirectories

---

## Git Strategy

### Pre-Migration
```bash
git tag pre-reorganization-$(date +%Y-%m-%d)
git checkout -b reorganization
```

### Post-Migration
```bash
git add -A
git commit -m "Reorganize repository structure

- Categorize files by purpose (active, client, research, docs, hiring)
- Standardize directory naming to snake_case
- Create numbered prefixes for logical ordering
- Add README documentation for new structure

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com"
```

### Merge Strategy
- Create PR for team review
- Squash merge to single commit on main
- Keep tag for rollback if needed

---

## Team Responsibilities

### MLOps Team Members
| Member | Responsibility |
|--------|----------------|
| Arnab | Review active project categorization |
| Nirmalendu | Verify script paths still work post-migration |
| Soumya | Review client project organization |
| Ajmal | Update documentation |
| Siddharth | Test hiring directory structure |

### AVP Product (Aritra)
- Final approval on structure
- Communicate changes to stakeholders
- Update any external references

---

## Success Criteria

1. [ ] All 292 files successfully migrated
2. [ ] No broken file paths in code
3. [ ] Team can navigate to any file within 30 seconds
4. [ ] New team members understand structure without extensive training
5. [ ] .gitignore properly excludes generated/large files
6. [ ] README.md exists at root and in each major directory

---

## Open Questions

1. Should `junior_python_hiring` be moved to a separate repository for privacy?
2. Are there any compliance/legal considerations for client project organization?
3. Should large datasets be moved to external storage (S3, etc.)?
4. Do we need a separate area for "shared utilities" used across projects?
5. Should we implement a monorepo tool (nx, turborepo) for better project management?

---

## Appendix: File Inventory

### By Category

#### Active Projects (~100 files)
- comments_agent: 11 files (Python, Excel, docs)
- medwiki_facts_extractor: 16 files (Python, tests)
- gemma_dspy: 5 files (Python project)
- user_match: ~20 files (scripts, docs, data)
- banner_modfn_procedure: 9 files (docs, procedures)

#### Client Projects (~25 files)
- MICE: 5 files (legal, docs)
- econnect: 10 files (Python scripts, JSON, CSV)

#### Research (~10 files)
- bloom-filter-use-cases: 3 files
- vm_comparison: 2 files
- PoC-Repo: 1 file
- calculators: 1 file

#### Documentation (~50 files)
- Dec Tech Review Preparation: 12 files
- template_issue: 4 files
- Various markdown at root

#### Hiring (~100+ files)
- junior_python_hiring: 50+ candidate folders with submissions

---

**Next Steps:** Schedule team review meeting to discuss and approve this plan.
