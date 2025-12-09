# Comments Response Agent Framework

## Purpose

An AI-powered agent that reads every comment on CLIRNET medical content and generates thoughtful, medically-informed responses. Responses are clearly labeled as coming from an AI Assistant.

---

## 1. System Overview

```
┌─────────────────────────────────────────────────────────────┐
│                  Comments Response Agent                     │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   ┌─────────────┐     ┌─────────────┐     ┌─────────────┐   │
│   │   Comment   │────▶│   Context   │────▶│  Response   │   │
│   │   Input     │     │   Enricher  │     │  Generator  │   │
│   └─────────────┘     └─────────────┘     └─────────────┘   │
│                              │                    │          │
│                              ▼                    ▼          │
│                       ┌─────────────┐     ┌─────────────┐   │
│                       │   Article   │     │   Output    │   │
│                       │   Context   │     │   Store     │   │
│                       └─────────────┘     └─────────────┘   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Input Data Structure

Each comment contains:

| Field | Description | Example |
|-------|-------------|---------|
| `type_id` | Article identifier | `35952` |
| `type` | Content type | `medwiki`, `clinical_video`, `training` |
| `title` | Article title | "A Clinician's Guide to CBC Interpretation" |
| `user_master_id` | Commenter ID | `322020` |
| `comment` | Comment text | "Very useful in day to day practice" |
| `added_on` | Timestamp | `2025-11-07T11:37:30` |

---

## 3. Comment Classification

The agent first classifies each comment to determine response strategy:

| Category | Pattern | Response Approach |
|----------|---------|-------------------|
| **Appreciation** | "Good", "Nice", "Excellent", "Very useful" | Thank + add value |
| **Question** | Contains "?", "how", "what", "why", "can" | Direct answer with citations |
| **Feedback** | Suggestions, complaints, issues | Acknowledge + address |
| **Discussion** | Medical opinions, case sharing | Engage + expand |
| **Test/Spam** | "test", single characters, duplicates | Skip or minimal response |

---

## 4. Response Generation Rules

### 4.1 Response Structure

```
[Acknowledgment] + [Value Addition] + [Engagement Prompt]
```

**Example:**
```
Thank you for your feedback, Doctor! You're right that CBC interpretation
is fundamental to daily clinical practice. A key point to remember is that
the RDW (Red Cell Distribution Width) is often overlooked but can be an
early indicator of iron deficiency even before hemoglobin drops.

Would you like to share any specific CBC patterns you've found challenging
to interpret in your practice?

— AI Assistant
```

### 4.2 Response Guidelines

| Guideline | Description |
|-----------|-------------|
| **Tone** | Professional, collegial, respectful of medical expertise |
| **Length** | 50-150 words (concise but substantive) |
| **Medical accuracy** | Reference evidence-based guidelines, cite sources when possible |
| **Personalization** | Reference the specific article/topic |
| **Engagement** | End with a question or invitation to discuss |
| **Signature** | Always end with "— AI Assistant" |

### 4.3 Content-Type Specific Approaches

| Content Type | Focus |
|--------------|-------|
| `medwiki` | Clinical guidelines, recent updates, practical applications |
| `clinical_video` | Key takeaways, related techniques, implementation tips |
| `training` | Learning outcomes, practice integration, CME value |

---

## 5. Response Templates

### Template 1: Appreciation Response
```
Thank you for your kind words, Doctor! [Article Topic] is indeed crucial
for [clinical context].

One additional consideration: [relevant medical insight not in article].

Have you encountered any challenging cases related to this topic?

— AI Assistant
```

### Template 2: Question Response
```
Great question! [Direct answer to question].

According to [guideline/source], [supporting evidence].

[Practical tip for implementation].

Feel free to share more about your specific case for further discussion.

— AI Assistant
```

### Template 3: Feedback Response
```
Thank you for sharing this feedback. [Acknowledge the specific point].

[Address the concern or explain the rationale].

Your input helps us improve the content for the medical community.

— AI Assistant
```

### Template 4: Discussion Response
```
Excellent point, Doctor! Your observation about [topic] aligns with
recent findings in [relevant area].

[Expand on the discussion with additional context].

What has been your experience with [related aspect]?

— AI Assistant
```

---

## 6. Medical Knowledge Integration

### 6.1 Knowledge Sources

The agent should reference:
- Current clinical practice guidelines (ACC/AHA, WHO, RCOG, etc.)
- Recent medical literature (within 2-3 years)
- Drug interactions and contraindications
- Differential diagnosis considerations
- Evidence levels (Level A, B, C recommendations)

### 6.2 Safety Guardrails

| Rule | Implementation |
|------|----------------|
| No diagnosis | Never diagnose specific patient cases |
| No prescriptions | Never recommend specific dosages or drugs for patients |
| Defer to physician | Always acknowledge the doctor's clinical judgment |
| Cite uncertainty | Clearly state when evidence is limited |
| Emergency redirect | For urgent queries, recommend immediate specialist consultation |

---

## 7. Processing Pipeline

### 7.1 Batch Processing Flow

```python
for each comment in comments:
    1. Classify comment type
    2. Extract article context (title, type, topic)
    3. Identify medical domain (cardiology, orthopedics, etc.)
    4. Generate response using LLM
    5. Apply safety checks
    6. Store response with metadata
    7. Log progress to file
