#!/usr/bin/env python3
"""
List all Epics in Azure DevOps project
"""

import os
import requests
from pathlib import Path

# Load .env file if it exists
env_file = Path(__file__).parent / '.env'
if env_file.exists():
    with open(env_file) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                os.environ[key] = value

# Configuration
ADO_PAT = os.environ.get('AZURE_DEVOPS_PAT')
ADO_ORG = "stephaniefigas"
ADO_PROJECT = "Steph Learning environment"

def list_epics():
    """List all Epic work items in the project"""

    if not ADO_PAT:
        print("Error: AZURE_DEVOPS_PAT environment variable not set")
        print("Please set it using: export AZURE_DEVOPS_PAT=your_pat_token")
        return

    auth = ("", ADO_PAT)

    # WIQL query to get all Epics
    wiql_query = {
        "query": "SELECT [System.Id], [System.Title], [System.State], [System.Description] FROM WorkItems WHERE [System.WorkItemType] = 'Epic' ORDER BY [System.Id]"
    }

    # Query for work items
    wiql_url = f"https://dev.azure.com/{ADO_ORG}/{ADO_PROJECT}/_apis/wit/wiql?api-version=7.0"

    response = requests.post(
        wiql_url,
        json=wiql_query,
        auth=auth,
        headers={"Content-Type": "application/json"}
    )

    if response.status_code != 200:
        print(f"✗ Failed to retrieve epics")
        print(f"  Error: {response.text}")
        return

    work_items = response.json().get("workItems", [])

    if not work_items:
        print(f"No epics found in project: {ADO_PROJECT}")
        return

    # Get detailed information for each epic
    epic_ids = [str(item["id"]) for item in work_items]
    ids_string = ",".join(epic_ids)

    details_url = f"https://dev.azure.com/{ADO_ORG}/{ADO_PROJECT}/_apis/wit/workitems?ids={ids_string}&api-version=7.0"

    response = requests.get(details_url, auth=auth)

    if response.status_code != 200:
        print(f"✗ Failed to retrieve epic details")
        print(f"  Error: {response.text}")
        return

    epics = response.json().get("value", [])

    print(f"Epics in '{ADO_PROJECT}':")
    print("=" * 80)

    for epic in epics:
        fields = epic.get("fields", {})
        epic_id = epic.get("id", "N/A")
        title = fields.get("System.Title", "No title")
        state = fields.get("System.State", "N/A")
        description = fields.get("System.Description", "")

        # Remove HTML tags from description for cleaner output
        import re
        clean_description = re.sub('<[^<]+?>', '', description) if description else "No description"
        clean_description = clean_description.strip()[:100]  # First 100 chars

        print(f"\n📋 Epic #{epic_id}: {title}")
        print(f"   State: {state}")
        if clean_description:
            print(f"   Description: {clean_description}{'...' if len(description) > 100 else ''}")

    print("\n" + "=" * 80)
    print(f"Total epics: {len(epics)}")

if __name__ == "__main__":
    list_epics()
