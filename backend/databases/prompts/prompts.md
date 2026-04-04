# Database Prompts

*Note: These are scaffold prompts. Always provide the AI with the suggested context files to ensure accurate results and save token usage.*

## Design a schema from scratch
```text
Task: Design a PostgreSQL schema including tables, relations, and indices for this application.
Context to provide: 
- `backend/standards.md` (or relevant database standards if created)
- `backend/decisions.md`

Input:
[Describe your application in 2-3 sentences and list main entities]
```

## Debug a slow query
```text
Task: Analyze slow production query, explain the bottleneck, and provide a fix.
Context to provide: 
- `backend/performance/standards.md`
- `backend/performance/skills/performance-fundamentals.md`

Input:
[Paste SQL query, table sizes, current indices, and EXPLAIN ANALYZE output]
```

## Design ClickHouse schema
```text
Task: Design ClickHouse schema with optimized ORDER BY keys and implementation code.
Context to provide: 
- `backend/standards.md`

Input:
[Describe application, tracking events, and required analytical questions]
```

## Choose between databases
```text
Task: Recommend the most suitable database for this use case based on patterns and scale.
Context to provide: 
- `backend/decisions.md`

Input:
[Describe data, access patterns, current scale, and existing database stack]
```

## Write a migration
```text
Task: Write a database migration file and flag potential downtime or data loss risks.
Context to provide: 
- `backend/standards.md`

Input:
[Describe change, current schema, and your ORM]
```