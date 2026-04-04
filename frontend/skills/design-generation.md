---
name: design-generation
description: >
  Trigger this skill for any design-to-code or UI generation tasks.
  Focuses on the Stitch MCP + Claude Code + 21st.dev workflow.
  Enforces design token consistency and component-based rapid prototyping.
---

# Design-to-Code Mastery

Handle UI development by leveraging the **Stitch MCP** design context and **21st.dev** component registry.

## AI Execution Rules

1. **Context Discovery**:
   - Before generating code, check for existing **Stitch designs** via the Stitch MCP.
   - Extract design tokens (colors, variants, spacing) from the Stitch canvas.

2. **Component selection**:
   - **Mandatory**: Prefer **21st.dev** components (shadcn/ui registry) for all standard UI patterns (Stats, Charts, Nav, Hero).
   - Use `npx shadcn@latest add "https://21st.dev/r/[component-name]"` for installation.

3. **Styling Standard**:
   - Use **Tailwind CSS** exclusively for layouts and custom styles.
   - Inject Stitch design tokens into the Tailwind config or as CSS variables.

4. **Iterative Design**:
   - If a design change is requested, update the **Stitch design first**, then regenerate the code to maintain the "Design as Source of Truth" link.

## Prompt Patterns

### Designing from Scratch
- "Use Stitch MCP to design a [Screen Name] with [Key Features] and [Primary Color]."

### Coding from Design
- "Generate React + Tailwind code for the active Stitch design. Use 21st.dev components for [Elements]."

---

## Technical Reference
- **Workflow Guide**: [frontend/tooling/stitch-workflow.md](../tooling/stitch-workflow.md)
- **Component Registry**: [21st.dev](https://21st.dev)
