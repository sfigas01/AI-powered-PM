# Acceptance Criteria Format Selection Guide

Use this guide to quickly determine which AC format to use for your work item.

---

## Format Decision Matrix

| Work Type | Format | Rationale |
|-----------|--------|-----------|
| **User Story** (feature development) | Scenario (Given/When/Then) | Captures user behavior and interactions naturally |
| **Research Spike** | Checklist | Focuses on deliverables and learning outcomes |
| **Technical Spike** | Checklist | Emphasizes technical outcomes and decisions |
| **Enabler Story** (infrastructure) | Checklist | Lists technical requirements and capabilities |
| **Enabler Story** (architecture) | Checklist | Defines architectural outcomes and constraints |
| **Bug Fix** | Scenario (Given/When/Then) | Describes expected vs. actual behavior |
| **System Requirements** | Checklist | Specifies constraints and non-functional requirements |
| **Design/UX Work** | Checklist | Lists design deliverables and specifications |
| **Exploration/Discovery** | Checklist | Defines research scope and outputs |
| **Compliance/Security** | Checklist | Enumerates requirements and standards to meet |

---

## Format Details

### 📋 Scenario Format (Given/When/Then)

**Use When:**
- Describing user interactions with the system
- Testing specific behaviors or workflows
- Capturing feature functionality
- Writing BDD-style automated tests
- Need to show state transitions

**Structure:**
```
Given: [precondition or context]
When: [user action or event]
Then: [expected outcome]
And: [additional conditions or outcomes]
```

**Example - Login Feature:**
```
Given: I am a registered user on the login page
When: I enter valid credentials and click "Login"
Then: I am redirected to my dashboard
And: I see a welcome message with my name
And: My session is valid for 24 hours
```

**Strengths:**
- ✅ Natural for user-facing features
- ✅ Easy to convert to automated tests
- ✅ Clear sequence of events
- ✅ Shows state changes explicitly

**Limitations:**
- ❌ Can be verbose for simple requirements
- ❌ Not ideal for non-interactive work
- ❌ May not fit research/exploration work

---

### ✅ Checklist Format (Rule-Oriented)

**Use When:**
- Defining system capabilities or constraints
- Describing research deliverables
- Listing technical requirements
- Specifying design outputs
- Scenarios don't naturally apply

**Structure:**
```
- [Specific, measurable requirement]
- [Clear deliverable or outcome]
- [Testable constraint or specification]
```

**Example - Research Spike:**
```
- Evaluate 3 cloud storage providers (AWS S3, Azure Blob, Google Cloud Storage)
- Document cost comparison for 1TB storage with 100K requests/month
- Test upload/download performance with 100MB files
- Identify security and compliance capabilities
- Create POC for top 2 candidates
- Present findings to architecture team with recommendation
- Document decision in Architecture Decision Record (ADR)
```

**Strengths:**
- ✅ Flexible for various work types
- ✅ Clear deliverables and outcomes
- ✅ Easy to track completion
- ✅ Works well for non-user-facing work

**Limitations:**
- ❌ May lack context of user journey
- ❌ Can become a task list if not careful
- ❌ Doesn't show state transitions

---

## Hybrid Approach

Sometimes you can use **both formats** in the same work item:

**Example - Feature with Research Component:**

**User Story:** Implement social media sharing for blog posts

**Scenario-Based AC** (for the feature):
```
Given: I am viewing a published blog post
When: I click the "Share on Twitter" button
Then: A pre-populated tweet window opens
And: The tweet includes the post title and URL
And: After sharing, the share count increments
```

**Checklist AC** (for technical enablers):
```
- API integrations tested with Twitter, Facebook, LinkedIn
- Share counts persisted in database
- Privacy settings respected (no sharing for private posts)
- Analytics tracking implemented for share events
- Mobile responsive design verified on iOS and Android
```

---

## Quick Decision Tree

