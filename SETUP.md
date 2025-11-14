# Setup Guide

This guide will help you set up the AI-powered PM workspace with all required MCP (Model Context Protocol) servers and integrations.

## Overview

This project uses MCP servers to integrate Claude Code with external services:

- **Notion MCP Server**: Creates and manages SAFe epics in Notion for stakeholder review
- **Azure DevOps MCP Server**: Creates and updates work items (features, stories) in Azure DevOps

## Prerequisites

Before you begin, ensure you have:

- [Claude Code CLI](https://claude.com/claude-code) installed and configured
- Node.js and npm installed (for running MCP servers via `npx`)
- Access to a Notion workspace (free or paid account)
- Access to an Azure DevOps organization

## Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-powered-PM.git
cd AI-powered-PM
```

## Step 2: Configure Environment Variables

### Create Your .env File

Copy the example environment file:

```bash
cp .env.example .env
```

Now you'll need to populate this file with your actual API keys. Follow the instructions below for each service.

### Get Your Notion API Key

1. Go to [https://www.notion.so/my-integrations](https://www.notion.so/my-integrations)
2. Click **"+ New integration"**
3. Give it a name (e.g., "Claude AI-PM Integration")
4. Select the workspace you want to integrate with
5. Click **"Submit"** to create the integration
6. Copy the **"Internal Integration Token"** (starts with `secret_`)
7. **IMPORTANT**: Grant the integration access to your pages:
   - Open your Notion workspace
   - Navigate to the page(s) you want Claude to access (e.g., "SAFe Epic Template")
   - Click the **"••• More"** menu → **"Add connections"**
   - Find and select your integration name
   - Click **"Confirm"**

8. Paste the token into your `.env` file:
   ```
   NOTION_API_KEY=secret_your_actual_token_here
   ```

**Required Notion Capabilities:**
- Read content
- Update content
- Insert content

**Learn more**: [Notion API Authorization](https://developers.notion.com/docs/authorization)

### Get Your Azure DevOps Personal Access Token

1. Sign in to your Azure DevOps organization at `https://dev.azure.com/{your-organization}`
2. Click on your profile icon in the top right → **"Personal access tokens"**
3. Click **"+ New Token"**
4. Configure your token:
   - **Name**: "Claude AI-PM Integration" (or your preferred name)
   - **Organization**: Select your organization
   - **Expiration**: Choose an appropriate expiration (90 days recommended for security)
   - **Scopes**: Click "Show all scopes" and select:
     - ✅ **Work Items**: Read, write, & manage
5. Click **"Create"**
6. **IMPORTANT**: Copy the token immediately (it won't be shown again!)
7. Paste the token into your `.env` file:
   ```
   AZURE_DEVOPS_PAT=your_actual_pat_here
   ```

**Note**: If you lose your token, you'll need to generate a new one.

**Learn more**: [Azure DevOps Personal Access Tokens](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate)

## Step 3: Configure MCP Servers

The MCP servers are already configured in `.mcp.json`. They will automatically load environment variables from your `.env` file.

### Current Configuration

```json
{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": ["-y", "@notionhq/notion-mcp-server"]
    },
    "azure-devops": {
      "command": "npx",
      "args": ["-y", "@azure-devops/mcp", "stephaniefigas"]
    }
  }
}
```

**Note**: Update the Azure DevOps organization name (`stephaniefigas`) to match your organization if different.

## Step 4: Verify Your Setup

### Test Notion Connection

Start Claude Code in this directory and try:

```
Can you search Notion for "SAFe Epic Template"?
```

If successful, Claude should find pages in your Notion workspace.

### Test Azure DevOps Connection

Try listing work items:

```
Can you list the recent work items in Azure DevOps?
```

If successful, Claude should be able to access your ADO projects.

## Step 5: Set Up Your Notion Workspace (Optional but Recommended)

For the epic-writer skill to work optimally:

1. Create a page in Notion called **"SAFe Epic Template"**
2. Grant your integration access to this page (see Step 2 above)
3. Optionally, create a template page structure with sections for:
   - Epic Name
   - Description
   - Problem Statement
   - Solution Approach
   - Business Outcome Hypothesis
   - Success Metrics

The epic-writer skill will create new epics as sub-pages under this template page.

## Troubleshooting

### "Cannot access Notion" or "Permission denied"

**Solution**: Ensure you've granted your Notion integration access to the specific pages:
1. Open the page in Notion
2. Click "••• More" → "Add connections"
3. Select your integration
4. Click "Confirm"

### "Azure DevOps authentication failed"

**Solutions**:
- Verify your PAT hasn't expired
- Check that you selected the correct scopes (Work Items: Read, write, & manage)
- Ensure your `.env` file is in the project root directory
- Verify the organization name in `.mcp.json` matches your ADO organization

### "MCP server not responding"

**Solutions**:
- Ensure Node.js and npm are installed: `node --version && npm --version`
- Try manually installing the MCP servers:
  ```bash
  npx -y @notionhq/notion-mcp-server --help
  npx -y @azure-devops/mcp --help
  ```
- Check that your `.env` file is properly formatted (no quotes around values, no spaces around `=`)

### ".env file not being loaded"

**Solutions**:
- Ensure the file is named exactly `.env` (not `.env.txt` or `env`)
- Verify the file is in the root directory of the project
- Check file permissions: `ls -la .env`
- Restart Claude Code after creating/modifying `.env`

## Security Best Practices

1. **Never commit your `.env` file** - It's already in `.gitignore`, but double-check
2. **Rotate your tokens regularly** - Set expiration dates on PATs
3. **Use minimum required permissions** - Only grant the scopes you actually need
4. **Store tokens securely** - Consider using a password manager for backup copies
5. **Review integration access** - Periodically audit what pages your Notion integration can access

## Getting Help

If you encounter issues not covered here:

1. Check the [Notion API documentation](https://developers.notion.com/docs)
2. Review [Azure DevOps REST API docs](https://learn.microsoft.com/en-us/rest/api/azure/devops/)
3. Check [Claude Code documentation](https://docs.claude.com/claude-code)
4. Open an issue in this repository with details about your problem

## Next Steps

Once setup is complete, you can:

- Use the `/safe-epic-creator` skill to transform meeting notes into Notion epics
- Run `./create-ado-features.py` to create features in Azure DevOps
- Use the `/ac-helper` skill to review and improve acceptance criteria
- Explore the workflows documented in `README.md`

## Additional Resources

- [Model Context Protocol (MCP) Documentation](https://modelcontextprotocol.io/)
- [SAFe Framework Overview](https://scaledagileframework.com/)
- [Notion API Reference](https://developers.notion.com/reference)
- [Azure DevOps REST API Reference](https://learn.microsoft.com/en-us/rest/api/azure/devops/)
