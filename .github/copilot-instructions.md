# AI Coding Agent Instructions for MBAi 448

## Project Overview
**MBAi 448: Applied AI for Business** is a Northwestern Kellogg graduate course combining business and technology leadership with hands-on AI/ML experience. This repository contains weekly assignments that guide students through AI concepts, tools, and real-world applications.

**Current Focus**: Week 01 introduces students to VS Code, GitHub Copilot, and Custom Agents. The assignment uses contrasting AI agent dispositions to explore how instruction framing shapes behavior and output.

---

## Repository Structure

- **`week_01/`** – First module content
  - `assignment_01/` – Custom AI agents exercise with reference materials (State of AI Report 2025)
  - `slido/` – Poll/survey content for lectures
  - `Week 01_Class*.pdf` – Lecture slides
- **`.github/agents/`** – (in root) Templates for creating custom agents
- **`README.md`** – Course description, instructor info, assignment overview

---

## Key Patterns & Conventions

### Custom Agent Design
Agents in this course live in `.github/agents/` directories and demonstrate instruction-based behavior variation:

1. **Format**: `.md` files with `chatagent` code block (VS Code agent syntax)
2. **Structure**: Agents have explicit identity + worldview + core beliefs
3. **Example**: `pessimistic_agent.md` uses systemic risk framing; optimist uses market efficiency framing
4. **Best Practice**: Include supporting documentation (rationale, interaction examples, belief system) alongside the agent definition

### Instruction Framing Matters
The assignment teaches that small instruction changes have large behavioral effects:
- Same material processed through different agents yields different interpretations
- Emphasis, tone, and uncertainty handling vary based on framing
- This is a **teaching tool**, not a production pattern—help students observe how instruction design shapes AI output

---

## Critical Developer Workflow

### Running Course Content
1. **Assignments**: Open `week_XX/assignment_XX/` in VS Code
2. **Custom Agents**: Access `.github/agents/` within assignment folder; reference `demo.agent.md` as template
3. **Interactive Testing**: Use Copilot's **Ask** feature to query assignment materials with different agents
4. **Comparison**: Run same prompt through multiple agents to observe behavior changes

### Assignment Submission
- Student agents go in `.github/agents/` directory within assignment folder
- Include agent definition file (`.md`) + supporting materials if applicable
- Document the agent's disposition/worldview clearly in comments or separate README

---

## Important Integration Points

- **GitHub Copilot Ask functionality** – Primary interaction method (docs: https://code.visualstudio.com/docs/copilot/chat/copilot-chat)
- **Custom Agents** – Built via agent manifest syntax (docs: https://code.visualstudio.com/docs/copilot/customization/custom-agents)
- **Canvas LMS** – Course hub, syllabus, office hours, and official assignment submissions
- **Slack** – Support channel: https://join.slack.com/t/mbai448/signup

---

## Quick Reference for Instructors/TAs

### Expected Workflow for New Weeks
1. Create `week_XX/assignment_XX/` directory
2. Add `instructions.md` with assignment scope
3. Include reference materials (`.txt` files, PDFs, or external links)
4. Add example agent in `.github/agents/demo.agent.md` (optional; students delete/modify as needed)
5. Document submission expectations in README or instructions

### Common Agent Construction Pattern
```chatagent
# [Agent Name]: [Disposition/Role]

## Identity & Core Philosophy
[Explicit worldview, not just tone]

## Key Beliefs/Heuristics
- [Belief 1]
- [Belief 2]
...

## How I Process Information
[Decision-making framework specific to this agent]
```

---

## What NOT to Do (Course Design Principles)

- **Don't** focus on code generation—Week 01 is about understanding tooling, not writing code
- **Don't** create agents without clear contrasting worldviews—the value is in observing differences
- **Don't** assume one agent is "correct"—the exercise teaches that framing creates perspective
- **Don't** rely on production-grade agent engineering patterns—this is pedagogy, not production AI

---

## Questions for Course Maintainers

When adding future weeks, clarify:
1. Is the week teaching *agent design* or *application of agents to a domain*?
2. Should students create custom agents, or work with provided ones?
3. What materials should agents have access to (readings, datasets, external APIs)?
4. How should submissions be organized if assignments span multiple weeks?
