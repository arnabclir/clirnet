"""Concurrent medical article processor with real-time progress monitoring."""

import asyncio
import csv
import json
import os
import time
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional
import sys

import dspy
from extractor import ExtractionPipeline


@dataclass
class ArticleJob:
    """Article processing job."""

    medwiki_id: str
    title: str
    description: str
    index: int


@dataclass
class ProcessingResult:
    """Result of processing an article."""

    medwiki_id: str
    index: int
    success: bool
    data: Optional[Dict[str, Any]]
    error: Optional[str]
    processing_time: float
    timestamp: str


class ConcurrentProcessor:
    """Process articles concurrently with real-time monitoring."""

    def __init__(
        self,
        api_key: str,
        model: str = "MiniMax-M2",
        max_concurrent: int = 20,
        timeout: int = 60,
        rate_limit_delay: float = 0.05,
        output_dir: str = "output",
    ):
        """
        Initialize concurrent processor.

        Args:
            api_key: MiniMax API key
            model: Model name
            max_concurrent: Maximum concurrent API calls
            timeout: Timeout per article in seconds
            rate_limit_delay: Delay between batches in seconds
            output_dir: Output directory for results
        """
        self.api_key = api_key
        self.model = model
        self.max_concurrent = max_concurrent
        self.timeout = timeout
        self.rate_limit_delay = rate_limit_delay
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Initialize pipeline
        self.pipeline = None
        self._setup_lm()

        # Statistics
        self.total_processed = 0
        self.successful = 0
        self.failed = 0
        self.start_time = None
        self.processing_times = []

        # Output files
        self.results_file = self.output_dir / "results_live.json"
        self.progress_csv = self.output_dir / "progress.csv"
        self.progress_txt = self.output_dir / "progress.txt"
        self.checkpoint_file = self.output_dir / "checkpoint.json"
        self.errors_log = self.output_dir / "errors.log"

        # Initialize checkpoint
        self.completed_ids = self._load_checkpoint()

        # Initialize output files
        self._initialize_files()

    def _setup_lm(self):
        """Setup the language model."""
        lm = dspy.LM(
            model=f"openai/{self.model}",
            api_key=self.api_key,
            api_base="https://api.minimax.io/v1",
        )
        dspy.settings.configure(lm=lm)
        self.pipeline = ExtractionPipeline()

    def _load_checkpoint(self) -> set:
        """Load completed article IDs from checkpoint."""
        if self.checkpoint_file.exists():
            with open(self.checkpoint_file, "r") as f:
                data = json.load(f)
                return set(data.get("completed_ids", []))
        return set()

    def _save_checkpoint(self):
        """Save checkpoint with completed article IDs."""
        checkpoint_data = {
            "completed_ids": list(self.completed_ids),
            "total_completed": len(self.completed_ids),
            "last_updated": datetime.now().isoformat(),
        }
        # Atomic write
        temp_file = self.checkpoint_file.with_suffix(".tmp")
        with open(temp_file, "w") as f:
            json.dump(checkpoint_data, f, indent=2)
        temp_file.replace(self.checkpoint_file)

    def _initialize_files(self):
        """Initialize output files."""
        # Initialize results file with empty array
        if not self.results_file.exists():
            with open(self.results_file, "w", encoding="utf-8") as f:
                f.write("[\n")

        # Initialize progress CSV with headers
        if not self.progress_csv.exists():
            with open(self.progress_csv, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(
                    [
                        "index",
                        "medwiki_id",
                        "status",
                        "processing_time",
                        "timestamp",
                        "error",
                    ]
                )

        # Initialize progress text
        self._update_progress_txt()

    def _append_result(self, result: Dict[str, Any]):
        """Append result to results file."""
        # Read current content
        with open(self.results_file, "r", encoding="utf-8") as f:
            content = f.read().rstrip()

        # Check if we need to add comma
        needs_comma = not content.endswith("[\n")

        # Append new result
        with open(self.results_file, "a", encoding="utf-8") as f:
            if needs_comma:
                f.write(",\n")
            json.dump(result, f, indent=2, ensure_ascii=False)

    def _finalize_results_file(self):
        """Close the JSON array in results file."""
        with open(self.results_file, "a", encoding="utf-8") as f:
            f.write("\n]\n")

    def _append_progress_csv(self, result: ProcessingResult):
        """Append progress entry to CSV."""
        with open(self.progress_csv, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(
                [
                    result.index,
                    result.medwiki_id,
                    "success" if result.success else "failed",
                    f"{result.processing_time:.2f}",
                    result.timestamp,
                    result.error or "",
                ]
            )

    def _update_progress_txt(self):
        """Update human-readable progress file."""
        elapsed = time.time() - self.start_time if self.start_time else 0
        avg_time = (
            sum(self.processing_times) / len(self.processing_times)
            if self.processing_times
            else 0
        )

        success_rate = (
            (self.successful / self.total_processed * 100)
            if self.total_processed > 0
            else 0
        )

        # Calculate ETA
        articles_per_sec = self.total_processed / elapsed if elapsed > 0 else 0

        progress_text = f"""
========================================
MedWiki Facts Extractor - Progress
========================================
Started: {datetime.fromtimestamp(self.start_time).strftime("%Y-%m-%d %H:%M:%S") if self.start_time else "N/A"}
Elapsed: {elapsed / 60:.1f} minutes

Articles Processed: {self.total_processed}
  [OK] Successful: {self.successful}
  [X] Failed: {self.failed}
  Success Rate: {success_rate:.1f}%

Performance:
  Average Time: {avg_time:.2f}s per article
  Processing Rate: {articles_per_sec * 60:.1f} articles/minute
  Concurrent Workers: {self.max_concurrent}

Last Updated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
========================================
"""

        with open(self.progress_txt, "w", encoding="utf-8") as f:
            f.write(progress_text)

    def _log_error(self, medwiki_id: str, error: str):
        """Log error to errors file."""
        timestamp = datetime.now().isoformat()
        with open(self.errors_log, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] Article {medwiki_id}: {error}\n")

    async def _process_single_article(
        self, job: ArticleJob, semaphore: asyncio.Semaphore
    ) -> ProcessingResult:
        """
        Process a single article with timeout and error handling.

        Args:
            job: Article job to process
            semaphore: Semaphore for rate limiting

        Returns:
            ProcessingResult
        """
        async with semaphore:
            start_time = time.time()
            timestamp = datetime.now().isoformat()

            try:
                # Run the synchronous pipeline in executor with timeout
                loop = asyncio.get_event_loop()
                extraction = await asyncio.wait_for(
                    loop.run_in_executor(
                        None, self.pipeline.forward, job.title, job.description
                    ),
                    timeout=self.timeout,
                )

                # Build result
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

                return ProcessingResult(
                    medwiki_id=job.medwiki_id,
                    index=job.index,
                    success=True,
                    data=result_data,
                    error=None,
                    processing_time=processing_time,
                    timestamp=timestamp,
                )

            except asyncio.TimeoutError:
                processing_time = time.time() - start_time
                error_msg = f"Timeout after {self.timeout}s"
                self._log_error(job.medwiki_id, error_msg)
                return ProcessingResult(
                    medwiki_id=job.medwiki_id,
                    index=job.index,
                    success=False,
                    data=None,
                    error=error_msg,
                    processing_time=processing_time,
                    timestamp=timestamp,
                )

            except Exception as e:
                processing_time = time.time() - start_time
                error_msg = str(e)
                self._log_error(job.medwiki_id, error_msg)
                return ProcessingResult(
                    medwiki_id=job.medwiki_id,
                    index=job.index,
                    success=False,
                    data=None,
                    error=error_msg,
                    processing_time=processing_time,
                    timestamp=timestamp,
                )

    async def _process_batch(self, jobs: List[ArticleJob], resume: bool = False):
        """
        Process a batch of articles concurrently.

        Args:
            jobs: List of article jobs
            resume: Whether to skip already completed articles
        """
        # Filter out completed articles if resuming
        if resume:
            jobs = [job for job in jobs if job.medwiki_id not in self.completed_ids]
            if not jobs:
                print("  All articles in batch already completed, skipping...")
                return

        # Create semaphore for rate limiting
        semaphore = asyncio.Semaphore(self.max_concurrent)

        # Create tasks for all jobs
        tasks = [self._process_single_article(job, semaphore) for job in jobs]

        # Process all concurrently
        results = await asyncio.gather(*tasks)

        # Save results incrementally
        for result in results:
            self.total_processed += 1
            self.processing_times.append(result.processing_time)

            if result.success:
                self.successful += 1
                self._append_result(result.data)
                self.completed_ids.add(result.medwiki_id)
            else:
                self.failed += 1

            # Append to progress CSV
            self._append_progress_csv(result)

            # Print progress
            status = "[OK]" if result.success else "[X]"
            print(
                f"  {status} [{self.total_processed}] Article {result.medwiki_id}: "
                f"{result.processing_time:.2f}s"
            )

        # Update checkpoint
        self._save_checkpoint()

        # Update progress text every batch
        self._update_progress_txt()

        # Rate limiting delay
        await asyncio.sleep(self.rate_limit_delay)

    async def process_csv(
        self, csv_path: str, limit: Optional[int] = None, resume: bool = False
    ):
        """
        Process articles from CSV file.

        Args:
            csv_path: Path to CSV file
            limit: Maximum number of articles to process
            resume: Whether to resume from checkpoint
        """
        print(f"\n*** Starting Concurrent MedWiki Facts Extractor ***")
        print(f"   CSV: {csv_path}")
        print(f"   Model: {self.model}")
        print(f"   Max Concurrent: {self.max_concurrent}")
        print(f"   Timeout: {self.timeout}s")
        if limit:
            print(f"   Limit: {limit} articles")
        if resume:
            print(f"   Resume: Yes ({len(self.completed_ids)} already completed)")
        print()

        self.start_time = time.time()

        # Load jobs from CSV
        jobs = []
        try:
            with open(csv_path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for idx, row in enumerate(reader, 1):
                    if limit and idx > limit:
                        break

                    title = row.get("raw_title", "").strip()
                    description = row.get("raw_description", "").strip()
                    medwiki_id = row.get("medwiki_id", str(idx))

                    if not title or not description:
                        continue

                    # Skip if already completed and resuming
                    if resume and medwiki_id in self.completed_ids:
                        continue

                    jobs.append(
                        ArticleJob(
                            medwiki_id=medwiki_id,
                            title=title,
                            description=description,
                            index=idx,
                        )
                    )

        except FileNotFoundError:
            print(f"[ERROR] CSV file not found at {csv_path}")
            sys.exit(1)

        print(f"Loaded {len(jobs)} articles to process")
        print()

        # Process in batches
        batch_size = (
            self.max_concurrent * 2
        )  # Process 2 rounds of concurrent calls per batch
        total_batches = (len(jobs) + batch_size - 1) // batch_size

        for batch_idx in range(0, len(jobs), batch_size):
            batch_jobs = jobs[batch_idx : batch_idx + batch_size]
            batch_num = batch_idx // batch_size + 1

            print(
                f"Processing batch {batch_num}/{total_batches} "
                f"({len(batch_jobs)} articles)..."
            )

            await self._process_batch(batch_jobs, resume=resume)

        # Finalize results file
        self._finalize_results_file()

        # Final statistics
        elapsed = time.time() - self.start_time
        avg_time = (
            sum(self.processing_times) / len(self.processing_times)
            if self.processing_times
            else 0
        )

        print()
        print("=" * 50)
        print("*** Processing Complete! ***")
        print("=" * 50)
        print(f"Total Processed: {self.total_processed}")
        print(f"  [OK] Successful: {self.successful}")
        print(f"  [X] Failed: {self.failed}")
        print(f"  Success Rate: {self.successful / self.total_processed * 100:.1f}%")
        print()
        print(f"Time Elapsed: {elapsed / 60:.1f} minutes")
        print(f"Average Time: {avg_time:.2f}s per article")
        print(
            f"Processing Rate: {self.total_processed / elapsed * 60:.1f} articles/minute"
        )
        print()
        print(f"Results saved to:")
        print(f"   {self.results_file}")
        print(f"   {self.progress_csv}")
        print(f"   {self.progress_txt}")
        if self.failed > 0:
            print(f"   {self.errors_log}")
        print("=" * 50)


async def main(
    csv_path: str,
    api_key: str,
    limit: Optional[int] = None,
    max_concurrent: int = 20,
    resume: bool = False,
):
    """Main entry point."""
    processor = ConcurrentProcessor(api_key=api_key, max_concurrent=max_concurrent)
    await processor.process_csv(csv_path, limit=limit, resume=resume)


if __name__ == "__main__":
    # This file is meant to be imported, not run directly
    # Use run_concurrent.py instead
    pass
