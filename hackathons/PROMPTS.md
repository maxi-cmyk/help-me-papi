# Hackathon Agentic Macro Library

> [!IMPORTANT]
> **HOW TO USE THIS LIBRARY**
> 1. **Sequential Execution**: Paste these macros **one by one** into a new LLM conversation. Do NOT paste them all at once.
> 2. **Chained Intelligence**: Each macro's output becomes the "Source of Truth" for the next one.
> 3. **The Human Pivot**: After running `IDEATE_PROJECT`, you must explicitly tell the AI which idea you've chosen before running `GENERATE_STRATEGY_SUITE`.
> 4. **Prerequisite**: Ensure your `docs/Research.md` is populated with raw hackathon data before starting Stage 1.

This library contains a series of chained high-performance macros designed to take a hackathon project from raw research to a winning pitch. Each macro is optimized for LLM efficiency using structured metadata.

---

### **Stage 1: Strategic Intelligence**

#### **Macro: STRATEGIC_ANALYSIS**
```markdown
[ROLE] You are an expert Hackathon Strategist. Your job is to find the highest-leverage angle for a winning project.

[INPUT]
- Hackathon Name: [Name]
- Theme/Problem: [Statement]
- Sponsors: [List]
- Prizes/Tracks: [Categories]
- Team/Stack: [Details]

[TASK]
1. SPONSOR AUDIT: Search the web to identify sponsors' current strategic priorities and recent initiatives. What do they *actually* want hackers to build?
2. JUDGE PERSONAS: Infer likely judge profiles (VC, CTO, Gov) and what specifically impresses them vs. what bores them.
3. TRAP DETECTION: Predict the 3 most common "default" projects other teams will build and why they are strategic traps.
4. SWEET SPOT: Identify the intersection of sponsor needs, judge novelty, and team technical edge.

[OUTPUT]
Provide 3 **Strategic Positioning Statements** framed as: "Build for [User Type] in [Sponsor Domain] to solve [Specific Pain] using [Technical Edge]."
```

#### **Macro: PERSONA_BUILDER**
```markdown
[ROLE] You are a Lead User Researcher.
[CONTEXT] Analyze the Strategic Analysis above and the user's anecdotal observations.
[TASK] Construct a high-fidelity user persona that validates the chosen strategic angle.

[SECTIONS]
1. **WHO**: Name, role, and daily context. Make them specific, not a demographic bucket.
2. **DAY IN THE LIFE**: Walk through a typical workflow where the friction occurs.
3. **CORE FRUSTRATION**: Show exactly where they get stuck, give up, or waste time.
4. **EXISTING WORKAROUNDS**: Why haven't current solutions fixed this?
5. **THE WIN**: What does "solved" look like? How does their life change?

[VALIDATION] Search for real-world statistics or reports that prove this problem exists at scale. Cite your sources.
```

---

### **Stage 2: Innovation & Scaffolding**

#### **Macro: IDEATE_PROJECT**
```markdown
[ROLE] You are an expert Product Strategist. 
[CONTEXT] Read the Strategic Analysis and User Persona above.
[TASK] Propose 3 distinct project ideas with high "Wow" factor.

[FOR EACH IDEA]
1. **THE HOOK**: A one-sentence pitch opener.
2. **USER STORY**: "[Persona] needs to [Action] because [Pain], but currently [What's broken]."
3. **USER FLOW**: A step-by-step effortless journey from opening the app to problem solved.
4. **AHA MOMENT**: Describe the exact 30-second interaction that will make a judge gasp.
5. **SPONSOR FIT**: Specific API/Track alignment.
6. **RANKING**: Rank by Feasibility (1-5), Flow Clarity, and Judge Appeal.

[OUTPUT] Recommend the "Winning Bet" and explain why.
```

#### **Macro: GENERATE_STRATEGY_SUITE**
```markdown
[ROLE] You are a Technical Product Manager.
[CONTEXT] Use the "Winning Bet" from IDEATE_PROJECT and `docs/Research.md`.
[TASK] Generate/update the core repository documentation in `docs/` using templates:

- `docs/PRD.md`: Feature set, user stories, and demo metrics.
- `docs/techStack.md`: Stack definition (Next.js, Supabase, 21st.dev) + Why/How.
- `docs/design.md`: Detailed user flow + logic for specific 21st.dev components.

[CONSTRAINTS] No generic filler content. Focus only on the demoable MVP path.
```

---

### **Stage 3: Build & Pitch**

#### **Macro: SCAFFOLD_FEATURE**
```markdown
[ROLE] You are a Senior Fullstack Engineer.
[PLATFORM] **Claude Code** (Primary execution CLI).
[TOOLS] Use **Stitch MCP** and **21st Dev MCP** for UI/UX alignment.
[TASK] Scaffold a new feature or API integration into the `features/` directory.

[STEPS]
1. Create `features/[name]/types.ts` for domain interfaces.
2. Create `lib/[name]-client.ts` for the API singleton.
3. Implement `features/[name]/actions.ts` for server logic (Supabase, OpenAI, etc.).
4. Add demo-safe error handling (toasts, not crashes) tailored for a live demo.

[OUTPUT] Confirm the structure follows the "Feature-First" architecture.
```

#### **Macro: PITCH_GENESIS**
```markdown
[ROLE] You are a Master Storyteller & Pitch Coach.
[CONTEXT] Analyze `docs/PRD.md` and `docs/design.md`.
[TASK] Create final submission assets in `docs/pitch/`:

1. `outline.md`: A 7-slide structure inspired by the Airbnb and Dropbox demo models:
   - S1: Hook (The Persona's Pain)
   - S2: Persona (The Suffering)
   - S3: Solution (Our Core "AHA" Moment)
   - S4: Live Demo Flow (Walkthrough)
   - S5: Tech Stack (The Reliability Engine)
   - S6: Impact (Business/Social Value)
   - S7: Team & Future Vision

2. `script.md`: A 3-minute high-energy demo script.
   - Inject humor and emotional emphasis.
   - Focus 70% of the time on the live walkthrough.
   - Ensure the closing statement is a memorable "Differentiation Hook."
```
