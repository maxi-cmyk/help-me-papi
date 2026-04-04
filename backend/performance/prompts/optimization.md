# Performance Prompts

*Note: These are scaffold prompts. Always provide the AI with the suggested context files to ensure accurate results and save token usage.*

## Debug a slow endpoint
```text
Task: Identify the likely bottleneck and give specific fixes for this slow API endpoint.
Context to provide: 
- `backend/performance/standards.md`
- `backend/performance/skills/performance-fundamentals.md`
- `backend/performance/decisions.md`

Input:
[Paste your route handler code and EXPLAIN ANALYZE output here]
```

## Find and fix N+1 queries
```text
Task: Identify all N+1 query patterns and rewrite using proper eager loading or batching.
Context to provide: 
- `backend/performance/standards.md`
- `backend/performance/skills/performance-fundamentals.md`

Input:
[Paste your route handler code here]
```

## Design a caching layer
```text
Task: Design a caching strategy including keys, invalidation, and implementation code.
Context to provide: 
- `backend/performance/standards.md`
- `backend/performance/skills/caching-strategies.md`
- `backend/performance/decisions.md`

Input:
[Describe data to cache, change frequency, and access patterns]
```

## Write a k6 load test
```text
Task: Write a k6 load test script with ramp-up, thresholds, and proportioned traffic.
Context to provide: 
- `backend/performance/standards.md`

Input:
[List endpoints, traffic patterns, and success criteria]
```

## Optimize PostgreSQL queries
```text
Task: Analyze query plan, suggest indexes, and query rewrites for optimal performance.
Context to provide: 
- `backend/performance/standards.md`
- `backend/performance/skills/performance-fundamentals.md`

Input:
[Paste SQL query and EXPLAIN ANALYZE output]
```

## Set up background jobs
```text
Task: Implement background jobs to offload long-running operations.
Context to provide: 
- `backend/performance/standards.md`
- `backend/performance/decisions.md`

Input:
[Describe operations to offload and your deployment setup]
```