"""Entry point for concurrent medical article processing."""

import argparse
import asyncio
import os
import sys

from concurrent_processor import main


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Process medical articles concurrently with real-time monitoring"
    )

    parser.add_argument(
        "csv_path",
        nargs="?",
        default="clirnet_articles.csv",
        help="Path to CSV file with articles (default: clirnet_articles.csv)",
    )

    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Maximum number of articles to process (default: all)",
    )

    parser.add_argument(
        "--concurrent",
        type=int,
        default=20,
        help="Maximum concurrent API calls (default: 20)",
    )

    parser.add_argument(
        "--resume",
        action="store_true",
        help="Resume from checkpoint, skipping already processed articles",
    )

    parser.add_argument(
        "--api-key",
        default=None,
        help="MiniMax API key (default: from MINIMAX_API_KEY env var)",
    )

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    # Get API key
    api_key = args.api_key or os.getenv("MINIMAX_API_KEY")

    if not api_key:
        # Use default key from project
        api_key = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJHcm91cE5hbWUiOiJBcm5hYiBTYWhhIiwiVXNlck5hbWUiOiJBcm5hYiBTYWhhIiwiQWNjb3VudCI6IiIsIlN1YmplY3RJRCI6IjE5ODI3MzczNjYwNjU4ODExMzciLCJQaG9uZSI6IiIsIkdyb3VwSUQiOiIxOTgyNzM3MzY2MDYxNjgyNzM3IiwiUGFnZU5hbWUiOiIiLCJNYWlsIjoiYXJuYWIuc2FoYUBjbGlybmV0LmNvbSIsIkNyZWF0ZVRpbWUiOiIyMDI1LTExLTAxIDIwOjE2OjM0IiwiVG9rZW5UeXBlIjoxLCJpc3MiOiJtaW5pbWF4In0.m3XeUnVbGE9jojnNGWTy-kGar55vqSf1mVLOapIx2DUkjNVlvMpqVcELeL1f8d6AVkRiZFCV60K9ZEmRHUmHhCj3dgVA8CZGr_Mr5J9CmnXZC3CxpaNh2Bdobve8t8fGX4Xp3Gsq8EEFPBu15vsJC7BTnA2NIoE-D7a_wpvb3Na7-aA7lz-hwlB7oNlZJM4ppp0xIAhlLIWyf_oH3NqHmXTM22xcvYcC61qLDDJV5tjX25ALgHpfCmWttUnBjnOAr5m_z7Fe2MBHm2iyCKPT68QnprmE4vbvf9g9QUT_7KZY1ewsY8X0eVh8GGP2_fh9GFFB7i15jCGxXy4jejKn0Q"

    # Verify CSV exists
    if not os.path.exists(args.csv_path):
        print(f"[ERROR] CSV file not found at {args.csv_path}")
        sys.exit(1)

    # Print configuration
    print("\n" + "=" * 60)
    print("  MedWiki Facts Extractor - Concurrent Processing")
    print("=" * 60)
    print(f"  CSV File: {args.csv_path}")
    print(f"  Concurrent Workers: {args.concurrent}")
    if args.limit:
        print(f"  Article Limit: {args.limit}")
    else:
        print(f"  Article Limit: All articles in CSV")
    if args.resume:
        print(f"  Mode: Resume (skip completed)")
    print("=" * 60)
    print()
    print("Monitor progress in real-time:")
    print("   tail -f output/progress.txt")
    print("   tail -f output/progress.csv")
    print("   tail -f output/results_live.json")
    print()

    # Run async main
    try:
        asyncio.run(
            main(
                csv_path=args.csv_path,
                api_key=api_key,
                limit=args.limit,
                max_concurrent=args.concurrent,
                resume=args.resume,
            )
        )
    except KeyboardInterrupt:
        print("\n\n[WARNING] Processing interrupted by user")
        print("Progress saved! Use --resume to continue from checkpoint")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n[FATAL ERROR] {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)
