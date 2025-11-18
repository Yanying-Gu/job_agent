## Overview

This experiment sets up an n8n multi-agent flow dedicated to CV refinement. A master agent coordinates two specialized tool agents, ensuring CV updates and reviews happen in a single automated loop.

## Agent Roles

- **Master Agent**  
  Orchestrates the workflow using `master_agent_prompt.txt`. It receives the user request along with a JSON-formatted job description payload, interprets intent, sequences calls to tool agents, and consolidates the final response.

- **Update CV Agent**  
  Follows `update_cv_agent_prompt.txt` to rewrite or improve the CV. It focuses on tailoring language, structure, and keyword alignment to specific job targets.

- **CV Review Agent**  
  Uses `cv_review_agent_prompt.txt` to critique the updated CV, checking coherence, tone, and alignment with job descriptions.

## Workflow Summary

1. Master agent receives the user request and JSON job description from n8n.
2. Master agent delegates to the Update CV agent for drafting or revisions.
3. Master agent forwards the result to the CV Review agent for critique.
4. Master agent aggregates review feedback and returns the consolidated output.

## Related Files

- `master_agent_prompt.txt` – core instructions for the orchestrator.
- `update_cv_agent_prompt.txt` – guidance for generating CV updates.
- `cv_review_agent_prompt.txt` – guidance for reviewing updated CVs.
- `../../data/jd_template.json` – template describing desired job attributes.
- `../../data/job_description.json` – sample JSON job description payload referenced by the master agent.

## Notes

- Ensure n8n nodes reference the renamed prompt files.
- Future iterations can add more tool agents (e.g., cover letter generation) within the same orchestration pattern.

