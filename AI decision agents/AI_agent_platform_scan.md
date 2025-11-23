# AI Agent Platform Landscape for Government Benefits Adjudication

## Executive Summary

This environmental scan evaluates AI agent platforms and frameworks specifically for accelerating government benefits adjudication decision-making. The focus is on systems that can assist human adjudicators while maintaining compliance, auditability, and fairness requirements essential to high-stakes government decisions.

**Key Finding**: 13% of Federal AI use cases impact public rights or safety and require concrete safeguards before deployment. Benefits adjudication falls squarely in this category, requiring human-in-the-loop oversight, explainability, and robust compliance frameworks.

---

## Current State: AI in Government Benefits Adjudication

### Proven Use Cases

**Social Security Administration (SSA)**
- **Quick Disability Determination (QDD)**: Uses predictive algorithms to identify claims where favorable disability determination is highly likely with readily available medical evidence
- **Purpose**: Maximizes quality, speed, and consistency of adjudicator decision-making
- **Approach**: AI prioritizes cases for expedited *human* review (not autonomous decisions)

**Centers for Medicare & Medicaid Services (CMS)**
- **Platform**: Palantir Foundry + SAS Analytics
- **Results**: Uncovered $210 million in fraudulent claims in one year
- **Focus**: Fraud detection and pattern recognition supporting investigators

**Veterans Affairs (VA)**
- Implementing AI for claims processing to reduce backlogs
- Focus on decision support rather than autonomous decision-making

### Operational Benefits Documented

- **Processing time**: Local authorities reduced assessment time from 25 minutes to 3 minutes using automation
- **Cost reduction**: Up to 50% reduction in claims processing expenses
- **Efficiency gains**: 30% improvement in claim-journey efficiency
- **Investigative workload**: 35% reduction with AI-powered case prioritization
- **Accuracy**: 99.99% claim validation accuracy in some implementations

### Critical Success Factors

1. **Human-in-the-Loop (HITL)**: All successful government implementations maintain human oversight
2. **Explainability**: Systems must provide clear rationale for recommendations
3. **Auditability**: Complete decision trails for compliance and appeals
4. **Fairness**: Bias detection and mitigation built into workflows

---

## Regulatory & Compliance Framework

### Required Certifications for Government Use

**FedRAMP (Federal Risk and Authorization Management Program)**
- Mandatory for cloud service providers handling federal government data
- Based on NIST SP 800-53 (400+ security controls)
- Requires authorization at Moderate or High risk levels for AI systems
- "Assess once, use many" model reduces redundant audits
- Action-level approvals required for AI governance

**SOC 2 (Service Organization Control 2)**
- Self-assessment of security controls
- Required for demonstrating data protection and privacy
- AI-specific considerations: provable oversight for privileged actions
- Often stepping stone to FedRAMP compliance

**Additional Requirements**
- **NIST AI Risk Management Framework**: Framework for identifying and managing AI risks
- **EU AI Act Article 14** (for international systems): Requires effective human oversight with manual operation, intervention, and real-time monitoring capabilities
- **State-level regulations**: E.g., New York's LOADinG Act forbids automated decision-making in public assistance without safeguards

### Key Compliance Differences

| Aspect | FedRAMP | SOC 2 |
|--------|---------|-------|
| Authority | Federal mandate | Voluntary standard |
| Scope | Cloud security for gov data | General security controls |
| Standards | NIST + FISMA | Self-established controls |
| Audit | Government-approved 3PAO | Independent auditor |
| AI Requirements | Mandatory oversight & explainability | Recommended governance |

---

## Decision-Making Framework for Benefits Adjudication

### Human-in-the-Loop Models

**1. Appeals-Based Model** (Recommended for High-Stakes Decisions)
- AI makes initial assessment
- Human expert reviews only flagged or appealed cases
- Based on judicial appellate process analogy
- Reduces workload while maintaining oversight
- Example: QDD prioritizes cases for human review

**2. Co-Pilot Model** (Recommended for Medium-Stakes)
- AI provides recommendations alongside evidence
- Human adjudicator makes all final decisions
- AI surfaces relevant information and patterns
- Maintains human agency throughout process

**3. Automation-with-Escalation Model** (Low-Stakes Only)
- AI handles routine, clear-cut cases automatically
- Complex or borderline cases escalate to humans
- Strict thresholds for automatic approval
- All decisions logged and auditable

