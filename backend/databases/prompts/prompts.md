# Database Prompts

## Design a schema from scratch
```
I'm building [describe your app in 2-3 sentences].

The main entities are: [list them, e.g. Users, Posts, Comments, Likes].

Help me design a PostgreSQL schema for this. Include:
- Table names and columns with types
- Primary keys and foreign keys
- Indexes for likely query patterns
- Any junction tables needed for many-to-many relationships

I'm using [Prisma / Drizzle / raw SQL].
```

## Debug a slow query
```
This query is running slowly in production:

[paste the SQL query]

Table sizes: [e.g. users: 2M rows, orders: 50M rows]
Current indexes: [paste output of \d tablename or the schema]
EXPLAIN ANALYZE output: [paste if available]

What's causing the slowdown and how do I fix it?
```

## Design an analytics event schema for ClickHouse
```
I want to track user events in ClickHouse for analytics.

My app does: [describe briefly]
Events I want to track: [e.g. page_view, button_click, purchase, sign_up]
Questions I'll need to answer: [e.g. DAU, conversion funnel, revenue by country]

Design a ClickHouse table schema for this, including:
- Column types
- The ORDER BY key (important for ClickHouse performance)
- How to send events from my Node.js API
```

## Choose between databases
```
I need to store [describe the data] for [describe the use case].

My access patterns are:
- [e.g. look up by user ID]
- [e.g. aggregate by date]
- [e.g. full-text search by name]

My scale is roughly [number of rows / requests per day].
I'm already using [list your current databases].

Which database should I use for this and why?
```

## Write a migration
```
I need to add [describe the change] to my database.

Current schema: [paste relevant table definitions]
ORM: [Prisma / Drizzle / raw SQL]

Write the migration file. Flag anything that could cause downtime or data loss.
```