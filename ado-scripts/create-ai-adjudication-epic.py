#!/usr/bin/env python3
"""
Create AI-Powered Benefits Adjudication Epic in Azure DevOps
"""

import os
import requests

# Configuration
ADO_PAT = os.environ.get('AZURE_DEVOPS_PAT')
ADO_ORG = "stephaniefigas"
ADO_PROJECT = "Steph Learning environment"

BASE_URL = f"https://dev.azure.com/{ADO_ORG}/{ADO_PROJECT}/_apis/wit/workitems"

# Epic data
epic_data = {
    "title": "AI-Powered Benefits Adjudication System",
    "description": """<h2>Epic Description</h2>
<p>Establish an AI-powered decision support system to accelerate government benefits adjudication while maintaining transparency, fairness, and human oversight. This system will leverage agentic AI, intelligent document processing, and rules engines to reduce decision times from weeks to days, improve consistency, and enable adjudicators to focus on complex cases requiring human judgment.</p>

<h2>Target Audience</h2>
<h3>Primary Users:</h3>
<ul>
<li>Benefits adjudicators and case workers processing eligibility determinations</li>
<li>Benefits program managers overseeing adjudication operations</li>
<li>Citizens applying for government benefits (indirect beneficiaries through faster decisions)</li>
</ul>

<h3>Secondary Stakeholders:</h3>
<ul>
<li>IT operations and platform teams</li>
<li>Compliance and audit functions</li>
<li>Policy and regulatory teams</li>
</ul>

<h2>Problem Statement / Need</h2>
<h3>Current Pain Points:</h3>
<ul>
<li>Benefits adjudication takes weeks to months, delaying critical support to citizens</li>
<li>Manual document processing and data extraction creates bottlenecks and errors</li>
<li>Inconsistent application of complex eligibility rules across jurisdictions and adjudicators</li>
<li>High-volume routine cases consume resources that should focus on complex situations</li>
<li>Limited capacity to detect fraud before payments are issued</li>
<li>Lack of visibility into case status and processing bottlenecks</li>
</ul>

<h3>Why This Matters:</h3>
<ul>
<li>Federal agencies reported potential 35% cost savings over ten years through AI-enabled case processing</li>
<li>Citizens in need experience significant delays receiving essential benefits</li>
<li>Inconsistent decisions create equity concerns and increase appeals</li>
<li>Manual processes cannot scale to meet demand spikes (e.g., unemployment surges)</li>
</ul>

<h3>Impact of Not Solving:</h3>
<ul>
<li>Continued delays harm vulnerable populations</li>
<li>Missed opportunity to prevent fraud (IRS recovered $5B+ through AI-based review)</li>
<li>Competitive disadvantage as other jurisdictions modernize faster</li>
<li>Growing technical debt as vendor solutions create lock-in</li>
</ul>

<h2>Why Now?</h2>
<h3>Market Maturity:</h3>
<ul>
<li>Agentic AI systems moving from experimental to production-ready with proven ROI</li>
<li>Federal AI use cases more than doubled in 2024, with 9% focused on benefits delivery</li>
<li>Multiple agencies (SSA, VBA, CMS, USCIS) demonstrating successful implementations</li>
</ul>

<h3>Strategic Timing:</h3>
<ul>
<li>Window of opportunity to establish strategy before fragmented implementations create technical debt</li>
<li>Increasing vendor pressure requires informed response capability</li>
<li>Multiple BDM projects expressing interest in agentic capabilities independently</li>
</ul>

<h3>Risk of Not Acting Now:</h3>
<ul>
<li>Vendor lock-in from uncoordinated project decisions</li>
<li>Technical debt from siloed implementations</li>
<li>Loss of platform economies of scale</li>
</ul>

<h2>Proposed Solution / Core Features</h2>
<p><strong>High-Level Approach:</strong> Hybrid platform combining enterprise workflow capabilities with custom AI agents for complex reasoning, supplemented by specialized tools for document processing and rules execution.</p>

<h3>Core Capabilities:</h3>
<ol>
<li><strong>Intelligent Document Processing (IDP)</strong> - Automated extraction of data from claims, medical records, forms, and identity documents; 60% reduction in manual processing costs</li>
<li><strong>AI-Powered Decision Agents</strong> - Agentic AI system for complex eligibility reasoning using LangChain/LangGraph with Anthropic Claude</li>
<li><strong>Rules Engine for Eligibility Determination</strong> - Centralized business rules engine (Drools) for consistent eligibility criteria application</li>
<li><strong>Risk-Based Case Prioritization</strong> - AI-powered fraud detection and risk scoring with automated routing</li>
<li><strong>Human-in-the-Loop Workflows</strong> - Seamless escalation of edge cases to human adjudicators with AI recommendations</li>
<li><strong>Explainability and Audit Trail</strong> - Human-readable explanations for all AI-assisted decisions with complete audit trail</li>
<li><strong>Platform Workflow Orchestration</strong> - Case management integration with cross-system data integration</li>
</ol>""",
    "acceptance_criteria": """<h2>Business Outcome Hypothesis</h2>
<p>We believe that implementing an AI-powered benefits adjudication system for benefits adjudicators and case workers will achieve 50% reduction in routine case processing time while maintaining 90%+ decision accuracy and improving fraud detection.</p>

<h2>Success Metrics</h2>

<h3>Pilot Phase (Months 1-6):</h3>
<ul>
<li>90%+ accuracy on historical case validation</li>
<li>50%+ reduction in time-to-decision for pilot benefit type</li>
<li>100% of AI decisions include human-readable explanations</li>
<li>Adjudicator satisfaction score ≥4/5</li>
</ul>

<h3>Production MVP (Months 6-12):</h3>
<ul>
<li>60% of routine cases processed with minimal human intervention</li>
<li>Average time-to-decision: &lt;2 weeks (from baseline 4-6 weeks)</li>
<li>False positive rate &lt;5%</li>
<li>False negative rate &lt;2%</li>
<li>Fraud detection: $10M+ in prevented improper payments in first year</li>
</ul>

<h3>Scale Phase (Months 12-24):</h3>
<ul>
<li>System processing 75%+ of all incoming cases across 3+ benefit types</li>
<li>Adjudicator productivity: 100% increase in cases handled per FTE</li>
<li>Operating cost reduction: 15-20%</li>
<li>Appeal rate reduction: 10%</li>
<li>ROI: Positive return within 18 months</li>
</ul>

<h2>In Scope</h2>
<h3>Phase 1 - Pilot (Months 1-6):</h3>
<ul>
<li>1-2 straightforward benefit types (e.g., unemployment insurance)</li>
<li>Document processing for standard forms</li>
<li>Basic eligibility rules engine</li>
<li>Historical case validation</li>
<li>Human-in-the-loop workflows</li>
</ul>

<h3>Phase 2 - Production MVP (Months 6-12):</h3>
<ul>
<li>Production deployment for pilot benefit type</li>
<li>Integration with existing case management system</li>
<li>Fraud detection and risk scoring</li>
<li>Adjudicator training and change management</li>
<li>Compliance and security certification</li>
</ul>

<h3>Phase 3 - Scale (Months 12-24):</h3>
<ul>
<li>Expansion to 3+ additional benefit types</li>
<li>Advanced multi-agent reasoning for complex cases</li>
<li>Cross-program enrollment automation</li>
<li>Predictive analytics for proactive outreach</li>
</ul>

<h2>Out of Scope</h2>
<ul>
<li>Complete replacement of human adjudicators (human oversight always required)</li>
<li>Benefits policy changes or eligibility criteria modifications</li>
<li>Citizen-facing AI chatbot for application assistance (separate initiative)</li>
<li>Integration with all legacy systems (phased approach by priority)</li>
<li>Fully automated decisions without human review capability</li>
<li>Appeals processing automation (initial release)</li>
</ul>""",
    "priority": 1,
    "value_area": "Business",
    "time_criticality": "High"
}

