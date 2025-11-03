# Epic: AI Voice Agent for Service Canada Call Centres

## Epic Overview

**Epic ID:** EPIC-001
**Epic Name:** AI Voice Agent for Service Canada Call Centres
**Product Owner:** Stephanie (Product Manager)
**Created:** November 1, 2024
**Target Delivery:** Q2 FY2025 (Pilot), Q4 FY2025 (Full Deployment)
**Status:** Discovery & Planning

---

## Executive Summary

Implement an AI-powered voice agent system to handle routine inquiries for Service Canada's Employment Insurance (EI) and Pensions/Guaranteed Income Supplement (OAS/GIS) call centres. The solution aims to dramatically reduce wait times (from 18-35 minutes to under 5 minutes), improve information accuracy (from 80-84% to 98%+), and enhance citizen satisfaction while maintaining dignified, accessible service for vulnerable populations.

**Business Impact:**
- **Volume:** 12,000-38,000 daily calls across both programs
- **Routine Call Deflection:** 65-75% of calls suitable for AI handling
- **Cost Savings:** Potential redeployment of 30-40% of agent capacity to complex cases
- **Citizen Experience:** Projected satisfaction improvement from 64-68% to 75-78%+
- **Service Standards:** Return to meeting 80-85% service standard targets (currently at 58-65%)

---

## Problem Statement

### Current State Challenges

#### 1. Unacceptable Wait Times
**Employment Insurance (EI):**
- Average wait time: 18-25 minutes (2022-23 baseline, improved to 1-4 minutes in 2023-24 with $574M investment)
- Peak period wait times: 45-90+ minutes
- Daily call volume: 15,000-20,000 calls (doubles during crises)
- 200+ agents struggling to meet demand

**Pensions/GIS (OAS):**
- Average wait time: 25-35 minutes
- Peak period wait times: up to 120 minutes
- Daily call volume: 12,000-18,000 calls
- 180 agents across three sites

**Impact:** Vulnerable populations (unemployed Canadians, low-income seniors averaging age 73) waiting hours for simple answers about critical income support.

#### 2. Information Accuracy Crisis
**Quality Assurance Findings:**
- **EI:** 15-18% total error rate, 6% serious errors leading to financial hardship
- **OAS:** 16-20% total error rate, 5-6% serious errors
- **Root Causes:**
  - Complex, frequently changing regulations (e.g., quarterly GIS income threshold updates)
  - Multiple benefit types with varying eligibility rules
  - Insufficient agent training (parallel CRA data shows <30 min/year training per agent)
  - Legacy systems requiring navigation of multiple screens during calls

**Real Impact Examples:**
- **EI Case:** Agent misinformed claimant about earnings limits ($200/week vs. actual 50-cent deduction per dollar earned above 90% threshold), resulting in overpayment and Member of Parliament inquiry
- **OAS Case:** Agent incorrectly advised widow not to report spouse's death, causing 8-month delay in increased GIS benefits during bereavement period

#### 3. Workforce Sustainability
- **Turnover:** 25-28% annually (below industry average of 30-45% but still high for government)
- **Emotional Burden:** Agents serving scared, angry, desperate citizens facing financial crisis
- **Union Concerns:** PSAC concerns about AI-driven job cuts (3,300 call centre jobs lost at CRA in 2024)
- **Performance Pressure:** Missing service standards (80-85% targets) while hitting only 58-65%

---

## Opportunity

### High-Volume Routine Inquiries (65-75% of Total Calls)

**Employment Insurance:**
- Application status inquiries
- Payment date questions
- Access code resets
- Reporting reminders
- Hours worked confirmations
- Benefit eligibility explanations
- Reporting obligation procedures

**Pensions/GIS:**
- Payment date inquiries
- Benefit amount confirmations
- Address updates
- Direct deposit setup
- SIN verification
- Explanation of annual statements
- Tax filing requirements for GIS
- Application intake (basic information collection)

### AI Advantages Over Human Agents

1. **Consistency:** Always pulls current policy data; no outdated information or memory lapses
2. **Accuracy:** Eliminates human error in policy interpretation for straightforward questions
3. **Availability:** 24/7 access, immediate response times
4. **Scalability:** Handles volume spikes without additional staffing costs
5. **Patience:** Unlimited patience for repetition, especially critical for senior demographic
6. **Bilingual Capability:** Seamless English/French service without language barriers
7. **Integration:** Real-time file access eliminates manual system navigation delays

---

## User Personas

