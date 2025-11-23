#!/usr/bin/env python3
"""
List all User Stories for a specific Feature in Azure DevOps
"""

import os
import sys
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

def list_stories_for_feature(feature_id):
    """List all User Story work items for a specific feature"""

    if not ADO_PAT:
        print("Error: AZURE_DEVOPS_PAT environment variable not set")
        return

    auth = ("", ADO_PAT)

    # WIQL query to get all User Stories under the specified feature
    wiql_query = {
        "query": f"SELECT [System.Id], [System.Title], [System.State], [System.Parent], [Microsoft.VSTS.Scheduling.StoryPoints] FROM WorkItems WHERE [System.WorkItemType] = 'User Story' AND [System.Parent] = {feature_id} ORDER BY [System.Id]"
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
        print(f"✗ Failed to retrieve user stories")
        print(f"  Error: {response.text}")
        return

    work_items = response.json().get("workItems", [])

    if not work_items:
        print(f"No user stories found for Feature #{feature_id}")
        return

    # Get detailed information for each story
    story_ids = [str(item["id"]) for item in work_items]
    ids_string = ",".join(story_ids)

    details_url = f"https://dev.azure.com/{ADO_ORG}/{ADO_PROJECT}/_apis/wit/workitems?ids={ids_string}&api-version=7.0"

    response = requests.get(details_url, auth=auth)

    if response.status_code != 200:
        print(f"✗ Failed to retrieve story details")
        print(f"  Error: {response.text}")
        return

    stories = response.json().get("value", [])

    # Get feature details
    feature_url = f"https://dev.azure.com/{ADO_ORG}/{ADO_PROJECT}/_apis/wit/workitems/{feature_id}?api-version=7.0"
    feature_response = requests.get(feature_url, auth=auth)

    feature_title = "Unknown Feature"
    if feature_response.status_code == 200:
        feature_data = feature_response.json()
        feature_title = feature_data.get("fields", {}).get("System.Title", "Unknown Feature")

    print(f"User Stories for Feature #{feature_id}: {feature_title}")
    print("=" * 80)

    total_points = 0
    for story in stories:
        fields = story.get("fields", {})
        story_id = story.get("id", "N/A")
        title = fields.get("System.Title", "No title")
        state = fields.get("System.State", "N/A")
        story_points = fields.get("Microsoft.VSTS.Scheduling.StoryPoints", None)
        description = fields.get("System.Description", "")

        # Remove HTML tags from description for cleaner output
        import re
        clean_description = re.sub('<[^<]+?>', '', description) if description else "No description"
        clean_description = clean_description.strip()[:150]  # First 150 chars

        print(f"\n📝 Story #{story_id}: {title}")
        print(f"   State: {state}")
        print(f"   Story Points: {story_points if story_points else 'N/A'}")
        if clean_description:
            print(f"   Description: {clean_description}{'...' if len(description) > 150 else ''}")

        if story_points:
            total_points += story_points

    print("\n" + "=" * 80)
    print(f"Total user stories: {len(stories)}")
    print(f"Total story points: {total_points}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 list-ado-stories.py <feature_id>")
        print("\nExample: python3 list-ado-stories.py 5")
        sys.exit(1)

    feature_id = sys.argv[1]
    list_stories_for_feature(feature_id)
