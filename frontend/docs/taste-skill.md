# Taste Skill — Anti-Slop Frontend Framework

**What it is**: [leonxlnx/taste-skill](https://github.com/leonxlnx/taste-skill) ([tasteskill.dev](https://tasteskill.dev/)) is a popular third-party Claude Code / Cursor / Codex skill that gives the agent a stronger design vocabulary and actively steers it away from generic, boilerplate-looking UIs. 76k+ stars, MIT licensed.

It ships as a set of portable `SKILL.md` files that the agent loads on demand.

## When to use it

- Greenfield UI where you want a distinct visual identity (not the default "AI slop" look).
- Re-styling an existing project that feels generic.
- You want the agent to produce varied layouts (not every page centered, same hero, same cards).

## Installing

```bash
# Install everything from the repo
npx skills add https://github.com/leonxlnx/taste-skill

# Install a specific skill by name
npx skills add https://github.com/leonxlnx/taste-skill --skill "design-taste-frontend"
```

Or paste any `SKILL.md` content into your prompt / Claude Code session.

## Skills available

| Skill | What it does |
|---|---|
| `design-taste-frontend` (v2) | Default. Reads brief, infers design language, tunes three dials (VARIANCE / MOTION / DENSITY). Brief inference, design-system map, anti-slop rules. |
| `design-taste-frontend-v1` | Original v1, preserved for projects depending on its exact behavior. |
| `gpt-taste` | Stricter variant for GPT/Codex: higher layout variance, stronger motion direction. |
| `image-to-code` | Image-first: generate site references, analyze, then implement. |
| `redesign-existing-projects` | Audit an existing UI, then fix layout / spacing / hierarchy / styling. |
| `high-end-visual-design` | Polished, calm, expensive UI: softer contrast, whitespace, premium fonts, spring motion. |
| `minimalist-ui` | Editorial product UI (Notion/Linear vibes), restrained palette, crisp structure. |
| `industrial-brutalist-ui` | Hard mechanical language: Swiss type, sharp contrast, experimental layout. |
| `full-output-enforcement` | When the model ships half-finished work: full output, no placeholders. |
| `stitch-design-taste` | Google Stitch-compatible rules, optional `DESIGN.md` export format. |

### Image generation skills (output images only, then hand to coding agent)

- `imagegen-frontend-web` — website comps (hero, landing, multi-section)
- `imagegen-frontend-mobile` — mobile screens and flows
- `brandkit` — logo directions, palettes, type, identity applications

## Settings (taste-skill only)

The skill exposes three 1–10 dials at the top of the file:

- **DESIGN_VARIANCE** — Layout experimentation (lower: centered/clean · higher: asymmetric/modern).
- **MOTION_INTENSITY** — Animation depth (lower: hover only · higher: scroll/magnetic).
- **VISUAL_DENSITY** — Information per viewport (lower: spacious · higher: dense dashboards).

Tune these before generating to steer the output without re-prompting.

## Pairing with other skills

- **Impeccable** (see `frontend/docs/impeccable-skill.md`) — the design *audit* complement. Taste Skill generates; Impeccable critiques and detects slop. Run both: generate with taste, audit with `/impeccable audit`.
- **Stitch MCP** — for Google Stitch integration (design-to-code workflow with Stitch MCP).
- **21st Dev MCP** — for shadcn/ui component sourcing.

## Why it's documented here

This repo's `frontend/standards.md` and `frontend/PROMPTS.md` already mandate a Clarity-First aesthetic. Taste Skill is the implementation partner that enforces it at generation time — it gives the agent explicit permission to vary layouts, tune motion, and avoid the default "centered hero + cards + Inter" pattern that every model falls into without guidance.

## Reference

- Repo: https://github.com/leonxlnx/taste-skill
- Site / docs: https://tasteskill.dev
- Changelog: https://www.tasteskill.dev/changelog