### Requirements for Meaningful Human Oversight

Based on regulatory guidance and research:

1. **Competence**: Humans must understand system capabilities, limitations, and proper use
2. **Authority**: Power to override AI recommendations without penalty
3. **Explainability**: AI must provide clear rationale for recommendations
4. **Contextual Awareness**: System recognizes outliers and edge cases
5. **Bias Monitoring**: Continuous evaluation for demographic disparities
6. **Accountability Principles**:
   - Acting within duty
   - Explainability of decisions
   - Necessity and proportionality
   - Complete record-keeping
   - Clear redress mechanisms
   - Independent oversight

### Risk Areas Requiring Mitigation

**Automation Bias**
- Risk: Adjudicators over-rely on AI recommendations without critical review
- Mitigation: Training, UI design showing confidence levels, mandatory review of edge cases

**Selective Adherence**
- Risk: Adjudicators cherry-pick AI advice, accepting favorable recommendations while ignoring unfavorable
- Mitigation: Require documentation when overriding AI, pattern monitoring

**False Sense of Security**
- Risk: HITL becomes "rubber stamping" without addressing underlying algorithmic concerns
- Mitigation: Meaningful review requirements, performance monitoring, regular audits

**Bias Amplification**
- Risk: Historical biases in training data perpetuate or worsen discrimination
- Mitigation: Fairness testing, diverse training data, demographic impact analysis

---

## Platform Evaluation Framework

### Category 1: Code-First Frameworks

**Best for**: Custom government solutions requiring full control and auditability

| Platform | Strengths for Gov | Considerations | FedRAMP Status |
|----------|------------------|----------------|----------------|
| **LangChain + LangGraph** | Extensive tooling, strong community, LangSmith observability | Requires dev team, complex deployment | Via cloud providers |
| **LlamaIndex** | Strong retrieval capabilities, works with secure local models | Data pipeline complexity | Via cloud providers |
| **Semantic Kernel** | .NET integration (common in gov), Microsoft ecosystem | Newer, smaller community | Azure (Microsoft FedRAMP) |
| **Haystack** | Production-focused, strong pipeline management | Smaller ecosystem than LangChain | Via cloud providers |
| **AutoGen / CrewAI** | Multi-agent coordination, useful for complex workflows | Still emerging, less battle-tested | Via cloud providers |

**Implementation Considerations**:
- All require significant development resources
- Full control over data flow and decision logic
- Can integrate with legacy government systems
- Require separate hosting and security infrastructure
- Best for agencies with strong technical teams

**Recommended Use**: Custom applications requiring unique workflows, legacy system integration, or on-premises deployment

---

### Category 2: Enterprise Cloud Platforms (FedRAMP Authorized)

**Best for**: Agencies needing rapid deployment with built-in compliance

| Platform | Key Features | Government Clients | FedRAMP Level |
|----------|-------------|-------------------|---------------|
| **Google Vertex AI** | 200+ models, agent development kit, multi-agent environments | NYC MTA (operations optimization) | FedRAMP Authorized |
| **Azure AI Studio** | Microsoft ecosystem, .NET integration, orchestration tools | UC Riverside (data analytics), many federal agencies | FedRAMP High |
| **AWS Bedrock Agents** | AWS integration, choice of models, tool-calling APIs | Multiple federal agencies | FedRAMP High |
| **IBM watsonx** | Enterprise focus, governance tools, explainability features | Various government healthcare | FedRAMP Authorized |
| **Palantir Foundry** | Used by CMS ($210M fraud detection), strong data integration | CMS, VA, multiple agencies | FedRAMP High |

**Key Advantages**:
- Pre-certified security and compliance
- Built-in audit trails and governance
- Enterprise support and SLAs
- Integration with existing cloud infrastructure
- Observability and monitoring included

**Recommended Use**: Federal agencies or large state programs requiring enterprise-grade solutions with immediate compliance

---

### Category 3: Low-Code/No-Code Government Solutions

**Best for**: Departments with limited technical resources or rapid prototyping

