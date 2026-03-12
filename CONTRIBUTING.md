# Contributing

Quick guide for anyone adding to the repo.

## The 30-second version

1. Write your note in `inbox.md` with a `#domain/topic` tag.
2. Run `python3 organiser.py` to sort it into the right file.
3. Run `python3 organiser.py --catalog` to update the index.
4. Commit and push.

## Adding content

### Option A: Inbox (recommended for quick notes)

Open `inbox.md` and add a block with a tag. Separate blocks with a blank line.

```markdown
Useful pattern for handling optimistic updates with server actions
#backend/skills/nextjs

Great Tailwind plugin for animations: https://example.com
#frontend/resources/ui-ux

Not sure what file this belongs in yet, but it's a frontend skill
#frontend/skills
```

The first two tags route to specific files. The third is a **folder-level tag** — it lands in `frontend/skills/_inbox.md` so you can file it properly later.

Then run the organiser to sort everything:

```bash
python3 organiser.py           # sort inbox
python3 organiser.py --dry-run # preview first if you're unsure
```

### Option B: Direct edit

If you know exactly where something belongs, just edit the file directly. No need to go through inbox.

### Creating a new file

If you tag something that doesn't have a file yet, two options:

```bash
# Let the organiser create it for you
python3 organiser.py --create

# Or create it manually
mkdir -p database/skills
touch database/skills/migrations.md
```

Shorthand tags (like `#database/migrations`) default to the `skills/` subfolder when auto-created. Use the explicit form (`#database/resources/migrations`) if you want a different content type.

### Folder-level tags

If you know the domain and content type but not the specific file, tag with just the folder:

```markdown
Some auth notes I haven't filed yet
#backend/skills
```

This lands in `backend/skills/_inbox.md`. Periodically review `_inbox.md` files and move blocks into named files. These files are excluded from the catalog.

## File conventions

### Contributor tag

Add this as the **first line** of any file you create or meaningfully contribute to:

```markdown
<!-- @your-name -->
```

Multiple contributors:

```markdown
<!-- @maxi, @jin, @wei -->
```

This isn't about ownership — it's so anyone can quickly find who to ask about a topic. The catalog uses these to build a contributor index.

### Content types

Each domain can have these subfolders:

| Folder | What goes in it |
|--------|----------------|
| `skills/` | How-to guides, workflows, principles, playbooks |
| `prompts/` | Copy-paste prompts for AI tools (Claude, GPT, Copilot) |
| `resources/` | Links, libraries, tools, cheat sheets, references |
| `ideas/` | Experiments, half-baked thoughts, backlog items |

Not every domain needs every subfolder. Create them as needed.

### Headings

Start each file with a `# Title` heading. The catalog uses this as the display name. Without it, the catalog falls back to the filename.

## Domains

| Domain | What belongs here | Who typically owns it |
|--------|-------------------|----------------------|
| `frontend/` | UI/UX, components, styling, frameworks, client-side logic | |
| `backend/` | Server logic, APIs, auth, middleware, deployment, Vercel config | |
| `database/` | Supabase, SQLite, schemas, migrations, queries, RLS policies | |
| `AI/` | RAG, ML, embeddings, LLM workflows, fine-tuning | |
| `hackathons/` | Strategy, playbooks, judging tips, starter stacks (**logistics only**) | |
| `hardware/` | Hardware-specific notes | |
| `others/` | Cross-domain patterns, anything that doesn't fit above | |

Fill in the "Who typically owns it" column as you go — it helps newcomers know where to direct questions.

## What NOT to put in hackathons/

If it teaches a technical skill, it belongs in the domain folder, not hackathons. Hackathons is for logistics: strategy, time management, team coordination, judging criteria.

Instead of duplicating, hackathons links into domain folders:

```markdown
## Recommended auth setup
See [backend/skills/auth.md](../backend/skills/auth.md) for the full pattern.
```

## Keeping things tidy

After adding or moving content:

```bash
python3 organiser.py --catalog
```

This rebuilds `catalog.md` so everyone can browse what's available. Commit it alongside your changes.

## Questions?

If a tag isn't resolving or you're not sure where something belongs, check `catalog.md` for the current structure, or just ask in the group.