### Persona 1: Unemployed Worker - "Michael"
**Demographics:** 38 years old, recently laid off from manufacturing job
**Tech Comfort:** Moderate; uses smartphone daily
**Emotional State:** Anxious about finances, frustrated by bureaucracy
**Needs:**
- Quick answers about application status
- Understanding of reporting requirements
- Clarity on when payments will arrive
- Reassurance that benefits are being processed

**Pain Points:**
- Can't afford to wait 45 minutes on hold during job search
- Needs immediate answers to budget household expenses
- Finds government websites confusing

**AI Solution Fit:** High - routine status and payment questions, needs speed over empathy

---

### Persona 2: Low-Income Senior - "Dorothy"
**Demographics:** 73 years old, widow, receiving OAS/GIS
**Tech Comfort:** Low; struggles with smartphone, prefers phone calls
**Emotional State:** Vulnerable, sometimes confused, worried about losing benefits
**Needs:**
- Patient, clear explanations about benefit amounts
- Understanding of why payments changed
- Help with reporting requirements for GIS
- Reassurance that benefits are secure

**Pain Points:**
- Mild hearing impairment; needs information repeated
- Sometimes forgets what she already asked
- Intimidated by technology and bureaucracy
- Fixed income makes any payment disruption critical

**AI Solution Fit:** Medium - requires specially designed senior-friendly AI with easy human escalation option

---

### Persona 3: Stressed Parent - "Aisha"
**Demographics:** 31 years old, on maternity/parental EI benefits
**Tech Comfort:** High; comfortable with all digital tools
**Emotional State:** Time-stressed, needs efficiency
**Needs:**
- Quick answers while caring for newborn
- Understanding of how part-time work affects benefits
- Deadline reminders for reporting
- Fast resolution without long phone waits

**Pain Points:**
- Limited windows of time to make calls (baby naps)
- Can't wait on hold with crying infant
- Needs accurate information to avoid overpayment issues

**AI Solution Fit:** Very High - ideal user for AI-first service with human escalation if needed

---

## Success Metrics

### Primary KPIs

| Metric | Current Baseline | 6-Month Target | 12-Month Target | Measurement Method |
|--------|-----------------|----------------|-----------------|-------------------|
| **Average Wait Time (EI)** | 18-25 min (2022-23) | <10 min | <5 min | Call centre telephony system |
| **Average Wait Time (OAS)** | 25-35 min | <10 min | <5 min | Call centre telephony system |
| **Information Accuracy** | 80-84% | 95%+ | 98%+ | QA reviews of AI transcripts |
| **Citizen Satisfaction (EI)** | 68% | 73% | 75%+ | Post-call surveys |
| **Citizen Satisfaction (OAS)** | 64% | 73% | 78%+ | Post-call surveys |
| **Service Standard Achievement (EI)** | 65% of calls answered | 75% | 80%+ | Performance reporting |
| **Service Standard Achievement (OAS)** | 58% of calls answered | 75% | 85%+ | Performance reporting |
| **Routine Call Deflection Rate** | 0% (baseline) | 40% | 60-70% | Call routing analytics |

### Secondary KPIs

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| **AI Resolution Rate** | 85%+ (calls resolved without human transfer) | Call completion tracking |
| **Transfer to Human Rate** | <15% of AI-handled calls | Call routing analytics |
| **Abandoned Call Rate** | <5% | Telephony system |
| **First Call Resolution** | 90%+ | Call outcome tracking |
| **Average Handle Time (AI)** | <4 minutes | Call duration tracking |
| **Peak Period Wait Time** | <15 minutes | Real-time monitoring |
| **Agent Satisfaction/Burnout** | Improved turnover (<20%) | HR metrics, employee surveys |

### Compliance & Risk Metrics

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| **Privacy Breach Incidents** | 0 | Security incident reports |
| **Bilingual Service Quality** | 95%+ accuracy both languages | QA reviews |
| **Accessibility Compliance** | 100% (TTY, VRS integration) | Accessibility audits |
| **Senior Opt-Out Rate** | Track and minimize | User preference data |
| **Serious Error Rate** | <1% | Critical incident tracking |

---

## User Stories

### Theme 1: Routine Inquiry Automation

#### Story 1.1: Payment Date Inquiry (EI)
**As a** EI claimant
**I want to** ask an AI agent when my next payment will be deposited
**So that** I can budget my household expenses without waiting on hold

