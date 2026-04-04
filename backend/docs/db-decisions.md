# Database Decisions

## PostgreSQL as the default relational DB (over MySQL)
Postgres has better JSON support (JSONB), better full-text search, more advanced indexing (partial indexes, GIN indexes), and is the standard in the modern startup ecosystem. Supabase, Neon, and Railway all default to Postgres. MySQL is fine but Postgres wins on ecosystem and features.

## Supabase as the managed Postgres choice for early-stage
Supabase bundles Postgres + auth + realtime + storage + edge functions. It removes a lot of early infrastructure work. The free tier is generous. Downside: vendor lock-in on the auth/realtime layer, but the Postgres itself is portable.

## Neon for preview/staging environments
Neon supports branching  you can create a copy of your database per PR branch, run tests against it, then delete it. Pairs well with Vercel preview deployments.

## Upstash for Redis (over self-hosted)
Upstash is serverless and bills per request. At startup scale, you're not running enough Redis operations to justify a dedicated instance. Upstash also has a free tier and integrates directly with Vercel.

## ClickHouse for analytics (separate from operational DB)
Do not run analytics queries on your main Postgres database. A `SELECT COUNT(*) GROUP BY country` over 10M rows will lock up your DB and affect your users. ClickHouse is built specifically for this workload. Route events there asynchronously.

## Drizzle over Prisma for newer projects
Prisma has better docs and a gentler learning curve. Drizzle is more lightweight, has better TypeScript inference, and generates less abstraction overhead. For hackathons or quick projects, Prisma. For production work, Drizzle is worth the setup.

## No raw SQL in route handlers
All queries go through an ORM or query builder. Raw SQL strings in route handlers are harder to refactor, easier to accidentally make injectable, and break IDE autocomplete.