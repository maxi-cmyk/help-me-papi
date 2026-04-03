# Backend Documentation

This directory contains our highly modular, domain-driven backend documentation. It is rigorously structured to prevent AI context fragmentation when generating node code, databases, or CI pipelines.

## How to use this folder effectively

To get the most out of this structure when collaborating with an AI, follow this workflow:

1. **Attach the Mastery Skill**: When starting a new backend project, always attach the relevant overarching skill file from [`/skills`](./skills) (e.g., `webdev-backend.md` for production architecture or `hackathon-backend.md` for fast Vercel/Supabase prototyping). This gives the AI all constraints for language scaling, deployment, and framework choice.
2. **Combine with Prompts**: Use the templates in the local `PROMPTS.md` files (like `databases/prompts/prompts.md` or `api-design/prompts/design-and-review.md`) as your initial query. When generating, attach specific domain definitions (e.g. `auth/skills/auth-fundamentals.md`) alongside the prompt so the AI acts flawlessly.
3. **Modify per Project**: Use these files as a baseline. When you spin up a specialized project that uses non-standard infrastructure, copy and edit the local `decisions.md` directly into that project repository.

## Architecture & Directory Structure

- **[`api-design/`](./api-design/)**: Rules for creating REST vs GraphQL boundaries, Zod validation, and maintaining envelope tracking for error responses. 
- **[`auth/`](./auth/)**: Strict standards covering OAuth callbacks, session vs. JWT token implementation loops, and cryptographic safety.
- **[`ci-cd/`](./ci-cd/)**: Vercel vs Railway choices, GitHub actions orchestration, and monorepo release rules.
- **[`databases/`](./databases/)**: Schemas constraints spanning Prisma/Drizzle implementations to basic row level security constraints.
- **[`architecture/`](./architecture/)**: Fundamental structuring paradigms like Monoliths vs Microservices.
- **[`performance/`](./performance/)**: Strict standards for DB queries and edge function latencies.
- **[`security/`](./security/)**: Rules detailing rate-limiting, edge mitigations and attack deflections.
- **[`ideas/`](./ideas/)**: Scrappy thoughts, feature notes, and rapid prototyping logs.
