# help-me-papi

Shared knowledge base for prompts, skills, resources, and ideas — split by domains across frontend, backend, database, AI, and more.

## How to Use

1. Write notes in `inbox.md`, add `@github_user` first line, `#domain/topic` on the second line
2. Run `python3 organiser.py` to sort them into the repo
3. Run `python3 organiser.py --catalog` to rebuild the index
4. Commit and push

See [CONTRIBUTING.md](CONTRIBUTING.md) for the contributer guide.

## File Structure

```
├── frontend/          # UI/UX, components, styling, frameworks
├── backend/           # Server logic, APIs, auth, deployment (Vercel + Next.js)
├── database/          # Supabase, SQLite, schemas, migrations
├── AI/                # RAG, ML, embeddings, LLM workflows
├── hackathons/        # Strategy, playbooks, starter stacks (logistics only)
├── hardware/          # Hardware-specific notes
├── tools/             # Automation, custom CLI scripts, and MCP Servers
├── others/            # Cross-domain patterns, anything that doesn't fit above
├── inbox.md           # Drop notes here, sort them later
├── catalog.md         # Auto-generated index of everything
└── organiser.py       # The sorting engine
```

Each domain avoids nested subdirectories to prevent context fragmentation. The standard 4-pillar structure is:

- `skills/` — Foundational playbooks, tools, and workflows
- `ideas/` — Scrappy thoughts, experiments, backlog
- `guidelines.md` — Consolidated standards, decisions, toolings, and references
- `PROMPTS.md` — Copy-paste AI prompt templates

### Tag formats

| Format | Example | Routes to |
|--------|---------|-----------|
| `#domain/content-type/topic` | `#backend/skills/auth` | `backend/skills/auth.md` |
| `#domain/topic` | `#backend/auth` | `backend/skills/auth.md` (defaults to skills/) |
| `#domain/content-type` | `#frontend/skills` | `frontend/skills/_inbox.md` (folder-level) |

Folder-level tags land in `_inbox.md` inside that folder — a staging area you can sort into named files later. Tags are case-insensitive (`#ai/skills` finds `AI/skills/`).

Because we only use `skills` and `ideas` as route-able subdirectories, shorthand tags will naturally default into the `skills/` subfolder when auto-created. All other core documentation should be explicitly created at the domain's root.

## Sorting

```bash
python3 organiser.py                    # sort inbox.md
python3 organiser.py --dry-run          # preview without changing anything
python3 organiser.py --create           # auto-create files/folders for new tags
python3 organiser.py path/to/file.md    # sort a different file
```

The organiser backs up `inbox.md` to `inbox.md.bak` before modifying it, deduplicates blocks, and prints a summary of what moved where.

## Catalog

```bash
python3 organiser.py --catalog
```

Regenerates `catalog.md` — a browsable index of every file grouped by domain, with contributor attribution. `_inbox.md` staging files are excluded. Commit it alongside your changes so everyone can browse what's available.