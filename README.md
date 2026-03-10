# help-me-papi

Consolidated notes, prompts, skills, resources, and ideas across frontend, backend, database, deployment, AI and case by case use for hackathons.

## Structure

- `shared/` for cross-domain patterns, references, and repo-level ideas.
- `frontend/`, `backend/`, `database/`, `deployment/` for domain-specific material.
- `AI/` for AI-specific domains such as `RAG/` and `ML/`.
- `hackathons/` for strategy notes, prompts, and reusable references.

Each domain follows the same high-level pattern:

- `skills/` for reusable workflows, principles, and playbooks.
- `resources/` for links, libraries, tools, and references.
- `ideas/` for experiments, backlog items, and opportunities.
- `prompts/` for task-specific prompts.
- `standards.md` for rules and guardrails.
- `decisions.md` for important repo or domain decisions.

## Organiser

Tag notes with `#domain/topic` or `#domain/content-type/topic`, for example `#frontend/ui-ux` or `#backend/skills/auth`.

Run `python3 organiser.py` to sort notes from `inbox.md`, or `python3 organiser.py path/to/file.md` to sort a different file.
