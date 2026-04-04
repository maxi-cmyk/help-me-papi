---
name: startup-frontend
description: Frontend patterns for scalable, production-ready React/Next.js applications. Emphasizes feature-sliced design, tight component boundaries, and optimized Web Vitals.
---

# Startup / WebDev Frontend Practices

Frontend patterns optimized for maintainability, clean collaboration across developer teams, and long-term scaling. 

**Language Default**: TypeScript. In production apps, the cost of debugging runtime `undefined` errors drastically outweighs the time spent setting up `interface` shapes. Use Zod for runtime boundary validation.

**When to use this skill**: Web development for startups, enterprise software, applications expected to live for years, or any project facing real users.
**When NOT to use this skill**: Weekend hackathons, temporary disposable prototypes. Use `hackathon-frontend` instead.

---

## Core Principles

1. **Feature-Sliced Architecture.** Do not dump 100 components into `/components`. Co-locate domain logic inside `features/`.
2. **Generic UI Isolation.** Keep generic UI components (`Button`, `Modal`) entirely ignorant of your business logic. They should receive primitive props (`isOpen`) rather than full data objects.
3. **Strict Web Vitals.** Adhere rigorously to the 60fps rule and layout shift prevention. If a component causes jank, it is fundamentally broken.
4. **State Locality.** Global state is a last resort. If data only matters to a specific feature, keep it in that feature's specific hook or local component state. Server state belongs in data-fetching hooks (React Query/SWR/TRPC), not manual global state syncs.
5. **Accessibility is Non-Negotiable.** WCAG AA contrast rules and full keyboard navigation for trapped-focus elements must be tested before merging.

---

## Stack Decision Tree

```
Are we building an SEO-sensitive application or a full-stack monolithic app?
 Yes  Next.js App Router + Tailwind + Shadcn UI
 No (It's a pure single page application behind a login wall)
     Does it require crazy client-side performance?  Vite + React + Tailwind
     Something else  Evaluate based on team familiarity (Remix, Astro)
```

---

## Navigating the Frontend Domains

For specialized tasks, manually attach the following context files to your prompt to ensure the highest quality output:

### 1. [Architecture and Feature Design](../architecture/skills/component-patterns.md)
**When to attach**: When structuring new features, deciding on data-flow between components, or implementing the Feature-Sliced Design (FSD) directory structure.

### 2. [UI/UX and Clarity Standards](../ui-ux/standards.md)
**When to attach**: For all UI development. Ensures the interface adheres to the "Clarity-First" reduction framework, handles empty/error states, and maintains accessibility (WCAG AA).

### 3. [Performance and Rendering](../performance/skills/rendering-and-loading.md)
**When to attach**: Before optimizing Core Web Vitals, adding complex animations, or loading external assets. Prevents layout shifts (CLS) and ensures GPU-accelerated transitions.

### 4. [Design System and Aesthetics](../design-inspos/decisions.md)
**When to attach**: When styling new components to ensure they match the project's visual source of truth (e.g., Apple-like Glassmorphism or specific brand themes).

### 5. [Libraries and Tooling](../tooling/resources/libraries.md)
**When to attach**: When adding new dependencies or choosing between unstyled primitives (Radix, React Aria). Ensures we stick to the project's approved tech stack.

---

## Execution Workflow

1. Discuss state boundaries with the user before generating large blocks of code.
2. Build generic UI components into `components/ui/` purely using styling tokens.
3. Build the actual business view inside `features/[domain]/components/`.
4. Ensure the visual aesthetic maps correctly to the constraints in `design-inspos/`.
