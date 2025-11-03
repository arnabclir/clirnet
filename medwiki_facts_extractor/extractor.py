"""DSPy signatures for medical article fact extraction."""

import dspy
from pydantic import BaseModel, Field
from typing import List


class KeyFact(BaseModel):
    """A key fact extracted from the article."""

    fact: str = Field(description="The key fact statement")
    supporting_statement: str = Field(
        description="Supporting evidence or explanation for the fact"
    )


class ArticleExtraction(BaseModel):
    """Complete extraction from a medical article."""

    summary: str = Field(description="3-4 line summary of the article")
    key_facts: List[KeyFact] = Field(
        description="5-6 key facts with supporting statements"
    )
    topics: List[str] = Field(description="Main medical topics covered")
    keywords: List[str] = Field(description="Important keywords and terms")


class ExtractArticleSignature(dspy.Signature):
    """Extract structured information from a medical article."""

    title: str = dspy.InputField(desc="Title of the medical article")
    description: str = dspy.InputField(
        desc="Full description/content of the medical article"
    )

    summary: str = dspy.OutputField(desc="3-4 line concise summary of the article")
    key_facts_json: str = dspy.OutputField(
        desc="""JSON array of 5-6 key facts, each with 'fact' and 'supporting_statement' fields.
        Example: [{"fact": "...", "supporting_statement": "..."}, ...]"""
    )
    topics: str = dspy.OutputField(
        desc="Comma-separated list of main medical topics covered (e.g., Nephritis, Diabetes, Hypertension)"
    )
    keywords: str = dspy.OutputField(
        desc="Comma-separated list of 5-10 important medical keywords and terms"
    )


class ExtractionPipeline(dspy.Module):
    """Pipeline for extracting facts from articles using DSPy."""

    def __init__(self):
        super().__init__()
        self.extractor = dspy.ChainOfThought(ExtractArticleSignature)

    def forward(self, title: str, description: str) -> ArticleExtraction:
        """Extract facts from an article."""
        # Call the signature
        result = self.extractor(title=title, description=description)

        # Parse key facts JSON
        import json

        try:
            key_facts_list = json.loads(result.key_facts_json)
            key_facts = [KeyFact(**fact) for fact in key_facts_list]
        except (json.JSONDecodeError, TypeError):
            # Fallback if JSON parsing fails
            key_facts = [KeyFact(fact="Could not parse facts", supporting_statement="")]

        # Parse topics and keywords
        topics = [t.strip() for t in result.topics.split(",") if t.strip()]
        keywords = [k.strip() for k in result.keywords.split(",") if k.strip()]

        return ArticleExtraction(
            summary=result.summary,
            key_facts=key_facts,
            topics=topics,
            keywords=keywords,
        )
