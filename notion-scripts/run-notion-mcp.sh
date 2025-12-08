#!/bin/bash

# Log file for debugging
LOG_FILE="/tmp/notion-mcp.log"

log() {
    echo "$(date): $1" >> "$LOG_FILE"
}

# Start logging
log "Starting Notion MCP server wrapper..."

# Get the absolute path to the project root (assuming script is in notion-scripts/)
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
log "Project root: $PROJECT_ROOT"

# Function to export env vars from a file
load_env() {
    local env_file="$1"
    if [ -f "$env_file" ]; then
        log "Loading environment from $env_file"
        set -a
        source "$env_file"
        set +a
    else
        log "Environment file $env_file not found"
    fi
}

# Source .env files
load_env "$PROJECT_ROOT/.env.local"
load_env "$PROJECT_ROOT/.env"

# Check for required API key (basic check)
if [ -z "$NOTION_API_KEY" ]; then
    log "ERROR: NOTION_API_KEY is not set!"
else
    log "NOTION_API_KEY is set (length: ${#NOTION_API_KEY})"
fi

# Run the MCP server
# Using npx -y to avoid prompts. 
# We direct stderr to the log file to capture crash info.
log "Executing npx @notionhq/notion-mcp-server..."
exec /usr/local/bin/npx -y @notionhq/notion-mcp-server 2>> "$LOG_FILE"
