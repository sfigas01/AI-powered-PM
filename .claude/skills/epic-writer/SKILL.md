---
name: safe-epic-creator
description: "Convert meeting notes, transcripts, presentations, and product owner descriptions into structured SAFe (Scaled Agile Framework) epics and save them to Notion. Use this skill when the user needs to (1) Create a SAFe epic from raw information sources, (2) Transform unstructured meeting content or descriptions into a formal epic format, (3) Generate epics that include audience, problem statement, solution, business hypothesis, and success metrics, or (4) Save formatted epics to Notion for review and feedback."
---

# SAFe Epic Creator

Transform unstructured information from meetings, transcripts, presentations, and descriptions into well-structured SAFe epics and save them to Notion.

## Workflow

### Step 1: Gather and Understand the Input

Review all provided materials:
- Meeting transcripts (automated or hand-written notes)
- Product owner descriptions
- Presentation decks
- Any other contextual information

Identify key information:
- Who the intended users/audience are
- What problem or need exists
- Why this is important or urgent now (timing factors)
- What the solution should accomplish (core features/capabilities)
- Any mentioned business value or outcomes
- Any metrics or success criteria mentioned

If critical information is missing, ask the user targeted clarifying questions ONE AT A TIME (per user preference).

### Step 2: Structure the Epic

Read the SAFe epic template reference file to understand the required structure:

```bash
view references/safe_epic_template.md
```

Extract and organize information into these required components:

1. **Epic Name**: Create a clear, concise name (3-7 words)
2. **Epic Description**: Brief overview (2-4 sentences)
3. **Target Audience**: Identify who this is for
4. **Problem Statement/Need**: What problem exists and why it matters
5. **Why Now**: What makes this timely or urgent (market conditions, strategic timing, competitive pressures)
6. **Proposed Solution/Core Features**: What should this do and the 3-7 core capabilities/features
7. **Business Outcome Hypothesis**: Formulate a hypothesis using the format:
   - "We believe that [doing this] for [these people] will achieve [this outcome]. We will know we are successful when we see [this measurable signal]."
8. **Leading Indicators/Success Metrics**: Define specific, measurable metrics with target values
9. **Non-Functional Requirements**: Include if relevant (performance, security, scalability, etc.)
10. **In Scope/Out of Scope**: Clarify boundaries (optional but recommended)
11. **Dependencies**: List if known
12. **Estimated Timeline/Effort**: Include if available

### Step 3: Draft the Epic

Create a well-formatted epic that:
- Uses clear, business-focused language
- Avoids unnecessary technical jargon
- Is specific about outcomes and metrics
- Focuses on value delivery
- Remains concise but comprehensive

When information is ambiguous or missing, make reasonable inferences based on context, but note any assumptions made.

### Step 4: Save to Notion

Search for the "SAFe Epic Template" page in Notion:

```
notion-search with query: "SAFe Epic Template"
```

Create the epic as a sub-page under "SAFe Epic Template" using the `notion-create-pages` tool with the formatted epic content in Notion-flavored Markdown.

Structure the Notion page with clear sections using headers and appropriate formatting for readability.

### Step 5: Confirm and Offer Iteration

After saving to Notion:
- Provide the link to the newly created epic
- Summarize the key components included
- Offer to make adjustments based on feedback
- Note any assumptions made that should be validated

## Tips for Quality Epics

- **Be specific**: Vague descriptions lead to vague epics. Push for concrete details.
- **Focus on outcomes, not outputs**: Emphasize the business value and user impact, not just features.
- **Quantify when possible**: Metrics should have numbers and timeframes.
- **Keep the audience in mind**: Every epic should clearly identify who benefits.
- **Make hypotheses testable**: Success criteria should be measurable and observable.

## Handling Different Input Types

**Meeting transcripts**: Look for discussion of problems, proposed solutions, stakeholder concerns, and any mentioned success criteria. Extract decisions and action items that inform the epic.

**Product owner descriptions**: These often contain the "what" but may need you to infer or ask about the "why" and "who."

**Presentation decks**: Focus on problem statements, proposed solutions, market analysis, and business cases. These often contain good material for the business hypothesis.

**Hand-written notes**: May be less structured. Look for key phrases about pain points, desired outcomes, and stakeholder needs.
