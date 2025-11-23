# Notion MCP Server Setup

This document describes how the Notion integration is configured for AI-assisted product management workflows.

## Overview

The Notion MCP (Model Context Protocol) server enables Claude Code to interact with your Notion workspace, allowing you to:
- Search for pages and databases
- Create new pages and database entries
- Update existing pages
- Retrieve page content
- Add comments and reactions
- And more...

## Configuration

The Notion MCP server is configured in `.mcp.json`:

```json
{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": ["-y", "@notionhq/notion-mcp-server"],
      "env": {
        "NOTION_API_KEY": "ntn_l3754755308MRiuFPGKfMPOvc2uRWcjVBJLPMlKnPdF3Pu"
      }
    }
  }
}
```

## How It Works

1. **MCP Server**: The `@notionhq/notion-mcp-server` package provides a standardized interface for Claude Code to interact with Notion's API
2. **API Key**: The `NOTION_API_KEY` environment variable authenticates requests to your Notion workspace
3. **Tools**: Once connected, Claude Code has access to tools like:
   - `mcp__notion__search` - Search for pages and databases
   - `mcp__notion__create_pages` - Create new pages
   - `mcp__notion__update_page` - Update existing pages
   - `mcp__notion__get_page` - Retrieve page content
   - And more...

## Getting Your Notion API Key

If you need to create a new Notion integration or rotate your API key:

1. Go to https://www.notion.so/my-integrations
2. Click "New integration"
3. Give it a name (e.g., "Claude Code Integration")
4. Select the workspace you want to connect
5. Set the capabilities:
   - Read content ✓
   - Update content ✓
   - Insert content ✓
6. Click "Submit" to create the integration
7. Copy the "Internal Integration Token" (starts with `ntn_`)
8. Update the `NOTION_API_KEY` in `.mcp.json`

## Granting Access to Pages

Important: After creating the integration, you need to share specific pages/databases with it:

1. Open the Notion page or database you want Claude to access
2. Click the "..." menu in the top right
3. Scroll to "Add connections"
4. Select your integration (e.g., "Claude Code Integration")
5. Repeat for all pages/databases you want to access

## Security Notes

- The API key in `.mcp.json` is protected by `.gitignore` to prevent accidental commits
- The Notion integration can only access pages that have been explicitly shared with it
- You can revoke access at any time by removing the integration from your Notion workspace

## Usage Examples

Once configured and Claude Code is restarted, you can:

### Search for pages
```
"Find all pages in my Notion workspace"
```

### Create a new page
```
"Create a new SAFe epic page in Notion with [details]"
```

### Update existing content
```
"Update the status of the epic we created yesterday"
```

### Like pages
```
"Like all the pages in my Notion workspace"
```

## Troubleshooting

### MCP tools not available
- Ensure you've restarted Claude Code after updating `.mcp.json`
- Verify the API key is correct
- Check that pages have been shared with the integration

### "Page not found" errors
- Make sure the specific page has been shared with your integration
- The integration can only access pages explicitly shared with it

### Rate limiting
- Notion's API has rate limits (3 requests per second)
- Claude Code will automatically handle rate limiting with retries
