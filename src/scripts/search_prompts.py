"""CLI tool to search prompts using PromptRegistry."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# Add src to path
REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_DIR = REPO_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from job_agent.utils.prompt_registry import PromptRegistry


def main() -> None:
    """CLI entry point for searching prompts."""
    parser = argparse.ArgumentParser(description="Search prompts by metadata")
    parser.add_argument("--workflow", help="Filter by workflow name")
    parser.add_argument("--version", help="Filter by version")
    parser.add_argument("--purpose", help="Filter by purpose (substring)")
    parser.add_argument("--agent-role", help="Filter by agent role (substring)")
    parser.add_argument("--tags", nargs="+", help="Filter by tags (must have ALL)")
    parser.add_argument("--model-hint", help="Filter by model hint (substring)")
    parser.add_argument("--created-after", help="Filter by creation date (YYYY-MM-DD)")
    parser.add_argument("--created-before", help="Filter by creation date (YYYY-MM-DD)")
    parser.add_argument("--list-all", action="store_true", help="List all prompts")
    parser.add_argument(
        "--format",
        choices=["json", "table", "summary"],
        default="summary",
        help="Output format",
    )

    args = parser.parse_args()

    registry = PromptRegistry()

    if args.list_all:
        results = registry.list_all()
    else:
        results = registry.search(
            workflow=args.workflow,
            version=args.version,
            purpose=args.purpose,
            agent_role=args.agent_role,
            tags=args.tags,
            model_hint=args.model_hint,
            created_after=args.created_after,
            created_before=args.created_before,
        )

    if args.format == "json":
        print(json.dumps(results, indent=2))
    elif args.format == "table":
        # Simple table output
        if not results:
            print("No prompts found.")
            return
        print(f"{'Workflow':<20} {'Version':<10} {'Agent Role':<30} {'Purpose':<50}")
        print("-" * 110)
        for prompt in results:
            print(
                f"{prompt.get('workflow', 'N/A'):<20} "
                f"{prompt.get('version', 'N/A'):<10} "
                f"{prompt.get('agent_role', 'N/A'):<30} "
                f"{prompt.get('purpose', 'N/A')[:50]:<50}"
            )
    else:  # summary
        print(f"Found {len(results)} prompt(s):\n")
        for prompt in results:
            print(f"Workflow: {prompt.get('workflow', 'N/A')}")
            print(f"Version: {prompt.get('version', 'N/A')}")
            print(f"Agent Role: {prompt.get('agent_role', 'N/A')}")
            print(f"Purpose: {prompt.get('purpose', 'N/A')}")
            print(f"File: {prompt.get('relative_path', 'N/A')}")
            if prompt.get("tags"):
                print(f"Tags: {', '.join(prompt.get('tags', []))}")
            print()


if __name__ == "__main__":
    main()

