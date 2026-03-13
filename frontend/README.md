# Frontend

This directory contains frontend-specific skills, resources, ideas, prompts, standards, and decisions. 

## Philosophy: Clarity-First Design
Our frontend approach heavily prioritizes an **elegant, Apple-like, Clarity-First aesthetic**. The core foundation is built upon vanilla HTML, CSS, and JavaScript. 

- **HTML** must strictly be semantic.
- **CSS** should focus on minimalism, purposeful whitespace, and refined typography.
- **JavaScript** should be added purposefully to enhance interaction through micro-animations, rather than bloating the application.

> "Good design is as little design as possible." — Dieter Rams

## Architecture & Documentation Structure

The frontend documentation is structured into core pillars to prevent context fragmentation:

- **[`SKILLS.md`](./SKILLS.md)**: The foundational constraint framework. Read this or provide it as a system prompt to an AI before proposing any UI changes.
- **[`design-system.md`](./design-system.md)**: The single source of truth for component APIs, styling tokens (colors, glassmorphism, typography), and strict multimodal accessibility rules.
- **[`architecture-and-perf.md`](./architecture-and-perf.md)**: The engineering rules. Covers our "Vanilla-First" principle, CSS scoping decisions, and strict 60fps rendering constraints.
- **[`inspiration-and-tools.md`](./inspiration-and-tools.md)**: The external directory. Lists the UI kits we use (e.g., Radix) and the products/aesthetics we study.
- **[`PROMPTS.md`](./AI-PROMPTS.md)**: Copy-paste prompt templates for consistent component generation and rigorous UX reviews.
- **`/ideas`**: Scrappy thoughts, feature notes, and UI experiments (e.g., fluid typography, dynamic islands).
