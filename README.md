# help-me-papi

A high-velocity, domain-driven framework designed specifically for **Agentic Development** (AI + Human pair programming). This repository is structured to be a "plug-and-play" brain for Claude Code and other agentic IDEs, ensuring speed and consistency across all project phases.

---

##  The Agentic Workflow

Instead of writing code from scratch, you **Chain Macros**. Each domain folder contains a `PROMPTS.md` with standardized macros in the `[ROLE]` / `[TASK]` / `[OUTPUT]` format.

1.  **STRATEGY Phase**: Use `hackathons/PROMPTS.md` -> `IDENTIFY_PERSONA` and `IDEATE_PROJECT`.
2.  **SCAFFOLD Phase**: Use domain-specific macros like `SCAFFOLD_UI_COMPONENT` (Frontend) or `SCAFFOLD_FEATURE` (Hackathons).
3.  **POLISH Phase**: Use `AUDIT_UI_CLARITY` or `REVIEW_UX_HEURISTICS` to refine the output.

---

##  Repository Directory

Every domain follows the same cohesive, non-repetitive structure:

###  [Hackathons](./hackathons/)
*   **`PROMPTS.md`**: Strategic macros for ideation, scaffolding, and pitching.
*   **[`strategy-and-resources.md`](./hackathons/strategy-and-resources.md)**: The "Battle Plan" from T-minus 2 hours setup to the final pitch.
*   **`skills/`**: Centralized hackathon toolkits ([`backend.md`](./hackathons/skills/backend.md), [`frontend.md`](./hackathons/skills/frontend.md), [`hackathon-strategy.md`](./hackathons/skills/hackathon-strategy.md)).
*   **`docs/`**: High-level hackathon standards and pitch resources.

###  [Frontend](./frontend/)
*   **`PROMPTS.md`**: UI/UX specialist macros including component scaffolding.
*   **`docs/`**: Standards for Clarity-First design, Design System variables, and Tooling (Claude Code/Stitch/21st Dev).
*   *Standards: Whitespace-first, Semantic HTML, Token-based CSS.*

###  [Backend](./backend/)
*   **`PROMPTS.md`**: System design and API scaffolding macros.
*   **`docs/`**: Standards for API (Rest/GQL), Database (Supabase/Postgres), and Auth (Clerk).
*   *Standards: Security-first, modular service layers, explicit error envelopes.*

###  [AI & RAG](./AI/)
*   **`PROMPTS-ML.md` / `PROMPTS-RAG.md`**: Specialized macros for model selection and vector search pipelines.
*   **`docs/`**: Standards for prompt engineering and RAG architecture.

###  [Tools & MCP](./tools/)
*   **`docs/`**: Manuals for **Stitch MCP** (CSS sync) and **21st Dev MCP** (Component sourcing).

---

##  Setup & Execution

### Pre-Hackathon Checklist
Ensure your agent is equipped with the right tools before starting:
- **21st Dev**: `claude mcp add 21st-dev npx -y @21st-dev/mcp`
- **Stitch**: `claude mcp add stitch npx -y @_davideast/stitch-mcp proxy`

### The "Feature-First" Rule
All projects must follow the `features/[name]/` architecture. 
- `types.ts`: Domain interfaces.
- `actions.ts`: Server-side logic.
*This prevents AI context fragmentation and makes deployment atomic.*

---

##  Knowledge Management
This repo is a living library.
- **Standards**: Move proven patterns into the `domain/docs/` folder.
- **Skills**: Add tactical "how-to" files into the `domain/skills/` folder.
- **Ideas**: Draft project backlogs in `domain/ideas/`.

### 1. The Inbox
Drop raw notes or snippets into `inbox.md`. Tag each block with a categorical comment on the first line:
```markdown
#frontend/ui-ux/skills/new-pattern
## New UI Pattern
...
```

### 2. Processing the Inbox
Run the organization CLI to automatically move tagged blocks to their final destination:
```bash
python3 organiser.py
```
- **Tag Shorthand**: `#domain/topic` defaults to `domain/skills/topic.md`.
- **Rebuild Catalog**: Refresh the searchable index with `python3 organiser.py --catalog`.