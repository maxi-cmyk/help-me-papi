# Database Standards

## Schema
- Use migrations for all schema changes — never manually ALTER in production
- All tables have `id` (UUID or serial), `created_at`, `updated_at`
- Use `snake_case` for column names
- Add indexes on any column used in a WHERE, JOIN, or ORDER BY clause
- Avoid nullable columns where possible — prefer default values

## Queries
- No raw SQL strings in application code — use ORM or query builder
- No N+1 queries — always eager-load related data in a single query
- For analytics or reporting queries, run against ClickHouse or a read replica, not the primary DB

## Connection management
- Never open a new DB connection per request — use a connection pool
- For serverless (Vercel), use a pooled connection string (Supabase/Neon provide this)
- Set a connection limit appropriate to your plan

## Data hygiene
- Soft-delete (add `deleted_at` column) rather than hard-delete for user-facing data
- Never store plaintext passwords — always hashed (bcrypt or argon2)
- Sensitive fields (SSN, card numbers, etc.) are encrypted at the application layer

## Backup and safety
- Always test migrations on staging before running on production
- Keep migrations backward-compatible — don't drop a column until the old code is gone
- Verify backups exist and are restorable before going to production