**Acceptance Criteria:**
- [ ] AI authenticates caller using SIN or access code
- [ ] AI accesses claimant file and retrieves next payment date
- [ ] AI provides date in clear, conversational language
- [ ] AI confirms direct deposit setup or explains mail timing
- [ ] AI offers to answer additional payment-related questions
- [ ] Call completed in <3 minutes average
- [ ] 98%+ accuracy verified through file comparison

**Story Points:** 5
**Priority:** P0 (Pilot Launch)

---

#### Story 1.2: Application Status Check (EI)
**As a** recently unemployed worker
**I want to** check the status of my EI application via AI
**So that** I know if my claim is being processed without long wait times

**Acceptance Criteria:**
- [ ] AI authenticates caller
- [ ] AI retrieves current application stage from system
- [ ] AI explains status in plain language (received, under review, approved, payment scheduled)
- [ ] AI provides expected timeline for next steps
- [ ] AI escalates to human if application shows red flags or unusual delays
- [ ] Call completed in <4 minutes average

**Story Points:** 8
**Priority:** P0 (Pilot Launch)

---

#### Story 1.3: GIS Payment Amount Explanation (OAS)
**As a** low-income senior receiving GIS
**I want to** understand why my GIS payment changed this quarter
**So that** I'm not worried about losing my benefits

**Acceptance Criteria:**
- [ ] AI speaks slowly and clearly (senior-optimized pacing)
- [ ] AI retrieves current and previous quarter benefit amounts
- [ ] AI explains reason for change (cost of living adjustment, income threshold change, etc.)
- [ ] AI confirms next payment date
- [ ] AI offers to repeat information if requested
- [ ] AI detects confusion and offers human transfer
- [ ] Call completed in <5 minutes average (allowing for senior pace)

**Story Points:** 13
**Priority:** P1 (Phase 2)

---

### Theme 2: Self-Service Administrative Tasks

#### Story 2.1: Access Code Reset (EI)
**As a** EI claimant who lost my access code
**I want to** reset my code through AI voice authentication
**So that** I can complete my biweekly report without agent assistance

**Acceptance Criteria:**
- [ ] AI verifies identity using multi-factor authentication (SIN, DOB, postal code)
- [ ] AI generates and provides new access code
- [ ] AI confirms code verbally and offers to repeat
- [ ] AI explains how to use code for biweekly reporting
- [ ] Security audit trail created for all resets
- [ ] Call completed in <3 minutes

**Story Points:** 8
**Priority:** P0 (Pilot Launch)

---

#### Story 2.2: Address Update (OAS)
**As a** OAS beneficiary who recently moved
**I want to** update my address through the AI agent
**So that** I continue receiving my payments and correspondence

**Acceptance Criteria:**
- [ ] AI authenticates caller
- [ ] AI collects new address details with confirmation
- [ ] AI reads back full address for verification
- [ ] AI updates system in real-time
- [ ] AI confirms update and explains timeline for changes to take effect
- [ ] AI offers to update direct deposit if needed
- [ ] Call completed in <6 minutes

**Story Points:** 13
**Priority:** P1 (Phase 2)

---

### Theme 3: Policy Education & Guidance

#### Story 3.1: Reporting Obligations Explanation (EI)
**As a** EI claimant starting part-time work
**I want to** understand my reporting obligations from AI
**So that** I don't accidentally commit fraud or lose benefits

**Acceptance Criteria:**
- [ ] AI explains biweekly reporting requirement
- [ ] AI clarifies that all earnings must be reported
- [ ] AI explains 50-cent deduction rule and 90% income threshold
- [ ] AI provides examples of what constitutes "earnings"
- [ ] AI escalates to human if caller describes unusual income situation
- [ ] AI accuracy validated at 98%+ through policy expert review
- [ ] Call completed in <6 minutes

**Story Points:** 13
**Priority:** P1 (Phase 2)

---

#### Story 3.2: GIS Eligibility Explanation (OAS)
**As a** senior approaching age 65
**I want to** understand if I qualify for GIS through AI
**So that** I can access additional benefits I'm entitled to

**Acceptance Criteria:**
- [ ] AI explains GIS eligibility criteria (income-tested, OAS requirement)
- [ ] AI provides current income threshold for caller's marital status
- [ ] AI explains quarterly adjustments concept
- [ ] AI confirms tax filing requirement
- [ ] AI offers to transfer to human for application assistance
- [ ] Senior-paced delivery with repetition support
- [ ] Call completed in <7 minutes

**Story Points:** 13
**Priority:** P1 (Phase 2)

---

### Theme 4: Accessibility & Vulnerable Population Support