def create_epic():
    """Create an epic work item in Azure DevOps"""

    if not ADO_PAT:
        print("Error: AZURE_DEVOPS_PAT environment variable not set")
        return

    # Create the epic with all fields
    create_payload = [
        {
            "op": "add",
            "path": "/fields/System.Title",
            "value": epic_data["title"]
        },
        {
            "op": "add",
            "path": "/fields/System.Description",
            "value": epic_data["description"]
        },
        {
            "op": "add",
            "path": "/fields/Microsoft.VSTS.Common.AcceptanceCriteria",
            "value": epic_data["acceptance_criteria"]
        },
        {
            "op": "add",
            "path": "/fields/Microsoft.VSTS.Common.Priority",
            "value": epic_data["priority"]
        },
        {
            "op": "add",
            "path": "/fields/Microsoft.VSTS.Common.ValueArea",
            "value": epic_data["value_area"]
        }
    ]

    headers = {"Content-Type": "application/json-patch+json"}
    auth = ("", ADO_PAT)

    print("Creating AI-Powered Benefits Adjudication Epic in Azure DevOps...")
    print(f"Organization: {ADO_ORG}")
    print(f"Project: {ADO_PROJECT}")
    print()

    # Create epic
    response = requests.post(
        f"{BASE_URL}/$Epic?api-version=7.0",
        json=create_payload,
        headers=headers,
        auth=auth
    )

    if response.status_code not in [200, 201]:
        print(f"✗ Failed to create epic")
        print(f"  Error: {response.text}")
        return None

    epic_id = response.json()["id"]
    epic_url = response.json()["_links"]["html"]["href"]

    print(f"✓ Successfully created Epic #{epic_id}")
    print(f"  Title: {epic_data['title']}")
    print(f"  Priority: {epic_data['priority']}")
    print(f"  Value Area: {epic_data['value_area']}")
    print()
    print(f"View in ADO: {epic_url}")
    print()
    print("=" * 80)

    return epic_id

if __name__ == "__main__":
    create_epic()
