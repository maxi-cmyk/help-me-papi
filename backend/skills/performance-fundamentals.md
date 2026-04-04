# Backend Performance

## Mental model: where time actually goes

Before optimizing anything, understand where the time goes in a typical API request:

```
Incoming request
   Network (client  server)           ~150ms    (you can't control this)
   Framework routing + middleware       ~02ms     (negligible)
   Auth check (session lookup)          ~15ms     (usually Redis or in-memory)
   Database queries                     ~1ms10s   (YOUR BIGGEST LEVER)
   Business logic / computation         ~050ms    (rarely the bottleneck)
   Serialization + response             ~05ms     (negligible unless huge payload)
```

In almost every backend performance problem, the database is the bottleneck. Optimize there first.

---

## N+1 queries  the most common performance bug

### What it is

An N+1 query happens when you fetch a list of N items, then run an additional query for each item to get related data. You end up making N+1 database round-trips instead of 1 or 2.

### Example

You want to display 20 blog posts with their authors' names.

**The N+1 version (wrong):**
```typescript
// 1 query to fetch posts
const posts = await db.post.findMany({ take: 20 });

// Then 20 more queries  one per post  to fetch each author
for (const post of posts) {
  post.author = await db.user.findUnique({ where: { id: post.authorId } });
}
```

This runs 21 database queries. If you have 100 posts per page, it's 101. At scale this kills your DB.

**The correct version:**
```typescript
// 1 query  JOIN fetches posts and authors together
const posts = await db.post.findMany({
  take: 20,
  include: { author: true },  // Prisma
});
```

