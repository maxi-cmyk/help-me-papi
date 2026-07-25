# /impeccable  Design Vocabulary Skill

**What it is**: [`pbakaus/impeccable`](https://github.com/pbakaus/impeccable) ([impeccable.style](https://impeccable.style/)) is a third-party Claude Code (and Cursor/Codex/Gemini CLI/GitHub Copilot/Grok Build/OpenCode) skill built on top of Anthropic's original [`frontend-design`](https://github.com/anthropics/skills/tree/main/skills/frontend-design) skill. It gives the agent an explicit design vocabulary and actively steers it away from the handful of tells every model reaches for when it hasn't been told otherwise: Inter/DM Sans for everything, purple-to-blue gradients, cards nested in cards, gray text on colored backgrounds, the rounded-square icon tile above every heading.

It ships as **1 skill, 23 commands, live browser iteration, and 60 deterministic detector rules** for catching AI-generated design slop before it ships.

## Why we're documenting it here

This repo's `standards.md` and `PROMPTS.md` already mandate a Clarity-First, whitespace-first, semantic-HTML aesthetic (see [`README.md`](../README.md)). `/impeccable` operationalizes that same philosophy as a runnable skill inside Claude Code, so it's a natural companion to the `SCAFFOLD_UI_COMPONENT` and `AUDIT_UI_CLARITY` macros in [`PROMPTS.md`](../PROMPTS.md).

## Installing it into this repo/project

Pick one of the options below (all verified against the upstream README as of the skill's v4 release).

### Option A  CLI installer (recommended for a single project)
```bash
npx impeccable install
```
Detects your harness folders (`~/.claude`, `.cursor`, etc.), lets you pick providers, and asks project vs. global scope. Non-interactive form:
```bash
npx impeccable install --providers=claude --scope=project
```
Update later with `npx impeccable update`.

### Option B  Git submodule (recommended for teams who want it vendored/pinned)
```bash
git submodule add https://github.com/pbakaus/impeccable .impeccable
npx impeccable link --source=.impeccable --providers=claude,cursor
git add .gitmodules .impeccable .claude .cursor
git commit -m "Add Impeccable skills"
```
Swap `--providers` for whichever harnesses this project actually uses (`claude`, `cursor`, `gemini`, `codex`, `github`, `grok`, `opencode`, `pi`, `qoder`, `trae`, `trae-cn`, `rovo-dev`, `vibe`). To update:
```bash
git submodule update --remote .impeccable
npx impeccable link --source=.impeccable --providers=claude,cursor
```

### Option C  Claude Code plugin marketplace
```bash
/plugin marketplace add pbakaus/impeccable
```
Then open `/plugin` inside Claude Code and install "Impeccable" from the list.

### Option D  `npx skills add` (general-purpose skills installer)
```bash
npx skills add pbakaus/impeccable
```
Installs one shared build for every harness rather than the one compiled for your specific tool  functionally complete but not tailored. Update with `npx skills update`.

Whichever option you use, requires **Node 22.12+**.

## First run

Once installed, inside Claude Code:
```
/impeccable init
```
`init` asks whether the surface is **brand** (marketing, landing, portfolio) or **product** (app UI, dashboard, tool), then writes `PRODUCT.md` (and optionally `DESIGN.md`) so every later command has design context: audience, brand/product lane, voice, anti-references, colors, type, and components.

## Usage

All commands are invoked as:
```
/impeccable <command> <target>
```

The most relevant commands for this repo's workflow:

| Command | What it does |
|---|---|
| `/impeccable init` | One-time setup: gather design context, write `PRODUCT.md`/`DESIGN.md` |
| `/impeccable audit <target>` | Technical quality checks (a11y, performance, responsive)  pairs with our `AUDIT_ACCESSIBILITY` macro |
| `/impeccable critique <target>` | UX design review: hierarchy, clarity, emotional resonance  pairs with `REVIEW_UX_HEURISTICS` |
| `/impeccable polish <target>` | Final pass, design-system alignment, shipping readiness |
| `/impeccable craft <target>` | Full shape-then-build flow with visual iteration |
| `/impeccable shape <target>` | Plan UX/UI before writing code (spec-first) |
| `/impeccable document` | Generate a root `DESIGN.md` from existing project code |
| `/impeccable extract` | Pull reusable components/tokens into the design system |
| `/impeccable harden <target>` | Error handling, i18n, text overflow, edge cases |
| `/impeccable typeset` / `colorize` / `layout` | Targeted fixes for type, color, and spacing |
| `/impeccable live` | Visual variant mode: iterate on elements directly in the browser |

Full list of all 23 commands: [github.com/pbakaus/impeccable#23-commands](https://github.com/pbakaus/impeccable#23-commands).

Usage examples straight from the upstream repo:
```bash
/impeccable audit blog           # Audit blog hub + post pages
/impeccable critique landing     # UX design review
/impeccable polish settings      # Final pass before shipping
/impeccable harden checkout      # Add error handling + edge cases
```
Or freeform:
```
/impeccable redo this hero section
```
Pin a frequently used command as its own shortcut with `/impeccable pin <command>` (e.g. `pin audit` creates `/audit`).

## Anti-patterns it enforces

Straight from the skill's own guidance  it will actively push back on:
- Overused fonts (Arial, Inter, system defaults)
- Gray text on colored backgrounds
- Pure black/gray (always tint)
- Wrapping everything in cards, or nesting cards inside cards
- Bounce/elastic easing (reads as dated)

These overlap directly with this repo's `standards.md` Clarity-First rules, which is why `AUDIT_UI_CLARITY` in `PROMPTS.md` calls `/impeccable audit`/`critique` as its verification step.

## CI / non-agent usage

The detector also runs headless for CI gates:
```bash
npx impeccable detect src/
```
59+ deterministic rules, JSON output, exit codes suitable for failing a PR check.

## Reference

- Repo: https://github.com/pbakaus/impeccable
- Site / full docs: https://impeccable.style/
- Command reference: https://impeccable.style/docs
