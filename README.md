# help-me-papi

Shared knowledge base for prompts, skills, resources, and ideas — split by domains across frontend, backend, database, AI, and more.

## The AI Workflow

To use this repository effectively as an AI pair programmer, follow this three-step execution loop:

1. **Attach the Mastery Skill**: When starting a project, drop the relevant master skill into the AI context from `/skills` folders (e.g., `frontend/skills/startup-frontend.md`). This gives the AI the high-level boundaries and architectural logic you want to follow.
2. **Combine with Prompts**: Use task-specific templates from the local `PROMPTS.md` files or specialized domain prompt folders (e.g., `backend/api-design/prompts/design-and-review.md`).
3. **Modify per Project**: These files are your baseline. For specific projects with unique constraints, fork and modify the rule-files (like `decisions.md`) directly in that project repository to ensure the AI's generation matches your local reality.

## File Structure

The repository is split into specialized domains, each with its own internal modular structure:

- **`frontend/`**: Architecture, design-inspos, performance, and UI-UX.
- **`backend/`**: API design, auth, databases, security, and CI-CD.
- **`hardware/`**: Firmware architecture, low-level math, components, and performance.
- **`hackathons/`**: Strategy, pitch planning, and high-velocity boilerplate setups.
- **`AI/`**: RAG and ML flow documentation.
- **`tools/`**: Automation scripts and Model Context Protocol (MCP) servers.
- **`others/`**: Shared, cross-domain resources and generic patterns.

## The Organiser

This repository uses a sorting CLI to manage knowledge intake.

### 1. The Inbox
Drop raw notes or snippets into `inbox.md`. Tag each block with a comment on the first line:
```markdown
#frontend/ui-ux/skills/new-pattern
## New UI Pattern
...
```

### 2. Running the Sorting
Run the CLI to automatically move tagged blocks to their final destination:
```bash
python3 organiser.py
```
- Tag Shorthand: `#domain/topic` defaults to `domain/skills/topic.md`.
- Catalog: Rebuild the browsable index of everything with `python3 organiser.py --catalog`.

## Shared Resources

Use the **`others/`** directory for any pattern or documentation that applies universally across the stack (e.g., generic coding standards, general documentation frameworks). Before creating a new file in a specific domain, check if a shared pattern already exists in `others/`.