# Hackathon Strategy & Resources

This guide outlines the high-velocity "Agentic" strategy for winning hackathons, leveraging the structured repository patterns and AI macros defined in this workspace.

---

## Part 1: Pre-Hackathon Optimization

The hackathon starts **before** the clock begins. Use these steps to ensure you are standing on a solid foundation.

### **1. The Pre-Hackathon Checklist**
- [ ] **GitHub Readiness**: Create a private repo and invite all team members. Add a `.gitignore` for Node/Next.js/Python.
- [ ] **Deployment Pipe**: Connect your GitHub to **Vercel** or **Railroad**. Connect your first "Hello World" commit immediately.
- [ ] ### **T-Minus 2 Hours: The Environment Warmup**
- [ ] **Auth & DB**: Finalize one Supabase project. Ensure `.env.local` is shared with all team members.
- [ ] **GitHub & Deployment**: Main repo created. Vercel/similar "push-to-deploy" linked to `main`.
- [ ] **MCP Tooling Setup**:
    - [ ] **21st Dev**: `claude mcp add 21st-dev npx -y @21st-dev/mcp`
    - [ ] **Stitch**: `claude mcp add stitch npx -y @_davideast/stitch-mcp proxy`
    - [ ] **Auth**: Ensure **Claude Code** is authenticated and has permission to write to the project root.
- [ ] **Prompt Priming**: Open a new LLM thread. Paste the `hackathons/PROMPTS.md` Stage 1 macros to "initialize" the agent's strategy.
- [ ] **Inbox/Brain Setup**: Ensure the `hackathons/docs/` and `hackathons/features/` folders exist and are clean.

### **2. Pre-Hackathon Optimizations**
- **Boilerplate Warmup**: Have a clean `Next.js + Tailwind + Lucide + Framer Motion` boilerplate ready. Don't waste 30 mins on `npm init`.
- **Dependency Pre-loading**: Pre-install common "demo-winners" like `sonner` (toasts), `zod` (validation), and `clsx` (styling).
- **AI Context Priming**: Test that your AI (Claude/Cursor) can read your `skills/SKILLS.md` and this strategy file correctly.
- **Seed Logic**: Prepare a generic `seed.ts` script that pushes JSON to your DB so you can hydrate your UI with fake data in seconds.

---

## Part 2: The Agentic Playbook

Winning a hackathon is 30% Strategy, 20% Speed, and 50% "The Narrative." We automate the speed using the **[Agentic Macro Library](./PROMPTS.md)**.

### **Phase 1: Research & Positioning (T-Minus 0-2 Hours)**
*Use Macros: `STRATEGIC_ANALYSIS`, `PERSONA_BUILDER`*

1. **Strategic Intelligence**: Don't just pick a theme. Identify sponsor "Sweet Spots" and predict "Strategic Traps" (generic projects).
2. **Deep Research**: Centralize all findings in `docs/Research.md`. This file is the primary context source for all subsequent AI generations.
3. **The Persona**: Define the user's "Day in the Life" and a "Core Frustration" that needs to be solved.

### **Phase 2: Innovation & Scaffolding (T-Minus 2-4 Hours)**
*Use Macros: `IDEATE_PROJECT`, `GENERATE_STRATEGY_SUITE`*

1. **The "Wow" Feature**: Identify the specific 30-second interaction that will make judges gasp (The "AHA Moment").
2. **Docs-as-Code**: Generate the core strategy suite in the `docs/` folder:
    - `docs/PRD.md`: Full feature set and demo metrics.
    - `docs/techStack.md`: Rationalizing the stack (Next.js, Supabase, etc.).
    - `docs/design.md`: User flow and component logic.
3. **Environmental Setup**:
    - Build `.env.example` immediately.
    - Connect GitHub to Vercel/Supabase for auto-deployments.

### **Phase 3: The "Feature-First" Build (T-Minus 4-20 Hours)**
*Use Macro: `SCAFFOLD_FEATURE`*

1. **Strict Architecture**: All new logic belongs in the `features/` directory. No component bloat.
2. **Demo-Safe Engineering**:
    - Implement `Seed.ts` to ensure your local and production DBs always have rich demo data.
    - Use "Toasts, not Crashes" for error handling.
3. **The 50% Mark**: The core "Wow" feature must be end-to-end by the halfway point. Fake/Hardcode non-essential data (Auth/Settings).

### **Phase 4: The Narrative & Final Push (The Final 4 Hours)**
*Use Macro: `PITCH_GENESIS`*

1. **Pitch-First Strategy**: While the build finishes, start the assets in `docs/pitch/`:
    - `outline.md`: Use the Airbnb/Dropbox "Problem-first" models.
    - `script.md`: A 3-minute script with emotional resonance.
2. **Sanity Check**: 
    - Does it work on mobile? 
    - Are the empty states handled (e.g., "Create your first project" buttons)?
    - Is the AHA moment explainable in 30 seconds without a keyboard?

---

## Part 2: References & Tools

### Rapid Deployment
- **Vercel**: Instant production environment.
- **Supabase**: Auth, DB, and Storage. Use `dev` branching for risky changes.
- **`.env.example` is Law**: Every secret key must be added here to prevent blocking teammates.

### Assets & Components
- **Stitch MCP**: Rapid UI prototyping and design token extraction.
- **21st.dev**: Premium component library for modern aesthetics.
- **CapCut/iMovie**: Rapid demo video editing.

### Pitch Inspiration
- **[Dropbox MVP Demo](https://techcrunch.com/2011/10/19/dropbox-minimal-viable-product/)**: Relatable storytelling.
- **Airbnb Pitch Deck**: Extreme focus on problem/solution metrics.
- **[Devpost](https://devpost.com)**: Study previous winning projects for your specific track.
