# AI-powered-PM

## Overview

This repository demonstrates a workflow (or workflows) for leveraging AI to handle Product or Portfolio Management tasks end-to-end. The goal is to learn how to use AI exclusively for core PM responsibilities, streamlining the product development process through automation and intelligent assistance. 
This repo is my own side project used for learning about AI and does not represent the views of my employer.
All content here is created using AI and what is publicly availble on the internet.

## Purpose

This repo serves as a workspace and showcase for using AI to:

- **Create Product Requirements Documents (PRDs)**: Generate comprehensive PRDs and solicit feedback/comments
- **Break Down Work**: Decompose product initiatives into manageable features and user stories
- **Generate Status Reports**: Automatically create project status updates and progress reports

By using AI for these tasks, this project explores how product management workflows can be enhanced, accelerated, and made more efficient through artificial intelligence.

## Getting Started

### Prerequisites

- [Claude Code CLI](https://claude.com/claude-code) installed
- Node.js and npm installed
- Access to Notion (for epic creation)
- Access to Azure DevOps (for work item management)

### Setup

**IMPORTANT**: Before using this repository, you must configure authentication for the MCP servers.

See **[SETUP.md](./SETUP.md)** for detailed instructions on:
- Getting your Notion API key
- Creating an Azure DevOps Personal Access Token
- Configuring your `.env` file
- Verifying your setup works
- Troubleshooting common issues

**Quick Start**:
```bash
# 1. Copy the environment template
cp .env.example .env

# 2. Edit .env and add your API keys
# Follow SETUP.md for detailed instructions on obtaining keys

# 3. Start using Claude Code in this directory
```

## What I've Proven

This project demonstrates an end-to-end AI-assisted product management workflow, from research to delivery. Here's what's been validated:

### Research & Documentation
**Automated Research Synthesis**: Successfully used Claude via command line to conduct desk research that substantiates user interviews. Claude autonomously researches topics and saves findings to structured files, accelerating the research validation process.

### Epic Creation & Stakeholder Collaboration
**Template-Driven Epic Generation**: Demonstrated that Claude can transform user research into properly formatted epics using custom Claude Skills. While the current template is generic, this proves the concept that Skills can encode organization-specific templates and frameworks, ensuring consistency across product documentation.

**Notion Integration for Stakeholder Feedback**: Validated the ability to push generated epics directly to Notion for stakeholder review and collaboration. This creates a seamless handoff from AI-assisted generation to human review.
- *To-do*: Test importing comments back from Notion to close the feedback loop

### Work Breakdown & Azure DevOps Integration
**Automated Epic Decomposition**: Connected Claude to Azure DevOps (ADO) and successfully used it to break down epics into features and stories, then create them directly in ADO. This eliminates manual transcription work and reduces errors.
- *Future enhancement*: Build Claude Skills that encode different decomposition strategies (e.g., innovation/discovery workflows focused on proving Desirability-Viability-Feasibility vs. delivery workflows optimized for MVP releases)

### Quality Assurance Through Skills
**Context-Aware Acceptance Criteria Review**: Created a Claude Skill that reviews and suggests acceptance criteria based on SAFe best practices. The skill includes a decision matrix that helps Claude apply the right practices based on work item context (feature vs. user story, research vs. technical implementation, etc.).

**Why Skills Matter**: This approach demonstrates the power of context engineering and progressive disclosure. Rather than cramming all guidance, templates, and decision frameworks into every prompt, Skills allow you to:
- Encapsulate domain knowledge and best practices into reusable modules
- Provide Claude with relevant context only when needed, improving response quality
- Maintain organizational standards without prompt bloat
- Enable non-technical stakeholders to leverage sophisticated workflows through simple commands

### Bidirectional ADO Sync
**Feature Updates via MCP**: Validated the ability to update features in Azure DevOps using the MCP (Model Context Protocol), enabling bidirectional sync between AI-assisted workflows and enterprise tooling.

### Workflow Benefits
**Audit Trail & Version Control**: By orchestrating everything through the command line with VS Code and GitHub integration, this approach provides:
- Complete audit trail of all AI interactions and decisions
- Version control for all generated artifacts
- Well-organized file structure that's easy to navigate
- Reproducible workflows that can be shared and improved over time
- Transparent AI assistance that supports rather than obscures the product development process
