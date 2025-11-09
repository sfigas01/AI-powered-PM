# Quick Start Guide - Acceptance Criteria Helper

## How to Use This Skill

### Invoke the Skill

In Claude Code, type:
```
/skill ac-helper
```

Or naturally in conversation:
```
Use the ac-helper skill
```

---

## Common Use Cases

### 1️⃣ Review Existing Acceptance Criteria

```
Use the ac-helper skill

Please review the acceptance criteria for this story:

**Story**: [paste story title and description]

**Current Acceptance Criteria**:
- [paste existing AC]
```

**What happens next:**
- Claude asks clarifying questions about context
- Evaluates AC against best practices
- Provides specific feedback and suggestions
- Collaborates with you to refine

---

### 2️⃣ Write New Acceptance Criteria

```
Use the ac-helper skill

Help me write acceptance criteria for this:

**Story**: [paste story title and description]
```

**What happens next:**
- Claude asks about the work type (dev, research, enabler)
- Confirms understanding with you
- Determines appropriate format
- Drafts criteria collaboratively
- Iterates based on your feedback

---

### 3️⃣ Research/Spike Work

```
Use the ac-helper skill

I have a research spike without clear acceptance criteria:

**Spike**: Evaluate machine learning platforms for document classification

**Goal**: Determine which ML service to use for our document processing feature
```

**What happens next:**
- Claude focuses on learning outcomes
- Helps define deliverables
- Sets scope boundaries
- Creates measurable success criteria

---

## Expected Interaction Pattern

The skill is **collaborative**, not prescriptive:

1. **You share** the story/feature
2. **Claude asks** clarifying questions
3. **You provide** context and intent
4. **Claude drafts** initial AC
5. **You review** and give feedback
6. **Together you refine** until it's right

---

## What to Prepare

Before using the skill, have ready:
- ✅ Story/feature description
- ✅ User/stakeholder information
- ✅ Any existing AC (if reviewing)
- ✅ Context about value/outcome

---

## Quick Decision Tree

**What type of work is this?**

🔵 **Development Story** (building features)
→ Use **Scenario format** (Given/When/Then)

🟢 **Research/Spike** (learning/exploration)
→ Use **Checklist format** (deliverables/outcomes)

🟡 **Enabler Story** (infrastructure/architecture)
→ Use **Checklist format** (technical outcomes)

🟣 **System Requirements** (constraints/rules)
→ Use **Checklist format** (specifications)

---

## Examples You Can Copy/Paste

### For Development Stories:
```
Use the ac-helper skill

Story: As a customer, I want to filter products by price range so I can find items within my budget

Current AC:
- User can filter products
- Filters work correctly
- UI is updated
```

### For Research Spikes:
```
Use the ac-helper skill

Spike: Research authentication options for mobile app

We need to decide between OAuth, SAML, and custom JWT implementation. No current AC defined.
```

### For Enabler Stories:
```
Use the ac-helper skill

Enabler: Set up monitoring and alerting for production services

Current AC:
- Monitoring is configured
- Alerts are sent
- Team can view metrics
```

---

## Tips for Best Results

✅ **DO:**
- Share full context about the story
- Answer clarifying questions thoughtfully
- Provide feedback on drafts
- Iterate until AC feels right
- Think about how you'll test each criterion

❌ **DON'T:**
- Expect perfect AC without collaboration
- Skip context/background information
- Accept AC that feels untestable
- Include implementation details in AC
- Make AC too vague or too prescriptive

---

## Red Flags the Skill Will Catch

🚩 Implementation details ("use Redux for state management")
🚩 Vague criteria ("system works well")
🚩 Untestable statements ("user is happy")
🚩 Multiple AND/OR conditions in one criterion
🚩 Missing user perspective
🚩 No clear pass/fail outcome

---

## Success Looks Like

After using the skill, your acceptance criteria should be:

✨ **Testable** - Clear yes/no answers
✨ **Outcome-focused** - What success looks like
✨ **User-centric** - From stakeholder perspective
✨ **Measurable** - Specific and verifiable
✨ **Clear** - No ambiguity about "done"

---

## Need Help?

If the skill isn't working as expected:
1. Check you've invoked it with `/skill ac-helper`
2. Provide more context about your work item
3. Answer the clarifying questions thoroughly
4. Give feedback on drafts so Claude can refine

Remember: This is a **collaborative process**. The skill works best when you engage in dialogue rather than expecting one-shot answers!
