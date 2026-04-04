# Backend Documentation

This directory contains our highly modular, domain-driven backend documentation. It is rigorously structured to prevent AI context fragmentation when generating code, databases, or CI pipelines.

## Hackathon Focus (Speed over Perfection)

When building for a hackathon, prioritize **Time to Ship** and **Feature Velocity**.

- **Auth**: Use managed providers (Supabase Auth, Clerk) instead of rolling custom JWT logic.
- **Database**: Use Prisma or Drizzle for instant migrations and type safety.
- **Validation**: Use Zod for all incoming data to prevent runtime crashes.
- **Deployment**: Vercel (for serverless) or Railway (for persistent) with zero-config.
- **LLM Usage**: Use the specific "Hackathon" skill files in `/skills` to bias the AI toward rapid prototyping.

---

## Webdev Focus (Production Standards)

For standard production web applications, prioritize **Reliability** and **Developer Experience**.

- **Architecture**: Use Clean Architecture or Service Layers to decouple business logic from framework code.
- **CI/CD**: Robust pipelines with automated testing, linting, and type-checking on every PR.
- **Logging**: Structured, searchable logging (e.g., Pino) to enable rapid debugging in production.
- **API**: Versioned endpoints and well-documented schemas using Zod or OpenAPI.

---

## Startup Focus (Growth & Scalability)

For startups, prioritize **Observability** and the **Safety to Pivot**.

- **Security**: Implement proactive monitoring, rate-limiting, and OWASP-compliant security headers.
- **Scalability**: Move heavy tasks (e.g., image processing, bulk emails) to background jobs (BullMQ/Redis).
- **Monitoring**: Integrated error tracking (Sentry) and uptime monitoring to fix issues before users report them.
- **Data Safety**: Automated backups, disaster recovery plans, and Row-Level Security (RLS) as a baseline.

---

## How to use this folder effectively

To get the most out of this structure when collaborating with an AI, follow this workflow:

1. **Attach the Mastery Skill**: When starting a new backend project, always attach the relevant overarching skill file from [`/skills`](./skills) (e.g., `webdev-backend.md` for production or `hackathon-backend.md` for speed).
2. **Combine with Prompts**: Use the templates in the local `prompts/` subdirectories. Attach specific domain definitions (e.g. `auth/skills/auth-fundamentals.md`) alongside the prompt.
3. **Modify per Project**: Use these files as a baseline. For specialized projects, copy the `decisions.md` file to your project root.

---

## Architecture & Directory Structure

Every domain follow a strict modular structure:
`domain/`
├── `skills/` — Domain-specific fundamentals and best practices.
├── `prompts/` — Robust, token-efficient scaffolds for AI generation.
├── `resources/` — Curated links, libraries, and external documentation.
├── `ideas/` — Scrappy thoughts and rapid prototyping logs.
├── `standards.md` — Hard rules for the domain (e.g., security checklists).
└── `decisions.md` — Architectural choices and justifications.

### Domains:
- **[`api-design/`](./api-design/)**: REST/GraphQL boundaries, Zod validation, and error envelopes.
- **[`auth/`](./auth/)**: OAuth, session/JWT implementation, and cryptographic safety.
- **[`ci-cd/`](./ci-cd/)**: Vercel/Railway choices, GitHub Actions, and release rules.
- **[`databases/`](./databases/)**: Prisma/Drizzle schemas, RLS, and migration standards.
- **[`architecture/`](./architecture/)**: Fundamental structuring (Monoliths vs Microservices).
- **[`performance/`](./performance/)**: Query optimization and edge function latency rules.
- **[`security/`](./security/)**: Rate-limiting, attack deflection, and security headers.
- **[`ideas/`](./ideas/)**: Cross-domain brainstorming and feature notes.
