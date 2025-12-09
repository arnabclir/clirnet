# Comments Response Agent - Implementation Plan

## Overview

Build an AI-powered system to generate medically-informed responses to 1,112 doctor comments on CLIRNET content. Responses will be generated using Claude 3.5 Sonnet, validated with safety checks, and auto-posted if they pass all checks.

**Timeline:** 1-2 weeks
**Scope:** Core generation engine (JSON/CSV output, no web UI)
**Posting:** Auto-post responses passing safety checks
**Budget:** $5-20 (Claude 3.5 Sonnet for all responses)

---

## Project Structure

```
D:\writing\clirnet\comments_agent\
├── pyproject.toml              # NEW: uv dependency management
├── .env                        # NEW: API keys (gitignored)
├── .python-version             # NEW: 3.12.10
│
├── src/
│   ├── __init__.py             # NEW
│   ├── config.py               # NEW: Configuration with pydantic-settings
│   ├── models.py               # NEW: Pydantic models for type safety
│   ├── classifier.py           # NEW: Comment categorization logic
│   ├── response_generator.py  # NEW: Claude API integration
│   ├── safety_checker.py       # NEW: Medical guardrails
│   ├── progress_monitor.py     # NEW: File-based progress tracking
│   └── batch_processor.py      # NEW: Main orchestration
│
├── prompts/
│   ├── system_prompt.txt       # NEW: Base medical safety prompt
│   └── templates/
│       ├── appreciation.txt    # NEW: Template for appreciation comments
│       ├── question.txt        # NEW: Template for questions
│       ├── feedback.txt        # NEW: Template for feedback
│       └── discussion.txt      # NEW: Template for discussions
│
├── scripts/
│   ├── excel_to_toon.py        # EXISTS: Keep as-is
│   ├── process_comments.py     # NEW: Main execution script
│   └── retry_failed.py         # NEW: Reprocess failed comments
│
├── data/
│   ├── input/
│   │   └── comments_toon.txt   # EXISTS: 1,112 comments
│   └── output/
│       ├── responses_YYYYMMDD.json    # NEW: Generated responses
│       ├── responses_YYYYMMDD.csv     # NEW: For review
│       ├── skipped_comments.json      # NEW: Test/spam/duplicates
│       ├── failed_comments.json       # NEW: Processing errors
│       └── progress.json              # NEW: Real-time status
│
└── logs/
    └── processing_YYYYMMDD.log        # NEW: Detailed logs
```

---

## Implementation Steps

### **Week 1: Foundation & Core Logic**

#### Day 1: Project Setup
**Goal:** Set up development environment and dependencies

1. **Initialize uv project**
   ```bash
   cd D:\writing\clirnet\comments_agent
   uv init --name clirnet-comments-agent --python 3.12
   ```

2. **Add dependencies**
   ```bash
   uv add anthropic pandas python-toon pydantic pydantic-settings \
          python-dotenv rich tenacity httpx openpyxl
   ```

3. **Create `.env` file**
   ```bash
   ANTHROPIC_API_KEY=sk-ant-...
   MODEL=claude-3-5-sonnet-20241022
   BATCH_SIZE=10
   MAX_RETRIES=3
   ```

4. **Create directory structure**
   - Create `src/`, `prompts/`, `prompts/templates/`, `scripts/`, `data/output/`, `logs/`

**Deliverable:** Working Python environment with all dependencies

---

#### Day 2: Data Models & Configuration
**Goal:** Type-safe foundation for entire system

