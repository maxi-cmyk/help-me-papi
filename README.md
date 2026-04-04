# help-me-papi

A modular, domain-driven framework for rapid prototyping and high-standard software development. This repository is strictly organized to prevent AI context fragmentation and to provide a "choose-your-own-adventure" setup for different engineering goals.

---

## Development Paths

Select the focus area that matches your project goals to bias the generation and standards appropriately.

### Hackathon Focus
**Goal: Speed over Perfection**
Prioritize time-to-ship, feature velocity, and "Visual Wow". Leverage managed services (Supabase, Clerk) and high-impact UI trends (Glassmorphism, gradients) to deliver a polished MVP in hours.

### Webdev Focus
**Goal: Production Standards**
Focus on long-term maintainability, SEO, and architectural performance. Adhere to Feature-Sliced Design (FSD), strict accessibility compliance (WCAG AA), and robust CI/CD pipelines.

### Startup Focus
**Goal: Growth and Scalability**
Optimized for iterative growth, observability, and reliable scale. Includes standards for security-first architecture (OWASP), background job management, and deep analytics integration.

---

## AI-First Workflow

To use this repository effectively as an AI pair programmer, follow this three-step execution loop:

1. **Attach Mastery Skill**: At the start of a project, attach the relevant master skill file from the domain's `/skills` folder (e.g., `frontend/skills/startup-frontend.md`) to establish high-level architectural boundaries.
2. **Attach Domain Context**: When working on specific features, include the `standards.md`, `decisions.md`, and `skills/` files from that domain folder.
3. **Use Scaffold Prompts**: Use the token-efficient, context-aware prompt templates located in each domain's `prompts/` directory to ensure accurate generation.

---

## Repository Structure

The repository is split into specialized domains, each following a standardized modular architecture:

- **`frontend/`**: UI-UX heuristics, design inspirations, performance, and architecture.
- **`backend/`**: API design, authentication, databases, security, and CI-CD.
- **`hardware/`**: Firmware architecture, low-level math, components, and performance.
- **`hackathons/`**: Speed strategy, pitch planning, and high-velocity setups.
- **`AI/`**: RAG implementation and machine learning flow documentation.
- **`tools/`**: Automation scripts and Model Context Protocol (MCP) servers.
- **`others/`**: Shared Cross-domain resources and generic patterns.

---

## Knowledge Management

This repository uses a sorting CLI to manage knowledge intake and documentation indexing.

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