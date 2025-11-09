#!/usr/bin/env python3
"""
Create Features in Azure DevOps for AI Voice Agent Epic
"""

import os
import json
import requests

# Configuration
ADO_PAT = os.environ.get('AZURE_DEVOPS_PAT')
ADO_ORG = "stephaniefigas"
ADO_PROJECT = "Steph Learning environment"
EPIC_ID = 2

BASE_URL = f"https://dev.azure.com/{ADO_ORG}/{ADO_PROJECT}/_apis/wit/workitems"

# Features data (F2-F6, since F1 already exists as #35)
features = [
    {
        "title": "F2: Viability Validation - Business Case & ROI",
        "description": "<strong>Outcome:</strong> Validated business case with financial model and executive buy-in",
        "acceptance_criteria": """<ul>
<li>Financial model completed with 5-year projections including all implementation costs, recurring costs, and savings</li>
<li>ROI calculated with payback period, NPV, and sensitivity analysis documented</li>
<li>Business impact quantified across all key metrics: Service standard improvement (baseline vs. projected), Citizen satisfaction improvement (baseline vs. projected), Error reduction impact (current vs. projected error rates), Agent satisfaction and retention impact</li>
<li>Non-financial value quantified (political/reputational value, MP inquiry reduction)</li>
<li>Executive stakeholder engagement completed with documented feedback from DM, ADM, Directors, and CFO</li>
<li>Union engagement completed with PSAC leadership alignment on pilot approach and no-layoff commitment</li>
<li>Formal executive approval obtained (written authorization to proceed to pilot)</li>
<li>Business case demonstrates clear ROI that justifies investment</li>
<li>Executive Director accepts business case as sufficient for budget approval</li>
</ul>""",
        "story_points": 21,
        "priority": 1
    },
    {
        "title": "F3: Feasibility Validation - Technical & Integration",
        "description": "<strong>Outcome:</strong> Validated technical architecture and integration approach",
        "acceptance_criteria": """<ul>
<li>Legacy system integration assessment completed with documented capabilities, constraints, and risks for all critical systems (EI mainframe, OAS database, telephony, CRM, identity management)</li>
<li>AI platform vendor evaluation completed with RFI responses from 5-8 vendors and comparison scorecard delivered</li>
<li>Preferred vendor recommendation provided (1-2 vendors) with supporting rationale</li>
<li>Proof of Concept demonstrated showing successful end-to-end integration: Authentication flow validated, Data retrieval from test systems confirmed, Voice interaction quality verified, Performance targets met (response latency &lt;1s, data retrieval &lt;2s), Bilingual capability validated</li>
<li>Technical risks identified with documented mitigation strategies</li>
<li>Data quality assessment completed with gaps identified and remediation plan defined</li>
<li>Data governance requirements documented (ownership, refresh schedules, retention)</li>
<li>PoC findings demonstrate technical feasibility with acceptable risk profile</li>
<li>Executive Director accepts technical approach as viable for implementation</li>
</ul>""",
        "story_points": 34,
        "priority": 1
    },
    {
        "title": "F4: Governance Analysis - Responsible AI & Compliance",
        "description": "<strong>Outcome:</strong> Complete governance framework and compliance roadmap",
        "acceptance_criteria": """<ul>
<li>Algorithmic Impact Assessment (AIA) completed per Treasury Board Directive on Automated Decision-Making with impact level determined and bias mitigation strategies documented</li>
<li>Responsible AI testing completed with documented fairness metrics across demographics (language, age, disability, gender/accent)</li>
<li>AI ethics review board composition and process defined</li>
<li>Privacy Impact Assessment (PIA) completed and approved by Office of the Privacy Commissioner with all feedback addressed</li>
<li>Security Assessment & Authorization (SA&A) completed with Security Authorization to Operate (ATO) obtained</li>
<li>Threat and Risk Assessment (TRA) completed with documented security controls and mitigation strategies</li>
<li>Legal and regulatory compliance analysis completed covering: Official Languages Act compliance approach defined, Accessibility compliance (AODA, WCAG 2.1 AA) validated, EI Act and OAS Act authority confirmed with legal counsel, Liability and accountability framework established</li>
<li>All compliance documentation approved by legal counsel (written sign-off)</li>
<li>Governance framework demonstrates full compliance with all applicable laws and regulations</li>
<li>Executive Director accepts governance approach as meeting all compliance requirements</li>
</ul>""",
        "story_points": 34,
        "priority": 1
    },
    {
        "title": "F5: Enterprise Adoption Readiness - Architecture & Change",
        "description": "<strong>Outcome:</strong> Architecture design, change management plan, and readiness assessment",
        "acceptance_criteria": """<ul>
<li>Enterprise architecture design completed with high-level solution architecture documented (AI platform, integration, data, security, monitoring layers)</li>
<li>Architecture diagrams created (logical and physical) and aligned with ESDC enterprise architecture standards</li>
<li>Scalability and high availability requirements defined (concurrent call capacity, disaster recovery)</li>
<li>Reusability approach documented for other ServiceX programs (CPP, disability)</li>
<li>Change management plan completed including: Change impact assessment across all affected roles, Agent redeployment strategy with timeline (phased over 18 months), Training program designed with curriculum and materials, Communication plan defined (executive, agent, union, citizen-facing)</li>
<li>Operational readiness assessment completed with gaps identified and remediation plan defined</li>
<li>Service Level Agreements (SLAs) defined for AI platform (uptime, latency, accuracy thresholds)</li>
<li>Monitoring dashboard design completed with KPIs defined and wireframes/mockups created</li>
<li>Change adoption success metrics established</li>
<li>Organization demonstrated readiness to adopt AI at enterprise scale</li>
<li>Executive Director accepts adoption plan as comprehensive and achievable</li>
</ul>""",
        "story_points": 34,
        "priority": 2
    },
    {
        "title": "F6: PRD Development & Solution Train Handoff",
        "description": "<strong>Outcome:</strong> Production-ready PRD, business case, and adoption plan",
        "acceptance_criteria": """<ul>
<li>Comprehensive PRD (version 1.0) completed synthesizing all research from Features 1-5 with all required sections: Executive summary, business case, and ROI; User research findings and personas; Functional and non-functional requirements; Technical architecture and integration requirements; Governance and compliance requirements; Success metrics and KPIs; Pilot plan and rollout phases; Risks and mitigation strategies</li>
<li>All appendices attached (research reports, financial model, technical assessments, PIA/SA&A, vendor recommendation)</li>
<li>PRD reviewed by executive stakeholders with feedback incorporated</li>
<li>Executive business case finalized with formal budget approval obtained (signed authorization for $2.5M one-time, $975K annual)</li>
<li>Handoff sessions completed with solution train teams (Product Owner, Technical, Governance, UX)</li>
<li>All handoff artifacts delivered to solution train (PRD, business case, research reports, architecture diagrams, compliance docs, change plan)</li>
<li>Solution train acceptance of handoff confirmed (written sign-off)</li>
<li>Transition plan established with innovation team role during build phase defined</li>
<li>PRD is production-ready and provides sufficient detail for solution train to begin implementation</li>
<li>Executive Director accepts PRD and handoff as complete</li>
</ul>""",
        "story_points": 21,
        "priority": 1
    }
]

