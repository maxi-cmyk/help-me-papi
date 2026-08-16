# Backend Core Standards

Cross-cutting rules that apply to the entire backend, regardless of domain.

## API Responses
- All APIs must return JSON with a consistent shape.
- Success: `{ "data": { ... } }`
- Error: `{ "error": "Message", "details": { ... } }`

## Secrets & Config
- All secrets go in environment variables (`.env.local`), never in code.
- `.env*.local` must always be in `.gitignore`.

## Database Access
- All DB queries should go through an ORM (Prisma/Drizzle) or query builder.
- No raw SQL in route handlers or controllers.

## Security
- Rate limit all public endpoints.
- Validate all incoming request payloads against a schema (e.g. Zod).

---

## Dual-App Monorepo Pattern (Epicenter Case Study)

When a product has **two distinct user-facing apps** (e.g., patient portal + nurse dashboard) sharing one backend:

```
epicenter/
├── frontend/
│   ├── patient/     # Vercel project 1, port 3000
│   ├── nurse/       # Vercel project 2, port 3001
│   └── shared/      # types, tokens, safe presentation primitives
├── backend/         # FastAPI, single Railway API + worker
├── supabase/        # migrations + seeds
└── docs/            # PRD, workflow, deployment runbook
```

### Contract-First Design
- The **FastAPI schema is the contract**. Both frontends call the same endpoints, never each other.
- After any backend request/response change, **regenerate TypeScript contracts** (`npm run contracts:generate`) and verify (`npm run contracts:check`). Keep the generated types checked in so frontend and backend can't drift silently.

### Demo Mode
- For local dev and automated tests, add an explicit `DEMO_MODE=true` that uses synthetic principals (fake patient/nurse IDs) instead of real Clerk sessions. This lets the whole app run without provisioning live auth providers — but document clearly: this mode proves workflow, not real isolation.

### LLM-Through-Backend (Epicenter Lesson)

When the product uses a frontier model (OpenAI, Claude):

- **Never expose the key to the browser.** The browser talks to FastAPI; FastAPI talks to OpenAI. The key lives only in the backend's `.env` or Railway secrets.
- **Never name a browser env var with `NEXT_PUBLIC_*` prefix for secrets.** That prefix is only for genuinely public config (API URL, publishable key).
- **Pin the model** once evaluated. A pinned model + eval set gives reproducible behavior. "Latest" is a silent regression.
- **Graceful degradation**: normal workflows, dashboards, and simulators must continue to work when the LLM is unavailable. The LLM is an enhancement, not the only path.

### MCP Publication (Streamable HTTP)

If you expose custom MCP servers (Operations, Insurance Format Registry) for external platforms (Copilot Studio):
- Serve over **public HTTPS Streamable HTTP**, not just local stdio.
- Keep the business logic in the backend; the MCP server is a thin adapter that wraps it. Don't fork logic.
- Document a verification checklist: tool discovery works, a read-only synthetic call succeeds, licensing is approved.

### Gated Task Flow (Epicenter Lesson)

For complex workflows (patient registration → nurse review → billing):
- Model the flow as **explicit gated steps** with a clear state machine. Each gate has preconditions and post-conditions.
- Keep the patient on **one persistent ticket** throughout. Exceptions don't create new tickets — they stay on the same record.
- A **deterministic simulator** (serial_baseline, single_ticket, dynamic_allocation) lets the team replay scenarios without touching operational data. The simulator must never write to production tables.