#### Story 4.1: Senior-Friendly Voice Interaction (OAS)
**As a** 73-year-old senior with mild hearing loss
**I want** the AI to speak slowly, clearly, and repeat information patiently
**So that** I can understand my benefits without frustration

**Acceptance Criteria:**
- [ ] AI detects caller age from file and adjusts pacing automatically
- [ ] AI speaks 15-20% slower than standard speed
- [ ] AI uses simple, jargon-free language
- [ ] AI offers to repeat information without requiring explicit request
- [ ] AI detects confusion markers ("what?", long pauses) and adjusts approach
- [ ] AI offers human transfer if caller seems frustrated
- [ ] Senior satisfaction rating 75%+ on post-call survey

**Story Points:** 21
**Priority:** P0 (Critical for OAS launch)

---

#### Story 4.2: Easy Human Escalation (Both Programs)
**As a** caller who prefers human service or has a complex question
**I want to** immediately transfer to a human agent at any point
**So that** I'm not forced to use technology I'm uncomfortable with

**Acceptance Criteria:**
- [ ] "Press 0 for human agent" announced at call start
- [ ] AI recognizes phrases like "I want a person," "speak to someone," "this isn't working"
- [ ] Transfer happens within 10 seconds of request
- [ ] AI provides summary of call to human agent (context transfer)
- [ ] No repeated authentication required after transfer
- [ ] Transfer logged for quality tracking
- [ ] Opt-out rate tracked but not penalized

**Story Points:** 8
**Priority:** P0 (Non-negotiable requirement)

---

#### Story 4.3: Bilingual Service Excellence (Both Programs)
**As a** francophone Canadian
**I want to** receive service in French that's natural and accurate
**So that** I can access government services in my official language

**Acceptance Criteria:**
- [ ] AI detects language preference from caller history or IVR selection
- [ ] AI handles mid-call language switching seamlessly
- [ ] French service uses natural Quebec French dialect (not European French)
- [ ] All policy information accurately translated and current
- [ ] Bilingual QA reviews show 98%+ accuracy in both languages
- [ ] No degradation in response time or capability between languages
- [ ] Official Languages Act compliance verified

**Story Points:** 13
**Priority:** P0 (Legal requirement)

---

### Theme 5: Edge Case Detection & Escalation

#### Story 5.1: Elder Abuse Detection (OAS)
**As a** call centre manager
**I want** AI to detect potential elder abuse indicators
**So that** vulnerable seniors are escalated to trained human agents

**Acceptance Criteria:**
- [ ] AI detects keywords: "family taking money," "someone forcing me," "threats," etc.
- [ ] AI detects unusual transaction patterns (e.g., "why did someone withdraw my GIS?")
- [ ] AI detects third-party pressure (background voices coaching caller)
- [ ] AI immediately escalates to specialized human agent with alert
- [ ] Agent receives transcript and flagged concerns
- [ ] Incident logged for follow-up protocols
- [ ] Zero false negatives (all indicators captured)

**Story Points:** 21
**Priority:** P1 (Before broad OAS rollout)

---

#### Story 5.2: Compassionate Care Benefit (EI)
**As a** caller inquiring about compassionate care EI
**I want** to be immediately transferred to a human agent
**So that** I receive empathetic support during end-of-life family situations

**Acceptance Criteria:**
- [ ] AI recognizes keywords: "dying," "terminal," "compassionate care," "gravely ill"
- [ ] AI responds with empathy script: "I'm very sorry for what you're going through. Let me connect you with a specialist who can help."
- [ ] Transfer happens within 15 seconds
- [ ] Agent receives context flag: "Compassionate Care - Handle with Sensitivity"
- [ ] No attempt to answer questions via AI
- [ ] 100% escalation rate for this scenario

**Story Points:** 8
**Priority:** P0 (Critical sensitivity requirement)

---

#### Story 5.3: Overpayment Dispute Detection (Both Programs)
**As a** caller disputing an overpayment notice
**I want** to be escalated to a human who can review my case
**So that** I don't receive incorrect information that worsens my situation

**Acceptance Criteria:**
- [ ] AI recognizes keywords: "overpayment," "I don't owe this," "dispute," "appeal"
- [ ] AI confirms basic case details but does not provide advice
- [ ] AI explains next steps will be discussed with specialist
- [ ] AI escalates to trained overpayment specialist
- [ ] Agent receives file number and dispute summary
- [ ] No resolution attempted by AI
- [ ] Transfer time <30 seconds

**Story Points:** 13
**Priority:** P0 (Risk mitigation)

---

## Technical Requirements

### Integration Requirements

