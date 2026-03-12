<!-- @maxi-cmyk -->
# API Design

Practical API patterns for hackathons and small apps. Not enterprise architecture — just enough structure to keep your routes clean, your errors helpful, and your frontend team (or future you) not confused.

## Pick Your Style

### Next.js App Router (Route Handlers)

Use when your frontend is already Next.js. No separate server needed.

```
app/api/
├── auth/
│   ├── login/route.js
│   └── signup/route.js
├── projects/
│   ├── route.js              # GET (list), POST (create)
│   └── [id]/
│       └── route.js          # GET (one), PATCH (update), DELETE
└── webhooks/
    └── stripe/route.js
```

Each `route.js` exports functions named by HTTP method:

```javascript
// app/api/projects/route.js
import { NextResponse } from 'next/server';

export async function GET(request) {
  const { searchParams } = request.nextUrl;
  const page = Number(searchParams.get('page') ?? 1);

  const projects = await getProjects({ page });
  return NextResponse.json(projects);
}

export async function POST(request) {
  const body = await request.json();

  // validate first, always
  if (!body.name || body.name.length === 0) {
    return NextResponse.json(
      { error: 'Name is required' },
      { status: 400 }
    );
  }

  const project = await createProject(body);
  return NextResponse.json(project, { status: 201 });
}
```

If you're using TypeScript for a particular project, add Zod for schema validation:

```typescript
// with Zod (TypeScript projects only)
const parsed = ProjectSchema.safeParse(body);
if (!parsed.success) {
  return NextResponse.json(
    { error: 'Invalid input', details: parsed.error.flatten() },
    { status: 400 }
  );
}
```

### Python Flask / FastAPI

Use when the hackathon needs Python (ML models, data processing, sponsor SDK is Python-only).

```python
# Flask — quick and dirty
@app.route('/api/projects', methods=['GET'])
def list_projects():
    projects = db.get_projects()
    return jsonify(projects)

@app.route('/api/projects', methods=['POST'])
def create_project():
    data = request.get_json()
    # validate
    project = db.create_project(data)
    return jsonify(project), 201
```

```python
# FastAPI — better for anything with types or docs
@app.get('/api/projects')
async def list_projects():
    return await db.get_projects()

@app.post('/api/projects', status_code=201)
async def create_project(data: ProjectCreate):
    return await db.create_project(data)
```

FastAPI gives you automatic OpenAPI docs at `/docs` — useful for demoing an API to judges.

## Rules That Save Time

### 1. Consistent response shape

Pick one shape and use it everywhere:

```json
// Success
{ "data": { ... } }

// Error
{ "error": "What went wrong", "details": { ... } }

// List
{ "data": [...], "count": 42 }
```

Never return a raw array at the top level. Never mix shapes between endpoints.

### 2. Validate at the edge

Check input the moment it arrives, before it touches any logic.

```javascript
// Simple JS validation — good enough for hackathons
function validateProject(body) {
  const errors = [];
  if (!body.name || typeof body.name !== 'string') errors.push('name is required');
  if (body.name && body.name.length > 100) errors.push('name too long');
  if (body.type && !['web', 'mobile', 'api'].includes(body.type)) errors.push('invalid type');
  return errors;
}

// In your handler
const errors = validateProject(body);
if (errors.length > 0) {
  return NextResponse.json({ error: 'Invalid input', details: errors }, { status: 400 });
}
```

This catches bad data early, gives clear error messages, and means your service layer can trust its inputs.

### 3. Use proper HTTP status codes

You only need these:

| Code | When |
|------|------|
| `200` | Success (GET, PATCH) |
| `201` | Created (POST) |
| `204` | Deleted (DELETE, no body) |
| `400` | Bad input (validation failed) |
| `401` | Not logged in |
| `403` | Logged in but not allowed |
| `404` | Thing doesn't exist |
| `500` | Something broke on our end |

### 4. One error handler

Don't scatter try/catch everywhere. Create a wrapper:

```javascript
// lib/api-handler.js
export function withErrorHandler(handler) {
  return async (req) => {
    try {
      return await handler(req);
    } catch (error) {
      if (error.statusCode) {
        return NextResponse.json(
          { error: error.message },
          { status: error.statusCode }
        );
      }
      console.error('Unhandled:', error);
      return NextResponse.json(
        { error: 'Internal server error' },
        { status: 500 }
      );
    }
  };
}

// Usage
export const GET = withErrorHandler(async (req) => {
  const data = await getStuff();
  return NextResponse.json({ data });
});
```

### 5. Don't over-engineer for a hackathon

Things you **don't need** for a demo:
- Pagination (unless your demo has lots of data)
- Rate limiting
- API versioning (`/v1/`, `/v2/`)
- GraphQL (REST is faster to build)
- Microservices (one repo, one deployment)

Things you **do need**:
- Input validation on every endpoint
- Consistent error responses
- Working auth on protected routes
- One clean happy path that demos well