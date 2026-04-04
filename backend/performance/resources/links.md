# Performance Resources

## PostgreSQL query analysis
- https://explain.depesz.com — paste EXPLAIN ANALYZE output, get a visual breakdown
- https://explain.dalibo.com — alternative visual EXPLAIN ANALYZE tool
- https://use-the-index-luke.com — free book on SQL indexing, one of the best practical references
- https://www.postgresql.org/docs/current/performance-tips.html — official performance tips
- https://pganalyze.com — continuous query performance monitoring (paid, but has a free tier)

## ORM query optimization
- https://www.prisma.io/docs/orm/prisma-client/queries/query-optimization-performance — Prisma performance guide
- https://orm.drizzle.team/docs/performance — Drizzle performance guide

## Caching
- https://redis.io/docs/manual/patterns — Redis patterns including caching
- https://upstash.com/docs/redis/sdks/ratelimit-ts/overview — Upstash rate limiting
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching — HTTP caching headers

## Background jobs
- https://docs.bullmq.io — BullMQ docs
- https://inngest.com/docs — Inngest docs (serverless-friendly)
- https://trigger.dev/docs — Trigger.dev docs (alternative to Inngest)
- https://github.com/timgit/pg-boss — pg-boss (Postgres-backed queue, no Redis needed)

## Load testing
- https://k6.io/docs — k6 docs
- https://k6.io/docs/test-types/load-testing — different load test types explained
- https://grafana.com/docs/k6/latest/results-output — interpreting k6 results

## Connection pooling
- https://www.pgbouncer.org — PgBouncer docs
- https://neon.tech/docs/connect/connection-pooling — Neon connection pooling
- https://supabase.com/docs/guides/database/connecting-to-postgres — Supabase connection pooling