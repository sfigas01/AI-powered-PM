#!/usr/bin/env python3
"""
List all Notion databases accessible with the integration token
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
NOTION_API_KEY = os.environ.get('NOTION_API_KEY')
NOTION_VERSION = "2022-06-28"

def list_databases():
    """List all Notion databases"""

    if not NOTION_API_KEY:
        print("Error: NOTION_API_KEY environment variable not set")
        return

    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json"
    }

    # Search for all databases
    search_url = "https://api.notion.com/v1/search"
    search_payload = {
        "filter": {
            "property": "object",
            "value": "database"
        }
    }

    response = requests.post(search_url, headers=headers, json=search_payload)

    if response.status_code != 200:
        print(f"✗ Failed to connect to Notion")
        print(f"  Error: {response.status_code} - {response.text}")
        return

    data = response.json()
    databases = data.get("results", [])

    if not databases:
        print("No databases found. Make sure you've:")
        print("1. Shared databases with your integration in Notion")
        print("2. Given the integration access to the pages/databases you want to access")
        return

    print("Notion Databases:")
    print("=" * 80)

    for db in databases:
        db_id = db.get("id", "N/A")
        title_obj = db.get("title", [])

        # Extract title text
        if title_obj and len(title_obj) > 0:
            title = title_obj[0].get("plain_text", "Untitled")
        else:
            title = "Untitled"

        url = db.get("url", "")
        created_time = db.get("created_time", "")
        last_edited = db.get("last_edited_time", "")

        print(f"\n📊 {title}")
        print(f"   ID: {db_id}")
        print(f"   URL: {url}")
        print(f"   Created: {created_time[:10] if created_time else 'N/A'}")
        print(f"   Last edited: {last_edited[:10] if last_edited else 'N/A'}")

    print("\n" + "=" * 80)
    print(f"Total databases: {len(databases)}")

if __name__ == "__main__":
    list_databases()
