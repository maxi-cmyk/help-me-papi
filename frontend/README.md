# Frontend Documentation

This directory contains our highly modular, domain-driven frontend documentation. It is designed to be highly AI-friendly and perfectly organized so you instantly know where to find rules, aesthetic inspirations, or architectural decisions.

## Philosophy: Clarity-First Design
Our frontend approach heavily prioritizes an **elegant, Apple-like, Clarity-First aesthetic**. The core foundation is built upon vanilla HTML, CSS, and JavaScript. 

- **HTML** must strictly be semantic.
- **CSS** should focus on minimalism, purposeful whitespace, and refined typography.
- **JavaScript** should be added purposefully to enhance interaction through micro-animations, rather than bloating the application.

> "Good design is as little design as possible." — Dieter Rams

---

## How to use this folder effectively

To get the most out of this structure when collaborating with an AI (or onboarding new developers), follow this workflow:

1. **Attach the Mastery Skill**: When starting a new feature or project, always attach the relevant overarching skill file from [`/skills`](./skills) (e.g., `startup-frontend.md` for production or `hackathon-frontend.md` for fast prototyping). This gives the AI the broad boundary definitions and architectural rules you want.
2. **Combine with Prompts**: Use the templates in [`PROMPTS.md`](./PROMPTS.md) as your initial query. When doing so, attach the most specific domain skill files alongside the prompt. For example, if designing a new page, attach `PROMPTS.md` + `startup-frontend.md` + `ui-ux/skills/clarity-first.md`.
3. **Modify per Project**: Use these files as a general baseline outline. If you are starting a different project (e.g., a cyberpunk-themed interface rather than a minimal Apple-like interface), modify the localized definitions (like the resources and `design-inspos/decisions.md` file) directly inside the project folder so the rules fit the app precisely.

---

## Architecture & Directory Structure

To prevent context fragmentation when using AI, all concepts have been rigorously separated into their own domains:

- **[`architecture/`](./architecture/)**: Rules concerning routing logic, generic vs. domain-driven components (Feature-Sliced Design), and clean backend integration.
- **[`design-inspos/`](./design-inspos/)**: The aesthetic source of truth. Contains styling tokens for glassmorphism and typography, as well as visual execution plans for alternative themes (Arcade, Y2K Aero, Brutalism).
- **[`performance/`](./performance/)**: Strict engineering standards built to eliminate jank. Enforces the 60fps rule and layout shift (CLS) prevention.
- **[`ui-ux/`](./ui-ux/)**: The UX heuristics command center. Controls the "Clarity-First" logic on how to structure an interface's focal point, spatial hierarchies, and hard rules on multimodal accessibility (WCAG AA). 
- **[`tooling/`](./tooling/)**: Explains exactly what functional libraries (Radix, React Aria, Tailwind) we rely on—and strictly why we avoid pre-built heavy UI kits.
- **[`ideas/`](./ideas/)**: Scrappy thoughts, feature notes, and UI experiments (e.g., fluid typography, dynamic islands).
- **[`PROMPTS.md`](./PROMPTS.md)**: Copy-paste prompt templates for consistent component generation and rigorous UX reviews.
