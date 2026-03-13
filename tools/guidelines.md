# Developer Tools Guidelines

Standards and recommendations for automating workflows using CLIs and MCPs.

---

## Part 1: Model Context Protocol (MCP)

**What is it?** A standard that lets AI assistants (like Claude or Cursor) securely connect to external tools. Instead of the AI being isolated, an MCP server gives it "hands and eyes" to query your databases, read API docs, or trigger deployments.

### How to Install MCPs
The general logic for installing an MCP server is pointing your AI assistant to an executable script (usually via `npx` or `uvx`) that runs the server locally over `stdio`.

**For Cursor:**
1. Navigate to **Cursor Settings** > **Features** > **MCP Servers**.
2. Click **+ Add new MCP server**.
3. Set the Type to `command` (or SSE if remote).
4. Enter the run command (e.g. `npx -y @modelcontextprotocol/server-sqlite --db /path/to/my/db.sqlite`).

**For Claude Desktop:**
1. Open your Claude Desktop settings and click **Developer** > **Edit Config**.
2. Add the server to the `mcpServers` JSON object:
```json
{
  "mcpServers": {
    "sqlite": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sqlite", "--db", "/path/to/my/db.sqlite"]
    }
  }
}
```
*(Note: Restart your AI assistant completely after modifying the config!)*

### Recommended Off-the-Shelf MCPs
Check the official [Anthropic MCP Servers Registry](https://github.com/modelcontextprotocol/servers) for standard tools.

- **Frontend: [21st.dev MCP](https://github.com/21st-dev/21st-mcp)**
  - *Why:* Gives the AI direct access to high-end, modern React/Tailwind/Framer UI components.
- **Backend & Database: [Supabase MCP](https://github.com/supabase/community-mcp) & [SQLite](https://github.com/modelcontextprotocol/servers/tree/main/src/sqlite)**
  - *Why:* Supabase MCP lets the AI query your Postgres schema and generate RLS policies. An SQLite MCP allows the AI to natively read your local Python/FastAPI hackathon databases without you copy-pasting tables.
- **Deployment & Infra: [Vercel](https://github.com/vercel/mcp-server)**
  - *Why:* Allows the AI to check deployment statuses, read Vercel Edge Runtime logs, and debug those pesky silent middleware failures directly from your editor.
- **AI & RAG: Pinecone / pgvector**
  - *Why:* Connects the AI directly to your vector store so it can independently test chunking strategies and debug retrieval relevancy.
- **General: [GitHub](https://github.com/modelcontextprotocol/servers/tree/main/src/github) & [Brave Search](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search)**
  - *Why:* Reads repo context, open PRs, and searches the live web for the absolute latest API docs before writing code.

---

## Part 2: Command Line Interfaces (CLIs)

**What are they?** Small, focused terminal tools built to automate repetitive repo tasks (like `organiser.py`).

### CLI Standards
- **Python:** Use `argparse` for simple scripts. Use `Typer` or `Click` for complex, multi-command CLIs.
- **Node.js:** Use `Commander.js` if you need to build a CLI that relies heavily on NPM packages.
- **Rules of thumb:**
  - Always support `--help`.
  - Prefer `--dry-run` modes for scripts that destructively edit files.
  - Fail fast and print obvious, color-coded error messages.
