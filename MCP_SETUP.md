# MCP Server Setup Guide

This project uses Model Context Protocol (MCP) servers to integrate Claude Code with external tools like Notion and Azure DevOps.

## Quick Start

### 1. Copy the Environment Template

```bash
cp .env.example .env.local
```

### 2. Configure Your API Keys

Edit `.env.local` and add your actual API credentials:

```bash
# Notion Integration
NOTION_API_KEY=your_notion_integration_token

# Azure DevOps
AZURE_DEVOPS_PAT=your_personal_access_token
AZURE_DEVOPS_ORG=stephaniefigas
```

### 3. Verify MCP Server Configuration

The `.mcp.json` file in the project root defines which MCP servers are available:

```json
{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": ["-y", "@notionhq/notion-mcp-server"],
      "env": {
        "NOTION_API_KEY": "${NOTION_API_KEY}"
      }
    },
    "azure-devops": {
      "command": "npx",
      "args": ["-y", "@azure-devops/mcp", "stephaniefigas"],
      "env": {
        "AZURE_DEVOPS_PAT": "${AZURE_DEVOPS_PAT}",
        "AZURE_DEVOPS_ORG": "${AZURE_DEVOPS_ORG}"
      }
    }
  }
}
```

## Getting API Credentials

### Notion API Key

1. Visit [Notion Integrations](https://www.notion.so/my-integrations)
2. Click "+ New integration"
3. Give it a name (e.g., "Claude Code MCP")
4. Select the workspace you want to access
5. Copy the "Internal Integration Token"
6. Share the specific Notion pages/databases with your integration

### Azure DevOps Personal Access Token (PAT)

1. Go to [Azure DevOps User Settings](https://dev.azure.com/stephaniefigas/_usersSettings/tokens)
2. Click "+ New Token"
3. Give it a descriptive name (e.g., "Claude Code MCP")
4. Set expiration as needed
5. Select scopes:
   - **Work Items**: Read, write, & manage
   - **Code**: Read (if accessing repos)
   - **Project and Team**: Read
6. Click "Create" and copy the token immediately (it won't be shown again)

## How MCP Servers Work with Claude Code Web

### File Organization

- **`.mcp.json`** - Lives in project root, defines available MCP servers
  - ✅ Checked into git (contains NO secrets, only env var references)
  - ✅ Available across all web sessions
  - ✅ Shared with team members

- **`.env.local`** - Contains actual API keys and secrets
  - ❌ NOT checked into git (in `.gitignore`)
  - ⚠️  Must be recreated in each environment
  - 🔒 Keeps credentials secure

- **`.env.example`** - Template showing required variables
  - ✅ Checked into git
  - 📝 Documents what credentials are needed

### Security Best Practices

1. **Never hardcode API keys** in `.mcp.json` - always use environment variables
2. **Always use `.env.local`** for secrets (never `.env`)
3. **Rotate tokens regularly** - set expiration dates on PATs
4. **Use minimal permissions** - only grant scopes actually needed
5. **Separate tokens per environment** - don't reuse production tokens for development

## Verifying MCP Setup

In Claude Code, you can check MCP server status:

```
/mcp
```

This will show which servers are connected and available.

## Troubleshooting

### MCP Server Not Loading

1. **Check file location**: `.mcp.json` must be in project root (not `.claude/` subdirectory)
2. **Verify environment variables**: Ensure `.env.local` exists and has the correct keys
3. **Check syntax**: JSON must be valid (use a JSON validator)
4. **Restart Claude Code**: Sometimes requires a session restart to pick up changes

### Authentication Errors

1. **Notion**: Verify the integration has access to the pages/databases you're trying to access
2. **Azure DevOps**: Ensure PAT hasn't expired and has required scopes
3. **Environment variables**: Check for typos in variable names (they're case-sensitive)

### Server Won't Start

1. **Check npx**: Ensure Node.js and npm are installed
2. **Network access**: Some environments may block npx from downloading packages
3. **View logs**: Check Claude Code logs for specific error messages

## Project-Specific Usage

This project uses MCP servers for:

- **Notion MCP**: Creating and updating SAFe epics, pushing documentation for stakeholder review
- **Azure DevOps MCP**: Breaking down epics into features/stories, creating work items, updating status

See the main [README.md](README.md) for more details on the AI-powered PM workflow.
