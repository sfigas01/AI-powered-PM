#!/bin/bash

# Script to create all user stories in Azure DevOps
# Feature IDs: F1=5, F2=6, F3=7, F4=8, F5=9, F6=10

PAT="${AZURE_DEVOPS_PAT}"
ORG_URL="https://dev.azure.com/stephaniefigas/Steph%20Learning%20environment"

# Function to create a user story
create_story() {
    local title="$1"
    local description="$2"
    local acceptance_criteria="$3"
    local story_points="$4"
    local parent_feature_id="$5"

    curl -u :${PAT} \
      "${ORG_URL}/_apis/wit/workitems/\$User%20Story?api-version=7.0" \
      -X POST \
      -H "Content-Type: application/json-patch+json" \
      -s \
      -d "[
        {
          \"op\": \"add\",
          \"path\": \"/fields/System.Title\",
          \"value\": \"${title}\"
        },
        {
          \"op\": \"add\",
          \"path\": \"/fields/System.Description\",
          \"value\": \"${description}<br/><br/><strong>Acceptance Criteria:</strong><br/>${acceptance_criteria}\"
        },
        {
          \"op\": \"add\",
          \"path\": \"/fields/System.State\",
          \"value\": \"New\"
        },
        {
          \"op\": \"add\",
          \"path\": \"/fields/Microsoft.VSTS.Scheduling.StoryPoints\",
          \"value\": ${story_points}
        },
        {
          \"op\": \"add\",
          \"path\": \"/relations/-\",
          \"value\": {
            \"rel\": \"System.LinkTypes.Hierarchy-Reverse\",
            \"url\": \"https://dev.azure.com/stephaniefigas/_apis/wit/workItems/${parent_feature_id}\"
          }
        }
      ]" | jq -r '.id'
}

echo "Creating F1 stories..."

# F1.1
create_story \
  "F1.1: Conduct Citizen Persona Research (EI Claimants)" \
  "<strong>As an</strong> innovation researcher<br/><strong>I want to</strong> conduct in-depth interviews with EI claimants<br/><strong>So that</strong> we understand their needs, pain points, and receptiveness to AI voice service" \
  "Recruit 15-20 EI claimants representing diverse demographics<br/>Conduct 45-60 minute semi-structured interviews<br/>Record, transcribe, and thematically code all interviews<br/>Create 3-5 detailed persona documents with user journeys<br/>Identify top 5 jobs to be done for EI callers<br/>Document receptiveness score<br/>Deliver research summary report" \
  8 \
  5

echo "Created story F1.1"
sleep 2

# F1.2
create_story \
  "F1.2: Conduct Citizen Persona Research (OAS/GIS Seniors)" \
  "<strong>As an</strong> innovation researcher<br/><strong>I want to</strong> conduct in-depth interviews with OAS/GIS beneficiaries (seniors)<br/><strong>So that</strong> we understand senior-specific needs, accessibility requirements, and concerns about AI" \
  "Recruit 15-20 seniors (65+) representing diverse backgrounds<br/>Conduct 45-60 minute interviews with optional family member present<br/>Include accessibility expert in interview analysis<br/>Create 3-5 senior-specific personas with accessibility profiles<br/>Document critical accessibility requirements<br/>Assess elder abuse risk detection needs<br/>Deliver research summary with senior design recommendations" \
  8 \
  5

echo "Created story F1.2"
sleep 2

# F1.3
create_story \
  "F1.3: Conduct Call Centre Agent Research" \
  "<strong>As an</strong> innovation researcher<br/><strong>I want to</strong> interview call centre agents (both EI and OAS)<br/><strong>So that</strong> we understand agent pain points, workflow needs, and concerns about AI impact on jobs" \
  "Recruit 10-15 agents representing different experience levels<br/>Conduct 45-minute interviews covering routine vs complex calls<br/>Conduct 2-3 shadowing sessions observing live calls<br/>Document top 10 routine call types suitable for AI deflection<br/>Identify agent workflow pain points AI could alleviate<br/>Assess union concerns and job security fears<br/>Deliver research summary with agent impact recommendations" \
  8 \
  5

echo "Created story F1.3"
sleep 2

# F1.4
create_story \
  "F1.4: Analyze Call Centre Data &amp; Transcripts" \
  "<strong>As a</strong> data analyst<br/><strong>I want to</strong> analyze existing call centre data and transcripts<br/><strong>So that</strong> we quantify call volumes, types, duration, and identify patterns suitable for AI" \
  "Obtain 3-6 months of call centre data (both EI and OAS)<br/>Analyze sample of 200+ call transcripts or recordings<br/>Create call type taxonomy with volume estimates<br/>Calculate % of calls suitable for AI deflection (target: 65-75%)<br/>Identify peak volume periods requiring AI scalability<br/>Deliver quantitative analysis report with AI opportunity sizing" \
  5 \
  5

