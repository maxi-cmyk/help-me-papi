---
name: caching-strategies
description: Guidelines on backend caching.
---

# Caching Strategies

## The Rule of Thumb
Do not implement caching until you have a proven performance bottleneck. Premature caching is the root of complex state-invalidation bugs.

## Levels of Caching
1. **Database-Level:** Rely on Postgres indexing and connection pooling before reaching for standard application caching.
2. **Server-Level Data Caching (Redis/Memcached):** Use for computationally expensive queries or calls to rate-limited external APIs. Ensure every cache entry has a clear TTL (Time To Live).
3. **CDN / Edge Caching:** Utilize Vercel Edge caching or Cloudflare to serve static assets and heavily accessed public API routes without hitting your origin server.