| Platform | Government Features | Use Cases | Compliance |
|----------|-------------------|-----------|-----------|
| **Salesforce Government Cloud** | Claims adjudication agents, case management | Pitched for benefits backlog processing | FedRAMP Authorized |
| **ServiceNow Government Platform** | AI chatbots, predictive case routing, workflow automation | 87% of 250 cities planning/piloting | FedRAMP High |
| **Appian** | Low-code workflow, case management, AI integration | Government process automation | FedRAMP In-Process |
| **Google Dialogflow (Gov)** | Conversational AI, citizen services | Building permits, information requests | FedRAMP via Google Cloud |
| **Microsoft Power Platform (GCC)** | Copilot agents, workflow automation, integration with Office 365 | Various government departments | FedRAMP High |

**Real Government Examples**:
- **Building permits**: Municipalities reduced call center volume dramatically, cut time seeking permit information by 50%
- **CBP Translate**: Customs agents communicate with non-English speakers
- **Citizen services**: 24/7 automated assessment with human escalation

**Limitations**:
- Less customization than code-first approaches
- Vendor lock-in considerations
- May not handle complex legacy integrations
- Platform-specific limitations on data handling

**Recommended Use**: Citizen-facing services, standard workflows, rapid pilots, departments without large dev teams

---

### Category 4: Specialized Decision Support Platforms

**Best for**: Benefits-specific or healthcare claims processing

| Platform/Approach | Specialization | Key Features | Adoption |
|------------------|---------------|--------------|----------|
| **Healthcare Claims AI** (Innovaccer, etc.) | Healthcare benefits | Patient data consolidation, risk flagging, social determinants | Growing in Medicare/Medicaid |
| **Insurance Claims Platforms** (adaptable) | Claims adjudication patterns | 200% ROI documented, 3-second claim settlement (Lemonade) | Private sector, adaptable to public |
| **Custom SSA-style Systems** | Disability/benefits specific | Predictive models, case prioritization, evidence gathering | SSA QDD program |
| **Fraud Detection Platforms** | Benefits fraud | Pattern recognition, anomaly detection, investigator support | CMS, various state programs |

**Key Differentiators**:
- Domain-specific models trained on claims/benefits data
- Pre-built workflows for common adjudication scenarios
- Integration with medical/benefits databases
- Fraud detection capabilities

**Recommended Use**: Large-scale benefits programs (disability, unemployment, healthcare) requiring specialized domain knowledge

---

## Evaluation Criteria for Benefits Adjudication

### Technical Requirements

**Must-Have**:
- [ ] FedRAMP Moderate or High authorization (federal) OR SOC 2 Type II (state/local)
- [ ] Explainable AI with decision rationale
- [ ] Complete audit trails (all decisions, overrides, data access)
- [ ] Human-in-the-loop workflow support
- [ ] Role-based access control (RBAC)
- [ ] PII/PHI protection and encryption at rest/in transit
- [ ] Integration capabilities with existing case management systems

**Highly Desired**:
- [ ] Bias detection and fairness monitoring
- [ ] Multi-language support
- [ ] Accessibility compliance (Section 508)
- [ ] On-premises or government cloud deployment options
- [ ] API for legacy system integration
- [ ] Real-time performance monitoring
- [ ] Confidence scoring for AI recommendations

### Operational Requirements

**Performance Metrics**:
- Processing time reduction target (e.g., 25 min → 3 min)
- Accuracy/error rate thresholds
- Case volume capacity
- Response time for citizen inquiries
- System uptime requirements (99.9%+)

**Cost Considerations**:
- Licensing model (per user, per case, per API call)
- Infrastructure costs (cloud vs. on-prem)
- Training and change management costs
- Ongoing maintenance and support
- Expected ROI timeline (typically 12-24 months)

**Change Management**:
- Adjudicator training requirements
- Public communication strategy
- Stakeholder buy-in (unions, advocacy groups)
- Phased rollout vs. full deployment
- Success metrics and KPIs

### Risk Assessment

| Risk Category | Mitigation Strategies |
|--------------|----------------------|
| **Algorithmic Bias** | Fairness testing, diverse training data, demographic impact analysis, regular audits |
| **Data Privacy Breach** | Encryption, access controls, FedRAMP compliance, regular penetration testing |
| **Automation Bias** | Training programs, UI showing confidence levels, mandatory review protocols |
| **System Downtime** | Failover procedures, manual process backup, 99.9%+ uptime SLA |
| **Public Trust** | Transparency about AI use, clear appeals process, human final decision-maker |
| **Legal/Regulatory** | Legal review, compliance monitoring, documented decision rationale |
| **Vendor Lock-in** | Open standards, data portability, exit strategy in contract |

