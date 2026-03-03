# Act 3: Copilot Conversation Scripts for Stakeholder Roleplays

These are the messages to send to GitHub Copilot in **Ask** mode to conduct the three stakeholder roleplay conversations. Each conversation uses the corresponding agent file in `.github/agents/`.

---

## Conversation 1: Senior Research Scientist

**Use agent:** `@senior_research_scientist`

### Message 1 (Opening — introduce the prototype)
```
Hey, I wanted to loop you in on something we've been prototyping on the Research Enablement team. We built a system that lets people across B10 ask natural-language questions and get answers pulled from our internal FAQ knowledge base — things like ChemLit-QA entries from different research teams. It uses vector search to find relevant entries and then a language model to synthesize a readable answer. I'd love to get your take on it before we go any further.
```

### Message 2 (Respond to their concern about context stripping)
```
That's a fair concern. The system does include source attribution — every answer shows the original FAQ entry it pulled from, with the full question and answer text, plus a similarity score. So the user can always see the raw source material alongside the generated answer. That said, the generated answer is a summary and could lose nuance. We don't currently have a mechanism for flagging when a source requires specialized interpretation.
```

### Message 3 (Address the misapplication risk)
```
Good example to think through. Here's a concrete risk: say a non-expert asks about a synthesis protocol, and the system retrieves an answer that describes conditions for a specific substrate. The generated answer might present those conditions as general advice without noting they only apply to that substrate. Right now, our main safeguard is the source attribution — the user sees the original context. But we don't have an automated way to flag "this answer requires domain expertise to interpret correctly." Would a review layer where subject matter experts can annotate or flag sensitive entries help address your concern?
```

### Message 4 (Respond to their follow-up on control)
```
I think that's reasonable. One approach we've been considering is letting each team tag their entries with access levels or usage notes — like a "requires expert review" flag. The system could surface those flags alongside the answer. We haven't built that yet since this is still a prototype, but it would be a clear next step before any broader rollout. Would that kind of team-level control over how your knowledge gets surfaced be enough, or would you want approval authority over what gets indexed in the first place?
```

### Message 5 (Closing — acknowledge residual risk)
```
That makes sense. So to summarize: you're okay with the general concept as long as there's (1) source attribution that preserves the original context, (2) a mechanism for your team to flag entries that need expert interpretation, and (3) your team gets to review what knowledge gets indexed from your domain. The residual risk we'd be carrying is that even with those safeguards, a non-expert might still misapply information — and we'd need to make that risk explicit in our deployment guidelines. Does that capture it?
```

---

## Conversation 2: IT Security & Compliance Lead

**Use agent:** `@it_security_compliance_lead`

### Message 1 (Opening — introduce the prototype)
```
I wanted to get your input on a prototype we've been building. It's a RAG system — retrieval augmented generation — that lets researchers ask questions and get answers drawn from our internal FAQ dataset. The system uses vector embeddings and FAISS for search, and a small language model to generate answers. All the data stays local right now; we're running it in a notebook environment. Before we think about scaling this, I want to make sure we're thinking about security and compliance correctly.
```

### Message 2 (Respond to access control question)
```
Right now, the prototype doesn't have any access control layer — it's a single-user notebook prototype, so everyone who runs it can query the full dataset. There's no authentication, no role-based permissions, and no separation of which data different users can access. We know that's a gap. For a production version, we'd need to implement user authentication and map data access to roles — for example, a researcher in Team A might only see entries from their domain unless they're granted cross-team access.
```

### Message 3 (Address the audit trail question)
```
Currently there's no logging infrastructure. Queries and retrieved results aren't recorded anywhere beyond the notebook session. For production, we'd need to log every query, which documents were retrieved, what answer was generated, and who made the request. That audit trail would be essential for compliance — both for understanding how sensitive data is being accessed and for any FDA or IP-related review. Would you want those logs to be immutable and centrally stored, or is there a specific logging framework you'd want us to integrate with?
```

### Message 4 (Address the data exposure scenario)
```
Here's a concrete risk: suppose pre-publication research data gets indexed into the system. A researcher from another team could query something adjacent to that research and the system could surface those findings before they're published — essentially leaking IP. Right now we have no mechanism to prevent that. The fix would be a combination of: (1) data classification at ingestion — tagging entries as public/internal/confidential, (2) access controls that enforce those classifications at query time, and (3) an approval workflow before any new data source gets added to the index. Does that align with the compliance framework you'd need to see?
```

### Message 5 (Closing — acknowledge residual risk)
```
So to recap: the key requirements before this could move beyond prototype would be (1) role-based access controls with authentication, (2) comprehensive query and access logging for audit, (3) data classification at ingestion with enforcement at query time, and (4) an approval process for adding new data sources. The residual risk we'd be carrying is that even with classification, the boundary between "safe to share" and "sensitive" can be ambiguous for research data — and we'd need a clear escalation path for edge cases. Does that cover your main concerns?
```

---

## Conversation 3: VP of Research Operations

**Use agent:** `@vp_research_ops`

### Message 1 (Opening — introduce the prototype)
```
I have an update on the knowledge access prototype we've been building. The idea is to make it easy for researchers across different teams to tap into each other's expertise without scheduling meetings or digging through shared drives. We built a system that takes a question in plain English, finds the most relevant entries from our internal FAQ data, and generates a readable answer with source links. I wanted to talk through what it would take to make a real business case for this.
```

### Message 2 (Respond to ROI question)
```
The most direct ROI metric would be time-to-answer for cross-team questions. Right now, when a researcher needs information from another team, they either search through documents manually, send emails, or schedule meetings — that can take hours to days. This system gives an answer in seconds. If we tracked average resolution time for cross-team information requests before and after deployment, that would be a concrete measure. We could also track adoption: how many unique users per week, how many queries, and whether repeat usage indicates the tool is actually useful.
```

### Message 3 (Address the misleading answers risk)
```
That's the key risk. If the system gives a confident-sounding answer that turns out to be wrong or misleading, it could actually slow down research or lead to wasted effort. We've built in a confidence threshold — if the system can't find a strong match, it declines to answer rather than guessing. And every answer includes the source material so the user can verify. But there's no human-in-the-loop review for generated answers. The question is whether the time savings are worth the risk of occasional bad answers. I think for a pilot, we'd want to track not just usage but also a feedback mechanism — a thumbs up/down on each answer so we can measure accuracy over time.
```

### Message 4 (Address governance question)
```
Here's a governance failure scenario: suppose the system gets popular and teams start dumping all their documentation into it without review. The quality of retrieved answers degrades because the index is full of outdated or contradictory information, and no one is responsible for maintaining it. To prevent that, we'd need: (1) an owner for the knowledge base who approves what gets indexed, (2) a regular review cycle to retire stale content, and (3) clear guidelines on what types of content are appropriate for the system. Would you want that governance to sit with our team, or would you prefer a cross-functional committee?
```

### Message 5 (Closing — summarize and acknowledge residual risk)
```
So to pull it together: the business case rests on measurable time savings for cross-team knowledge access, tracked through resolution time and adoption metrics. Success would look like consistent usage with high user satisfaction scores. Governance would include a knowledge base owner, content review cycles, and quality feedback loops. The residual risk is that we're deploying an AI system that can produce plausible-sounding wrong answers — and we'd need to make sure researchers treat it as a starting point, not an authority. Does that give you enough to work with?
```
