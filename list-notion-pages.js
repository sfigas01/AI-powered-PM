#!/usr/bin/env node

const https = require('https');

const NOTION_API_KEY = process.argv[2];
const NOTION_VERSION = '2022-06-28';

if (!NOTION_API_KEY) {
  console.error('Usage: node list-notion-pages.js <NOTION_API_KEY>');
  process.exit(1);
}

function makeNotionRequest(path, method = 'GET', body = null) {
  return new Promise((resolve, reject) => {
    const options = {
      hostname: 'api.notion.com',
      path: path,
      method: method,
      headers: {
        'Authorization': `Bearer ${NOTION_API_KEY}`,
        'Notion-Version': NOTION_VERSION,
        'Content-Type': 'application/json'
      }
    };

    const req = https.request(options, (res) => {
      let data = '';

      res.on('data', (chunk) => {
        data += chunk;
      });

      res.on('end', () => {
        try {
          const parsed = JSON.parse(data);
          if (res.statusCode >= 400) {
            reject(new Error(`Notion API error: ${res.statusCode} - ${JSON.stringify(parsed)}`));
          } else {
            resolve(parsed);
          }
        } catch (e) {
          reject(new Error(`Failed to parse response: ${e.message}`));
        }
      });
    });

    req.on('error', (e) => {
      reject(e);
    });

    if (body) {
      req.write(JSON.stringify(body));
    }

    req.end();
  });
}

async function searchAllPages() {
  console.log('Searching for all pages in your Notion workspace...\n');

  try {
    const response = await makeNotionRequest('/v1/search', 'POST', {
      filter: {
        property: 'object',
        value: 'page'
      },
      page_size: 100
    });

    if (!response.results || response.results.length === 0) {
      console.log('No pages found in your Notion workspace.');
      return [];
    }

    console.log(`Found ${response.results.length} pages:\n`);
    console.log('='.repeat(80));

    const pages = [];

    response.results.forEach((page, index) => {
      const title = getPageTitle(page);
      const id = page.id;
      const url = page.url;

      pages.push({ id, title, url });

      console.log(`${index + 1}. ${title}`);
      console.log(`   ID: ${id}`);
      console.log(`   URL: ${url}`);
      console.log('-'.repeat(80));
    });

    // Save to JSON file for reference
    const fs = require('fs');
    fs.writeFileSync('notion-pages.json', JSON.stringify(pages, null, 2));
    console.log('\nPage list saved to notion-pages.json');

    return pages;
  } catch (error) {
    console.error('Error searching pages:', error.message);
    throw error;
  }
}

function getPageTitle(page) {
  // Try to get title from properties
  if (page.properties) {
    // Look for title property
    for (const [key, value] of Object.entries(page.properties)) {
      if (value.type === 'title' && value.title && value.title.length > 0) {
        return value.title.map(t => t.plain_text).join('');
      }
    }
  }

  // Fallback to parent info or "Untitled"
  return 'Untitled Page';
}

// Run the search
searchAllPages().catch(error => {
  console.error('Failed to list pages:', error.message);
  process.exit(1);
});
