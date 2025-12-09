"""Process medical articles and extract facts using DSPy and MiniMax-M2."""

import csv
import json
import os
import sys
from pathlib import Path
from typing import List, Dict, Any

import dspy
from extractor import ExtractionPipeline, ArticleExtraction


class ArticleProcessor:
    """Process CSV articles and extract facts."""

    def __init__(self, api_key: str, model: str = "MiniMax-M2"):
        """
        Initialize the processor with MiniMax-M2 configuration.

        Args:
            api_key: MiniMax API key
            model: Model name (default: MiniMax-M2)
        """
        self.api_key = api_key
        self.model = model
        self.pipeline = None
        self._setup_lm()

    def _setup_lm(self):
        """Setup the language model with MiniMax configuration."""
        lm = dspy.LM(
            model=f"openai/{self.model}",
            api_key=self.api_key,
            api_base="https://api.minimax.io/v1",
        )
        dspy.settings.configure(lm=lm)
        self.pipeline = ExtractionPipeline()

    def process_csv(self, csv_path: str) -> List[Dict[str, Any]]:
        """
        Process articles from CSV and extract facts.

        Args:
            csv_path: Path to CSV file with 'raw_title' and 'raw_description' columns

        Returns:
            List of extraction results with metadata
        """
        results = []

        try:
            with open(csv_path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for idx, row in enumerate(reader, 1):
                    title = row.get("raw_title", "").strip()
                    description = row.get("raw_description", "").strip()
                    article_id = row.get("medwiki_id", str(idx))

                    if not title or not description:
                        print(f"⚠️  Skipping row {idx}: missing title or description")
                        continue

                    print(f"📄 Processing article {idx}: {title[:50]}...")

                    try:
                        extraction = self.pipeline.forward(
                            title=title, description=description
                        )

                        result = {
                            "medwiki_id": article_id,
                            "title": title,
                            "summary": extraction.summary,
                            "key_facts": [
                                {
                                    "fact": fact.fact,
                                    "supporting_statement": fact.supporting_statement,
                                }
                                for fact in extraction.key_facts
                            ],
                            "topics": extraction.topics,
                            "keywords": extraction.keywords,
                        }
                        results.append(result)
                        print(
                            f"   ✓ Extracted: {len(extraction.key_facts)} facts, "
                            f"{len(extraction.topics)} topics, "
                            f"{len(extraction.keywords)} keywords"
                        )

                    except Exception as e:
                        print(f"   ✗ Error processing article {idx}: {str(e)}")
                        continue

        except FileNotFoundError:
            print(f"Error: CSV file not found at {csv_path}")
            sys.exit(1)
        except Exception as e:
            print(f"Error reading CSV: {str(e)}")
            sys.exit(1)

        return results

    def save_results(
        self,
        results: List[Dict[str, Any]],
        output_path: str = "output/extracted_data.json",
    ):
        """
        Save extraction results to JSON file.

        Args:
            results: List of extraction results
            output_path: Path to save JSON output
        """
        output_dir = Path(output_path).parent
        output_dir.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)

        print(f"\n💾 Results saved to {output_path}")
        print(f"   Total articles processed: {len(results)}")


def main():
    """Main entry point for processing articles."""
    # Load API key from environment or use provided key
    api_key = os.getenv("MINIMAX_API_KEY")

    if not api_key:
        # Use the key from idea.md for testing
        api_key = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJHcm91cE5hbWUiOiJBcm5hYiBTYWhhIiwiVXNlck5hbWUiOiJBcm5hYiBTYWhhIiwiQWNjb3VudCI6IiIsIlN1YmplY3RJRCI6IjE5ODI3MzczNjYwNjU4ODExMzciLCJQaG9uZSI6IiIsIkdyb3VwSUQiOiIxOTgyNzM3MzY2MDYxNjgyNzM3IiwiUGFnZU5hbWUiOiIiLCJNYWlsIjoiYXJuYWIuc2FoYUBjbGlybmV0LmNvbSIsIkNyZWF0ZVRpbWUiOiIyMDI1LTExLTAxIDIwOjE2OjM0IiwiVG9rZW5UeXBlIjoxLCJpc3MiOiJtaW5pbWF4In0.m3XeUnVbGE9jojnNGWTy-kGar55vqSf1mVLOapIx2DUkjNVlvMpqVcELeL1f8d6AVkRiZFCV60K9ZEmRHUmHhCj3dgVA8CZGr_Mr5J9CmnXZC3CxpaNh2Bdobve8t8fGX4Xp3Gsq8EEFPBu15vsJC7BTnA2NIoE-D7a_wpvb3Na7-aA7lz-hwlB7oNlZJM4ppp0xIAhlLIWyf_oH3NqHmXTM22xcvYcC61qLDDJV5tjX25ALgHpfCmWttUnBjnOAr5m_z7Fe2MBHm2iyCKPT68QnprmE4vbvf9g9QUT_7KZY1ewsY8X0eVh8GGP2_fh9GFFB7i15jCGxXy4jejKn0Q"

    # Get CSV path
    csv_path = "clirnet_articles.csv"
    if not os.path.exists(csv_path):
        print(f"Error: CSV file not found at {csv_path}")
        sys.exit(1)

    print("🚀 Starting MedWiki Facts Extractor")
    print(f"   CSV: {csv_path}")
    print(f"   Model: MiniMax-M2")
    print()

    processor = ArticleProcessor(api_key=api_key)
    results = processor.process_csv(csv_path)
    processor.save_results(results)

    print("\n✅ Processing complete!")


if __name__ == "__main__":
    main()
