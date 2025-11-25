"""Sync the multi_agent workflow prompt into the exported workflow JSON."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import frontmatter

# Add src directory to path so we can import job_agent modules if needed later
REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_DIR = REPO_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

WORKFLOW_PATH = REPO_ROOT / "workflow" / "multi_agent.json"
PROMPT_PATH = REPO_ROOT / "prompts" / "multi_agent" / "master_agent_prompt.txt"


def update_workflow() -> None:
    """Read the master prompt and inject it into the AI Agent node."""
    if not PROMPT_PATH.exists():
        raise FileNotFoundError(f"Prompt file not found: {PROMPT_PATH}")

    post = frontmatter.loads(PROMPT_PATH.read_text(encoding="utf-8"))
    prompt_text = post.content.strip()

    if not prompt_text:
        raise ValueError(f"Prompt file is empty or has no content: {PROMPT_PATH}")

    workflow_data = json.loads(WORKFLOW_PATH.read_text(encoding="utf-8"))
    nodes = workflow_data.get("nodes", [])

    agent_node = next(
        (node for node in nodes if node.get("type") == "@n8n/n8n-nodes-langchain.agent"),
        None,
    )
    if not agent_node:
        raise RuntimeError("No AI Agent node found in workflow.")

    parameters = agent_node.setdefault("parameters", {})
    parameters["promptType"] = "define"
    parameters["text"] = prompt_text

    WORKFLOW_PATH.write_text(json.dumps(workflow_data, indent=2), encoding="utf-8")
    print(
        f"Updated {WORKFLOW_PATH} with prompt from {PROMPT_PATH} "
        f"({len(prompt_text)} characters)."
    )


if __name__ == "__main__":
    update_workflow()

