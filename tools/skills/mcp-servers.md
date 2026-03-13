# MCP Server Sandbox

How to think about building your own MCP servers when off-the-shelf tools aren't enough.

## When to build one?
If you find yourself constantly copy-pasting data from an internal dashboard, a proprietary database, or a custom CMS into your AI prompts, you should build an MCP server. 

## The Core Concept
MCP servers expose three things:
1. **Resources:** Static text or files (e.g. "Here is the internal API schema").
2. **Tools:** Executable functions (e.g. "Create a new row in my dev database").
3. **Prompts:** Pre-defined context templates.

## Transport Layers
- **`stdio`:** The easiest way. Your AI config just paths to your local script (`node server.js`) and talks to it via standard input/output.
- **HTTP/SSE:** Used if the MCP server needs to live remotely.
