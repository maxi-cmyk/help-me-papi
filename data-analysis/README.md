# Data Analysis Documentation

This directory contains the playbooks, standards, and references for performing rigorous data analysis on hardware experiment results and simulation datasets.

## Development Paths

Manual attachment is required for high-standard execution. Refer to the master skill for guidance.

### Analysis Standards
**Goal: Statistical Integrity**
Strict data quality checks, non-parametric default methods, and explicit hypothesis verdicts. Adhere to the checklists in `standards.md`.

### Analytical Decisions
**Goal: Design Rationale**
Understand the philosophical choices behind modeling, cross-validation, and library selection in `decisions.md`.

### Analysis Scaffolds
**Goal: Rapid Scaffolding**
Use the token-efficient AI prompts in `prompts/scaffolds.md` for cleaning, testing, and modeling.

---

## How to use this folder effectively

To get the most out of this structure when collaborating with an AI, follow this workflow:

1. **Attach Mastery Skill**: Always start by attaching `skills/data-analysis-mastery.md` to establish high-level analytical boundaries.
2. **Attach Domain Context**: When performing specific tasks (e.g., cleaning, testing), attach `standards.md` or `decisions.md`.
3. **Use Scaffolds**: Use the specific prompts in `prompts/scaffolds.md` for generating accurate, context-aware code.

---

## Architecture & Directory Structure

Every domain follows a strict modular structure:

- **[`skills/`](./skills/)**: Data Analysis Mastery hub for human-centric navigation.
- **[`prompts/`](./prompts/)**: [Scaffolds](./prompts/scaffolds.md) for automated analysis.
- **[`resources/`](./resources/)**: Reference datasets and statistical tables.
- **[`ideas/`](./ideas/)**: [Experiments](./ideas/experiments.md) and automation backlogs.
- **[`standards.md`](./standards.md)**: Hard rules for data quality and statistical tests.
- **[`decisions.md`](./decisions.md)**: Philosophical and technical architectural choices.
