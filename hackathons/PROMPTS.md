# Hackathon Strategy Prompts

Three prompts that chain together in one conversation to help conceptualize and win hackathons.

---

## Prompt 1: Strategic Analysis
Copy everything below the line into a new conversation. Fill in the bracketed fields with whatever you have — leave blanks empty, say "research this" next to anything you want Claude to look up. 

Wait for Claude to ask you about your target user before moving to Prompt 2.

```text
You are a hackathon strategist. Your job is to analyze a hackathon's competitive landscape and help me find the highest-leverage angle for a winning project.

## What I Know

**Hackathon name:** [name, or leave blank]
**Problem statement / theme:** [paste the problem statement, theme, or track descriptions if available]
**Sponsors:** [list sponsor names — e.g. AWS, Stripe, a specific bank or NGO]
**Prizes & tracks:** [any specific prize categories, bonus tracks, or sponsor challenges]
**Judges:** [names and titles if known, otherwise leave blank]
**Location & context:** [city, venue, university, online — anything about the setting]
**Duration:** [e.g. 24hrs, 48hrs, weekend]
**Our team:** [brief — e.g. "2 fullstack devs (Next.js/React), 1 ML person, 1 designer" or just "3 CS students"]
**Our stack:** [what we're comfortable building with — e.g. Next.js, Supabase, Python, Vercel]
**Anything else:** [constraints, sponsor APIs we must use, hardware available, etc.]

---

## Your Task

Work through these sections in order. For any sponsor, judge, or organization I haven't provided details on, **search the web** to fill in gaps — look up what they do, their recent initiatives, their public priorities, and any relevant leadership quotes or blog posts. Cite what you find.

### 1. Sponsor & Stakeholder Analysis

For each sponsor:
- What they actually sell/do and who their customers are
- Their current strategic priorities (what are they pushing this quarter/year?)
- Their likely pain points and what they want hackers to solve.
- Which specific AI capabilities would impress the judges most given the tech stack provided?
- What they likely want to see from hackathon projects (use of their API? alignment with their mission? developer adoption?)
- The gap between what they *say* they want and what actually wins (if you can infer this from past events)

### 2. Judge Personas

For each judge (or judge *type* if names aren't known):

- **Background & lens**: What's their professional context? A VC judges differently from a CTO, who judges differently from a government official.
- **What impresses them**: Technical depth? Business viability? Social impact? Design polish? A working demo?
- **What bores them**: What have they seen a hundred times? What's the "obvious" project they'll be tired of by the 10th pitch?
- **Decision weight**: If there are multiple judges, who likely has the most influence on the final decision?

If I haven't provided judge names, infer likely judge profiles from the sponsor types and hackathon context (e.g. a fintech sponsor likely sends a product lead or engineering director).

Environmental Context: How does the local setting (e.g., Singapore’s "Smart Nation" goals) influence the relevance of a project?

### 3. Competitor Analysis

Based on the theme, sponsors, and setting, predict:
- **The 3 most common projects** other teams will build (the "default" ideas everyone gravitates toward)
- **Why those are traps**: crowded space, hard to differentiate, or technically ambitious without enough time
- **The underserved angles**: themes, user groups, or sponsor interests that most teams will overlook

### 4. Strategic Positioning

Given all of the above, where is the **sweet spot** — the intersection of:
- What sponsors want to see funded/adopted
- What judges haven't seen before
- What our team can actually build and demo well
- What solves a real problem for a specific user

Don't give me project ideas yet. Give me the 2–3 **strategic angles** we should be exploring — framed as positioning statements like "Build for [user type] in [sponsor's domain] using [our technical edge] to solve [specific pain point]."

Then **ask me** about our target user base before moving on. Specifically, ask me:
- Who we're thinking of building for (or who we've seen struggling with this problem)
- Any first-hand knowledge we have about this user group (do we know people like this? have we observed their workflow? have we been this user ourselves?)
- What we think their biggest friction points are
```

---

## Prompt 2: User Persona
After Prompt 1, Claude will ask you about your target user. Answer with whatever you know — real observations, people you've met, your own experience. Then send this:

```text
Based on what I just told you and the strategic analysis above, build one detailed user persona.

**Who they are**: Name, age range, role, daily context. Make them specific enough to feel like a real person we're building for, not a demographic bucket.

**A day in their life**: Walk through a typical day or workflow where the problem shows up. What are they doing before, during, and after the pain point? What tools or workarounds do they currently use?

**The core frustration**: What's broken, slow, confusing, or missing? Be specific — "it's hard to manage X" is too vague. Show the friction: where do they get stuck, give up, make errors, or waste time?

**What they've tried**: How have they attempted to solve this? What exists that partially works but falls short? Why haven't existing solutions fixed it?

**What good looks like for them**: If we solved this well, what does their experience feel like? What can they do now that they couldn't before? How do they know it's working?

**The judge lens**: Why would a sponsor or judge care about this person? How does helping them align with the hackathon's priorities?

After generating the persona, also research this user group — search for relevant statistics, reports, or news articles that validate the problem. We want hard numbers we can cite in our pitch (e.g. "X% of [user group] report [problem]" or "[industry] loses $Y annually to [friction]").
```

---

## Intermediate Step: Low-Fidelity Prototyping
Immediately after generating the persona and before moving to ideation, start your low-fidelity prototyping in parallel with setting up your dev environment.

- **Tools:** Use Figma, Stitch, or just draw it out on paper.
- **Goal:** Map out the 2-3 core screens that demonstrate the user flow. Align the team on the UX before writing any complex UI code.

---

## Prompt 3: Ideation
Run this in the **same conversation** after reviewing the persona and starting the prototyping phase.

```text
Now generate project ideas based on the strategic analysis and user persona above.

For each of the strategic angles you identified, propose 2–3 concrete project ideas. For each idea:

**One-liner:** What it is in one sentence (this becomes our pitch opener).

**The user story:** "[Persona name] needs to [action] because [pain point], but currently [what's broken]."

**User flow — step by step:** Map out exactly what the user does from the moment they open the app to the moment their problem is solved. For each step:
- What the user sees and does
- What happens behind the scenes
- Where the previous step leads to the next (the transition should feel obvious, not require thought)

This is critical. The flow must feel effortless — every screen should have one clear action, and the user should never wonder "what do I do now?" Flag any step where there's a risk of confusion, drop-off, or friction, and explain how you'd mitigate it.

**Demo script (3 minutes):** What a judge actually sees during our pitch. Structure this as:
- 0:00–0:30 — the hook (state the problem with the persona's story)
- 0:30–2:00 — the live demo (walk through the user flow, showing the key "aha" moment)
- 2:00–2:45 — how it works under the hood (brief tech explanation)
- 2:45–3:00 — the closer (impact statement, what's next)

**Tech approach:** How we'd build it with our stack in the time available. Flag anything risky or time-consuming. Separate what we'd build for the demo vs what we'd describe as "next steps."

**Sponsor alignment:** Specifically how this maps to what the sponsors want — name the API, the initiative, the strategic priority.

**Differentiation hook:** The one thing that makes a judge remember this project after seeing 30 pitches.

After listing all ideas, rank them:
- **Feasibility** (can we build a convincing demo in time?)
- **Flow clarity** (is the user journey simple enough to demo in 3 minutes and feel intuitive?)
- **Judge appeal** (does it stand out and align with criteria?)
- **Sponsor fit** (does it make a sponsor want to champion it?)

End with your top recommendation and why.
```
