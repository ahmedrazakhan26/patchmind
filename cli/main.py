"""CLI entry point for PatchMind."""

from __future__ import annotations

import argparse

from core.patch_engine import PatchEngine
from core.summarizer import PatchSummarizer


def main() -> None:
    """Main entry point for the PatchMind CLI."""

    parser = argparse.ArgumentParser(description="PatchMind CLI")
    parser.add_argument(
        "--changes",
        action="store_true",
        help="Display a summary of repository changes",
    )
    parser.add_argument(
        "--summary",
        action="store_true",
        help="Print a short summary of repository changes",
    )
    args = parser.parse_args()

    if args.changes or args.summary:
        engine = PatchEngine()
        try:
            result = engine.detect_changes()
        except RuntimeError as exc:
            print(f"Error: {exc}")
            return

        if args.changes:
            print("Added:")
            for p in result.added:
                print(f"  {p}")

            print("Modified:")
            for p in result.modified:
                print(f"  {p}")

            print("Deleted:")
            for p in result.deleted:
                print(f"  {p}")

        if args.summary:
            summary = PatchSummarizer.summarize(result)
            print(summary)


if __name__ == "__main__":
    main()
