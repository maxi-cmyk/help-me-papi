---
name: tools-mastery
description: Mastery skill for designing internal CLIs, automating workflows via Python/NodeJS, and architecting Model Context Protocol (MCP) servers.
---

# Automation and Tooling Mastery

This mastery skill governs the creation and maintenance of developer productivity tools, automation scripts, and custom Model Context Protocol (MCP) servers.

## Core Principles

1. **UX-First CLI Design**: Every tool must be intuitive, consistently flagged, and provide clear error feedback to the user.
2. **Minimal Dependency Footprint**: Prefer standard libraries (e.g., Python `argparse` or NodeJS `node:fs`) to keep tools lightweight and easy to distribute.
3. **Contextual Awareness (MCP)**: Custom servers should be designed to expose clear, well-documented tools and resources for AI consumption.

---

## Navigating the Tooling Domains

For specialized automation tasks, manually attach the following context files to your prompt to ensure a high standard of engineering:

### 1. [CLI Design and User Experience](./cli-design.md)
**When to attach**: When designing new command-line interfaces, adding flags, or structuring interactive help menus.

### 2. [MCP Server Architecture](./mcp-servers.md)
**When to attach**: When building custom Model Context Protocol servers to extend AI capabilities with local tools or resources.

### 3. [Data Analysis and Statistics](../data-analysis/skills.md)
**When to attach**: For Python-based automation involving large datasets, statistical analysis, or Conway's Game of Life simulation evaluation.

---

## Execution Workflow

1. Define the automation goal (e.g., "Build a git-log summarizer").
2. Attach the relevant master skill and sub-domain context listed above.
3. Use the localized `PROMPTS.md` in the tools root for scaffold generation.
