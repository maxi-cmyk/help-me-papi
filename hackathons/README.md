# Hackathons Documentation

This directory organizes ideas, file structures, and specific tactics built strictly for 24-48 hour Hackathon environments. 

## The "Product Manager vs Engineers" Model

Think of the repository separation as delegating responsibilities when collaborating with AI:

- The `hackathons/` folder is your **Product Manager & Architect**. You use this in Hours 1-3 to plan *WHAT* you are building and *WHY*.
- The `frontend/` and `backend/` folders are your **Engineers**. You use these in Hours 3-24 to dictate *HOW* the code should be written.

## Hackathon Workflow
To move as fast as possible, execute this exact loop:

1. **Phase 1: Brainstorming (Hours 13)**
   Feed `strategy-and-resources.md` and `PROMPTS.md` to the AI. Use these constraint guidelines to force the AI to strip away feature bloat, lock onto a minimum viable product, and write the pitch angle.
2. **Phase 2: Scaffolding (Hour 3)**
   Feed `file-structure.md` to the AI. Instruct it to generate the exact bash commands needed to scaffold your Next.js monolithic repo so you avoid split-deployment CORS issues.
3. **Phase 3: Coding Execution (Hours 4-24)**
   Stop using the PM folder. Open your IDE and drop `hackathons/skills/frontend.md` and `hackathons/skills/backend.md` into the AI context window. This ensures the AI skips enterprise optimization (like strict generic typing) and ruthlessly writes fast, dirty, demo-ready code.

## Organising Notes

Use `python3 organiser.py` to sort `#path/to/file` tagged blocks from the repo inbox, or any source file you pass in.

- Tags should resolve to an existing repo destination.
- Short tags like `#hackathons/persona` default to resolving into the `skills/` subfolder, creating `hackathons/skills/persona.md`.
- Full tags like `#frontend/skills/ui-ux` also work.
- Unmatched blocks stay in the source file.

## Architecture & Directory Structure

To maximize velocity during high-pressure events, the hackathon domain is categorized as:

- **[`prompts/`](./prompts/)**: [Scaffolds](./prompts/scaffolds.md) for rapid pitching and coding.
- **[`skills/`](./skills/)**: [Persona](./skills/persona.md) and velocity playbooks.
- **[`resources/`](./resources/)**: Boilerplates and demo-ready assets.
- **[`ideas/`](./ideas/)**: Pitch decks and raw project seeds.
- **[`standards.md`](./standards.md)**: Global hackathon rules (Speed > Perfection).
- **[`decisions.md`](./decisions.md)**: Stack choices and "fake it" justifications.
- **[`file-structure.md`](./file-structure.md)**: Next.js monolithic repo constraints.
- **[`strategy-and-resources.md`](./strategy-and-resources.md)**: Judging and pitch logic.