```

### 7.2 Progress Monitoring

Following MLOps team pattern - continuous file updates:

```python
{
    "status": "processing",
    "total_comments": 1112,
    "processed": 450,
    "skipped": 12,
    "errors": 2,
    "current_article": "A Clinician's Guide to CBC Interpretation",
    "updated_at": "2025-11-07T14:30:00"
}
```

---

## 8. Output Format

### 8.1 Response Record

```json
{
    "comment_id": "c_35952_322020_1730979450",
    "original_comment": "Very useful in day to day practice",
    "article_title": "A Clinician's Guide to CBC Interpretation",
    "article_type": "medwiki",
    "comment_category": "appreciation",
    "response": "Thank you for your feedback, Doctor! You're right that...",
    "generated_at": "2025-11-07T15:00:00",
    "model": "claude-3-opus",
    "tokens_used": 245
}
```

### 8.2 Batch Output File

```
output/
├── responses_2025-11-07.json      # All responses
├── responses_2025-11-07.csv       # For easy review/export
└── progress.json                   # Real-time progress
```

---

## 9. Quality Assurance

### 9.1 Pre-Generation Checks
- Skip duplicate comments (same user, same text, same article)
- Skip test comments ("test", single characters)
- Detect language (skip non-English for now)

### 9.2 Post-Generation Checks
- Response length within bounds (50-150 words)
- Contains signature "— AI Assistant"
- No prohibited content (specific diagnoses, prescriptions)
- Medical claims have qualifiers ("studies suggest", "guidelines recommend")

---

## 10. Example Responses

### Example 1: Simple Appreciation
**Comment:** "Very useful in day to day practice"
**Article:** "A Clinician's Guide to CBC Interpretation"

**Response:**
> Thank you, Doctor! CBC interpretation is indeed a cornerstone of daily clinical practice. One often-overlooked parameter is the RDW (Red Cell Distribution Width), which can signal early iron deficiency or mixed anemias before other indices change.
>
> A practical tip: when you see a normal MCV with elevated RDW, consider early iron deficiency or a combined deficiency state.
>
> Are there specific CBC patterns you encounter frequently in your practice?
>
> — AI Assistant

---

### Example 2: Technical Question
**Comment:** "Is there something wrong with the playback speed? Why can't I increase it?"
**Article:** "Management of Heatstroke: Immediate Interventions"

**Response:**
> Thank you for reporting this, Doctor. This appears to be a technical issue with the video player rather than the content itself. Our technical team has been notified.
>
> In the meantime, the key takeaways from this video on heatstroke management include: (1) rapid cooling is priority one—target core temp below 39°C within 30 minutes, (2) ice packs at groin, axilla, and neck are most effective, and (3) avoid antipyretics as they're ineffective for environmental hyperthermia.
>
> We'll work on resolving the playback issue. Thank you for your patience!
>
> — AI Assistant

---

### Example 3: Medical Discussion
**Comment:** "What is the Role of carovarine and vinpocetin that are usually promoted with gingko alkaloids"
**Article:** "Pharmacological therapy for tinnitus"

**Response:**
> Excellent question, Doctor! Caroverine and vinpocetine are indeed frequently marketed alongside Ginkgo biloba for tinnitus, though their evidence base varies.
>
> **Caroverine** is a glutamate antagonist that showed some promise in acute tinnitus in early studies, but robust RCT evidence remains limited.
>
> **Vinpocetine** is a synthetic derivative of vincamine with vasodilatory and neuroprotective properties. While some studies suggest benefit for inner ear circulation, Cochrane reviews have not found sufficient evidence to recommend routine use.
>
> Current guidelines suggest these may be considered as adjunctive therapy, but patient expectations should be managed carefully.
>
> What has been your clinical experience with these agents?
>
> — AI Assistant

---

## 11. Implementation Checklist

- [ ] Set up LLM API (Claude/OpenAI)
- [ ] Build comment classifier
- [ ] Create response templates
- [ ] Implement medical domain detection
- [ ] Add safety guardrails
- [ ] Build batch processing pipeline
- [ ] Create progress monitoring
- [ ] Design output storage
- [ ] Build review/approval interface
- [ ] Integration with CLIRNET backend

---

## 12. Future Enhancements

1. **Multi-language support** - Hindi, regional languages
2. **Specialist routing** - Complex queries to domain experts
3. **Sentiment tracking** - Monitor engagement trends
4. **Auto-posting** - Direct integration with comment system
5. **Feedback loop** - Learn from edited/rejected responses
