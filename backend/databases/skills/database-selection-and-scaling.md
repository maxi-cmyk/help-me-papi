---
name: database-selection-and-scaling
description: Guidelines on choosing a database (SQLite, Postgres) and how to scale it.
---

# Database Selection and Scaling

## Database Choice
- **Supabase (Postgres):** Use for Next.js apps or apps needing real-time updates and RLS. Offers easy auth + DB integration.
- **SQLite:** Use for basic Python backends (Flask/FastAPI) or local development. *Warning: Do not use SQLite on Vercel or other serverless providers with ephemeral filesystems.*

## Schema Rules
- **2-3 Tables Max for Prototypes:** Users + main entity + join table.
- **JSON Columns:** For flexible, uncertain data shapes, use JSONB.
- **Primary Keys:** Use UUIDs (Supabase) or TEXT/UUID (SQLite).
- **Timestamps:** Always include `created_at` and `updated_at`.