This runs 1 or 2 queries total (Prisma typically uses a second query with IN rather than a JOIN, but either way it's fixed-cost regardless of the number of posts).

**With raw SQL:**
```sql
-- One query with a JOIN
SELECT posts.*, users.name AS author_name
FROM posts
JOIN users ON posts.author_id = users.id
LIMIT 20;
```

### How to detect N+1 in development

Log all SQL queries your ORM runs. In Prisma:
```typescript
const db = new PrismaClient({
  log: ['query'],
});
```

If you see the same query repeated N times with different IDs, you have an N+1.

In production, use a tool like pganalyze or look at your database's slow query log.

### DataLoader pattern (for GraphQL or complex cases)

If you're in a situation where you can't easily eager-load (e.g. a GraphQL resolver), DataLoader batches individual lookups into a single query:

```typescript
import DataLoader from 'dataloader';

const userLoader = new DataLoader(async (userIds: readonly string[]) => {
  const users = await db.user.findMany({
    where: { id: { in: userIds as string[] } },
  });
  // DataLoader requires results in the same order as keys
  return userIds.map(id => users.find(u => u.id === id) ?? null);
});

// Now every resolver can call this independently, but they're batched
const author = await userLoader.load(post.authorId);
```

---

## PostgreSQL indexing  the most impactful single optimization

### What an index is

An index is a separate data structure that PostgreSQL maintains alongside your table. It lets the DB find rows matching a condition without scanning every row in the table.

Without an index:
```
SELECT * FROM orders WHERE user_id = 123;
-- PostgreSQL reads every single row in the orders table
-- On 10M rows: ~500ms
```

With an index on `user_id`:
```
CREATE INDEX idx_orders_user_id ON orders(user_id);
-- PostgreSQL uses a B-tree to jump directly to matching rows
-- On 10M rows: ~1ms
```

### When to add an index

Add an index on any column that appears in:
- `WHERE` clauses
- `JOIN ... ON` conditions
- `ORDER BY` clauses
- `GROUP BY` clauses

```sql
-- Common cases that need indexes
SELECT * FROM posts WHERE author_id = ?;        -- index on author_id
SELECT * FROM sessions WHERE token = ?;         -- index on token
SELECT * FROM events WHERE created_at > ?;      -- index on created_at
SELECT * FROM posts ORDER BY created_at DESC;   -- index on created_at

-- JOIN condition
SELECT * FROM posts JOIN users ON posts.author_id = users.id;
-- index on posts.author_id (users.id is already indexed as PK)
```

### How to check if your query uses an index

```sql
EXPLAIN ANALYZE SELECT * FROM orders WHERE user_id = 123;
```

Look for `Index Scan` (good) vs `Seq Scan` (full table scan, bad on large tables).

```
-- Good: uses the index
Index Scan using idx_orders_user_id on orders
  Index Cond: (user_id = 123)
  Actual rows: 15, loops: 1
  Actual time: 0.042 ms

-- Bad: reads every row
Seq Scan on orders
  Filter: (user_id = 123)
  Rows removed by filter: 9985
  Actual rows: 15, loops: 1
  Actual time: 487.312 ms
```

### Composite indexes

When you filter on multiple columns together, a composite index is more efficient than two separate indexes:

```sql
-- You frequently run:
SELECT * FROM posts WHERE author_id = ? AND status = 'published';

-- A composite index covers both conditions
CREATE INDEX idx_posts_author_status ON posts(author_id, status);
```

**Column order matters.** The leftmost column must match your most selective filter. The index above can also serve `WHERE author_id = ?` alone, but NOT `WHERE status = 'published'` alone (the leftmost rule).

### Partial indexes

Index only the rows you actually query. If you only ever query active users, don't index the inactive ones:

```sql
CREATE INDEX idx_users_active ON users(email) WHERE deleted_at IS NULL;
```

This index is smaller, faster to build, and faster to query.

### Indexes on foreign keys

PostgreSQL does NOT automatically create indexes on foreign key columns (unlike MySQL). Always add them manually:

```sql
-- If posts.author_id references users.id, add this:
CREATE INDEX idx_posts_author_id ON posts(author_id);
```

Without this, any JOIN or lookup by foreign key does a full table scan.

### The cost of indexes

Indexes are not free. Every index:
- Takes up disk space
- Slows down `INSERT`, `UPDATE`, and `DELETE` (the index must be updated too)
- Must be maintained by PostgreSQL's autovacuum

Don't add indexes speculatively. Add them when you have a proven slow query. A table with 20 indexes on it will have noticeably slow writes.

### Finding missing indexes in production

```sql
-- Find sequential scans on large tables (missing indexes)
SELECT schemaname, tablename, seq_scan, seq_tup_read, idx_scan
FROM pg_stat_user_tables
WHERE seq_scan > 0
ORDER BY seq_tup_read DESC;

-- Find slow queries (requires pg_stat_statements extension)
SELECT query, mean_exec_time, calls
FROM pg_stat_statements
ORDER BY mean_exec_time DESC
LIMIT 20;
```

---

## Query optimization patterns

### Select only what you need

```typescript
// Bad: fetches all columns, including large text fields, blobs, etc.
const users = await db.user.findMany();

// Good: only fetch what you actually use
const users = await db.user.findMany({
  select: { id: true, name: true, email: true },
});
```

In raw SQL: `SELECT id, name, email FROM users` not `SELECT *`.

This matters especially when tables have large text columns, JSON blobs, or many columns you don't need.

### Avoid COUNT(*) on large tables for pagination

```sql
-- This scans the entire table every time you load a page
SELECT COUNT(*) FROM posts WHERE author_id = 123;
```

Alternatives:
- Use cursor-based pagination (no COUNT needed)
- Maintain a counter in a separate column (increment on insert, decrement on delete)
- Use approximate counts for display: `SELECT reltuples FROM pg_class WHERE relname = 'posts'`

### Use database-level operations instead of application-level

```typescript
// Bad: fetch all, filter in JS
const users = await db.user.findMany();
const activeUsers = users.filter(u => u.active);

// Good: filter in the database
const activeUsers = await db.user.findMany({ where: { active: true } });
```

The database is orders of magnitude faster at filtering than your application code, and you avoid transferring unnecessary data over the network.

### Batch writes with transactions

```typescript
// Bad: 100 separate INSERT queries
for (const item of items) {
  await db.item.create({ data: item });
}

// Good: single transaction
await db.$transaction(
  items.map(item => db.item.create({ data: item }))
);

// Even better for very large batches: createMany
await db.item.createMany({ data: items });
```

---

## Caching strategies

Caching stores the result of expensive operations so you don't repeat them. The key question is always: **how stale is acceptable?**

### Cache-aside (lazy loading)  most common

```
Request comes in
   Check cache (Redis)
       Cache hit  return cached value
       Cache miss  query database  store in cache  return value
```

```typescript
async function getUser(userId: string) {
  const cacheKey = `user:${userId}`;
  
  // 1. Check cache
  const cached = await redis.get(cacheKey);
  if (cached) return JSON.parse(cached);
  
  // 2. Cache miss  query DB
  const user = await db.user.findUnique({ where: { id: userId } });
  if (!user) return null;
  
  // 3. Store in cache with a TTL (time to live)
  await redis.setex(cacheKey, 300, JSON.stringify(user)); // 300 seconds = 5 min
  
  return user;
}

// When a user is updated, invalidate their cache entry
async function updateUser(userId: string, data: Partial<User>) {
  const user = await db.user.update({ where: { id: userId }, data });
  await redis.del(`user:${userId}`);  // invalidate
  return user;
}
```

### Write-through caching

Update the cache at the same time as the database:

```typescript
async function updateUser(userId: string, data: Partial<User>) {
  const user = await db.user.update({ where: { id: userId }, data });
  await redis.setex(`user:${userId}`, 300, JSON.stringify(user));  // update cache too
  return user;
}
```

The cache is always fresh, but every write is slightly slower.

### What to cache

**Good candidates:**
- User profiles (read often, change rarely)
- Configuration / feature flags
- Expensive aggregations (leaderboards, counts, analytics summaries)
- Results of slow external API calls
- Static or semi-static content (product listings, category pages)

**Bad candidates:**
- Data that must be real-time (account balances, inventory counts where overselling is catastrophic)
- Data that changes on every request
- User-specific data with very short TTLs (often not worth the complexity)

### Cache stampede (thundering herd)

When a cached value expires, many simultaneous requests all miss the cache, all hit the database at once, and the DB gets hammered. Solutions:

1. **Probabilistic early expiration:** re-compute the cache slightly before it expires, based on how long the computation takes
2. **Mutex / lock:** when a cache miss occurs, acquire a lock, compute the value, release the lock. Other requests wait rather than all hitting the DB
3. **Stale-while-revalidate:** return the stale cached value immediately, re-compute in the background

---

## Database connection pooling

Postgres has a limit on simultaneous connections (typically 100). In a serverless environment (Vercel), each function invocation can open a new connection, easily exhausting this limit.

### The problem

```
Vercel function instance 1    DB connection 1
Vercel function instance 2    DB connection 2
...
Vercel function instance 100  DB connection 100   limit reached
Vercel function instance 101  ERROR: too many connections
```

### The solution: a connection pooler

**PgBouncer** (self-hosted) or **Supabase/Neon's built-in pooler** sits between your app and Postgres. Your app opens connections to the pooler; the pooler maintains a smaller set of real DB connections.

```typescript
// Use the pooled connection string from Supabase/Neon for serverless
// (usually port 6543 instead of 5432)
DATABASE_URL="postgres://user:pass@host:6543/db?pgbouncer=true"

// Use the direct connection string for migrations only
// (PgBouncer doesn't support some migration commands)
DATABASE_DIRECT_URL="postgres://user:pass@host:5432/db"
```

In Prisma:
```prisma
datasource db {
  provider  = "postgresql"
  url       = env("DATABASE_URL")        // pooled
  directUrl = env("DATABASE_DIRECT_URL") // direct, for migrations
}
```

---

## Async / background jobs

Not everything needs to happen in the request/response cycle. Move slow or non-critical work to background jobs.

### What belongs in a background job

- Sending emails (no user should wait for your email server)
- Image processing / resizing
- PDF generation
- Webhooks to third-party services
- Expensive report generation
- Syncing data to ClickHouse or analytics systems
- Sending push notifications

### Pattern with BullMQ (Node.js, Redis-backed)

```typescript
// Define a queue
import { Queue, Worker } from 'bullmq';
import { redis } from './redis';

const emailQueue = new Queue('emails', { connection: redis });

// Add a job from your API route (fast, returns immediately)
await emailQueue.add('welcome-email', {
  userId: user.id,
  email: user.email,
});
// API responds instantly  user doesn't wait for the email to send

// Worker processes jobs in the background (separate process)
const worker = new Worker('emails', async (job) => {
  if (job.name === 'welcome-email') {
    await sendWelcomeEmail(job.data.email);
  }
}, { connection: redis });
```

### Alternatives to BullMQ

- **Inngest**  serverless job queue, great for Vercel (no Redis needed)
- **Trigger.dev**  similar to Inngest, good DX
- **pg-boss**  Postgres-backed queue (no Redis needed, simpler stack)
- **Vercel Cron**  for scheduled jobs on a cron schedule

---

## Load testing

Don't guess about performance. Measure it before you need it to scale.

### k6  the standard tool

```javascript
// load-test.js
import http from 'k6/http';
import { sleep, check } from 'k6';

export const options = {
  stages: [
    { duration: '30s', target: 10 },   // ramp up to 10 users over 30s
    { duration: '1m', target: 10 },    // hold 10 users for 1 minute
    { duration: '30s', target: 50 },   // ramp up to 50 users
    { duration: '1m', target: 50 },    // hold 50 users
    { duration: '30s', target: 0 },    // ramp down
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'],  // 95% of requests must complete under 500ms
    http_req_failed: ['rate<0.01'],    // less than 1% error rate
  },
};

export default function () {
  const res = http.get('https://yourapi.com/api/posts');
  check(res, { 'status 200': (r) => r.status === 200 });
  sleep(1);
}
```

Run with: `k6 run load-test.js`

### What to measure

- **p50 (median):** half of requests are faster than this
- **p95:** 95% of requests are faster than this  the number that matters most for user experience
- **p99:** the long tail  your slowest requests
- **Error rate:** any errors under load indicate a breaking point
- **Database connections:** watch these under load  connection exhaustion is a common failure mode

### Baseline before you optimize

Run a load test before making changes, make the change, run again. If you can't measure the improvement, you can't know it worked.

---

## Quick checklist for a slow API endpoint

Work through this in order  each step is faster and higher-impact than the next:

1. Check for N+1 queries  log all SQL in development and count the queries
2. Check for missing indexes  run `EXPLAIN ANALYZE` on the slow query
3. Check what columns you're selecting  are you fetching large unused fields?
4. Check if result can be cached  is this data the same for many users?
5. Check for unbounded queries  is there a missing `LIMIT`?
6. Check if any work can be moved to a background job
7. Check connection pool  are you running out of connections under load?