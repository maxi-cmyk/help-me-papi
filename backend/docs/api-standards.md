# API Design Standards

## URLs
- Use kebab-case for multi-word paths: `/user-profiles` not `/userProfiles`
- Use plural nouns for collections: `/posts` not `/post`
- No verbs in URLs: `/users/123/deactivate` is acceptable for actions with no resource equivalent, but prefer `/users/123` PATCH with `{ active: false }`
- Max 2 levels of nesting: `/users/123/posts` yes, `/users/123/posts/456/comments/789/likes` no

## Response shape
All responses follow this envelope:

Success:
```json
{ "data": { ... } }
```
or for lists:
```json
{ "data": [...], "meta": { "nextCursor": "...", "hasMore": true } }
```

Error:
```json
{ "error": { "code": "SNAKE_CASE_STRING", "message": "Human readable", "details": [...] } }
```

Never return naked objects or arrays at the top level. The envelope makes it easy to add metadata without breaking clients.

## Status codes
- Use the correct status code  don't return 200 with `{ "success": false }` in the body
- 201 for created resources, include the created resource in the response
- 204 for deletes (no body)
- 400 for validation errors (include field-level details)
- 401 vs 403: know the difference

## Validation
- Validate all inputs at the route handler boundary using Zod or equivalent
- Never pass raw `req.body` to DB queries
- Strip unknown fields (`z.object({}).strict()` or `.strip()`)

## Pagination
- All list endpoints are paginated  no unbounded queries
- Default to cursor-based pagination
- Max page size: 100 items

## Rate limiting
- All public endpoints: 100 req/min per IP
- Auth endpoints: 10 req/15min per IP
- Return `Retry-After` header with 429 responses

## Versioning
- No versioning until you have external consumers you can't control
- When versioning: URL path (`/v1/`, `/v2/`) is preferred
- Maintain old versions for a defined deprecation period (minimum 3 months notice)

## Security
- CORS: explicit origin whitelist, never `*` in production
- All responses: `Content-Type: application/json`
- Sensitive data: never return passwords, full card numbers, or internal IDs where avoidable