**File:** `src/models.py`
```python
from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime

class CommentCategory(str, Enum):
    APPRECIATION = "appreciation"
    QUESTION = "question"
    FEEDBACK = "feedback"
    DISCUSSION = "discussion"
    SPAM = "spam"
    TECHNICAL = "technical"

class Comment(BaseModel):
    type_id: int
    type: str  # medwiki, clinical_video, training
    title: str
    user_master_id: int
    comment: str
    added_on: datetime

    @property
    def comment_id(self) -> str:
        """Unique ID for deduplication"""
        timestamp = int(self.added_on.timestamp())
        return f"c_{self.type_id}_{self.user_master_id}_{timestamp}"

class Classification(BaseModel):
    category: CommentCategory
    confidence: float = Field(ge=0.0, le=1.0)
    classified_at: datetime

class ResponseContent(BaseModel):
    text: str
    word_count: int
    model: str
    tokens_input: int
    tokens_output: int
    cost_usd: float
    generated_at: datetime

class SafetyCheckResult(BaseModel):
    passed: bool
    has_signature: bool
    word_count_valid: bool
    no_diagnosis: bool
    no_prescription: bool
    has_qualifiers: bool
    warnings: list[str] = []

class GeneratedResponse(BaseModel):
    comment_id: str
    comment: Comment
    classification: Classification
    response: ResponseContent
    safety_check: SafetyCheckResult
    review_status: str  # approved, pending_review, rejected
```

**File:** `src/config.py`
```python
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

class Settings(BaseSettings):
    # API Configuration
    anthropic_api_key: str
    model: str = "claude-3-5-sonnet-20241022"

    # Processing Parameters
    batch_size: int = 10
    max_retries: int = 3
    rate_limit_per_minute: int = 50

    # Paths
    base_dir: Path = Path(__file__).parent.parent
    input_toon_file: Path = base_dir / "data" / "input" / "comments_toon.txt"
    output_dir: Path = base_dir / "data" / "output"
    prompts_dir: Path = base_dir / "prompts"

    # Safety Thresholds
    min_word_count: int = 50
    max_word_count: int = 150

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
```

**Deliverable:** Type-safe data models and configuration

---

#### Day 3: Comment Classifier
**Goal:** Categorize comments to select appropriate response template

**File:** `src/classifier.py`
```python
import re
from anthropic import Anthropic
from .models import Comment, Classification, CommentCategory
from .config import settings

class CommentClassifier:
    def __init__(self):
        self.client = Anthropic(api_key=settings.anthropic_api_key)

    def classify(self, comment: Comment) -> Classification:
        """Classify comment using pattern matching + LLM fallback"""

        # Quick pattern-based classification
        text_lower = comment.comment.lower().strip()

        # Spam/Test detection
        if self._is_spam(text_lower):
            return Classification(
                category=CommentCategory.SPAM,
                confidence=1.0,
                classified_at=datetime.now()
            )

        # Technical issues
        if self._is_technical(text_lower):
            return Classification(
                category=CommentCategory.TECHNICAL,
                confidence=0.9,
                classified_at=datetime.now()
            )

        # Question detection
        if "?" in comment.comment or any(word in text_lower for word in ["what", "how", "why", "when", "can you"]):
            return Classification(
                category=CommentCategory.QUESTION,
                confidence=0.85,
                classified_at=datetime.now()
            )

        # Simple appreciation
        if self._is_appreciation(text_lower):
            return Classification(
                category=CommentCategory.APPRECIATION,
                confidence=0.8,
                classified_at=datetime.now()
            )

        # Use LLM for ambiguous cases
        return self._llm_classify(comment)

    def _is_spam(self, text: str) -> bool:
        """Detect test/spam comments"""
        spam_patterns = [
            r"^test\s*\d*$",
            r"^[a-z]$",  # single character
            r"^ok$",
            r"^\.+$",
        ]
        return any(re.match(pattern, text) for pattern in spam_patterns)

    def _is_technical(self, text: str) -> bool:
        """Detect technical issues"""
        technical_keywords = [
            "not playing", "can't play", "video", "playback",
            "speed", "loading", "error", "not working"
        ]
        return any(keyword in text for keyword in technical_keywords)

    def _is_appreciation(self, text: str) -> bool:
        """Detect simple appreciation"""
        appreciation_keywords = [
            "good", "nice", "excellent", "great", "useful",
            "helpful", "thank", "informative"
        ]
        return (len(text.split()) <= 10 and
                any(keyword in text for keyword in appreciation_keywords))

    def _llm_classify(self, comment: Comment) -> Classification:
        """Use LLM for complex classification"""
        prompt = f"""Classify this doctor's comment on a medical article.

Article: {comment.title}
Comment: {comment.comment}

Categories:
- appreciation: Simple positive feedback
- question: Asking for information
- feedback: Suggestions or concerns
- discussion: Medical insights or case sharing

Return only the category name."""

        response = self.client.messages.create(
            model=settings.model,
            max_tokens=20,
            messages=[{"role": "user", "content": prompt}]
        )

        category_text = response.content[0].text.strip().lower()
        category = CommentCategory(category_text)

        return Classification(
            category=category,
            confidence=0.7,
            classified_at=datetime.now()
        )
```

