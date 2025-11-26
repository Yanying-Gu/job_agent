## Prompt & Workflow Setup Template

Metadata:
- Type: workflow
- Tags: workflow, prompts, frontmatter, sync-script

Variables:
- `<NEW_WORKFLOW_NAME>`
- `<MASTER_PROMPT_FILE>`
- `<UPDATE_SCRIPT_PATH>`

Use this template whenever you introduce a new workflow (e.g., `workflow/<NEW_WORKFLOW_NAME>.json`) so prompts, scripts, and documentation stay consistent.

### 1. Frontmatter Prompt Files

- Store prompts under `prompts/<NEW_WORKFLOW_NAME>/`.
- Each prompt must begin with YAML frontmatter:
  ```yaml
  ---
  workflow: <NEW_WORKFLOW_NAME>
  purpose: <one-line description>
  agent_role: <role>
  version: v1
  tags: [ ... ]
  model_hints:
    - <hint>
  created_at: "YYYY-MM-DD"
  ---
  ```
- Place the original prompt content immediately after the frontmatter.

### 2. Update Existing Prompts

- Convert each `<agent>_prompt.txt` (master, update_cv, cv_review, etc.) to frontmatter format.
- Keep the instruction text intact unless explicitly requested.

### 3. Workflow Sync Script

- Create `src/scripts/update_<NEW_WORKFLOW_NAME>.py` modeled after `update_cv_enhancer.py` / `update_multi_agent.py`.
- The script should:
  1. Load the relevant prompt file with `frontmatter`.
  2. Inject the prompt text into the AI Agent node in `workflow/<NEW_WORKFLOW_NAME>.json`.
  3. Print a confirmation message.
- Run it via:
  ```bash
  poetry run python src/scripts/update_<new_workflow>.py
  ```

### 4. Documentation

- Update (or create) `prompts/<NEW_WORKFLOW_NAME>/README.md` to describe:
  - The agent roles and prompt files.
  - The workflow JSON location (`workflow/<NEW_WORKFLOW_NAME>.json`).
  - The sync script command.
- If needed, mention the new workflow/script in the root `README.md`.

### 5. Validation

- Ensure `poetry.lock` is updated if dependencies changed.
- Verify prompts load correctly via `PromptRegistry` / `search_prompts.py`.

### Completion Summary

When finished, summarize:
1. Which prompts were converted to frontmatter.
2. Which workflow sync script was added/updated.
3. Which docs/readme sections were touched.