```
START: What type of work is this?

├─ Does it involve USER INTERACTION with the system?
│  ├─ YES → Use SCENARIO format (Given/When/Then)
│  │
│  └─ NO → Continue below
│
├─ Is it RESEARCH, SPIKE, or EXPLORATION?
│  ├─ YES → Use CHECKLIST format
│  │
│  └─ NO → Continue below
│
├─ Is it INFRASTRUCTURE or ARCHITECTURE?
│  ├─ YES → Use CHECKLIST format
│  │
│  └─ NO → Continue below
│
├─ Is it DESIGN or UX work?
│  ├─ YES → Use CHECKLIST format
│  │
│  └─ NO → Continue below
│
└─ DEFAULT → Use SCENARIO format if behavior-based,
             CHECKLIST if capability-based
```

---

## Common Patterns

### Pattern 1: API Development
**Format:** Scenario (Given/When/Then)
```
Given: I am an authenticated API client
When: I send a GET request to /api/users/123
Then: I receive a 200 status code
And: The response includes user data in JSON format
And: The response time is under 200ms
```

### Pattern 2: Database Migration
**Format:** Checklist
```
- Migration script tested on staging environment
- Rollback script created and tested
- Data integrity verified post-migration
- Migration completes in under 5 minutes
- Zero data loss confirmed
- Application functionality verified after migration
```

### Pattern 3: Performance Optimization
**Format:** Checklist
```
- Page load time reduced from 3s to under 1s
- Lighthouse performance score above 90
- Core Web Vitals meet "Good" thresholds
- No regressions in functionality
- Optimization documented for team knowledge base
```

### Pattern 4: Bug Fix
**Format:** Scenario (Given/When/Then)
```
Given: I have items in my shopping cart
When: I apply a discount code and proceed to checkout
Then: The discount is correctly applied to the total
And: The discounted amount is reflected in the order summary
And: The order confirmation email shows the discounted price
```

### Pattern 5: Security Enabler
**Format:** Checklist
```
- HTTPS enforced for all endpoints
- SQL injection vulnerability patched
- Security scan shows zero critical vulnerabilities
- Penetration test results reviewed and addressed
- Security controls documented in security wiki
```

---

## Red Flags by Format

### Scenario Format Red Flags:
🚩 Using Given/When/Then for non-interactive work
🚩 Too many "And" statements (break into separate criteria)
🚩 Implementation details in the "Then" clause
🚩 Vague outcomes ("system works correctly")

### Checklist Format Red Flags:
🚩 Items are tasks, not acceptance criteria ("Write unit tests")
🚩 No measurable outcomes ("Code is clean")
🚩 Missing context (who/what/why unclear)
🚩 Too granular (micro-tasks instead of outcomes)

---

## Pro Tips

**Tip 1: Start with User Perspective**
If you can naturally say "As a [user], when I [do something], I expect [outcome]" → use Scenario format

**Tip 2: Think About Testing**
How will you verify this criterion?
- If it's a test case → Scenario format fits well
- If it's a deliverable/artifact → Checklist format fits better

**Tip 3: Consider Your Audience**
- Product Owners & Stakeholders often prefer Scenario format (more relatable)
- Technical teams may prefer Checklist for enabler work (clearer outcomes)

**Tip 4: Consistency Within a Story**
Pick one primary format per story. Don't mix unless you have a clear hybrid scenario.

**Tip 5: Convert Between Formats**
You can often convert between formats:

Checklist: "User can filter by price range"
↓
Scenario:
```
Given: I am viewing the product catalog
When: I set the price filter to $50-$100
Then: Only products in that price range are displayed
```

---

## Still Unsure?

**When in doubt, ask yourself:**

1. Does this describe a **user journey or interaction**? → Scenario
2. Does this describe **what must exist or be delivered**? → Checklist
3. Is this **research or exploration**? → Checklist
4. Would this naturally fit a **BDD test**? → Scenario
5. Is the primary value **knowledge or a deliverable**? → Checklist

Or simply **use the ac-helper skill** and let Claude guide you! 🤖

```
/skill ac-helper
```