**Deliverable:** Working classifier with pattern matching + LLM fallback

---

#### Day 4: Response Generator
**Goal:** Generate medically-informed responses using Claude

**File:** `prompts/system_prompt.txt`
```
You are a medical AI assistant for CLIRNET, responding to comments from doctors on medical articles, videos, and training content.

CRITICAL SAFETY RULES:
1. NEVER diagnose specific patient cases
2. NEVER prescribe medications or recommend specific dosages
3. NEVER provide emergency medical advice
4. ALWAYS defer to the doctor's clinical judgment
5. ALWAYS use qualifiers: "studies suggest", "guidelines recommend", "evidence indicates"
6. ALWAYS cite sources when making medical claims (e.g., "According to ACC/AHA guidelines...")

RESPONSE STRUCTURE:
1. Acknowledgment: Thank the doctor professionally
2. Value Addition: Provide relevant medical insight related to the article topic
3. Engagement Prompt: Ask a question to encourage further discussion
4. Signature: Always end with "— AI Assistant"

REQUIREMENTS:
- Length: 50-150 words
- Tone: Professional, collegial, respectful of medical expertise
- Personalize to the specific article and comment
- Provide evidence-based information
- Encourage engagement and discussion

FORMATTING:
- Use clear paragraphs
- No bullet points unless listing clinical criteria
- Professional medical vocabulary
- End every response with "— AI Assistant"
```

**File:** `prompts/templates/appreciation.txt`
```
The doctor wrote: "{comment}"
On the article: "{title}" ({type})

Generate a response that:
1. Thanks them for the positive feedback
2. Adds one relevant medical insight not fully covered in the article
3. Asks if they've encountered related clinical scenarios
4. Ends with "— AI Assistant"
```

**File:** `prompts/templates/question.txt`
```
The doctor asked: "{comment}"
On the article: "{title}" ({type})

Generate a response that:
1. Directly answers their question with evidence-based information
2. Cites relevant guidelines or studies
3. Provides practical clinical application
4. Invites them to share their experience
5. Ends with "— AI Assistant"
```

**File:** `src/response_generator.py`
```python
from anthropic import Anthropic
from tenacity import retry, stop_after_attempt, wait_exponential
from pathlib import Path
from .models import Comment, Classification, ResponseContent
from .config import settings

class ResponseGenerator:
    def __init__(self):
        self.client = Anthropic(api_key=settings.anthropic_api_key)
        self.system_prompt = self._load_prompt("system_prompt.txt")
        self.templates = {
            "appreciation": self._load_prompt("templates/appreciation.txt"),
            "question": self._load_prompt("templates/question.txt"),
            "feedback": self._load_prompt("templates/feedback.txt"),
            "discussion": self._load_prompt("templates/discussion.txt"),
            "technical": self._load_prompt("templates/technical.txt"),
        }

    def _load_prompt(self, filename: str) -> str:
        path = settings.prompts_dir / filename
        return path.read_text(encoding="utf-8")

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(min=1, max=60))
    def generate(self, comment: Comment, classification: Classification) -> ResponseContent:
        """Generate response with retry logic"""

        template = self.templates[classification.category.value]
        user_prompt = template.format(
            comment=comment.comment,
            title=comment.title,
            type=comment.type
        )

        response = self.client.messages.create(
            model=settings.model,
            max_tokens=300,
            system=self.system_prompt,
            messages=[{"role": "user", "content": user_prompt}]
        )

        response_text = response.content[0].text.strip()
        word_count = len(response_text.split())

        # Calculate cost (Sonnet pricing: $3/$15 per MTok)
        input_tokens = response.usage.input_tokens
        output_tokens = response.usage.output_tokens
        cost_usd = (input_tokens * 0.003 + output_tokens * 0.015) / 1000

        return ResponseContent(
            text=response_text,
            word_count=word_count,
            model=settings.model,
            tokens_input=input_tokens,
            tokens_output=output_tokens,
            cost_usd=cost_usd,
            generated_at=datetime.now()
        )
```

