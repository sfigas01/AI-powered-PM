#!/usr/bin/env python3
"""
List all Features in Azure DevOps project
"""

import os
import sys
import json

def list_features():
    """List all features in the Azure DevOps project"""
    ado_pat = os.environ.get('AZURE_DEVOPS_PAT')

    if not ado_pat:
        print("Error: AZURE_DEVOPS_PAT environment variable not set", file=sys.stderr)
        print("\nTo use this script, you need to:", file=sys.stderr)
        print("1. Create a Personal Access Token in Azure DevOps", file=sys.stderr)
        print("2. Set it as an environment variable: export AZURE_DEVOPS_PAT='your-pat'", file=sys.stderr)
        sys.exit(1)

    try:
        import requests
    except ImportError:
        print("Installing requests library...")
        os.system("pip3 install requests -q")
        import requests

    # Configuration
    ADO_ORG = "stephaniefigas"
    ADO_PROJECT = "Steph Learning environment"

    # Query for all Features
    query_url = f"https://dev.azure.com/{ADO_ORG}/{ADO_PROJECT}/_apis/wit/wiql?api-version=7.0"

    wiql_query = {
        "query": """
            SELECT [System.Id], [System.Title], [System.State], [System.Parent],
                   [Microsoft.VSTS.Scheduling.StoryPoints], [System.CreatedDate],
                   [System.ChangedDate], [Microsoft.VSTS.Common.Priority]
            FROM WorkItems
            WHERE [System.WorkItemType] = 'Feature'
            ORDER BY [System.Id] ASC
        """
    }

    headers = {"Content-Type": "application/json"}
    auth = ("", ado_pat)

    try:
        # Execute query
        response = requests.post(query_url, json=wiql_query, headers=headers, auth=auth)
        response.raise_for_status()

        query_results = response.json()
        work_items = query_results.get('workItems', [])

        if not work_items:
            print("\nNo features found in the project.")
            return

        print(f"\nFound {len(work_items)} feature(s) in project '{ADO_PROJECT}':\n")
        print("=" * 100)

        # Get detailed information for each work item
        all_features = []
        for item in work_items:
            item_id = item['id']
            item_url = f"https://dev.azure.com/{ADO_ORG}/{ADO_PROJECT}/_apis/wit/workitems/{item_id}?api-version=7.0"

            item_response = requests.get(item_url, headers=headers, auth=auth)
            item_response.raise_for_status()

            item_data = item_response.json()
            fields = item_data.get('fields', {})

            feature_info = {
                'id': item_id,
                'title': fields.get('System.Title', 'N/A'),
                'state': fields.get('System.State', 'N/A'),
                'parent': fields.get('System.Parent', None),
                'story_points': fields.get('Microsoft.VSTS.Scheduling.StoryPoints', 'N/A'),
                'priority': fields.get('Microsoft.VSTS.Common.Priority', 'N/A'),
                'created': fields.get('System.CreatedDate', 'N/A'),
                'changed': fields.get('System.ChangedDate', 'N/A'),
                'url': f"https://dev.azure.com/{ADO_ORG}/{ADO_PROJECT}/_workitems/edit/{item_id}"
            }

            all_features.append(feature_info)

            # Print feature details
            print(f"\nFeature #{item_id}: {feature_info['title']}")
            print(f"   State: {feature_info['state']}")
            print(f"   Story Points: {feature_info['story_points']}")
            print(f"   Priority: {feature_info['priority']}")
            if feature_info['parent']:
                print(f"   Parent Epic: #{feature_info['parent']}")
            print(f"   Created: {feature_info['created'][:10] if isinstance(feature_info['created'], str) else 'N/A'}")
            print(f"   Last Changed: {feature_info['changed'][:10] if isinstance(feature_info['changed'], str) else 'N/A'}")
            print(f"   URL: {feature_info['url']}")
            print("-" * 100)

        # Save to JSON
        output_file = "ado_features_list.json"
        with open(output_file, 'w') as f:
            json.dump(all_features, f, indent=2)

        print(f"\n✓ Full feature details saved to: {output_file}")

        # Summary statistics
        print(f"\n{'=' * 100}")
        print(f"SUMMARY:")
        print(f"  Total Features: {len(all_features)}")

        states = {}
        for f in all_features:
            state = f['state']
            states[state] = states.get(state, 0) + 1

        print(f"  By State:")
        for state, count in sorted(states.items()):
            print(f"    {state}: {count}")

        total_points = sum(f['story_points'] for f in all_features if isinstance(f['story_points'], (int, float)))
        print(f"  Total Story Points: {total_points}")
        print("=" * 100)

    except requests.exceptions.RequestException as e:
        print(f"Error querying Azure DevOps API: {e}", file=sys.stderr)
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response: {e.response.text}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    list_features()
