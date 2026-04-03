---
name: rest-conventions
description: Guidelines for REST API design and structuring route handlers.
---

# REST API Conventions

For basic Next.js and Python APIs:

## URLs and Methods
- Use plural nouns for resources: `/api/projects`, `/api/users`.
- Use correct HTTP methods:
    * `GET`: Retrieval
    * `POST`: Creation
    * `PATCH` or `PUT`: Updating
    * `DELETE`: Deletion

## Responses
Return JSON objects consistently.
- Success: `{ "data": { ... } }`
- Error: `{ "error": "Reason" }`
Never return a raw array at the top level.
