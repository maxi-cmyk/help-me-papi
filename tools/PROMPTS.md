# MCP & CLI Prompts

Templates to rapidly scaffold internal automation tools.

---

## Part 1: MCP Server Generation

```text
I need to build an MCP (Model Context Protocol) Server for my internal APIs. 

**My Stack:** [e.g. TypeScript / Python]
**Data Source:** [e.g. My custom CMS, my local SQLite file, a 3rd party API]

Please write the complete MCP server code using the official `@modelcontextprotocol/sdk`. 
1. Define the capabilities (resources, tools, or prompts).
2. Wire up the generic request handlers.
3. Show me the exact JSON configuration to add to my Claude/Cursor settings to connect it locally over `stdio`.
```

---

## Part 2: CLI Generation

```text
I need a robust CLI tool to automate a repetitive task.

**Language:** [e.g. Python using argparse / Node using Commander]
**Goal:** [What the script needs to do, e.g. "Rename all .jsx files to .tsx and update imports"]

Requirements:
- Parse command-line flags gracefully (always include a `--help`).
- Include a `--dry-run` flag so I can preview destructive actions without committing them.
- Print clear, user-friendly success/error messages to standard output.
- Use clean, modular functions that I can easily extend later.
```
