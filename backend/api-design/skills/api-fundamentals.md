# API Design

## REST conventions

REST isn't a formal spec — it's a set of conventions. The goal is predictability: a developer who has never seen your API should be able to guess the endpoints.

### URL design rules

URLs represent **resources** (nouns), not actions (verbs). The HTTP method is the verb.

```
[YES]  GET    /users              → list users
[YES]  GET    /users/123          → get user 123
[YES]  POST   /users              → create a user
[YES]  PATCH  /users/123          → update user 123 (partial)
[YES]  PUT    /users/123          → replace user 123 (full)
[YES]  DELETE /users/123          → delete user 123

[NO]   GET    /getUsers
[NO]   POST   /createUser
[NO]   POST   /users/123/delete
```

Nested resources for relationships:
```
GET  /users/123/posts          → all posts by user 123
GET  /users/123/posts/456      → post 456 by user 123
POST /users/123/posts          → create a post for user 123
```

Don't nest more than 2 levels deep — it becomes unreadable.

### HTTP methods

| Method | Idempotent? | Use for |
|---|---|---|
| GET | Yes | Read data, never mutates |
| POST | No | Create a resource, trigger an action |
| PUT | Yes | Replace a resource entirely |
| PATCH | No | Partial update |
| DELETE | Yes | Delete a resource |

**Idempotent** means calling it multiple times has the same effect as calling it once. GET /users/123 always returns the same user. DELETE /users/123 deletes the user — calling it again returns 404, but the state (user is gone) is the same.

### HTTP status codes — use them correctly

```
200 OK              → successful GET, PATCH, PUT
201 Created         → successful POST that created a resource
204 No Content      → successful DELETE (no body to return)

400 Bad Request     → client sent invalid data (validation error)
401 Unauthorized    → not authenticated (no valid token/session)
403 Forbidden       → authenticated but not authorized (wrong role)
404 Not Found       → resource doesn't exist
409 Conflict        → conflict with current state (e.g. email already taken)
422 Unprocessable   → validation failed (some teams use this over 400)
429 Too Many Req.   → rate limit exceeded

500 Internal Error  → something broke on the server
```

The most important distinction: **401 vs 403**. 401 = "I don't know who you are". 403 = "I know who you are, but you can't do this."

---

## Consistent error responses

Define one error shape and use it everywhere. Nothing is worse than some endpoints returning `{ "error": "..." }`, others `{ "message": "..." }`, and others `{ "errors": [...] }`.

### Recommended shape

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input",
    "details": [
      { "field": "email", "message": "Invalid email format" },
      { "field": "password", "message": "Must be at least 8 characters" }
    ]
  }
}
```

For simple errors:
```json
{
  "error": {
    "code": "NOT_FOUND",
    "message": "User not found"
  }
}
```

**Why a `code` field?** The `message` is for humans and might change. The `code` is for the frontend to programmatically branch on (`if (error.code === 'EMAIL_TAKEN') showEmailError()`).

### Error handler middleware (Express/Node)

```typescript
// types
interface AppError extends Error {
  statusCode?: number;
  code?: string;
  details?: unknown;
}

// throw this from anywhere
class ApiError extends Error {
  constructor(
    public statusCode: number,
    public code: string,
    message: string,
    public details?: unknown
  ) {
    super(message);
  }
}

// global error handler — register last in Express
app.use((err: AppError, req, res, next) => {
  const statusCode = err.statusCode ?? 500;
  const code = err.code ?? 'INTERNAL_ERROR';
  const message = statusCode === 500 ? 'Something went wrong' : err.message;

  // Don't leak stack traces in production
  if (process.env.NODE_ENV !== 'production') {
    console.error(err);
  }

  res.status(statusCode).json({
    error: { code, message, details: err.details }
  });
});

// Usage anywhere in route handlers:
throw new ApiError(404, 'NOT_FOUND', 'User not found');
throw new ApiError(400, 'VALIDATION_ERROR', 'Invalid input', validationErrors);
```

---

## Input validation

Never trust client input. Validate everything at the boundary (the route handler), before it touches your DB.

### With Zod (TypeScript)

```typescript
import { z } from 'zod';

const CreateUserSchema = z.object({
  email: z.string().email(),
  password: z.string().min(8).max(100),
  name: z.string().min(1).max(100),
});

