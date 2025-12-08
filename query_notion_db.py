#!/usr/bin/env python3
"""
Query a specific Notion database by name and list its entries
"""

import os
import sys
import requests
from pathlib import Path

# Load .env file (check .env.local first, then .env)
env_files = ['.env.local', '.env']
for env_name in env_files:
    env_file = Path(__file__).parent / env_name
    if env_file.exists():
        with open(env_file) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    if key not in os.environ:
                        os.environ[key] = value
        break

NOTION_API_KEY = os.environ.get('NOTION_API_KEY')
NOTION_VERSION = "2022-06-28"

if not NOTION_API_KEY:
    print("Error: NOTION_API_KEY not found")
    sys.exit(1)

HEADERS = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Notion-Version": NOTION_VERSION,
    "Content-Type": "application/json"
}

def search_database(query):
    url = "https://api.notion.com/v1/search"
    payload = {
        "query": query,
        "filter": {
            "property": "object",
            "value": "database"
        }
    }
    response = requests.post(url, headers=HEADERS, json=payload)
    if response.status_code != 200:
        print(f"Error searching: {response.text}")
        return []
    return response.json().get("results", [])

def get_database_pages(db_id):
    url = f"https://api.notion.com/v1/databases/{db_id}/query"
    response = requests.post(url, headers=HEADERS)
    if response.status_code != 200:
        print(f"Error querying db: {response.text}")
        return []
    return response.json().get("results", [])

def get_title(page):
    # Try to find the title property
    props = page.get("properties", {})
    for key, value in props.items():
        if value.get("type") == "title":
            title_obj = value.get("title", [])
            if title_obj:
                return title_obj[0].get("plain_text", "Untitled")
    return "Untitled"

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 query_notion_db.py <database name>")
        sys.exit(1)
    
    query = sys.argv[1]
    print(f"Searching for database matching '{query}'...")
    
    databases = search_database(query)
    
    if not databases:
        print("No databases found matching that name.")
        sys.exit(0)
        
    target_db = None
    # Try exact match first
    for db in databases:
        title = "Untitled"
        if db.get("title"):
             title = db["title"][0].get("plain_text", "")
        
        if title.lower() == query.lower():
            target_db = db
            break
            
    # Fallback to first result
    if not target_db:
        target_db = databases[0]
        
    db_title = "Untitled"
    if target_db.get("title"):
        db_title = target_db["title"][0].get("plain_text", "")
        
    print(f"Found database: {db_title} ({target_db['id']})")
    print("Fetching entries...")
    
    pages = get_database_pages(target_db["id"])
    print(f"Found {len(pages)} entries:\n")
    
    for page in pages:
        title = get_title(page)
        url = page.get("url")
        print(f"- {title} ({url})")

if __name__ == "__main__":
    main()