#### Systems Integration
- **EI Mainframe System:** Legacy system for EI claims processing - read-only API access required
- **OAS Beneficiary Database:** Real-time access to payment schedules, benefit amounts, beneficiary details
- **Call Centre Telephony System:** Integration for call routing, transfer, and queue management
- **Authentication System:** SIN validation, access code verification, multi-factor authentication
- **Knowledge Base:** Real-time policy document access (quarterly GIS updates, EI regulation changes)
- **CRM System:** Call logging, transcript storage, quality assurance tracking

#### Data Requirements
- **Real-time file access:** <2 second response time for beneficiary data retrieval
- **Policy accuracy:** Automated updates within 24 hours of policy changes (e.g., quarterly GIS threshold adjustments)
- **Call recording:** 100% of AI calls recorded and stored for 7 years (government retention policy)
- **Audit trail:** Complete log of all data accessed, changes made, transfers initiated

### Security & Privacy Requirements

#### Government of Canada Standards
- [ ] Protected B data classification compliance
- [ ] Privacy Impact Assessment (PIA) completed and approved
- [ ] Security Assessment and Authorization (SA&A) completed
- [ ] Threat and Risk Assessment (TRA) completed
- [ ] Compliance with Privacy Act and Access to Information Act
- [ ] Encryption at rest and in transit (AES-256 minimum)
- [ ] Multi-factor authentication for system access
- [ ] Role-based access control (RBAC)

#### Data Handling
- [ ] No SIN storage in voice logs (redaction/tokenization)
- [ ] PII minimization in AI training data
- [ ] Secure destruction of call recordings after retention period
- [ ] Geographic data residency (Canada-only storage)
- [ ] Breach notification protocols compliant with federal requirements

### Accessibility Requirements

#### WCAG 2.1 AA Compliance
- [ ] TTY (Teletypewriter) relay service integration
- [ ] VRS (Video Relay Service) compatibility for ASL/LSQ users
- [ ] Senior-optimized pacing (adjustable speech rate)
- [ ] Compatibility with assistive listening devices
- [ ] Multi-modal input support (voice, keypad)

#### Bilingual Requirements
- [ ] Official Languages Act compliance
- [ ] Natural French (Quebec dialect) and English
- [ ] Seamless language switching mid-call
- [ ] Equal quality and response time in both languages
- [ ] Regional accent recognition (Acadian, Joual, etc.)

### Performance Requirements

| Metric | Requirement | Measurement |
|--------|-------------|-------------|
| **Response Latency** | <1 second for AI response initiation | Real-time monitoring |
| **Data Retrieval Time** | <2 seconds for file access | API performance tracking |
| **Call Completion Rate** | >95% (successful resolution without technical failure) | System reliability monitoring |
| **Uptime** | 99.9% (max 8.76 hours downtime/year) | SLA monitoring |
| **Concurrent Call Capacity** | 10,000+ simultaneous calls | Load testing |
| **Peak Load Handling** | 2x normal volume without degradation | Stress testing |

---

## Pilot Plan

### Phase 0: Preparation & Stakeholder Engagement (Months 1-2)

#### Union Engagement
- [ ] Present AI strategy to PSAC leadership (emphasize augmentation, not replacement)
- [ ] Co-design pilot with union representatives
- [ ] Establish joint monitoring committee
- [ ] Secure union agreement for pilot participation

#### Senior Advisory Group (OAS-specific)
- [ ] Recruit 15-20 seniors representing diverse demographics
- [ ] Conduct focus groups on AI comfort levels
- [ ] User testing of voice interaction prototypes
- [ ] Incorporate feedback into design

#### Technical Setup
- [ ] Complete security assessments (PIA, SA&A, TRA)
- [ ] Establish sandbox environment with test data
- [ ] Integrate with test telephony system
- [ ] Build monitoring dashboards

---

### Phase 1: Limited Pilot - Payment Date Inquiries Only (Months 3-5)

#### Scope
- **Program:** EI only (lower risk demographic than seniors)
- **Call Type:** Payment date inquiries only
- **Volume:** Route 10% of payment date calls to AI
- **Duration:** 90 days

#### Success Criteria
- [ ] 95%+ accuracy on payment date information
- [ ] <3 minute average call duration
- [ ] <10% transfer rate to humans
- [ ] 70%+ caller satisfaction (equal to or better than human baseline)
- [ ] Zero serious errors or privacy breaches

#### Monitoring
- Daily reviews of call transcripts by QA team
- Weekly stakeholder reviews with union and management
- Real-time accuracy dashboard
- Caller satisfaction surveys (100% sample during pilot)