app.post('/users', async (req, res) => {
  const result = CreateUserSchema.safeParse(req.body);
  
  if (!result.success) {
    const details = result.error.errors.map(e => ({
      field: e.path.join('.'),
      message: e.message,
    }));
    throw new ApiError(400, 'VALIDATION_ERROR', 'Invalid input', details);
  }

  const { email, password, name } = result.data; // fully typed
  // ...create user
});
```

---

## API versioning

You'll eventually need to change your API in a breaking way. Versioning lets you do this without breaking existing clients.

### URL versioning (most common)

```
/v1/users
/v2/users
```

Simple, explicit, cacheable. Downside: URL proliferation over time.

### Header versioning

```
GET /users
API-Version: 2
```

Cleaner URLs but less visible. Harder to test in a browser.

### Recommendation for startups

**Don't version until you need to.** If you control all the clients (your own frontend), just make breaking changes and update both at once. Version when you have external API consumers you can't force to upgrade.

When you do version, **URL versioning** is the most practical.

---

## REST vs tRPC vs GraphQL

### tRPC — TypeScript-native, no schema needed

If your frontend and backend are both TypeScript (e.g. Next.js), tRPC is worth knowing. You define functions on the server and call them from the client with full type safety — no JSON schema, no code generation.

```typescript
// server
const appRouter = router({
  getUser: publicProcedure
    .input(z.object({ id: z.string() }))
    .query(async ({ input }) => {
      return db.user.findUnique({ where: { id: input.id } });
    }),
});

// client — fully typed, autocomplete works
const user = await trpc.getUser.query({ id: '123' });
//    ^ type is inferred from the server definition
```

**Use tRPC when:** full-stack TypeScript, you control both client and server, you want end-to-end type safety without the overhead of GraphQL.

**Don't use tRPC when:** you have mobile clients or third-party API consumers (they can't use tRPC's TypeScript client).

### GraphQL — client-driven queries

Client specifies exactly what data it needs. Good for complex data graphs with many relationships and varied client needs (e.g. web needs different fields than mobile).

**Use GraphQL when:** multiple different clients with different data needs, complex nested data with lots of optional fields.

**Don't use GraphQL when:** simple CRUD app, small team, you don't want to maintain a schema and resolver layer.

### The honest comparison

| | REST | tRPC | GraphQL |
|---|---|---|---|
| Learning curve | Low | Medium | High |
| Type safety | Manual | Automatic | With codegen |
| External consumers | Yes | No (TS only) | Yes |
| Flexibility for clients | Low | Low | High |
| Best for | Most APIs | Full-stack TS | Complex data graphs |

**For most startups:** REST or tRPC. GraphQL is powerful but adds significant complexity.

---

## Pagination

Never return unbounded lists. Always paginate.

### Cursor-based (recommended)

```
GET /posts?cursor=abc123&limit=20

Response:
{
  "data": [...],
  "nextCursor": "def456",   // null if no more results
  "hasMore": true
}
```

Uses a cursor (usually the last item's ID or created_at) to fetch the next page. Stable even if items are inserted or deleted between requests. Works well with infinite scroll.

### Offset-based (simpler but worse)

```
GET /posts?page=2&limit=20

Response:
{
  "data": [...],
  "total": 450,
  "page": 2,
  "totalPages": 23
}
```

Easier to implement and shows "page X of Y" UI, but breaks if items are inserted mid-pagination (the next page might skip or repeat items).

---

## Rate limiting

Add rate limiting to all public endpoints — especially auth endpoints.

```typescript
import rateLimit from 'express-rate-limit';

// General API rate limit
const apiLimiter = rateLimit({
  windowMs: 60 * 1000,   // 1 minute
  max: 100,              // 100 requests per minute per IP
  standardHeaders: true,
  message: { error: { code: 'RATE_LIMITED', message: 'Too many requests' } },
});

// Strict limit for auth endpoints
const authLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,  // 15 minutes
  max: 10,                    // 10 attempts per 15 min
});

app.use('/api', apiLimiter);
app.use('/api/auth', authLimiter);
```

---

## CORS

Configure CORS explicitly — never use `cors({ origin: '*' })` in production.

```typescript
import cors from 'cors';

app.use(cors({
  origin: process.env.ALLOWED_ORIGIN,   // 'https://yourapp.com'
  methods: ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'],
  allowedHeaders: ['Content-Type', 'Authorization'],
  credentials: true,   // required if using cookies
}));
```