**Deliverable:** Working response generator with retry logic

---

### **Week 2: Safety, Processing & Execution**

#### Day 5: Safety Checker
**Goal:** Validate responses against medical guardrails

**File:** `src/safety_checker.py`
```python
import re
from .models import ResponseContent, SafetyCheckResult
from .config import settings

class SafetyChecker:
    def check(self, response: ResponseContent) -> SafetyCheckResult:
        """Run all safety checks"""

        text = response.text
        warnings = []

        # Check 1: Signature
        has_signature = text.strip().endswith("— AI Assistant")
        if not has_signature:
            warnings.append("Missing signature")

        # Check 2: Word count
        word_count_valid = (settings.min_word_count <= response.word_count <= settings.max_word_count)
        if not word_count_valid:
            warnings.append(f"Word count {response.word_count} outside range {settings.min_word_count}-{settings.max_word_count}")

        # Check 3: No diagnosis
        diagnosis_patterns = [
            r"you have\s+\w+",
            r"diagnosed with",
            r"your patient has",
            r"this patient has",
            r"I diagnose"
        ]
        no_diagnosis = not any(re.search(pattern, text, re.IGNORECASE) for pattern in diagnosis_patterns)
        if not no_diagnosis:
            warnings.append("Contains diagnosis language")

        # Check 4: No prescriptions
        prescription_patterns = [
            r"prescribe\s+\d+\s*mg",
            r"take\s+\d+\s+tablets",
            r"administer\s+\d+",
            r"give\s+\d+\s*mg"
        ]
        no_prescription = not any(re.search(pattern, text, re.IGNORECASE) for pattern in prescription_patterns)
        if not no_prescription:
            warnings.append("Contains prescription language")

        # Check 5: Has qualifiers
        qualifier_keywords = ["may", "suggest", "recommend", "consider", "evidence", "studies", "guidelines"]
        has_qualifiers = any(keyword in text.lower() for keyword in qualifier_keywords)
        if not has_qualifiers:
            warnings.append("Missing qualifying language for medical claims")

        # Overall pass/fail
        critical_checks = [has_signature, word_count_valid, no_diagnosis, no_prescription]
        passed = all(critical_checks)

        return SafetyCheckResult(
            passed=passed,
            has_signature=has_signature,
            word_count_valid=word_count_valid,
            no_diagnosis=no_diagnosis,
            no_prescription=no_prescription,
            has_qualifiers=has_qualifiers,
            warnings=warnings
        )
```

**Deliverable:** Safety checker with medical guardrails

---

#### Day 6: Progress Monitor & Batch Processor
**Goal:** Orchestrate entire pipeline with progress tracking

