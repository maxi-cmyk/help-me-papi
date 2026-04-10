# Graphify for Claude Code 

Claude Code is Graphify's native and default platform. While you can use the standard setup, there is a specialized command that forces Claude to prioritize your knowledge graph before it blindly searches through your raw files. You will have to run this for every project.

1. Navigate to your target project folder in your terminal.
2. Run the Claude-specific integration command:

```bash
graphify claude install
```

3. Open Claude Code and type `/graphify` to build the graph.

**What this does**: It automatically creates `CLAUDE.md` rules and sets up a `PreToolUse` hook in your `settings.json`. If a knowledge graph exists, Claude intercepts its own Glob and Grep tool calls and reads your `graphify-out/GRAPH_REPORT.md` instead. This ensures it navigates your project structurally rather than relying on keyword matches, which saves a massive amount of API tokens.