---

## Implementation Roadmap

### Phase 1: Foundation (Months 1-3)

**Research & Assessment**
- [ ] Document current adjudication process and pain points
- [ ] Identify specific use cases (fraud detection, case prioritization, document extraction, etc.)
- [ ] Assess data quality and availability
- [ ] Review legal and regulatory requirements
- [ ] Engage stakeholders (adjudicators, unions, advocacy groups, legal)

**Pilot Selection**
- [ ] Choose 2-3 platforms from different categories for evaluation
- [ ] Define success metrics (processing time, accuracy, user satisfaction)
- [ ] Identify low-risk pilot use case (e.g., document classification, not final decisions)
- [ ] Establish evaluation criteria and timeline

### Phase 2: Pilot (Months 4-9)

**Small-Scale Implementation**
- [ ] Deploy pilot with 5-10 adjudicators on limited case types
- [ ] Implement robust HITL oversight
- [ ] Collect quantitative metrics (time, accuracy, volume)
- [ ] Gather qualitative feedback (adjudicator experience, trust levels)
- [ ] Monitor for bias or fairness issues
- [ ] Document all decisions and overrides

**Evaluation**
- [ ] Compare pilot results to baseline performance
- [ ] Assess ROI potential
- [ ] Identify issues and refinements needed
- [ ] Review compliance and audit trails
- [ ] Make go/no-go decision for expansion

### Phase 3: Scaling (Months 10-18)

**Phased Rollout**
- [ ] Expand to additional adjudicators and case types
- [ ] Implement comprehensive training program
- [ ] Establish ongoing monitoring and evaluation
- [ ] Set up feedback loops for continuous improvement
- [ ] Develop public communication materials
- [ ] Create appeals and redress procedures

**Optimization**
- [ ] Fine-tune models based on real-world performance
- [ ] Automate low-stakes decisions where appropriate
- [ ] Integrate with additional data sources
- [ ] Expand to additional benefit types or programs

### Phase 4: Maturity (Months 19+)

**Full Production**
- [ ] System handles majority of case volume with appropriate oversight
- [ ] Continuous bias and fairness monitoring
- [ ] Regular model retraining and updates
- [ ] Performance reporting to stakeholders
- [ ] Knowledge sharing with other agencies

---

## Platform Recommendations by Scenario

### Scenario 1: Federal Agency, Large Volume (e.g., SSA-scale)

**Recommended Approach**: Custom code-first solution with enterprise cloud infrastructure

**Platform Stack**:
- **Core**: LangChain + LangGraph for orchestration
- **Infrastructure**: Azure AI Studio or AWS Bedrock (FedRAMP High)
- **Observability**: LangSmith or Azure Monitor
- **Data**: Vector DB (Pinecone/Weaviate on FedRAMP cloud) + existing case management integration

**Rationale**:
- Scale requirements demand custom solution
- Full control over decision logic for auditability
- Can integrate with complex legacy systems
- Justify investment with volume

**Estimated Investment**: $2M-5M initial, $500K-1M annual
**Timeline**: 12-18 months to production
**ROI**: 18-24 months based on processing time reduction

---

### Scenario 2: State Benefits Agency, Moderate Volume

**Recommended Approach**: Enterprise low-code platform

**Platform Stack**:
- **Option A**: Salesforce Government Cloud (if already using Salesforce)
- **Option B**: ServiceNow Government Platform + AI module
- **Option C**: Microsoft Power Platform (if Microsoft shop)

**Rationale**:
- Faster time to value (6-9 months)
- Built-in compliance and security
- Lower technical resource requirements
- Pre-built case management workflows

**Estimated Investment**: $500K-1.5M initial, $200K-400K annual
**Timeline**: 6-9 months to production
**ROI**: 12-18 months

---

### Scenario 3: Municipal Benefits/Permits, Smaller Scale

**Recommended Approach**: No-code SaaS with citizen-facing chatbot

**Platform Stack**:
- **Citizen Interface**: Google Dialogflow or Microsoft Bot Framework
- **Workflow**: Low-code platform (Appian, ServiceNow, or Power Platform)
- **Simple cases**: Automated with escalation thresholds
- **Complex cases**: Route to human adjudicators

