"""PromptRegistry: Search and manage prompts with frontmatter metadata."""

from __future__ import annotations

import frontmatter
from pathlib import Path
from typing import Any

from job_agent.utils.file_utils import load_prompt_file


class PromptRegistry:
    """Registry for managing and searching prompts with frontmatter metadata."""

    def __init__(self, prompts_dir: Path | str | None = None) -> None:
        """
        Initialize the prompt registry.

        Args:
            prompts_dir: Path to prompts directory. Defaults to prompts/ relative to repo root.
        """
        if prompts_dir is None:
            # Assume this file is in src/job_agent/utils/, so go up to repo root
            repo_root = Path(__file__).resolve().parents[3]
            prompts_dir = repo_root / "prompts"
        self.prompts_dir = Path(prompts_dir)
        self._prompts_cache: list[dict[str, Any]] | None = None

    def _load_all_prompts(self) -> list[dict[str, Any]]:
        """Load all prompts from the prompts directory."""
        if self._prompts_cache is not None:
            return self._prompts_cache

        prompts = []
        for prompt_file in self.prompts_dir.rglob("*.txt"):
            try:
                content = prompt_file.read_text(encoding="utf-8")
                post = frontmatter.loads(content)

                prompt_data = {
                    "file_path": str(prompt_file),
                    "relative_path": str(prompt_file.relative_to(self.prompts_dir)),
                    "content": post.content,
                    **post.metadata,
                }
                prompts.append(prompt_data)
            except Exception as e:
                print(f"Warning: Failed to load {prompt_file}: {e}")

        self._prompts_cache = prompts
        return prompts

    def search(
        self,
        workflow: str | None = None,
        version: str | None = None,
        purpose: str | None = None,
        agent_role: str | None = None,
        tags: list[str] | None = None,
        model_hint: str | None = None,
        created_after: str | None = None,
        created_before: str | None = None,
    ) -> list[dict[str, Any]]:
        """
        Search prompts by various criteria.

        Args:
            workflow: Filter by workflow name
            version: Filter by version (e.g., "v1")
            purpose: Filter by purpose (substring match)
            agent_role: Filter by agent role (substring match)
            tags: Filter by tags (prompt must have ALL tags)
            model_hint: Filter by model hint (substring match in model_hints list)
            created_after: Filter by creation date (YYYY-MM-DD, inclusive)
            created_before: Filter by creation date (YYYY-MM-DD, inclusive)

        Returns:
            List of matching prompt dictionaries
        """
        all_prompts = self._load_all_prompts()
        results = []

        for prompt in all_prompts:
            # Filter by workflow
            if workflow and prompt.get("workflow") != workflow:
                continue

            # Filter by version
            if version and prompt.get("version") != version:
                continue

            # Filter by purpose (substring)
            if purpose and purpose.lower() not in prompt.get("purpose", "").lower():
                continue

            # Filter by agent_role (substring)
            if agent_role and agent_role.lower() not in prompt.get("agent_role", "").lower():
                continue

            # Filter by tags (must have ALL)
            if tags:
                prompt_tags = prompt.get("tags", [])
                if not all(tag in prompt_tags for tag in tags):
                    continue

            # Filter by model_hint (substring in model_hints list)
            if model_hint:
                model_hints = prompt.get("model_hints", [])
                if not any(
                    model_hint.lower() in str(hint).lower() for hint in model_hints
                ):
                    continue

            # Filter by creation date
            created_at = prompt.get("created_at")
            if created_at:
                if created_after and created_at < created_after:
                    continue
                if created_before and created_at > created_before:
                    continue

            results.append(prompt)

        return results

    def list_all(self) -> list[dict[str, Any]]:
        """List all prompts."""
        return self._load_all_prompts()

    def get_by_workflow(self, workflow: str) -> list[dict[str, Any]]:
        """Get all prompts for a specific workflow."""
        return self.search(workflow=workflow)

    def get_latest_version(self, workflow: str) -> dict[str, Any] | None:
        """Get the latest version of a prompt for a workflow."""
        prompts = self.get_by_workflow(workflow)
        if not prompts:
            return None

        # Sort by version (assuming semantic versioning or v1, v2, etc.)
        prompts.sort(key=lambda p: p.get("version", ""), reverse=True)
        return prompts[0]

    def clear_cache(self) -> None:
        """Clear the prompts cache (useful after adding new prompts)."""
        self._prompts_cache = None