echo "Created story F1.4"
sleep 2

# F1.5
create_story \
  "F1.5: Prototype &amp; User Testing - AI Voice Interaction (Wizard of Oz)" \
  "<strong>As a</strong> UX researcher<br/><strong>I want to</strong> conduct Wizard of Oz testing with citizens<br/><strong>So that</strong> we validate AI interaction design before technical build" \
  "Design 3-5 common call scenarios<br/>Create Wizard of Oz testing protocol<br/>Recruit 20-25 test participants (mix of EI claimants and seniors)<br/>Conduct simulated AI calls and observe user behavior<br/>Iterate interaction scripts based on feedback (minimum 2 rounds)<br/>Measure task completion rates and user satisfaction<br/>Document critical design requirements<br/>Deliver UX research report with validated interaction scripts" \
  13 \
  5

echo "Created story F1.5"
sleep 2

# F1.6
create_story \
  "F1.6: Competitive Analysis - AI Voice Agents in Government" \
  "<strong>As a</strong> market researcher<br/><strong>I want to</strong> analyze other government AI voice agent implementations<br/><strong>So that</strong> we learn from precedents and avoid common pitfalls" \
  "Research 5-10 government AI voice agent case studies<br/>Analyze use cases, success metrics, citizen satisfaction<br/>Interview 2-3 peer government contacts if possible<br/>Document lessons learned and best practices<br/>Identify risks to avoid based on precedents<br/>Deliver competitive analysis report with recommendations" \
  5 \
  5

echo "Created all F1 stories"
echo ""
echo "Creating F2 stories..."
sleep 2

# F2.1
create_story \
  "F2.1: Build Financial Model - Costs &amp; Savings" \
  "<strong>As a</strong> business analyst<br/><strong>I want to</strong> develop a detailed financial model<br/><strong>So that</strong> we can justify the investment and prove ROI" \
  "Document all one-time implementation costs<br/>Document all annual recurring costs<br/>Calculate projected savings (FTE redeployment, avoided hiring, error reduction)<br/>Build 5-year financial model with sensitivity analysis<br/>Calculate payback period, NPV, and ROI<br/>Deliver financial model spreadsheet and executive summary" \
  8 \
  6

echo "Created story F2.1"
sleep 2

# F2.2
create_story \
  "F2.2: Quantify Business Impact - Service Standards &amp; Citizen Outcomes" \
  "<strong>As a</strong> business analyst<br/><strong>I want to</strong> quantify non-financial business value<br/><strong>So that</strong> we demonstrate impact beyond cost savings" \
  "Model impact on service standards (current 58-65% to target 80-85%)<br/>Model citizen satisfaction improvement<br/>Quantify error reduction impact<br/>Assess agent satisfaction and retention impact<br/>Estimate political/reputational value<br/>Deliver business impact quantification report" \
  5 \
  6

echo "Created story F2.2"
sleep 2

# F2.3
create_story \
  "F2.3: Stakeholder Alignment - Executive &amp; Union Buy-In" \
  "<strong>As a</strong> stakeholder engagement lead<br/><strong>I want to</strong> secure executive and union support<br/><strong>So that</strong> we have organizational buy-in before proceeding" \
  "Conduct executive stakeholder interviews<br/>Present business case to executives and gather feedback<br/>Document executive concerns and requirements<br/>Conduct union engagement sessions with PSAC leadership<br/>Co-design pilot approach with union representatives<br/>Secure agreement on no-layoff commitment<br/>Obtain formal executive approval to proceed<br/>Deliver stakeholder alignment report with approval documentation" \
  8 \
  6

echo "Created all F2 stories"
echo ""
echo "Creating F3 stories..."
sleep 2

# F3.1
create_story \
  "F3.1: Technical Discovery - Legacy System Integration Assessment" \
  "<strong>As a</strong> technical architect<br/><strong>I want to</strong> assess integration feasibility with legacy systems<br/><strong>So that</strong> we understand technical constraints and risks" \
  "Conduct technical interviews with IT teams (EI mainframe, OAS database, telephony, CRM)<br/>Document current system capabilities and APIs<br/>Identify integration constraints and limitations<br/>Assess data quality and completeness<br/>Document technical risks and mitigation strategies<br/>Deliver technical integration assessment report" \
  8 \
  7

echo "Created story F3.1"
sleep 2

