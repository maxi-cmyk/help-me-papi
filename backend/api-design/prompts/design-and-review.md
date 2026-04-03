# API Design Prompts

## Design endpoints for a feature
```
I'm building [describe the feature, e.g. "a blog with posts, tags, and comments"].

The main entities are: [list them]

Design the REST API for this, including:
1. All endpoints (method + path + description)
2. Request body shape for POST/PATCH endpoints
3. Response shape for each endpoint
4. What status codes to return in success and error cases
5. Any pagination needed on list endpoints

I'm using [Express / Hono / Next.js API routes / Fastify].
```

## Design the error handling system
```
I'm starting a new Node.js API with [Express / Hono / Fastify].

Set up a consistent error handling system including:
1. A custom ApiError class I can throw anywhere
2. A list of error codes for common cases (validation, not found, unauthorized, etc.)
3. A global error handler middleware that formats all errors consistently
4. How to handle async errors in route handlers
5. How to ensure stack traces are never leaked in production

Use TypeScript.
```

## Review an existing API for problems
```
Here are my current API routes:

[paste your routes/controllers]

Review them for:
- Inconsistent naming or structure
- Wrong HTTP methods or status codes
- Missing validation
- Security issues (mass assignment, missing auth checks, etc.)
- Performance problems (N+1 queries, unbounded queries)
- Missing error handling

Suggest specific improvements.
```

## Set up tRPC in a Next.js project
```
I'm using Next.js [app router / pages router] with TypeScript.
Database: [Postgres with Prisma/Drizzle / other]
Auth: [Supabase / NextAuth / Clerk / other]

Set up tRPC end-to-end:
1. Install and configure tRPC
2. Create a router with a few example procedures (query + mutation)
3. Set up the client-side provider
4. Show how to call procedures from a React component
5. Show how to access the current user in a procedure
6. Show how to protect procedures with auth middleware
```

## Add rate limiting
```
I have a [Express / Next.js] API.
I need rate limiting on:
- All API routes: [X] requests per minute per IP
- Auth routes (/auth/login, /auth/register): stricter limits

I'm using [Redis via Upstash / in-memory / other] for storage.

Implement rate limiting middleware with proper 429 responses including Retry-After headers.
```