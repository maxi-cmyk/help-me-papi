# Tools Documentation

This directory is an organized space for automating Developer Experience (DevEx) via scripts, Command Line Interfaces (CLIs), and Model Context Protocol (MCP) servers. 

## How to use this folder effectively

To get the most out of this structure when collaborating with an AI (or onboarding new developers), follow this workflow:

1. **Attach the Mastery Skill**: When expanding capabilities, always load the appropriate skill from [`/skills`](./skills) into context. This gives the AI explicit constraints on how to architect new MCP endpoints or CLI flags, forcing it to utilize standardized interfaces.
2. **Combine with Prompts**: Directly load the templates hosted in [`PROMPTS.md`](./PROMPTS.md) as the initial request to explicitly guide the AI across the goal. Attach domain guides like `guidelines.md` or specific rules alongside the prompt.
3. **Modify per Project**: Adjust local references aggressively. When building a highly customized python analyzer versus a NodeJS testing rig, build localized instructions and tweak the overarching architecture rules locally.

## Architecture & Directory Structure

To maximize contextual understanding and streamline automation generation, everything is segmented into domains:

- **[`skills/`](./skills/)**: Foundational playbooks defining exactly how internal CLI tooling and MCP server architecture should be shaped.
- **[`data-analysis/`](./data-analysis/)**: Dedicated playbooks for structuring statistical tests, ML boundary guards, and rapid analytical experiment evaluation.
- **[`ideas/`](./ideas/)**: Scrappy logs mapping repetitive system processes you encounter that should be ultimately automated across the system loop.
- **[`guidelines.md`](./guidelines.md)**: A monolithic consensus defining exactly what automation stack paradigms exist (e.g., leveraging specific NodeJS utilities against Python `argparse`).
- **[`PROMPTS.md`](./PROMPTS.md)**: Instantly deployable prompt macros mapped to scaffold tools instantaneously when fed into AI generation constraints.