# F3.2
create_story \
  "F3.2: AI Platform Vendor Assessment &amp; RFI" \
  "<strong>As a</strong> technical lead<br/><strong>I want to</strong> evaluate AI platform vendors<br/><strong>So that</strong> we select the right technology partner" \
  "Define technical requirements for AI platform<br/>Issue RFI to 5-8 AI vendors<br/>Evaluate vendor responses on capability, experience, compliance, pricing<br/>Conduct 2-3 vendor demos with technical team<br/>Create vendor comparison scorecard<br/>Deliver vendor recommendation report with 1-2 preferred partners" \
  8 \
  7

echo "Created story F3.2"
sleep 2

# F3.3
create_story \
  "F3.3: Proof of Concept - AI Voice Integration Test" \
  "<strong>As a</strong> technical architect<br/><strong>I want to</strong> build a limited proof of concept<br/><strong>So that</strong> we validate technical integration is possible" \
  "Set up sandbox environment with test data<br/>Integrate preferred AI platform with sandbox<br/>Test end-to-end call flow (authentication, data retrieval, voice response)<br/>Measure performance (response latency, data retrieval time, voice quality)<br/>Document technical challenges encountered<br/>Deliver PoC demonstration and technical findings report" \
  13 \
  7

echo "Created story F3.3"
sleep 2

# F3.4
create_story \
  "F3.4: Data Requirements &amp; Quality Assessment" \
  "<strong>As a</strong> data analyst<br/><strong>I want to</strong> assess data availability and quality<br/><strong>So that</strong> we ensure AI can access accurate, real-time information" \
  "Inventory required data elements<br/>Assess data quality for each source (completeness, accuracy, timeliness)<br/>Document data gaps and quality issues<br/>Define data governance requirements<br/>Identify data remediation work needed before AI launch<br/>Deliver data requirements and quality assessment report" \
  5 \
  7

echo "Created all F3 stories"
echo ""
echo "Creating F4 stories..."
sleep 2

# F4.1
create_story \
  "F4.1: Responsible AI Assessment - Algorithmic Bias &amp; Fairness" \
  "<strong>As a</strong> responsible AI analyst<br/><strong>I want to</strong> assess algorithmic bias and fairness risks<br/><strong>So that</strong> we ensure equitable service for all citizen groups" \
  "Review Treasury Board Directive on Automated Decision-Making<br/>Conduct Algorithmic Impact Assessment (AIA)<br/>Test AI for bias across demographics (language, age, disability)<br/>Define fairness metrics and monitoring approach<br/>Establish AI ethics review board composition<br/>Document transparency requirements<br/>Deliver Responsible AI Assessment report with AIA documentation" \
  13 \
  8

echo "Created story F4.1"
sleep 2

# F4.2
create_story \
  "F4.2: Privacy Impact Assessment (PIA)" \
  "<strong>As a</strong> privacy analyst<br/><strong>I want to</strong> conduct a Privacy Impact Assessment<br/><strong>So that</strong> we comply with Privacy Act and protect citizen PII" \
  "Document data flows (collection, transmission, storage, access, retention)<br/>Assess privacy risks (breach, unauthorized access, PII in training data)<br/>Define privacy controls and mitigation (encryption, SIN redaction, RBAC)<br/>Engage Office of Privacy Commissioner for review<br/>Address Privacy Commissioner feedback<br/>Deliver completed PIA with approval documentation" \
  8 \
  8

echo "Created story F4.2"
sleep 2

# F4.3
create_story \
  "F4.3: Security Assessment &amp; Authorization (SA&amp;A)" \
  "<strong>As a</strong> security analyst<br/><strong>I want to</strong> conduct Security Assessment and Authorization<br/><strong>So that</strong> we meet Government of Canada security standards" \
  "Classify data sensitivity (Protected B)<br/>Conduct Threat and Risk Assessment (TRA)<br/>Document security controls (MFA, encryption, network security, audit logging)<br/>Conduct penetration testing in sandbox<br/>Engage departmental security team for SA&amp;A review<br/>Obtain Security Authorization to Operate (ATO)<br/>Deliver SA&amp;A documentation with ATO approval" \
  8 \
  8

echo "Created story F4.3"
sleep 2

# F4.4
create_story \
  "F4.4: Legal &amp; Regulatory Compliance Analysis" \
  "<strong>As a</strong> legal/compliance analyst<br/><strong>I want to</strong> assess all legal and regulatory requirements<br/><strong>So that</strong> we ensure full compliance before launch" \
  "Analyze Official Languages Act compliance<br/>Analyze accessibility compliance (AODA, WCAG 2.1 AA)<br/>Review EI Act and OAS Act for AI authority and limitations<br/>Assess liability and accountability framework<br/>Engage legal counsel for review and sign-off<br/>Deliver legal compliance analysis report with counsel approval" \
  5 \
  8

echo "Created all F4 stories"
echo ""
echo "Creating F5 stories..."
sleep 2