**Rationale**:
- Limited technical resources
- Focus on citizen experience improvement
- Rapid deployment (3-6 months)
- Lower investment threshold

**Estimated Investment**: $100K-300K initial, $50K-100K annual
**Timeline**: 3-6 months to production
**ROI**: 6-12 months

---

### Scenario 4: Research/Pilot Project

**Recommended Approach**: Multiple parallel evaluations

**Platform Stack**:
- **Code prototype**: LangChain + OpenAI on Azure (FedRAMP) - test custom logic
- **Low-code prototype**: ServiceNow or Salesforce trial - test ease of use
- **Specialized**: Domain-specific platform if available (healthcare claims, etc.)

**Rationale**:
- De-risk platform selection
- Learn organizational readiness
- Build stakeholder buy-in
- Identify optimal approach before major investment

**Estimated Investment**: $50K-200K for 6-month pilot
**Timeline**: 3-6 months evaluation
**Decision Point**: Choose path forward based on results

---

## Emerging Trends & Future Considerations

### Multi-Agent Systems (2025-2026)

**Current State**:
- Google Vertex AI offers agent development kit for multi-agent environments
- AutoGen and CrewAI enable agent coordination
- Growing use in complex government workflows

**Potential for Benefits Adjudication**:
- **Document Agent**: Extracts and verifies information from submissions
- **Evidence Agent**: Gathers supporting documentation from databases
- **Policy Agent**: Interprets regulations and eligibility criteria
- **Fraud Agent**: Checks for inconsistencies and red flags
- **Recommendation Agent**: Synthesizes inputs and provides decision rationale
- **Human Supervisor**: Reviews flagged cases and makes final determinations

**Timeline**: Experimental now, production-ready in 1-2 years for government use

### Autonomous Agents (Caution Advised)

**Industry Hype**: Salesforce and others pitching "autonomous" agents for government backlog processing

**Reality Check**:
- Definition of "AI agent" varies widely in autonomy levels
- No FedRAMP-authorized platforms currently offer fully autonomous decision-making for high-stakes cases
- Regulatory frameworks (NY LOADinG Act, etc.) restrict automated decisions in public assistance
- Human oversight remains mandatory for rights-impacting decisions

**Recommendation**: Focus on "decision support" and "automation with human oversight" rather than autonomous agents for benefits adjudication

### Explainable AI Advances

**Trend**: Moving beyond black-box models to interpretable AI
- LIME (Local Interpretable Model-Agnostic Explanations)
- SHAP (SHapley Additive exPlanations)
- Attention visualization for transformer models
- Natural language explanations of decisions

**Government Application**:
- Required for appeals and legal challenges
- Builds public trust
- Helps adjudicators understand and validate AI recommendations
- Supports bias detection and fairness monitoring

---

## Critical Success Factors

Based on current research and government implementations:

1. **Start with Human-in-the-Loop**: Do not attempt fully autonomous decisions in benefits adjudication
2. **Prioritize Explainability**: Choose platforms that provide clear decision rationale
3. **Ensure Compliance First**: FedRAMP/SOC2 before functionality
4. **Pilot Before Scaling**: Start with low-risk use cases (document classification, fraud flagging)
5. **Train Extensively**: Adjudicators must understand AI capabilities and limitations
6. **Monitor for Bias**: Continuous evaluation of demographic impacts
7. **Maintain Audit Trails**: Complete logging for compliance and appeals
8. **Plan for Appeals**: Clear process for challenging AI-supported decisions
9. **Communicate Transparently**: Public understanding of AI role builds trust
10. **Measure Rigorously**: Track processing time, accuracy, fairness, cost, and satisfaction

---

## Key Questions to Answer Before Selecting Platform

### Strategic Questions
1. What is the primary goal? (Reduce backlog, improve accuracy, detect fraud, enhance citizen experience?)
2. What is our risk tolerance for AI in decision-making?
3. What level of human oversight is appropriate for different case types?
4. What is our timeline for deployment? (6 months vs. 2 years changes platform choice)
5. What is our budget? (Initial investment and ongoing costs)

### Technical Questions
1. What is our current technical capacity? (Dev team size, skills, infrastructure)
2. What systems must the AI integrate with? (Case management, databases, identity verification)
3. What is our data quality and availability? (AI requires good training data)
4. What are our compliance requirements? (Federal = FedRAMP; State varies)
5. What is our preferred deployment model? (Cloud, on-prem, hybrid)

