"""Simple batch processor with timeout protection."""

import csv
import json
import os
import signal
import sys
import time
from pathlib import Path
from typing import List, Dict, Any, Optional

import dspy
from extractor import ExtractionPipeline


class TimeoutException(Exception):
    pass


def timeout_handler(signum, frame):
    raise TimeoutException("API call timed out")


def process_article(
    pipeline, title: str, description: str, timeout_sec: float = 60.0
) -> Optional[Dict[str, Any]]:
    """
    Process a single article with timeout protection.

    Args:
        pipeline: ExtractionPipeline instance
        title: Article title
        description: Article description
        timeout_sec: Timeout in seconds

    Returns:
        Extracted data dict or None if failed
    """
    # Set signal handler for timeout
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(int(timeout_sec) + 5)  # Add buffer

    try:
        result = pipeline(title=title, description=description)
        signal.alarm(0)  # Cancel alarm

        return {
            "summary": result.summary,
            "key_facts": [
                {
                    "fact": fact.fact,
                    "supporting_statement": fact.supporting_statement,
                }
                for fact in result.key_facts
            ],
            "topics": result.topics,
            "keywords": result.keywords,
        }
    except TimeoutException:
        signal.alarm(0)
        raise
    except Exception as e:
        signal.alarm(0)
        raise


def main():
    """Main batch processing function."""
    # Arguments
    limit = 10
    csv_path = "clirnet_articles.csv"
    output_path = "output/extracted_10.json"

    print("[START] Simple Batch Processor")
    print(f"   CSV: {csv_path}")
    print(f"   Limit: {limit} articles")
    print(f"   Output: {output_path}")
    print()

    # Check CSV exists
    if not os.path.exists(csv_path):
        print(f"[ERROR] CSV not found: {csv_path}")
        sys.exit(1)

    # Setup LM
    print("[SETUP] Configuring MiniMax-M2 LM...")
    api_key = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJHcm91cE5hbWUiOiJBcm5hYiBTYWhhIiwiVXNlck5hbWUiOiJBcm5hYiBTYWhhIiwiQWNjb3VudCI6IiIsIlN1YmplY3RJRCI6IjE5ODI3MzczNjYwNjU4ODExMzciLCJQaG9uZSI6IiIsIkdyb3VwSUQiOiIxOTgyNzM3MzY2MDYxNjgyNzM3IiwiUGFnZU5hbWUiOiIiLCJNYWlsIjoiYXJuYWIuc2FoYUBjbGlybmV0LmNvbSIsIkNyZWF0ZVRpbWUiOiIyMDI1LTExLTAxIDIwOjE2OjM0IiwiVG9rZW5UeXBlIjoxLCJpc3MiOiJtaW5pbWF4In0.m3XeUnVbGE9jojnNGWTy-kGar55vqSf1mVLOapIx2DUkjNVlvMpqVcELeL1f8d6AVkRiZFCV60K9ZEmRHUmHhCj3dgVA8CZGr_Mr5J9CmnXZC3CxpaNh2Bdobve8t8fGX4Xp3Gsq8EEFPBu15vsJC7BTnA2NIoE-D7a_wpvb3Na7-aA7lz-hwlB7oNlZJM4ppp0xIAhlLIWyf_oH3NqHmXTM22xcvYcC61qLDDJV5tjX25ALgHpfCmWttUnBjnOAr5m_z7Fe2MBHm2iyCKPT68QnprmE4vbvf9g9QUT_7KZY1ewsY8X0eVh8GGP2_fh9GFFB7i15jCGxXy4jejKn0Q"

    lm = dspy.LM(
        model="openai/MiniMax-M2",
        api_key=api_key,
        api_base="https://api.minimax.io/v1",
    )
    dspy.settings.configure(lm=lm)
    pipeline = ExtractionPipeline()
    print("[OK] LM configured")
    print()

    # Load articles
    print("[LOAD] Loading articles from CSV...")
    articles = []
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for idx, row in enumerate(reader, 1):
            title = row.get("raw_title", "").strip()
            description = row.get("raw_description", "").strip()
            article_id = row.get("medwiki_id", str(idx))

            if not title or not description:
                continue

            articles.append(
                {
                    "id": article_id,
                    "index": idx,
                    "title": title,
                    "description": description,
                }
            )

            if len(articles) >= limit:
                break

    print(f"[OK] Loaded {len(articles)} articles")
    print()

    # Process articles
    print("[PROCESS] Starting extraction...")
    print("=" * 70)

    results = []
    success_count = 0
    fail_count = 0

    for i, article in enumerate(articles, 1):
        progress = f"[{i}/{len(articles)}]"
        print(
            f"{progress} Article {article['index']} (ID: {article['id']}): {article['title'][:40]}..."
        )

        try:
            data = process_article(
                pipeline, article["title"], article["description"], timeout_sec=60.0
            )
            result_obj = {
                "medwiki_id": article["id"],
                "title": article["title"],
                **data,
            }
            results.append(result_obj)
            success_count += 1
            print(
                f"     [OK] Extracted {len(data['key_facts'])} facts, {len(data['topics'])} topics"
            )

        except TimeoutException:
            fail_count += 1
            print(f"     [TIMEOUT] Failed after 60s")
        except Exception as e:
            fail_count += 1
            print(f"     [ERROR] {str(e)[:50]}")

        time.sleep(0.5)  # Rate limiting

    print("=" * 70)
    print()

    # Save results
    print("[SAVE] Saving results...")
    output_dir = Path(output_path).parent
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"[OK] Saved to {output_path}")
    print()
    print("[STATS] Statistics:")
    print(f"   Total: {len(articles)}")
    print(f"   Success: {success_count}")
    print(f"   Failed: {fail_count}")
    print(f"   Success rate: {100 * success_count / len(articles):.1f}%")
    print()
    print("[DONE] Processing complete!")


if __name__ == "__main__":
    main()
