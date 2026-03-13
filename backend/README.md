# Backend

Backend architecture and documentation for hackathons and rapid prototyping. 

## Documentation Structure

The backend documentation is structured into core pillars to prevent context fragmentation:

- **[`SKILLS.md`](./skills/SKILLS.md)**: The foundational constraint framework for fast, demo-able backends. Read this or provide it as a system prompt to an AI before proposing any architecture changes.
- **[`architecture-and-api.md`](./architecture-and-api.md)**: The engineering rules. Covers route structuring, the "Vanilla-First" principle, database seeding, and our strict 2-3 table limit rule.
- **[`deployment-and-auth.md`](./deployment-and-auth.md)**: The DevOps rules. How to deploy to Vercel/Railway in hour one, set up basic Supabase/JWT authentication, and keep the application live.
- **[`PROMPTS.md`](./PROMPTS.md)**: Copy-paste prompt templates for instructing LLMs to generate feature code or debug complex production errors.
- **`/ideas`**: Scrappy thoughts, feature notes, and backlog items.
