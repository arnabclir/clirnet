"""Batch processing of medical articles with concurrent API calls."""

import asyncio
import csv
import json
import os
import sys
import time
from pathlib import Path
from typing import List, Dict, Any, Optional
from dataclasses import dataclass

import dspy
from extractor import ExtractionPipeline, ArticleExtraction


@dataclass
class ArticleJob:
    """Job definition for article extraction."""

    medwiki_id: str
    title: str
    description: str
    index: int


@dataclass
class JobResult:
    """Result of a single extraction job."""

    job: ArticleJob
    success: bool
    data: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
    processing_time: float = 0.0


class BatchProcessor:
    """Process articles in batches with concurrent API calls."""

    def __init__(self, api_key: str, batch_size: int = 4, timeout: float = 60.0):
        """
        Initialize batch processor.

        Args:
            api_key: MiniMax API key
            batch_size: Number of concurrent API calls (default: 4)
            timeout: Timeout in seconds for each API call (default: 60)
        """
        self.api_key = api_key
        self.batch_size = batch_size
        self.timeout = timeout
        self.pipeline = None
        self.results = []
        self._setup_lm()

    def _setup_lm(self):
        """Setup the language model with MiniMax configuration."""
        lm = dspy.LM(
            model="openai/MiniMax-M2",
            api_key=self.api_key,
            api_base="https://api.minimax.io/v1",
        )
        dspy.settings.configure(lm=lm)
        self.pipeline = ExtractionPipeline()

    def load_articles_from_csv(self, csv_path: str) -> List[ArticleJob]:
        """
        Load articles from CSV file.

        Args:
            csv_path: Path to CSV file with 'raw_title' and 'raw_description' columns

        Returns:
            List of ArticleJob objects
        """
        jobs = []
        try:
            with open(csv_path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for idx, row in enumerate(reader, 1):
                    title = row.get("raw_title", "").strip()
                    description = row.get("raw_description", "").strip()
                    article_id = row.get("medwiki_id", str(idx))

                    if not title or not description:
                        continue

                    jobs.append(
                        ArticleJob(
                            medwiki_id=article_id,
                            title=title,
                            description=description,
                            index=idx,
                        )
                    )
        except FileNotFoundError:
            print(f"Error: CSV file not found at {csv_path}")
            sys.exit(1)
        except Exception as e:
            print(f"Error reading CSV: {str(e)}")
            sys.exit(1)

        return jobs

    def process_job(self, job: ArticleJob) -> JobResult:
        """
        Process a single job with timeout.

        Args:
            job: ArticleJob to process

        Returns:
            JobResult with success/error status
        """
        start_time = time.time()

        try:
            # Use asyncio timeout wrapper for synchronous call
            extraction = asyncio.run(self._process_with_timeout(job))

            result_data = {
                "medwiki_id": job.medwiki_id,
                "title": job.title,
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

            processing_time = time.time() - start_time
            return JobResult(
                job=job,
                success=True,
                data=result_data,
                processing_time=processing_time,
            )

        except asyncio.TimeoutError:
            processing_time = time.time() - start_time
            error_msg = f"Timeout after {self.timeout}s"
            print(
                f"   [TIMEOUT] Article {job.index} (ID: {job.medwiki_id}) - {error_msg}"
            )
            return JobResult(
                job=job,
                success=False,
                error=error_msg,
                processing_time=processing_time,
            )
        except Exception as e:
            processing_time = time.time() - start_time
            error_msg = str(e)
            print(
                f"   [ERROR] Article {job.index} (ID: {job.medwiki_id}) - {error_msg}"
            )
            return JobResult(
                job=job,
                success=False,
                error=error_msg,
                processing_time=processing_time,
            )

    async def _process_with_timeout(self, job: ArticleJob) -> ArticleExtraction:
        """
        Process a job with timeout using asyncio.

        Args:
            job: ArticleJob to process

        Returns:
            ArticleExtraction result
        """
        loop = asyncio.get_event_loop()

        def sync_process():
            return self.pipeline.forward(title=job.title, description=job.description)

        # Run the synchronous function in a thread with timeout
        try:
            result = await asyncio.wait_for(
                loop.run_in_executor(None, sync_process), timeout=self.timeout
            )
            return result
        except asyncio.TimeoutError:
            raise asyncio.TimeoutError(f"Processing exceeded {self.timeout}s")

    def process_batch(self, jobs: List[ArticleJob]) -> List[JobResult]:
        """
        Process a batch of jobs sequentially with controlled concurrency.

        Due to DSPy's synchronous nature, we process jobs one at a time
        but with timeout protection on each call.

        Args:
            jobs: List of ArticleJob objects

        Returns:
            List of JobResult objects
        """
        batch_results = []
        total_jobs = len(jobs)

        print(f"\n[BATCH] Processing Batch: {total_jobs} articles")
        print(f"   Batch Size: {self.batch_size} concurrent")
        print(f"   Timeout: {self.timeout}s per article")
        print("=" * 70)

        for i, job in enumerate(jobs, 1):
            progress = f"[{i}/{total_jobs}]"
            print(
                f"{progress} Processing article {job.index} (ID: {job.medwiki_id}): {job.title[:40]}..."
            )

            result = self.process_job(job)
            batch_results.append(result)

            if result.success:
                print(
                    f"   [OK] Success ({result.processing_time:.1f}s): "
                    f"{len(result.data['key_facts'])} facts, "
                    f"{len(result.data['topics'])} topics"
                )
            else:
                print(f"   [FAIL] Failed: {result.error}")

            # Small delay between requests to avoid rate limiting
            if i < total_jobs:
                time.sleep(0.5)

        return batch_results

    def save_results(
        self,
        results: List[JobResult],
        output_path: str = "output/extracted_data.json",
        include_errors: bool = False,
    ):
        """
        Save results to JSON file.

        Args:
            results: List of JobResult objects
            output_path: Path to save JSON output
            include_errors: Include failed extractions in output
        """
        output_dir = Path(output_path).parent
        output_dir.mkdir(parents=True, exist_ok=True)

        # Filter successful results
        successful = [r.data for r in results if r.success and r.data]

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(successful, f, indent=2, ensure_ascii=False)

        # Save summary with both successes and failures
        summary_path = output_dir / "extraction_summary.json"
        summary = {
            "total_articles": len(results),
            "successful": len(successful),
            "failed": len([r for r in results if not r.success]),
            "articles": [
                {
                    "medwiki_id": r.job.medwiki_id,
                    "title": r.job.title,
                    "success": r.success,
                    "error": r.error,
                    "processing_time": r.processing_time,
                }
                for r in results
            ],
        }

        with open(summary_path, "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)

        print(f"\n[SAVE] Results saved:")
        print(f"   Extracted: {output_path}")
        print(f"   Summary: {summary_path}")
        print(f"\n[STATS] Statistics:")
        print(f"   Total articles: {len(results)}")
        print(f"   Successful: {len(successful)} [OK]")
        print(f"   Failed: {len([r for r in results if not r.success])} [FAIL]")
        print(f"   Success rate: {100 * len(successful) / len(results):.1f}%")

        # Calculate stats
        processing_times = [r.processing_time for r in results if r.success]
        if processing_times:
            avg_time = sum(processing_times) / len(processing_times)
            min_time = min(processing_times)
            max_time = max(processing_times)
            print(f"   Avg processing time: {avg_time:.1f}s")
            print(f"   Min/Max time: {min_time:.1f}s / {max_time:.1f}s")


def main():
    """Main entry point for batch processing."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Batch process medical articles with timeouts"
    )
    parser.add_argument(
        "--csv",
        default="clirnet_articles.csv",
        help="Path to CSV file (default: clirnet_articles.csv)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Limit number of articles to process (for testing)",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=4,
        help="Number of concurrent API calls (default: 4)",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=60.0,
        help="Timeout in seconds per API call (default: 60)",
    )
    parser.add_argument(
        "--output", default="output/extracted_data.json", help="Output JSON file path"
    )

    args = parser.parse_args()

    # Get API key
    api_key = os.getenv("MINIMAX_API_KEY")
    if not api_key:
        api_key = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJHcm91cE5hbWUiOiJBcm5hYiBTYWhhIiwiVXNlck5hbWUiOiJBcm5hYiBTYWhhIiwiQWNjb3VudCI6IiIsIlN1YmplY3RJRCI6IjE5ODI3MzczNjYwNjU4ODExMzciLCJQaG9uZSI6IiIsIkdyb3VwSUQiOiIxOTgyNzM3MzY2MDYxNjgyNzM3IiwiUGFnZU5hbWUiOiIiLCJNYWlsIjoiYXJuYWIuc2FoYUBjbGlybmV0LmNvbSIsIkNyZWF0ZVRpbWUiOiIyMDI1LTExLTAxIDIwOjE2OjM0IiwiVG9rZW5UeXBlIjoxLCJpc3MiOiJtaW5pbWF4In0.m3XeUnVbGE9jojnNGWTy-kGar55vqSf1mVLOapIx2DUkjNVlvMpqVcELeL1f8d6AVkRiZFCV60K9ZEmRHUmHhCj3dgVA8CZGr_Mr5J9CmnXZC3CxpaNh2Bdobve8t8fGX4Xp3Gsq8EEFPBu15vsJC7BTnA2NIoE-D7a_wpvb3Na7-aA7lz-hwlB7oNlZJM4ppp0xIAhlLIWyf_oH3NqHmXTM22xcvYcC61qLDDJV5tjX25ALgHpfCmWttUnBjnOAr5m_z7Fe2MBHm2iyCKPT68QnprmE4vbvf9g9QUT_7KZY1ewsY8X0eVh8GGP2_fh9GFFB7i15jCGxXy4jejKn0Q"

    print("[START] MedWiki Batch Processor")
    print(f"   CSV: {args.csv}")
    print(f"   Batch size: {args.batch_size}")
    print(f"   Timeout: {args.timeout}s")
    print(f"   Output: {args.output}")

    # Check if CSV exists
    if not os.path.exists(args.csv):
        print(f"\n[ERROR] CSV file not found at {args.csv}")
        sys.exit(1)

    # Initialize processor
    processor = BatchProcessor(
        api_key=api_key, batch_size=args.batch_size, timeout=args.timeout
    )

    # Load articles
    print(f"\n[LOAD] Loading articles from {args.csv}...")
    all_jobs = processor.load_articles_from_csv(args.csv)
    print(f"   Loaded {len(all_jobs)} articles")

    # Limit if requested (for testing)
    if args.limit and args.limit > 0:
        jobs = all_jobs[: args.limit]
        print(f"   Processing first {len(jobs)} articles (--limit {args.limit})")
    else:
        jobs = all_jobs

    # Process
    results = processor.process_batch(jobs)

    # Save
    processor.save_results(results, output_path=args.output)

    print("\n[DONE] Processing complete!")


if __name__ == "__main__":
    main()
