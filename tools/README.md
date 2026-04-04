# Tools Documentation

This directory is an organized space for automating Developer Experience (DevEx) via scripts, Command Line Interfaces (CLIs), and Model Context Protocol (MCP) servers. 

## How to use this folder effectively

To get the most out of this structure when collaborating with an AI (or onboarding new developers), follow this workflow:

1. **Attach the Mastery Skill**: When expanding capabilities, always load the appropriate skill from [`/skills`](./skills) into context. This gives the AI explicit constraints on how to architect new MCP endpoints or CLI flags, forcing it to utilize standardized interfaces.
2. **Combine with Prompts**: Directly load the templates hosted in [`PROMPTS.md`](./PROMPTS.md) as the initial request to explicitly guide the AI across the goal. Attach domain guides like `guidelines.md` or specific rules alongside the prompt.
3. **Modify per Project**: Adjust local references aggressively. When building a highly customized python analyzer versus a NodeJS testing rig, build localized instructions and tweak the overarching architecture rules locally.

## Architecture & Directory Structure

To maximize contextual understanding and developer efficiency, we segment the Repository Engine Room as follows:

- **[`mcp-servers/`](./mcp-servers/)**: [Skills](./mcp-servers/skills/), [Resources](./mcp-servers/resources/).
- **[`cli-tooling/`](./cli-tooling/)**: [Skills](./cli-tooling/skills/), [Resources](./cli-tooling/resources/).
- **[`skills/`](./skills/)**: Foundational playbooks for repository automation and orchestration.
- **[`skills/`](./skills/)**: Foundational playbooks for internal CLI and MCP architecture.
- **[`ideas/`](./ideas/)**: Scrappy logs mapping repetitive system processes.
- **[`standards.md`](./standards.md)**: Global tools engineering rules (Python vs Node, CLI flags).
- **[`decisions.md`](./decisions.md)**: Automation stack justifications.
- **[`PROMPTS.md`](./PROMPTS.md)**: Instantly deployable prompt macros for tool scaffolding.