### Organizational Questions
1. What is stakeholder readiness? (Adjudicators, unions, advocacy groups, leadership)
2. What is our change management capacity?
3. What training resources can we commit?
4. How will we measure success?
5. What is our communication strategy for the public?

---

## Additional Resources & Case Studies

### Government AI Resources
- [Federal AI Use Case Inventory 2024 - CIO.gov](https://www.cio.gov/ai-in-action/)
- [Administrative Conference of the United States - AI Resources](https://www.acus.gov/ai)
- [Roosevelt Institute - AI and Government Workers Report](https://rooseveltinstitute.org/publications/ai-and-government-workers/)
- [IBM - AI in Government Use Cases](https://www.ibm.com/think/topics/ai-in-government)

### Compliance & Frameworks
- [FedRAMP vs SOC 2 Comparison - SAP NS2](https://sapns2.com/fedramp-and-soc-2-whats-the-big-difference/)
- [FedRAMP for AI - Microsoft Guide](https://techcommunity.microsoft.com/blog/publicsectorblog/why-fedramp-adherence-matters-for-ai-in-government%E2%80%94and-how-microsoft-makes-it-pr/4448008)
- [Human-in-the-Loop AI Compliance](https://hoop.dev/blog/how-to-keep-human-in-the-loop-ai-control-fedramp-ai-compliance-secure-and-compliant-with-action-level-approvals/)

### Academic Research
- [AI in Adjudication and Administration - Coglianese & Ben Dor](https://scholarship.law.upenn.edu/faculty_scholarship/2118/)
- [Human-AI Interactions in Public Sector Decision Making - Oxford Academic](https://academic.oup.com/jpart/article/33/1/153/6524536)
- [Algorithmic Adjudication and Constitutional AI](https://scholar.smu.edu/scitech/vol27/iss1/3/)
- [Bridging the Gap: AI-Driven Decision-Making in Public Sector](https://www.sciencedirect.com/science/article/pii/S0740624X24000686)

### Platform-Specific Case Studies
- [Salesforce AI Agents in Government](https://www.salesforce.com/government/ai/)
- [Google AI for Government - PwC Report](https://www.pwc.com/gx/en/services/alliances/google/ai-for-gov-digital-sprinters.html)
- [Flowable - AI Agents in Public Sector](https://www.flowable.com/blog/business/ai-agents-public-sector-government-use-cases)
- [BCG - Benefits of AI in Government 2025](https://www.bcg.com/publications/2025/benefits-of-ai-in-government)

### ROI & Performance Data
- [AI Claims Processing ROI](https://news.designrush.com/ai-insurance-claims-200-roi-voltaire) (200% ROI in private sector)
- [Capita Benefits Automation](https://www.capita.com/expertise/government-services/local-government-services/benefits-automation-software) (25 min → 3 min processing)
- [Route Fifty - AI Agents Transformation Guide](https://www.route-fifty.com/artificial-intelligence/2025/06/ai-agents-government-transformation-guide-state-and-local-agencies/406269/)

---

## Conclusion & Next Steps

The AI agent landscape for government benefits adjudication is rapidly maturing, with proven use cases, regulatory frameworks, and compliant platforms available. However, the technology is not yet suitable for fully autonomous decision-making in high-stakes benefits adjudication.

**Recommended Immediate Actions**:

1. **Define Use Case**: Identify specific adjudication pain points (backlog, fraud, processing time, accuracy)
2. **Assess Readiness**: Evaluate technical capacity, data quality, stakeholder buy-in, and budget
3. **Select Pilot Approach**: Choose platform category based on scenario (see recommendations above)
4. **Establish Governance**: Define human oversight model, success metrics, and risk mitigation
5. **Engage Stakeholders**: Build coalition of adjudicators, legal, IT, privacy, and advocacy groups
6. **Start Small**: Pilot with low-risk use case before tackling final adjudication decisions

The evidence is clear: AI can significantly improve benefits adjudication speed and quality when implemented with appropriate human oversight, explainability, and safeguards. Success requires thoughtful platform selection, strong governance, and commitment to continuous monitoring for fairness and accuracy.

---

*Last Updated: November 2025*
*Research compiled from government case studies, academic research, and industry analysis*
