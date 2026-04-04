# Performance Decisions

## Measure before optimizing
Never optimize based on intuition. Run EXPLAIN ANALYZE, log queries, and load test first. Premature optimization wastes time and adds complexity that obscures real bottlenecks. The checklist in the skills file defines the order to investigate.

## Redis (Upstash) for caching over in-memory application cache
In-memory caches don't survive server restarts, don't work across multiple instances, and grow unboundedly. Redis is persistent, shared across instances, and has TTL built in. Upstash is the managed option — serverless pricing and no infrastructure to manage.

## BullMQ for job queues in persistent deployments, Inngest for serverless
BullMQ is battle-tested and Redis-backed, but requires a persistent worker process. Inngest works in serverless environments (Vercel) where you can't run a background worker — it triggers your Next.js API routes as jobs. Use BullMQ on Railway/Fly.io, Inngest on Vercel.

## DataLoader only for GraphQL or genuinely complex batching scenarios
DataLoader adds complexity. In most REST APIs, N+1 is solved more simply with ORM eager-loading (`include`). Only reach for DataLoader when you're in a resolver tree where you can't control how many times a function is called.

## Cursor-based pagination over offset for performance at scale
`OFFSET 10000 LIMIT 20` requires PostgreSQL to read and discard 10,000 rows before returning 20. Cursor-based pagination (`WHERE id > $cursor LIMIT 20`) always reads exactly 20 rows regardless of page number. The difference is negligible on small tables, significant on large ones.

## k6 for load testing over Artillery or Locust
k6 has the best JavaScript API, good defaults, and easy CI integration. Its threshold system lets you fail a test automatically if p95 exceeds a target. Artillery is a reasonable alternative if the team prefers YAML-based configuration.