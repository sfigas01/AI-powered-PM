#!/bin/bash

# Get the absolute path to the project root (assuming script is in ado-scripts/)
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# Source .env.local if it exists
if [ -f "$PROJECT_ROOT/.env.local" ]; then
    export $(grep -v '^#' "$PROJECT_ROOT/.env.local" | xargs)
fi

# Ensure ADO_MCP_AUTH_TOKEN is set from AZURE_DEVOPS_PAT
if [ -n "$AZURE_DEVOPS_PAT" ]; then
    export ADO_MCP_AUTH_TOKEN="$AZURE_DEVOPS_PAT"
fi

# Run the MCP server
# Using npx -y to avoid prompts
exec npx -y @azure-devops/mcp stephaniefigas --authentication envvar
