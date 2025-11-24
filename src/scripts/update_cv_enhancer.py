"""Sync the cv_enhancer prompt into its workflow JSON definition."""

from __future__ import annotations

import json
import sys
from pathlib import Path

# Add src directory to path so we can import job_agent
REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_DIR = REPO_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from job_agent.utils.file_utils import load_prompt_file

WORKFLOW_PATH = REPO_ROOT / "workflow" / "cv_enhancer.json"
PROMPT_PATH = REPO_ROOT / "prompts" / "cv_enhancer" / "cv_enhancer_prompt_v1.txt"


def update_workflow() -> None:
    """Read the prompt file and inject it into the AI Agent node."""
    prompt_text = load_prompt_file(PROMPT_PATH, ignore_comments=False)
    if not prompt_text:
        raise FileNotFoundError(f"Unable to read prompt from {PROMPT_PATH}")

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

