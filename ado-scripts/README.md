# Azure DevOps (ADO) Scripts

This folder contains Python scripts for interacting with Azure DevOps to manage work items programmatically.

## Prerequisites

- Python 3.x installed
- `requests` library: `pip install requests`
- Azure DevOps Personal Access Token (PAT) set as environment variable

## Configuration

The scripts use the following environment variables:

```bash
export AZURE_DEVOPS_PAT="your_pat_token_here"
export AZURE_DEVOPS_ORG="stephaniefigas"
```

**Default Project:** "Steph Learning environment"

## Available Scripts

### Listing Scripts

#### `list-ado-projects.py`
Lists all Azure DevOps projects in your organization.

```bash
python3 ado-scripts/list-ado-projects.py
```

#### `list-ado-epics.py`
Lists all Epic work items in the project.

```bash
python3 ado-scripts/list-ado-epics.py
```

#### `list-ado-features.py`
Lists all Feature work items in the project.

```bash
python3 ado-scripts/list-ado-features.py
```

#### `list-ado-stories.py`
Lists all User Story work items in the project.

```bash
python3 ado-scripts/list-ado-stories.py
```

### Creation Scripts

#### `create-ai-adjudication-epic.py`
Creates the "AI-Powered Benefits Adjudication System" epic with complete details.

```bash
python3 ado-scripts/create-ai-adjudication-epic.py
```

**Output:** Creates Epic work item with:
- Full description including problem statement, target audience, solution
- Acceptance criteria with success metrics across 3 phases
- Priority, value area, and other metadata

#### `create-ado-features.py`
Creates Features under a specified Epic (configured for Epic ID 2 by default).

```bash
python3 ado-scripts/create-ado-features.py
```

**Note:** Edit `EPIC_ID` variable in the script to target different epics.

#### `create-ado-stories.sh`
Shell script for creating User Stories (bulk creation).

```bash
bash ado-scripts/create-ado-stories.sh
```

## Script Structure

All Python scripts follow this pattern:

1. Load environment variables (AZURE_DEVOPS_PAT)
2. Set configuration (organization, project)
3. Make API calls to Azure DevOps REST API
4. Display results or confirmation

## API Reference

These scripts use the Azure DevOps REST API v7.0:
- Base URL: `https://dev.azure.com/{organization}/{project}/_apis/`
- Authentication: Basic auth with empty username and PAT as password
- Work Items API: `/wit/workitems`
- WIQL API: `/wit/wiql` (for queries)

## Common Modifications

### Change Target Project
Edit the `ADO_PROJECT` variable in each script:
```python
ADO_PROJECT = "Your Project Name"
```

### Change Epic Parent
For creation scripts, edit the `EPIC_ID` variable:
```python
EPIC_ID = 41  # Your target epic ID
```

### Customize Work Item Fields
Modify the payload in creation scripts to add/change fields:
```python
{
    "op": "add",
    "path": "/fields/System.Tags",
    "value": "AI; Benefits; Automation"
}
```

## Troubleshooting

### Authentication Errors
```
Error: AZURE_DEVOPS_PAT environment variable not set
```
**Solution:** Set the environment variable:
```bash
export AZURE_DEVOPS_PAT="your_token"
```

### 401 Unauthorized
**Solution:** PAT may be expired. Generate a new one in ADO and update the environment variable.

### 404 Not Found
**Solution:** Check that the project name and organization are correct.

## Security Notes

- Never commit your PAT to version control
- Store PAT in environment variables or secure key management
- Keep PAT permissions minimal (only what's needed for work item management)
- Rotate PATs regularly

## Future Enhancements

Potential additions to this script collection:
- Bulk work item updates
- Automated reporting/metrics
- Sprint planning automation
- Work item relationship management
- Integration with GitHub for syncing issues
