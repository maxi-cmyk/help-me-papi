# Performance Standards

## Query rules
- No N+1 queries — all relational data is eager-loaded in a single query or batched
- No `SELECT *` on tables with more than 10 columns or any large text/blob columns
- No unbounded queries — all list queries have a `LIMIT`
- No analytics or reporting queries on the primary database — use ClickHouse or a read replica
- All queries involving user-supplied IDs scope by the current user (also a security requirement)

## Indexes
- All foreign key columns have an index
- All columns used in WHERE, JOIN ON, or ORDER BY on tables over 10,000 rows have an index
- All new indexes are verified with EXPLAIN ANALYZE before deploying
- Index additions are monitored for write performance impact

## Caching
- Hot, read-heavy data that changes less than once per minute is a candidate for caching
- All cached values have an explicit TTL — nothing cached indefinitely
- Cache invalidation happens synchronously on write
- Cache keys follow the pattern: `entity:id:field` (e.g. `user:123:profile`)

## Response times (targets)
- p50: under 100ms for read endpoints
- p95: under 500ms for all endpoints
- p99: under 2000ms for all endpoints
- Any endpoint consistently over 500ms at p95 is flagged for investigation

## Background jobs
- Email sending always goes through a job queue — never inline in a request handler
- Any operation that may take over 2 seconds goes to a background job
- Jobs have retry logic with exponential backoff
- Failed jobs are logged and alert

## Connection pooling
- Serverless deployments always use the pooled connection string
- Direct connection string is used only for migrations
- Max connections per pool instance is set below the database's connection limit

## Load testing
- Load tests run before any significant traffic increase (launches, campaigns)
- Load tests establish a baseline on every major endpoint change
- p95 threshold in load tests: 500ms. Failing this blocks deployment.