---

### Phase 2: Expanded Pilot - Multiple Call Types (Months 6-8)

#### Scope
- **Program:** EI
- **Call Types:** Payment dates, application status, access code resets
- **Volume:** Route 30% of eligible calls to AI
- **Duration:** 90 days

#### Success Criteria
- [ ] 95%+ accuracy across all call types
- [ ] <4 minute average call duration
- [ ] <15% transfer rate to humans
- [ ] 72%+ caller satisfaction
- [ ] Agent satisfaction improvement (reduced burnout on repetitive calls)

---

### Phase 3: OAS Pilot - Senior-Focused Launch (Months 9-11)

#### Scope
- **Program:** OAS/GIS
- **Call Types:** Payment dates only (most straightforward)
- **Volume:** Route 10% of payment date calls to AI, with opt-out option
- **Duration:** 90 days

#### Success Criteria
- [ ] 98%+ accuracy (higher bar for vulnerable population)
- [ ] <5 minute average call duration (accounting for senior pace)
- [ ] <20% transfer rate (expecting more human escalation requests)
- [ ] 70%+ senior satisfaction
- [ ] <5% opt-out rate (seniors choosing human-only service)
- [ ] Zero complaints to MP offices or Ombudsman

#### Special Monitoring
- Senior advisory group reviews transcripts weekly
- Accessibility expert reviews for hearing/cognitive accommodation
- Dignity and respect qualitative assessment

---

### Phase 4: Full Production Rollout (Months 12-18)

#### Scope
- **Programs:** Both EI and OAS/GIS
- **Call Types:** All routine inquiries (65-75% of call volume)
- **Volume:** Route all eligible calls to AI with human fallback
- **Duration:** Ongoing operations

#### Transition Plan
- [ ] Month 12: 40% of eligible calls to AI
- [ ] Month 14: 60% of eligible calls to AI
- [ ] Month 16: 80% of eligible calls to AI
- [ ] Month 18: Full production (90%+ of routine calls to AI)

#### Agent Redeployment Strategy
- Complex case specialists (overpayments, appeals, compassionate care)
- AI training and quality assurance roles
- Proactive outreach (contacting claimants with incomplete applications)
- Policy interpretation and knowledge base maintenance

---

## Risks & Mitigation

### Risk 1: Public Backlash Against AI in Government Service
**Likelihood:** Medium | **Impact:** High

**Mitigation:**
- [ ] Transparent public communication about AI purpose (faster service, not job cuts)
- [ ] Always offer human option (press 0 at any time)
- [ ] Start with least vulnerable population (EI) before seniors (OAS)
- [ ] Monitor social media and MP feedback closely
- [ ] Prepare communications for Minister's office

**Contingency:**
- Pause rollout if >10% complaint rate or negative media coverage
- Pivot messaging to emphasize accessibility improvements
- Conduct public town halls if needed

---

### Risk 2: AI Provides Incorrect Information Leading to Financial Hardship
**Likelihood:** Low (with proper testing) | **Impact:** Critical

**Mitigation:**
- [ ] 98%+ accuracy requirement before launch
- [ ] Conservative escalation (when in doubt, transfer to human)
- [ ] Real-time monitoring for anomaly detection
- [ ] 100% call recording for dispute resolution
- [ ] Insurance/liability coverage for government accountability

**Contingency:**
- Immediate AI pause if serious error detected
- Manual review of all similar calls
- Proactive outreach to affected citizens
- Financial remediation protocol

---

### Risk 3: Union Resistance and Job Action
**Likelihood:** Medium | **Impact:** High

**Mitigation:**
- [ ] Early and continuous union engagement (joint design process)
- [ ] Commit to no layoffs due to AI (attrition only)
- [ ] Agent redeployment plan to more fulfilling roles
- [ ] Union representation on pilot monitoring committee
- [ ] Transparency on all metrics and outcomes

**Contingency:**
- Pause implementation if union recommends strike action
- Negotiate memorandum of understanding on AI scope
- Independent third-party review of job impact

---

### Risk 4: Senior Population Cannot/Will Not Use AI
**Likelihood:** Medium | **Impact:** Medium

**Mitigation:**
- [ ] Senior advisory group co-design
- [ ] Ultra-patient, slow-paced AI voice design
- [ ] Always available human option (no forced AI interaction)
- [ ] Extensive user testing with actual seniors (not just proxies)
- [ ] Hearing/cognitive accommodation features