# F5.1
create_story \
  "F5.1: Enterprise Architecture Design" \
  "<strong>As an</strong> enterprise architect<br/><strong>I want to</strong> design the target architecture for enterprise-wide AI voice<br/><strong>So that</strong> solution train has a clear blueprint to build from" \
  "Design high-level solution architecture (AI platform, integration, data, security, monitoring layers)<br/>Create architecture diagrams (logical and physical)<br/>Document technology stack and components<br/>Define scalability and high availability approach<br/>Identify reusability for other ServiceX programs<br/>Align with enterprise architecture standards<br/>Deliver enterprise architecture design document" \
  8 \
  9

echo "Created story F5.1"
sleep 2

# F5.2
create_story \
  "F5.2: Change Management &amp; Agent Redeployment Planning" \
  "<strong>As a</strong> change management lead<br/><strong>I want to</strong> develop a comprehensive change management plan<br/><strong>So that</strong> agents and stakeholders are prepared for AI adoption" \
  "Conduct change impact assessment<br/>Design agent redeployment strategy (complex cases, AI training, QA, proactive outreach)<br/>Develop training program and curriculum<br/>Design communication plan (executives, agents, union, citizens)<br/>Define success metrics for change adoption<br/>Deliver change management plan with training curriculum" \
  13 \
  9

echo "Created story F5.2"
sleep 2

# F5.3
create_story \
  "F5.3: Operational Readiness Assessment" \
  "<strong>As an</strong> operations lead<br/><strong>I want to</strong> assess operational readiness for AI launch<br/><strong>So that</strong> we identify gaps and prepare operations teams" \
  "Assess call centre operational readiness<br/>Assess IT operational readiness (24/7 support, incident response)<br/>Define service level agreements (uptime, latency, accuracy)<br/>Identify operational gaps and remediation plan<br/>Define pilot vs production operations differences<br/>Deliver operational readiness assessment and gap closure plan" \
  8 \
  9

echo "Created story F5.3"
sleep 2

# F5.4
create_story \
  "F5.4: Monitoring &amp; Performance Dashboard Design" \
  "<strong>As a</strong> data analyst<br/><strong>I want to</strong> design monitoring dashboards and KPIs<br/><strong>So that</strong> we can track AI performance and identify issues" \
  "Define key performance indicators (primary, secondary, compliance metrics)<br/>Design real-time monitoring dashboard<br/>Design executive reporting dashboard<br/>Define alerting thresholds and escalation protocols<br/>Create wireframes/mockups of dashboards<br/>Deliver dashboard design specification and KPI documentation" \
  5 \
  9

echo "Created all F5 stories"
echo ""
echo "Creating F6 stories..."
sleep 2

# F6.1
create_story \
  "F6.1: Product Requirements Document (PRD) Development" \
  "<strong>As a</strong> product manager<br/><strong>I want to</strong> synthesize all research into a comprehensive PRD<br/><strong>So that</strong> solution train has clear requirements to build from" \
  "Compile PRD with all sections (executive summary, business case, user research, functional/non-functional requirements, architecture, governance, KPIs, pilot plan, risks)<br/>Include appendices (research reports, financial model, technical assessments, compliance docs)<br/>Review PRD with executive stakeholders<br/>Incorporate feedback and finalize<br/>Deliver final PRD (v1.0) to solution train" \
  13 \
  10

echo "Created story F6.1"
sleep 2

# F6.2
create_story \
  "F6.2: Business Case Finalization &amp; Executive Approval" \
  "<strong>As a</strong> business analyst<br/><strong>I want to</strong> finalize the business case for executive sign-off<br/><strong>So that</strong> we have budget approval to proceed" \
  "Compile executive business case document<br/>Prepare executive presentation<br/>Present to executive decision-making committee<br/>Address executive questions and concerns<br/>Obtain formal budget approval (signed authorization)<br/>Deliver approved business case with budget authorization" \
  5 \
  10

echo "Created story F6.2"
sleep 2

# F6.3
create_story \
  "F6.3: Solution Train Handoff &amp; Knowledge Transfer" \
  "<strong>As a</strong> product manager<br/><strong>I want to</strong> conduct formal handoff to solution train<br/><strong>So that</strong> they can begin build with full context" \
  "Schedule handoff sessions with solution train teams<br/>Deliver all handoff artifacts (PRD, business case, research reports, financial model, architecture, compliance docs)<br/>Conduct Q&amp;A sessions<br/>Document open questions and dependencies<br/>Establish transition plan and feedback loops<br/>Obtain solution train acceptance of handoff<br/>Deliver handoff completion report" \
  3 \
  10

echo "Created all F6 stories"
echo ""
echo "All 24 stories created successfully!"
