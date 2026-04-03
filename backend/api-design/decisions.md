# API Design Decisions

## REST as the default over GraphQL or tRPC
REST has the widest compatibility (any client, any language), the lowest learning curve, and the most tooling. Start with REST. Move to tRPC if you're full-stack TypeScript and want end-to-end type safety. Only add GraphQL if you genuinely have multiple clients with wildly different data needs.

## tRPC for full-stack TypeScript projects
When frontend and backend are both TypeScript in the same repo, tRPC eliminates an entire category of bugs (mismatched API contracts) and removes the need for manual type definitions for API responses. The tradeoff is lock-in to TypeScript — you can't easily consume tRPC from a mobile app or third-party integration.

## Zod for runtime validation
TypeScript types are erased at runtime — they don't protect you from bad input. Zod validates at runtime and infers TypeScript types from the schema, so you get both. It's the standard in the TypeScript ecosystem.

## Envelope response format (`{ data: ... }` / `{ error: ... }`)
A bare object or array at the top level makes it impossible to add metadata (pagination cursors, request IDs, deprecation notices) without breaking existing clients. An envelope gives you room to evolve the response shape. The cost is one extra level of nesting — worth it.

## Cursor-based over offset pagination
Offset pagination breaks when items are inserted between page fetches (page 2 might repeat or skip items). Cursor-based pagination is stable. The downside is no "jump to page N" UI, but most modern UIs use infinite scroll anyway.

## No versioning until external consumers exist
Versioning adds maintenance overhead. If you own all the clients, just make the change and update everything at once. Introduce versioning when you have API consumers you can't force to upgrade on your schedule.