**File:** `src/progress_monitor.py`
```python
import json
from pathlib import Path
from datetime import datetime
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn

class ProgressMonitor:
    def __init__(self, output_dir: Path):
        self.progress_file = output_dir / "progress.json"
        self.console = Console()
        self.stats = {
            "status": "initializing",
            "started_at": datetime.now().isoformat(),
            "total_comments": 0,
            "processed": 0,
            "skipped": 0,
            "failed": 0,
            "approved": 0,
            "pending_review": 0,
            "total_cost_usd": 0.0,
        }

    def update(self, **kwargs):
        """Update progress stats"""
        self.stats.update(kwargs)
        self.stats["updated_at"] = datetime.now().isoformat()
        self._save()
        self._display()

    def _save(self):
        """Save to file (MLOps pattern)"""
        self.progress_file.write_text(json.dumps(self.stats, indent=2))

    def _display(self):
        """Display in terminal"""
        self.console.print(f"[green]Progress:[/green] {self.stats['processed']}/{self.stats['total_comments']} | "
                          f"[yellow]Cost:[/yellow] ${self.stats['total_cost_usd']:.2f}")
```

**File:** `src/batch_processor.py`
```python
from toon import decode
from pathlib import Path
from .models import Comment, GeneratedResponse
from .classifier import CommentClassifier
from .response_generator import ResponseGenerator
from .safety_checker import SafetyChecker
from .progress_monitor import ProgressMonitor
from .config import settings

class BatchProcessor:
    def __init__(self):
        self.classifier = CommentClassifier()
        self.generator = ResponseGenerator()
        self.safety_checker = SafetyChecker()
        self.monitor = ProgressMonitor(settings.output_dir)

        self.responses = []
        self.skipped = []
        self.failed = []

    def load_comments(self) -> list[Comment]:
        """Load comments from TOON file"""
        toon_data = settings.input_toon_file.read_text(encoding="utf-8")
        parsed = decode(toon_data)

        # Parse TOON structure (Sheet1 contains comments)
        sheet_data = parsed.get("Sheet1", [])
        comments = [Comment(**record) for record in sheet_data]

        # Deduplicate
        seen = set()
        unique_comments = []
        for c in comments:
            if c.comment_id not in seen:
                seen.add(c.comment_id)
                unique_comments.append(c)

        return unique_comments

    def process(self):
        """Main processing loop"""
        comments = self.load_comments()
        self.monitor.update(total_comments=len(comments), status="processing")

        for i, comment in enumerate(comments):
            try:
                # Classify
                classification = self.classifier.classify(comment)

                # Skip spam
                if classification.category == "spam":
                    self.skipped.append({"comment_id": comment.comment_id, "reason": "spam"})
                    self.monitor.update(skipped=len(self.skipped))
                    continue

                # Generate response
                response_content = self.generator.generate(comment, classification)

                # Safety check
                safety_result = self.safety_checker.check(response_content)

                # Determine review status
                review_status = "approved" if safety_result.passed else "pending_review"

                # Create response record
                generated_response = GeneratedResponse(
                    comment_id=comment.comment_id,
                    comment=comment,
                    classification=classification,
                    response=response_content,
                    safety_check=safety_result,
                    review_status=review_status
                )

                self.responses.append(generated_response)

                # Update stats
                self.monitor.update(
                    processed=i + 1,
                    approved=sum(1 for r in self.responses if r.review_status == "approved"),
                    pending_review=sum(1 for r in self.responses if r.review_status == "pending_review"),
                    total_cost_usd=sum(r.response.cost_usd for r in self.responses)
                )

                # Save checkpoint every 50 comments
                if (i + 1) % 50 == 0:
                    self._save_checkpoint()

            except Exception as e:
                self.failed.append({"comment_id": comment.comment_id, "error": str(e)})
                self.monitor.update(failed=len(self.failed))

        # Final save
        self._save_results()
        self.monitor.update(status="completed")

    def _save_checkpoint(self):
        """Save intermediate results"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        checkpoint_file = settings.output_dir / f"checkpoint_{timestamp}.json"
        self._save_to_file(checkpoint_file)

    def _save_results(self):
        """Save final results"""
        timestamp = datetime.now().strftime("%Y%m%d")

        # JSON
        json_file = settings.output_dir / f"responses_{timestamp}.json"
        self._save_to_file(json_file)

        # CSV
        csv_file = settings.output_dir / f"responses_{timestamp}.csv"
        self._save_to_csv(csv_file)

        # Skipped/Failed
        (settings.output_dir / "skipped_comments.json").write_text(
            json.dumps(self.skipped, indent=2)
        )
        (settings.output_dir / "failed_comments.json").write_text(
            json.dumps(self.failed, indent=2)
        )

    def _save_to_file(self, filepath: Path):
        """Save responses to JSON"""
        data = [r.model_dump(mode="json") for r in self.responses]
        filepath.write_text(json.dumps(data, indent=2, default=str))

    def _save_to_csv(self, filepath: Path):
        """Save responses to CSV for review"""
        import pandas as pd
        records = []
        for r in self.responses:
            records.append({
                "comment_id": r.comment_id,
                "article_title": r.comment.title,
                "comment": r.comment.comment,
                "category": r.classification.category.value,
                "response": r.response.text,
                "word_count": r.response.word_count,
                "status": r.review_status,
                "warnings": ", ".join(r.safety_check.warnings),
                "cost_usd": r.response.cost_usd
            })
        df = pd.DataFrame(records)
        df.to_csv(filepath, index=False)
```

