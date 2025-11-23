#!/usr/bin/env python3
"""
List all Azure DevOps projects
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

# Configuration from existing scripts
ADO_PAT = os.environ.get('AZURE_DEVOPS_PAT')
ADO_ORG = "stephaniefigas"

BASE_URL = f"https://dev.azure.com/{ADO_ORG}/_apis/projects"

def list_projects():
    """List all Azure DevOps projects in the organization"""

    if not ADO_PAT:
        print("Error: AZURE_DEVOPS_PAT environment variable not set")
        print("Please set it using: export AZURE_DEVOPS_PAT=your_pat_token")
        return

    auth = ("", ADO_PAT)

    response = requests.get(
        f"{BASE_URL}?api-version=7.0",
        auth=auth
    )

    if response.status_code != 200:
        print(f"✗ Failed to retrieve projects")
        print(f"  Error: {response.text}")
        return

    data = response.json()
    projects = data.get("value", [])

    if not projects:
        print("No projects found in organization: {ADO_ORG}")
        return

    print(f"Azure DevOps Projects in '{ADO_ORG}':")
    print("=" * 80)

    for project in projects:
        name = project.get("name", "N/A")
        project_id = project.get("id", "N/A")
        description = project.get("description", "No description")
        state = project.get("state", "N/A")
        visibility = project.get("visibility", "N/A")

        print(f"\n📁 {name}")
        print(f"   ID: {project_id}")
        print(f"   State: {state}")
        print(f"   Visibility: {visibility}")
        if description:
            print(f"   Description: {description}")

    print("\n" + "=" * 80)
    print(f"Total projects: {len(projects)}")

if __name__ == "__main__":
    list_projects()
