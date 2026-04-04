---
name: frontend
description: Frontend patterns for hackathons and prototypes. Prioritizes velocity, the "WOW demo", and zero-friction deployments.
---

# Hackathon Frontend Practices

Frontend patterns optimized for absolute speed, clarity, and demo-ability. Not enterprise architecture  just enough structure to win the pitch and prevent deployment disasters at 3:00 AM.

**Language Default**: JavaScript or TypeScript with `any`. Do not waste an hour fighting TypeScript utility types or generic inference constraints. 

**When to use this skill**: Weekend hackathons, temporary prototypes, MVPs built specifically to pitch to investors.
**When NOT to use this skill**: Any project that expects to be maintained for longer than 3 months. Use `startup-frontend` instead.

---

## Core Principles

1. **Velocity over Purity.** Code quality tradeoffs are acceptable as long as they don't block the visual pitch. Inline Tailwind heavily instead of trying to abstract every single layout wrapper.
2. **The "Hero Focus".** Spend 70% of your frontend effort on the first viewport the user sees (The Hero Section). This wins hackathons. Secondary pages can use absolute defaults.
3. **Monolithic Repo.** Keep the frontend and backend in a single Next.js project. You completely bypass CORS issues, split-deployment headaches, and sync issues.
4. **Use Pre-Built Primitives.** Copying Shadcn UI components is mandatory. Do not bespoke style a dropdown menu or modal from scratch.
5. **Fake Data Early.** Create beautiful UI states utilizing hardcoded JSON objects, then swap in the real API connection once it's completely ready. Don't let UI development block on a broken backend.

---

## Stack Decision Tree

```
Are we building for a hackathon?
 Yes  Next.js App Router + Tailwind + Shadcn UI (Hosted on Vercel)
 (There is no 'No'. This is the fastest stack to ship full-stack features).
```

---

## State Management Shortcut

- Do not set up complex Context providers or Redux sagas.
- Pass props manually down the tree if it's only 2 levels deep.
- If it's a global app state (like auth, or a shared map), throw it into a simple un-optimized `Zustand` store for instant access anywhere.

---

## Navigating the Frontend Domains

Even in a rush, some domains are non-negotiable for a winning demo. Manually attach these files to your prompt when focusing on specific polish:

### 1. [UI/UX and Clarity Standards](../ui-ux/standards.md)
**When to attach**: For all UI development. Ensures your MVP isn't cluttered and that the core user flow is ruthlessly simple for your pitch.

### 2. [Design System and Aesthetics](../design-inspos/decisions.md)
**When to attach**: When applying your chosen "flavor" (e.g., Glassmorphism). Ensures the AI generates CSS that is visually consistent and premium across all components.

### 3. [Architecture and Feature Design](../architecture/skills/component-patterns.md)
**When to attach**: Only when building your core "WOW" feature. Ensures the layout follows eye-tracking best practices for a high-impact demo.

---

## Deploy Early Checkout

1. Deploy the empty scaffolding to Vercel in Hour 1 to guarantee environment variables are configured.
2. Ensure the core "WOW" feature works perfectly on the live URL.
3. Have a fallback screen recording ready in case the venue Wi-Fi drops during the demo.