**Deliverable:** Complete processing pipeline

---

#### Day 7: Main Script & Testing
**Goal:** Create runnable script and test end-to-end

**File:** `scripts/process_comments.py`
```python
#!/usr/bin/env python3
"""Process comments and generate AI responses"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.batch_processor import BatchProcessor

def main():
    print("Starting Comments Response Agent...")
    processor = BatchProcessor()
    processor.process()
    print("✓ Processing complete!")
    print(f"✓ Results saved to {processor.monitor.progress_file.parent}")

if __name__ == "__main__":
    main()
```

**Testing:**
1. Test with 10 sample comments first
2. Review output quality
3. Verify safety checks work
4. Run full batch (1,112 comments)

**Deliverable:** Working end-to-end system

---

## Critical Files

| File | Purpose | Priority |
|------|---------|----------|
| `src/batch_processor.py` | Main orchestration | Critical |
| `src/response_generator.py` | Claude API integration | Critical |
| `src/safety_checker.py` | Medical guardrails | Critical |
| `prompts/system_prompt.txt` | AI behavior definition | Critical |
| `src/models.py` | Type-safe data structures | High |
| `src/classifier.py` | Comment categorization | High |
| `src/config.py` | Configuration management | Medium |

---

## Cost Estimate

**Assumptions:**
- 1,112 comments total
- ~100 test/spam (skip)
- 1,012 real comments to process
- Avg 300 input tokens (TOON context + prompt)
- Avg 150 output tokens (response)

**Calculation:**
- Input: 1,012 × 300 × $0.003/1K = $0.91
- Output: 1,012 × 150 × $0.015/1K = $2.28
- **Total: ~$3.20**

Well within $5-20 budget!

---

## Auto-Posting Implementation

**File:** `src/poster.py` (Day 8-9, optional)

```python
class ResponsePoster:
    def __init__(self, api_base_url: str):
        self.api_base_url = api_base_url

    def post_approved(self, responses: list[GeneratedResponse]):
        """Post responses that passed safety checks"""
        for response in responses:
            if response.review_status == "approved":
                self._post_to_api(response)

    def _post_to_api(self, response: GeneratedResponse):
        """POST to CLIRNET backend API"""
        # Implementation depends on backend API structure
        # POST /api/comments/{comment_id}/ai-response
        pass
```

---

## Success Criteria

- [ ] All 1,112 comments processed
- [ ] >95% pass safety checks (auto-approved)
- [ ] <5% require manual review
- [ ] Total cost <$5
- [ ] Processing time <30 minutes
- [ ] Responses saved to JSON/CSV

---

## Next Steps After Core

1. **Review Interface** (Week 3): Build FastAPI UI for manual review
2. **Backend Integration** (Week 4): Connect to CLIRNET API for auto-posting
3. **Monitoring Dashboard** (Week 5): Track response engagement metrics
4. **Continuous Processing** (Week 6): Handle new comments automatically
