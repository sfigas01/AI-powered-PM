#!/usr/bin/env python3
"""
Search Notion for pages related to a specific query.
Requires NOTION_TOKEN environment variable.
"""

import os
import sys
import json

def search_notion(query):
    """Search Notion for pages matching the query."""
    notion_token = os.environ.get('NOTION_TOKEN')

    if not notion_token:
        print("Error: NOTION_TOKEN environment variable not set", file=sys.stderr)
        print("\nTo use this script, you need to:", file=sys.stderr)
        print("1. Create a Notion integration at https://www.notion.so/my-integrations", file=sys.stderr)
        print("2. Copy the integration token", file=sys.stderr)
        print("3. Set it as an environment variable: export NOTION_TOKEN='your-token'", file=sys.stderr)
        sys.exit(1)

    try:
        import requests
    except ImportError:
        print("Installing requests library...")
        os.system("pip3 install requests -q")
        import requests

    headers = {
        "Authorization": f"Bearer {notion_token}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }

    # Search for pages
    search_url = "https://api.notion.com/v1/search"
    search_payload = {
        "query": query,
        "filter": {
            "property": "object",
            "value": "page"
        },
        "sort": {
            "direction": "descending",
            "timestamp": "last_edited_time"
        }
    }

    try:
        response = requests.post(search_url, headers=headers, json=search_payload)
        response.raise_for_status()

        results = response.json()
        pages = results.get('results', [])

        if not pages:
            print(f"\nNo pages found matching '{query}'")
            return

        print(f"\nFound {len(pages)} page(s) related to '{query}':\n")
        print("=" * 80)

        for i, page in enumerate(pages, 1):
            page_id = page.get('id')
            url = page.get('url')

            # Get page title
            title = "Untitled"
            properties = page.get('properties', {})

            # Try to get title from various property types
            for prop_name, prop_value in properties.items():
                if prop_value.get('type') == 'title':
                    title_array = prop_value.get('title', [])
                    if title_array:
                        title = ''.join([t.get('plain_text', '') for t in title_array])
                        break

            # Get last edited time
            last_edited = page.get('last_edited_time', 'Unknown')

            # Get created time
            created = page.get('created_time', 'Unknown')

            print(f"\n{i}. {title}")
            print(f"   ID: {page_id}")
            print(f"   URL: {url}")
            print(f"   Created: {created}")
            print(f"   Last Edited: {last_edited}")
            print("-" * 80)

        # Save results to JSON for programmatic access
        output_file = f"notion_search_{query.replace(' ', '_')}.json"
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2)

        print(f"\nFull results saved to: {output_file}")

    except requests.exceptions.RequestException as e:
        print(f"Error querying Notion API: {e}", file=sys.stderr)
        if hasattr(e.response, 'text'):
            print(f"Response: {e.response.text}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    query = sys.argv[1] if len(sys.argv) > 1 else "data fabric"
    search_notion(query)