def create_feature(feature_data):
    """Create a feature work item in Azure DevOps"""

    # First, create the feature with basic fields
    create_payload = [
        {
            "op": "add",
            "path": "/fields/System.Title",
            "value": feature_data["title"]
        },
        {
            "op": "add",
            "path": "/fields/System.Parent",
            "value": EPIC_ID
        }
    ]

    headers = {"Content-Type": "application/json-patch+json"}
    auth = ("", ADO_PAT)

    # Create feature
    response = requests.post(
        f"{BASE_URL}/$Feature?api-version=7.0",
        json=create_payload,
        headers=headers,
        auth=auth
    )

    if response.status_code not in [200, 201]:
        print(f"✗ Failed to create: {feature_data['title']}")
        print(f"  Error: {response.text}")
        return None

    feature_id = response.json()["id"]
    print(f"✓ Created Feature #{feature_id}: {feature_data['title']}")

    # Update with additional fields
    update_payload = [
        {
            "op": "add",
            "path": "/fields/System.Description",
            "value": feature_data["description"]
        },
        {
            "op": "add",
            "path": "/fields/Microsoft.VSTS.Common.AcceptanceCriteria",
            "value": feature_data["acceptance_criteria"]
        },
        {
            "op": "add",
            "path": "/fields/Microsoft.VSTS.Scheduling.StoryPoints",
            "value": feature_data["story_points"]
        },
        {
            "op": "add",
            "path": "/fields/Microsoft.VSTS.Common.Priority",
            "value": feature_data["priority"]
        }
    ]

    response = requests.patch(
        f"{BASE_URL}/{feature_id}?api-version=7.0",
        json=update_payload,
        headers=headers,
        auth=auth
    )

    if response.status_code == 200:
        print(f"  ✓ Updated with details (Story Points: {feature_data['story_points']}, Priority: {feature_data['priority']})")
    else:
        print(f"  ✗ Failed to update details: {response.text}")

    return feature_id

def main():
    if not ADO_PAT:
        print("Error: AZURE_DEVOPS_PAT environment variable not set")
        return

    print("Creating features in Azure DevOps...")
    print(f"Organization: {ADO_ORG}")
    print(f"Project: {ADO_PROJECT}")
    print(f"Parent Epic ID: {EPIC_ID}")
    print()
    print("Note: Feature F1 already exists as #35")
    print()

    created_features = []
    for feature in features:
        feature_id = create_feature(feature)
        if feature_id:
            created_features.append(feature_id)
        print()

    print("=" * 50)
    print(f"Successfully created {len(created_features)} features")
    print(f"Feature IDs: {created_features}")
    print("=" * 50)

if __name__ == "__main__":
    main()
