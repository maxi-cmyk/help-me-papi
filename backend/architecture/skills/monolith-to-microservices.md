---
name: monolith-to-microservices
description: Guidelines on when to split a monolith architecture into microservices.
---

# Monolith to Microservices

## Start with a Monolith
- Begin every project with a **Monolith** architecture. A single unified repository and deployable unit provides the highest development speed, least deployment overhead, and simplest debugging path.
- Keep the internal code modular (e.g., separating user logic from billing logic), but deploy it as one app.

## When to Split
Do not adopt microservices until you hit extreme organizational or scaling limits:
1. **Organizational Scale:** You have multiple distinct engineering teams stepping on each other's toes repeatedly, despite good CI and code ownership.
2. **Distinct Scaling Needs:** One specific feature (like a heavy ML video processing queue) requires entirely different server resources (e.g., massive GPUs) and scaling metrics than the rest of the web API.
