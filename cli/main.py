"""CLI entry point for PatchMind."""

from __future__ import annotations

import argparse

from core.patch_engine import PatchEngine
from core.summarizer import PatchSummarizer
from core.visualizer import PatchVisualizer


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
    parser.add_argument(
        "--analyze",
        action="store_true",
        help="Print intelligent analysis of modified files",
    )
    parser.add_argument(
        "--tree",
        action="store_true",
        help="Display repository changes in a tree view",
    )
    args = parser.parse_args()

    if args.changes or args.summary or args.analyze or args.tree:
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

        if args.tree:
            tree = PatchVisualizer.tree_summary(result)
            print(tree)

        if args.analyze:
            analysis = engine.analyze_changes()
            for path, info in analysis.items():
                print(f"{path}: {info['summary']}")


if __name__ == "__main__":
    main()
