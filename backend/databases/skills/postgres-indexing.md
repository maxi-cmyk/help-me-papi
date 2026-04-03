---
name: postgres-indexing
description: Guidelines on database indexing and performance tuning.
---

# Postgres Indexing and Performance

*This is a placeholder for detailed indexing and performance rules (such as N+1 query prevention, index types, caching).*

- Use B-tree indexes for standard equality/range checks.
- Avoid N+1 queries by leveraging eager loading via your ORM (e.g. Prisma `include`) or query joins.
- Use connection pooling (like Supavisor/PgBouncer) for serverless environments.
