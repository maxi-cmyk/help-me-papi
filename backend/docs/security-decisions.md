# Security Decisions

## Zod for input validation over manual checks
Manual validation (`if (!req.body.email || typeof req.body.email !== 'string')`) is tedious, inconsistent, and easy to forget. Zod defines a schema once and validates type, shape, length, format, and allowed values in a single call. It also infers TypeScript types from the schema, so validated data is immediately typed.

## argon2id over bcrypt
argon2id is the current OWASP recommendation. It is memory-hard (requires significant RAM to compute), making GPU-based brute force attacks much more expensive than against bcrypt. Use bcrypt only on runtimes where argon2 isn't available. Either way, never use MD5, SHA-1, or SHA-256 for passwords  they are not password hashing functions.

## Return 404 (not 403) when a user requests a resource they don't own
Returning 403 confirms the resource exists, enabling enumeration. An attacker can probe IDs and use 403 responses to discover valid resource IDs without owning them. Returning 404 gives no information  the resource might not exist, or the user might not be authorized. The exception is when you want to explicitly tell the user they're logged in but lack permission.

## Helmet for security headers over manual header setting
Helmet encapsulates best-practice header defaults and is maintained to reflect current browser support. Setting headers manually is error-prone and requires ongoing maintenance as browser security features evolve. Helmet's CSP configuration is still app-specific and must be set explicitly.

## Redis-backed rate limiting over in-memory
In-memory rate limiters don't work correctly when running multiple server instances  each instance has its own counter, so the actual limit is multiplied by the number of instances. Redis provides a shared counter across all instances. Upstash is the managed option for serverless environments.

## npm audit in CI over periodic manual review
Manual security reviews are infrequent and easy to skip. Running npm audit in CI with a failure threshold on high-severity vulnerabilities makes security review automatic and non-negotiable. The flag `--audit-level=high` fails the build only on high or critical issues, avoiding excessive noise from low-severity advisories.

## Structured logging (Pino) over console.log
console.log outputs unstructured text that is hard to search or alert on. Pino outputs JSON with consistent fields, which integrates with log aggregation tools (Logtail, Datadog, CloudWatch) and allows filtering by event type, user ID, or IP address  essential for security incident investigation.