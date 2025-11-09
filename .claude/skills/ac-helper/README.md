# Acceptance Criteria Helper Skill

A Claude skill for reviewing and writing acceptance criteria following SAFe best practices.

## Purpose

This skill helps you:
- **Review existing acceptance criteria** against best practices
- **Write new acceptance criteria** collaboratively with expert guidance
- **Ensure AC quality** for development stories, research spikes, and enabler work
- **Apply appropriate formats** (scenario-oriented vs. rule-oriented)

## When to Use

Use this skill when:
- You have a feature/story without acceptance criteria
- You want to review existing AC for quality and completeness
- You're unsure which AC format to use
- You need help writing testable, outcome-focused criteria
- You're working on research/spike work and need to define outcomes

## How to Use

### Reviewing Existing Acceptance Criteria

```
Use the ac-helper skill

I have a story with existing acceptance criteria. Can you review it?

[Paste your story and acceptance criteria]
```

The skill will:
1. Ask clarifying questions about context
2. Evaluate AC against best practices
3. Provide specific feedback and suggestions
4. Collaborate with you to refine the criteria

### Writing New Acceptance Criteria

```
Use the ac-helper skill

I need help writing acceptance criteria for this story:

[Paste your story description]
```

The skill will:
1. Ask questions to understand the work item
2. Confirm the type (dev story, research, enabler)
3. Determine the appropriate format
4. Draft criteria collaboratively with you
5. Iterate based on your feedback

## Best Practices Applied

The skill evaluates and creates AC based on:

✅ **Outcome-focused** - What, not how
✅ **Testable** - Clear pass/fail with yes/no answers
✅ **Clear & concise** - Simple, straightforward language
✅ **User-centric** - From stakeholder perspective
✅ **Measurable** - Verifiable and specific

## Formats Supported

### Scenario-Oriented (Given/When/Then)
Best for development stories and features:
```
Given: [context/precondition]
When: [action]
Then: [expected outcome]
And: [additional conditions]
```

### Rule-Oriented (Checklist)
Best for system requirements, enablers, and research:
```
- [Specific requirement]
- [Measurable deliverable]
- [Clear constraint]
```

## Research & Spike Work

For research stories and spikes, the skill helps define:
- Learning outcomes and questions to answer
- Deliverables (documentation, POCs, presentations)
- Scope boundaries and time limits
- Decision support and knowledge sharing

## Examples

### Example 1: Development Story

**Story**: As a user, I want to reset my password so I can regain access to my account

**AC Format**: Scenario-oriented (Given/When/Then)

```
Given: I am on the login page
When: I click "Forgot Password" and enter my email
Then: I receive a password reset email within 5 minutes
And: The reset link expires after 24 hours
And: I can successfully set a new password using the link
```

### Example 2: Research Spike

**Story**: Investigate AI service providers for customer support chatbot integration

**AC Format**: Rule-oriented (Checklist)

```
- Evaluate 3 AI service providers (Azure OpenAI, AWS Bedrock, Google Vertex AI)
- Test integration with sample customer support scenarios
- Document cost projections for 10K conversations/month
- Identify security and data privacy considerations
- Create proof-of-concept for top 2 candidates
- Present findings and recommendation to architecture team
- Document decision rationale in ADR
```

### Example 3: Enabler Story

**Story**: Set up automated performance testing pipeline

**AC Format**: Rule-oriented (Checklist)

```
- Pipeline executes on every PR to main branch
- Tests complete within 15 minutes
- Performance metrics captured: response time, throughput, error rate
- Results published to team dashboard
- Alerts triggered if response time > 500ms or error rate > 1%
- Documentation updated with pipeline usage instructions
```

## Tips for Success

1. **Provide context** - Share the full story description and any background
2. **Engage in dialogue** - Answer clarifying questions to improve relevance
3. **Iterate** - Review drafts and provide feedback for refinement
4. **Think testable** - Consider how you'll verify each criterion
5. **Focus on outcomes** - What success looks like, not implementation details

## Common Issues Addressed

❌ **Vague criteria** → ✅ Specific, measurable outcomes
❌ **Implementation details** → ✅ Outcome-focused requirements
❌ **Untestable statements** → ✅ Clear pass/fail criteria
❌ **Technical jargon** → ✅ User-centric language
❌ **Missing scope** → ✅ Bounded, achievable criteria

## Related Resources

- [SAFe Acceptance Criteria Guidance](https://framework.scaledagile.com/blog/glossary_term/acceptance-criteria-2)
- [INVEST Criteria](https://framework.scaledagile.com/story)
- [Behavior-Driven Development (BDD)](https://framework.scaledagile.com/blog/glossary_term/acceptance-criteria-2)

## Skill Invocation

To use this skill in Claude Code:

```
/skill ac-helper
```

Or in conversation:

```
Use the ac-helper skill to review this story's acceptance criteria
```
