# Tools Agentic Macro Library

> [!IMPORTANT]
> **HOW TO USE THIS LIBRARY**
> 1. **Context First**: Always provide the target API documentation or the directory structure of the files you intend to automate.
> 2. **Safety First**: All destructive CLI tools MUST include a `--dry-run` flag by default.
> 3. **Validation**: Use `TEST_CLI_TOOL` to verify functionality before deployment.

---

### **Stage 1: MCP Server Development**

#### **Macro: SCAFFOLD_MCP_SERVER**
```markdown
[ROLE] You are an MCP (Model Context Protocol) Specialist.
[CONTEXT] Analyze the Internal API / Data Source and the preferred stack (TS/Python).
[TASK] Build a production-ready MCP Server.

[TECHNICAL CONSTRAINTS]
- Use the official `@modelcontextprotocol/sdk`.
- Implement clear tool definitions with strict input validation.
- Standardize error responses to be LLM-readable.
- Connection: `stdio` (local development).

[OUTPUT]
1. SERVER CODE: The complete logic for the MCP server.
2. CONFIG JSON: The block to add to Claude/Cursor settings.
3. USAGE GUIDE: How to invoke the tools from an LLM.
```

---

### **Stage 2: Automation & CLI**

#### **Macro: GENERATE_AUTOMATION_CLI**
```markdown
[ROLE] You are a DevTools Engineer.
[CONTEXT] Paste the repetitive task description and the environment constraints.
[TASK] Build a robust, modular CLI tool.

[REQUIREMENTS]
1. FLAGS: Graceful parsing with `--help` and `--version`.
2. DRY-RUN: A mandatory `--dry-run` flag for all filesystem/API mutations.
3. LOGGING: Success/Error messages printed to stdout with appropriate exit codes.
4. MODULARITY: Extract core logic into a library that can be unit tested.

[OUTPUT]
Return the complete CLI script and a sample command to run it.
```

---

### **Stage 3: Testing & Debugging**

#### **Macro: TEST_CLI_TOOL**
```markdown
[ROLE] You are a QA Automation Engineer.
[CONTEXT] Paste the CLI script and a set of test cases.
[TASK] Verify the tool's reliability.

[CHECKLIST]
- EDGE CASES: What happens with empty inputs or missing files?
- PERMISSION: Handle read/write permission errors gracefully.
- IDEMPOTENCY: Does running the tool twice cause issues?

[OUTPUT] A suite of test commands and a report on any unhandled exceptions.
```