**Contingency:**
- If opt-out rate >15%, limit OAS AI to non-senior callers (adult children calling on behalf)
- Enhanced human staffing for OAS if AI adoption is low
- Hybrid model: AI for initial triage, human for all final answers

---

### Risk 5: Legacy System Integration Failures
**Likelihood:** Medium | **Impact:** High

**Mitigation:**
- [ ] Extensive integration testing in sandbox environment
- [ ] Fallback to manual agent data entry if API fails
- [ ] Read-only access initially (no automated changes to files)
- [ ] Phased integration (payment dates first, then full file access)
- [ ] IT support on standby during pilot

**Contingency:**
- Manual data entry by agents if systems integration fails
- Extended pilot timeline to resolve technical issues
- Consider API-less solution (AI scripts questions, agent enters data)

---

### Risk 6: Privacy Breach or Data Security Incident
**Likelihood:** Low (with proper controls) | **Impact:** Critical

**Mitigation:**
- [ ] Full SA&A and PIA before any production data access
- [ ] Encryption, access controls, audit trails
- [ ] Regular penetration testing and security audits
- [ ] Minimal PII in AI training data (use synthetic data)
- [ ] Geographic data residency (Canada-only cloud)

**Contingency:**
- Immediate system shutdown if breach detected
- Office of the Privacy Commissioner notification within 24 hours
- Public disclosure per federal breach protocol
- Independent security review before restart

---

## Budget Estimate

### One-Time Implementation Costs

| Item | Cost Estimate | Notes |
|------|---------------|-------|
| **AI Platform License** | $500K | Enterprise government contract |
| **Systems Integration** | $750K | EI mainframe, OAS database, telephony, CRM |
| **Security Assessments** | $200K | PIA, SA&A, TRA, penetration testing |
| **Training Data Preparation** | $150K | Transcript anonymization, synthetic data generation |
| **Agent Training & Change Management** | $300K | Workshops, documentation, support |
| **Pilot Operations Support** | $100K | Extra monitoring, QA resources |
| **Legal & Compliance Review** | $100K | Privacy, accessibility, Official Languages Act |
| **Contingency (20%)** | $400K | Risk buffer |
| **TOTAL ONE-TIME** | **$2.5M** | |

### Annual Recurring Costs

| Item | Annual Cost | Notes |
|------|-------------|-------|
| **AI Platform Subscription** | $400K | Per-call pricing model, 10M calls/year estimate |
| **System Maintenance & Support** | $150K | Integration updates, API management |
| **Call Recording Storage** | $50K | 7-year retention, cloud storage |
| **Ongoing QA & Monitoring** | $200K | 2 FTE quality assurance analysts |
| **Policy Update Management** | $100K | Quarterly GIS updates, EI regulation changes |
| **Security Audits** | $75K | Annual penetration testing, compliance |
| **TOTAL ANNUAL** | **$975K** | |

### Return on Investment (ROI)

**Projected Savings (Annual):**
- **Agent Capacity Redeployment:** 30-40% of routine call volume (150 FTE equivalent)
- **Avoided Hiring:** 50 FTE at $75K avg = $3.75M annually
- **Reduced Overpayment Errors:** Improved accuracy reduces $2M+ in error remediation costs
- **Improved Citizen Outcomes:** Reduced MP inquiries, fewer escalations, faster service

**Net Annual Savings:** ~$3M+ (after $975K recurring costs)
**Payback Period:** <12 months
**3-Year ROI:** 340%+

---

## Dependencies & Assumptions

### Dependencies
- [ ] Treasury Board approval for AI implementation in government services
- [ ] PSAC agreement to participate in pilot
- [ ] Shared Services Canada support for telephony integration
- [ ] Office of the Privacy Commissioner clearance on PIA
- [ ] Minister's office approval for public communications
- [ ] Senior management commitment to no-layoff guarantee

### Assumptions
- EI wait time improvements from 2023-24 investments are sustainable (not temporary spike)
- Legacy systems have sufficient API capability for real-time integration
- Call volume remains stable (no major economic crisis doubling call volume)
- Government budget allocation available in FY2025
- Union will engage constructively if no-layoff commitment maintained
- Senior population will accept AI if designed with accessibility in mind

---

## Stakeholder Map

### Executive Sponsors
- **Deputy Minister, ESDC:** Ultimate accountability for Service Canada operations
- **Assistant Deputy Minister, Service Canada:** Budget authority and strategic approval

