---
name: error-handling
description: Best practices for API error handling and status codes.
---

# Error Handling

## Global Error Wrappers
Avoid scattering `try/catch` logic across every single endpoint. Use a Higher-Order Function (in JS) or a decorator (in Python) to wrap handler routes.

```javascript
export function withErrorHandler(handler) {
  return async (req) => {
    try {
      return await handler(req);
    } catch (error) {
      if (error.statusCode) {
        return NextResponse.json({ error: error.message }, { status: error.statusCode });
      }
      return NextResponse.json({ error: 'Internal Server Error' }, { status: 500 });
    }
  };
}
```

## Status Codes
- `200`: Success
- `201`: Created
- `400`: Bad Request (Validation failed)
- `401`: Unauthorized (Not logged in)
- `403`: Forbidden (Logged in, but no permissions)
- `404`: Not Found
- `500`: Server Error
