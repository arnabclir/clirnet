# November 2025 Tech Review
## CLIRNET Technology Updates

---

# Slide 2: Mobile App Performance

## App Released with Performance Improvements

**Version:** V-7.2.5 (Production - 14 Nov) | V-7.2.6 (UAT)

**Loading Time Improvements:**
| Feature | Before | After | Improvement |
|---------|--------|-------|-------------|
| Share Link | 8 sec | 4 sec | **50%** |
| Auto Authentication | 9 sec | 3 sec | **67%** |

**Key Highlights:**
- Share functionality now **2x faster**
- Auto-auth flow reduced by **6 seconds**
- Smoother user experience on app launch

---

# Slide 3: Platform Improvements (October Deliverables)

## Backend & Data Quality Enhancements

### 1. ID Collection at Signup
- Mandate ID collection during user signup
- IDs now available to onboarding team for validation
- Streamlined verification process

### 2. Email Validation System
- **Problem:** Difficulty with vendor email delivery
- **Solution:** Implemented email address validation post-registration
- Only validated emails allowed in system communications

**Bulk Email Validation Results:**
| Status | Count |
|--------|-------|
| Deliverable | 422,267 |
| Not Deliverable | 66,218 |
| Error | 905 |

**Result:** Clean email database with **86%+ deliverable addresses**

### 3. User to Client ID Mapping
- Tech built to map users to clients
- Visible in Backend Portal against individual users
- Data tagging work in progress

---

# Slide 4: Session Flow Redesign

## New Session Experience

- Session Flow **redesigned and in development**
- Improved user journey through sessions
- Desktop - https://www.figma.com/proto/FUlR3adNgC6xJAcHsWHK5h/LiveCME-2025-Nov?page-id=0%3A1&node-id=135-1866&viewport=44%2C-3736%2C0.28&t=Zel5vum1QC5MbR8W-1&scaling=min-zoom&content-scaling=fixed&starting-point-node-id=135%3A1866
- Mobile - https://www.figma.com/proto/FUlR3adNgC6xJAcHsWHK5h/LiveCME-2025-Nov?page-id=0%3A1&node-id=587-12139&p=f&viewport=582%2C47%2C0.04&t=PvnVaJ4nATnxG7BH-1&scaling=scale-down&content-scaling=fixed&starting-point-node-id=587%3A12139 

**What's New:**
- Agents Introduction Pane
- Suggested Questions
- View Questions asked by Others

---

# Slide 4: Automated Content - Scale Achieved

## Content Generation at Scale

| Period | Generated | Published | Publish Rate |
|--------|-----------|-----------|--------------|
| October 2024 | 924 | 862 | 93% |
| November 2024 | 1,042 | 955 | 92% |
| **Total** | **1,966** | **1,817** | **92%** |

**Key Achievement:** Nearly **2,000 MedWikis** generated with **92% publish rate**

### 24 Medical Specialties Covered (As of 17th Nov)

| Rank | Specialty | Contents |
|------|-----------|----------|
| 1 | General Medicine / Internal Medicine | 196 |
| 2 | Obstetrics & Gynaecology | 159 |
| 3 | Paediatrics | 155 |
| 4 | Orthopaedics | 86 |
| 5 | General Surgery | 83 |
| 6 | Dermatology | 79 |
| 7 | Cardiology | 77 |
| 8 | Neurology | 70 |
| 9 | Anaesthesiology | 69 |
| 10 | Gastroenterology | 67 |

*+ 14 more specialties including Diabetology (59), Ophthalmology (48), Critical Care (43), Oncology (38), Pulmonology (36), ENT (27), Psychiatry (27), Nephrology (26), and others*

---

# Slide 5: Content Quality & Process

## Standardized Content Pipeline

**10-Step SOP Established:**

```
Topic Generation → Variant Selection → Duplicate Check →
Content Generation → Assignment → Editing & Fact-Check →
Citation Verification → Image Selection → Review → Publish
```

**Key Process Improvements:**
- Editorial guidelines updated for AI-generated images
- Specialty clustering implemented for writer expertise
- Quality checkpoints at multiple stages
- AMA citation style compliance enforced

**Workflow Efficiency:**
- Clear role assignments (writers vs reviewers)
- Systematic duplicate detection
- Structured approval chain

---

# Slide 6: AI Image Generation 

## Image Generation Evolution

### The Challenge
- Photorealistic AI images had anatomical errors (malformed fingers, etc.)
- Risk of content rejection during quality checks
- Conflict between "scientific/real" expectations and AI capabilities

### The Solution
- Shifted default style to **"Illustration Style"**
- Masks anatomical imperfections inherent in current AI technology
- Maintains scientific relevance while being production-safe

### Results
- **Sample batch** produced for review by Editorial team.
- Automated images **approved for MedWiki/Therapy Updates**
- Previous cover image guidelines retired
- Auto generated images are now being evaluated by editorial team for suitability.

---

# Slide 7: Duplicate Detection Optimization

## Semantic Search UI

### The Problem
- **25-45 minutes per article** spent on manual duplicate checking
- Writers searching portal manually for each topic variant
- Significant bottleneck in content pipeline

### The Solution
Built **LLM-powered Semantic Search UI**

**How It Works:**
```
Your Query: "hypertension treatment guidelines"
                    ↓
Expanded to 5+ variants:
• hypertension management guidelines
• HTN treatment protocols
• guidelines for managing essential hypertension
• clinical practice guidelines for blood pressure control
                    ↓
Deduplicated Results with Preview
```

**Features:**
- Intelligent query expansion (1 query → 5+ semantic variants)
- Deduplicated, curated results
- Rich content preview with dates
- Direct links to portal content

**Status:** Sent to Editorial team for testing

---

# Slide 8: VetNet & DentalNet Preparation

## Platform Expansion Readiness

### Multi-Vertical Strategy

- **VetNet & DentalNet integration: ON TRACK**
- Work progressing as per schedule
- Foundation being laid for multi-tenant platform

### What This Enables
- Expand CLIRNET model to veterinary professionals
- Dental practitioner engagement platform
- Shared infrastructure, specialized content


---

# Slide 9: Roadmap & Next Steps

## Upcoming Deliverables

| Initiative | Status | Timeline |
|------------|--------|----------|
| VetNet and DentalNet integration in CLIRNET | In Progress | 2 weeks |
| Content Generation agent improvements (Image, Citations and Format variation) | Immediate | Ongoing |
| Semantic Search CMS integration | Pending | TBD |
| Comment & Conversation agents | Under Development | 2 weeks |
| Content iteration loop - Enable feedback-based regeneration | Under Development | TBD |
| Loading time improvements | **Done** | Completed |

### Priority Focus Areas

1. **VetNet & DentalNet** - Continue on-schedule preparation
2. **Content iteration loop** - Enable feedback-based regeneration
3. **Efficiency gains** - Integrate semantic search into CMS

---

# Summary

## November Highlights

| Area | Achievement |
|------|-------------|
| **Content Scale** | 1,966 generated, 1,817 published (92% rate) |
| **App Performance** | 50-67% faster (Share: 8→4s, Auth: 9→3s) |
| **Data Quality** | 422K+ validated emails, ID collection live |
| **Content Generation Process** | 10-step SOP standardized |
| **Quality** | Image generation approved, editorial alignment |
| **Efficiency** | Semantic search UI built (25 min → faster) |
| **Platform** | VetNet/DentalNet on track |