### Primary Stakeholders
- **Trevor (Director, EI Call Centre Operations):** EI pilot owner, requirements definition
- **Brenda (Executive Director, OAS Contact Centre):** OAS pilot owner, senior accessibility champion
- **PSAC Leadership:** Union buy-in, agent engagement, job security concerns
- **Call Centre Agents (375+ staff):** End users, training recipients, change management

### Secondary Stakeholders
- **IT/Security Teams:** Systems integration, security assessments, ongoing support
- **Privacy Office:** PIA review, data governance, breach protocols
- **Communications Team:** Public messaging, MP liaison, media response
- **Policy Teams (EI & OAS):** Knowledge base accuracy, quarterly updates
- **Quality Assurance Teams:** Pilot monitoring, accuracy validation

### External Stakeholders
- **Citizens (Unemployed Canadians & Seniors):** End beneficiaries of improved service
- **Members of Parliament:** Constituent service expectations, political oversight
- **Office of the Privacy Commissioner:** Privacy compliance oversight
- **Treasury Board Secretariat:** Budget approval, government-wide AI standards
- **Auditor General:** Future audits of call centre performance
- **Senior Advocacy Groups:** Elder rights, accessibility, dignity in service

---

## Out of Scope (For Initial Epic)

The following are explicitly **out of scope** for this epic and may be considered for future iterations:

- **Proactive Outreach:** AI-initiated calls to claimants (requires different consent framework)
- **Application Processing:** AI completing full EI or OAS applications (too complex for v1.0)
- **Appeals & Disputes:** AI handling formal appeals or overpayment disputes (requires human judgment)
- **Other Service Canada Programs:** CPP, disability, passports (separate requirements)
- **Chatbot/Digital Channel:** This epic focuses on voice; digital AI is separate workstream
- **Agent-Facing AI Tools:** Co-pilot tools for agents (separate epic)
- **Predictive Analytics:** Using AI to predict claim outcomes or fraud (separate initiative)

---

## Next Steps

### Immediate Actions (Next 30 Days)
1. [ ] Secure executive sponsor approval for pilot budget ($2.5M)
2. [ ] Schedule stakeholder meetings: PSAC, Trevor, Brenda, IT, Privacy Office
3. [ ] Issue RFP for AI platform vendors (government procurement process)
4. [ ] Initiate PIA and SA&A processes
5. [ ] Recruit senior advisory group for OAS co-design

### Short-Term (30-90 Days)
6. [ ] Select AI platform vendor and negotiate contract
7. [ ] Complete security assessments and receive approvals
8. [ ] Establish pilot governance structure (monitoring committee, escalation protocols)
9. [ ] Begin systems integration in sandbox environment
10. [ ] Conduct union workshops and co-design sessions

### Medium-Term (90-180 Days)
11. [ ] Launch Phase 1 pilot (EI payment dates)
12. [ ] Daily monitoring and rapid iteration
13. [ ] Prepare Phase 2 expansion based on Phase 1 learnings
14. [ ] Begin OAS-specific accessibility testing with senior advisory group

### Long-Term (6-18 Months)
15. [ ] Full production rollout across both programs
16. [ ] Agent redeployment to complex case work
17. [ ] Measure ROI and report to Treasury Board
18. [ ] Publish public transparency report on AI performance
19. [ ] Plan for expansion to additional Service Canada programs

---

## Appendices

### Appendix A: Research Sources
- Employment Insurance Monitoring and Assessment Report 2024 (ESDC)
- Auditor General Report on Call Centres (Spring 2019)
- Auditor General Report on CRA Contact Centres (Fall 2024)
- Public Service Employee Survey 2024 (Statistics Canada)
- Client interview transcripts: Trevor (EI), Brenda (OAS)
- Research summaries: EI Call Centre Challenges, OAS Call Centre Challenges

### Appendix B: Regulatory Framework
- Privacy Act (R.S.C., 1985, c. P-21)
- Official Languages Act (R.S.C., 1985, c. 31)
- Directive on Automated Decision-Making (Treasury Board)
- WCAG 2.1 AA Accessibility Standards
- Protected B Data Classification Standard

### Appendix C: Contact Information
- **Product Owner:** Stephanie (Product Manager) - stephanie@example.gc.ca
- **EI Stakeholder:** Trevor (Director, EI Call Centre) - trevor@example.gc.ca
- **OAS Stakeholder:** Brenda (Executive Director, OAS) - brenda@example.gc.ca
- **Union Contact:** PSAC Local 70000 - callcentres@psac.ca

---

**Document Version:** 1.0
**Last Updated:** November 1, 2024
**Next Review Date:** December 1, 2024
**Status:** Awaiting Executive Approval
