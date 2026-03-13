---
name: "jira-story-analyzer"
displayName: "Jira Story Analyzer"
description: "Analyzes Jira user stories using AI to identify gaps, generate technical tasks, and create test cases. Supports OpenAI, Anthropic, and Groq (free) models. Includes special Blaze Rules Context mode for business rules projects."
keywords: ["jira", "story", "analysis", "requirements", "blaze", "test-cases", "sprint"]
author: "Miguel Angel Cervantes Juarez"
---

# Jira Story Analyzer

## Overview

Jira Story Analyzer is an AI-powered tool that analyzes Jira user stories to identify gaps, ambiguities, and improvement opportunities. It generates structured analysis with technical tasks, test cases, and actionable recommendations.

**Key capabilities:**
- Fetch and analyze individual Jira stories
- Generate comprehensive test cases in Gherkin format
- Analyze multiple stories together (sprint analysis) with dependency detection
- Special Blaze Rules Context mode for IBM Blaze Advisor projects
- Support for multiple AI providers: OpenAI (GPT-4), Anthropic (Claude), and Groq (free)

**Use cases:**
- Before sprint planning: Identify missing requirements and blockers
- During design reviews: Generate technical task breakdowns
- For QA teams: Auto-generate test scenarios
- Blaze Rules projects: Find specific functions to modify in large codebases

## Onboarding

### Prerequisites

**Required:**
- Python 3.8 or higher
- Jira account with API access
- At least one AI provider API key (OpenAI, Anthropic, or Groq)

**Optional:**
- Multiple AI provider keys for flexibility
- Groq API key for free tier usage

### Installation

**1. Install Python dependencies:**

The MCP server requires the following Python packages:
```bash
pip install mcp jira litellm python-dotenv
```

**2. Get Jira API Token:**
- Go to https://id.atlassian.com/manage-profile/security/api-tokens
- Click "Create API token"
- Copy the token (you'll need it for configuration)

**3. Get AI Provider API Key:**

Choose at least one:

**Option 1: Groq (Free)**
- Go to https://console.groq.com
- Create account (free)
- Navigate to "API Keys"
- Create new key
- Recommended model: `groq/llama-3.3-70b-versatile`

**Option 2: OpenAI (Paid)**
- Go to https://platform.openai.com
- Create API key
- Recommended model: `gpt-4-turbo`

**Option 3: Anthropic (Paid)**
- Go to https://console.anthropic.com
- Create API key
- Recommended model: `claude-3-5-sonnet-20241022`

### Configuration

**IMPORTANT: Credential Security**

The `mcp.json` file in the repo contains PLACEHOLDERS only. Before using this power:

1. **Create local config (recommended):**
   ```bash
   cd powers/jira-story-analyzer
   cp mcp.json mcp.local.json
   # Edit mcp.local.json with your real credentials
   ```

2. **The `mcp.local.json` file is in .gitignore** - your credentials won't be committed

3. **When installing the power in Kiro**, point to `mcp.local.json` instead of `mcp.json`

**Find your Jira Acceptance Criteria field:**

Different Jira instances use different custom fields for Acceptance Criteria. To find yours:

1. Open any Jira story that has acceptance criteria
2. Use the Jira REST API or inspect the story JSON
3. Look for custom fields like `customfield_10054`, `customfield_10000`, etc.
4. Common field names: `customfield_10054`, `customfield_10000`, `customfield_10007`

**Note:** The power will try multiple common fields automatically, but specifying the correct one improves reliability.

## Available MCP Tools

### fetch_story

Fetches a Jira user story with all details.

**Parameters:**
- `story_id` (string, required): Jira story ID (e.g., "PROJ-123")

**Returns:** Story details including title, description, acceptance criteria, comments, status, priority, and labels.

**Example:**
```
Use fetch_story with story_id="PROJ-456"
```

### analyze_story

Analyzes a Jira story using AI to identify gaps and generate recommendations.

**Parameters:**
- `story_id` (string, required): Jira story ID
- `model` (string, optional): AI model to use
  - Default: "gpt-4-turbo"
  - Options: "gpt-4-turbo", "claude-3-5-sonnet-20241022", "groq/llama-3.3-70b-versatile"
- `user_notes` (string, optional): Additional context or architectural notes

**Returns:** Structured 5-section analysis:
1. Quick Summary (complexity, business value)
2. What to Build (core features)
3. Critical Gaps (blockers, risks, questions)
4. Technical Tasks (backend, frontend, DB, testing)
5. Next Steps (ready to start?)

**Example:**
```
Use analyze_story with:
- story_id="PROJ-456"
- model="groq/llama-3.3-70b-versatile"
- user_notes="Must integrate with legacy system. Consider 5s timeout."
```

### analyze_story_blaze_mode

Special mode for IBM Blaze Advisor business rules projects. Analyzes the story and generates an optimized prompt for searching the Blaze codebase.

**Parameters:**
- `story_id` (string, required): Jira story ID
- `model` (string, optional): AI model to use

**Returns:**
- Standard AI analysis
- Extracted keywords (e.g., "HolidayPay", "ReserveTrip", "Edd")
- Optimized search prompt for finding relevant Blaze functions (fcn*) and rulesets (rs*)

**Example:**
```
Use analyze_story_blaze_mode with story_id="PROJ-789"
```

**Use case:** When working on Blaze Rules projects with 500+ business rule functions, this mode extracts specific technical keywords and generates a focused search strategy to find the exact functions that need modification.

### generate_blaze_prompt

Generate ONLY the Kiro search prompt for Blaze Rules projects without AI analysis. Fast and free - just extracts story info and formats it for Kiro to analyze the codebase.

**Parameters:**
- `story_id` (string, required): Jira story ID

**Returns:**
- Formatted prompt ready for Kiro to search the Blaze codebase
- No AI analysis (saves time and API costs)

**Example:**
```
Use generate_blaze_prompt with story_id="PROJ-789"
```

**Use case:** When you want Kiro to analyze the Blaze codebase directly without spending AI tokens on story analysis first. Perfect for quick searches or when you already understand the story requirements.

**Difference from analyze_story_blaze_mode:**
- `generate_blaze_prompt`: Fast, free, no AI analysis - just formats the story for Kiro
- `analyze_story_blaze_mode`: Full AI analysis + keyword extraction + optimized prompt

### generate_test_cases

Generates comprehensive test cases in Gherkin format (Given-When-Then).

**Parameters:**
- `story_id` (string, required): Jira story ID
- `model` (string, optional): AI model to use

**Returns:** Test scenarios including:
- Happy path scenarios (2-3)
- Edge cases (2-3)
- Error scenarios (2-3)
- Validation tests (1-2)

**Example:**
```
Use generate_test_cases with story_id="PROJ-456"
```

### analyze_sprint

Analyzes multiple Jira stories together to identify dependencies, conflicts, and generate an implementation plan.

**Parameters:**
- `story_ids` (array of strings, required): List of Jira story IDs
- `model` (string, optional): AI model to use

**Returns:** 9-section sprint analysis:
1. Sprint Overview
2. Stories Summary (table)
3. Dependency Analysis (technical, data, functional)
4. Conflicts & Overlaps
5. Risk Assessment
6. Missing Information
7. Implementation Plan (4 phases)
8. Recommendations
9. Success Metrics

**Example:**
```
Use analyze_sprint with story_ids=["PROJ-123", "PROJ-124", "PROJ-125"]
```

## Common Workflows

### Quick Reference: Tool Combinations

**Recommended workflow (thorough):**
```
1. fetch_story → Review → 2. analyze_story → 3. generate_test_cases
```

**Quick workflow (when story is known good):**
```
analyze_story → generate_test_cases
```

**Sprint planning:**
```
analyze_sprint (with multiple story IDs)
```

**Blaze Rules projects:**
```
Option 1 (with AI analysis): fetch_story → analyze_story_blaze_mode → Search codebase
Option 2 (fast, no AI): generate_blaze_prompt → Kiro searches codebase directly
```

---

### Workflow 1: Review and Analyze Story (Recommended)

**Goal:** Review story completeness before analysis, then identify gaps and generate recommendations.

**Steps:**
1. **Fetch story first** - Review description, acceptance criteria, and comments
2. **Decide if ready** - Check if story has enough information
3. **Analyze with AI** - Add any architectural notes and run analysis
4. **Generate test cases** - Create Gherkin scenarios for QA
5. **Review results** - Check for blockers and questions

**Example conversation with Kiro:**
```
You: "Fetch story PROJ-456 for me"
Kiro: [uses fetch_story]
      Story: PROJ-456
      Title: Implement user authentication
      Description: [shows full description]
      Acceptance Criteria: [shows AC]
      
You: "Looks good. Analyze this story. Note: Security critical - must comply with GDPR"
Kiro: [uses analyze_story with user_notes]
      ## 1. QUICK SUMMARY
      ...
      
You: "Generate test cases for this"
Kiro: [uses generate_test_cases]
      Feature: User Authentication
      ...
```

**Expected outcome:**
- First see complete story information
- Decide if story is ready for analysis
- Get comprehensive AI analysis with your notes included
- Receive test scenarios for QA team

**Why fetch first?**
- ✅ Review story completeness before spending AI tokens
- ✅ Identify missing information early
- ✅ Add relevant architectural notes based on what you see
- ✅ More efficient workflow

### Workflow 2: Quick Analysis (When Story is Known Good)

**Goal:** Fast analysis when you already know the story is complete.

**Steps:**
1. **Analyze directly** - Skip fetch if you trust the story is complete
2. **Review analysis** - Check gaps and technical tasks
3. **Generate tests if needed**

**Example conversation:**
```
You: "Analyze story PROJ-789 using Groq for speed"
Kiro: [uses analyze_story with model="groq/llama-3.3-70b-versatile"]
      ## 1. QUICK SUMMARY
      ...
```

**When to use:**
- Story was recently reviewed
- You're confident it's complete
- Need fast turnaround

### Workflow 3: Sprint Planning with Dependency Detection

**Goal:** Analyze multiple stories together to identify dependencies and create implementation plan.

**Steps:**
1. Collect all story IDs for the sprint
2. Run sprint analysis
3. Review dependency graph
4. Adjust sprint scope based on dependencies
5. Create implementation phases

**Example:**
```
analyze_sprint with story_ids=["PROJ-123", "PROJ-124", "PROJ-125", "PROJ-126"]
```

**Expected outcome:**
- Dependency graph showing which stories depend on others
- 4-phase implementation plan
- Risk assessment with mitigation strategies
- Clear understanding of sprint scope

### Workflow 3: Sprint Planning with Dependency Detection

**Goal:** Analyze multiple stories together to identify dependencies and create implementation plan.

**Steps:**
1. **Collect story IDs** - Get all stories for the sprint
2. **Run sprint analysis** - Analyze all together
3. **Review dependencies** - Check technical, data, and functional dependencies
4. **Adjust sprint scope** - Based on dependency graph
5. **Create phases** - Use 4-phase implementation plan

**Example conversation:**
```
You: "Analyze sprint with stories PROJ-123, PROJ-124, PROJ-125, PROJ-126"
Kiro: [uses analyze_sprint]
      ## 1. SPRINT OVERVIEW
      Sprint Goal: Implement user management system
      Total Stories: 4
      Complexity: Medium
      
      ## 3. DEPENDENCY ANALYSIS
      Technical Dependencies:
      - PROJ-123 → PROJ-124: "Story 124 requires API from 123"
      ...
```

**Expected outcome:**
- Dependency graph showing story relationships
- 4-phase implementation plan with timeline
- Risk assessment with mitigation strategies
- Clear sprint scope understanding

### Workflow 4: Blaze Rules Development

**Goal:** Find specific Blaze functions to modify for a business rules change.

**Steps:**
1. Analyze story in Blaze mode
2. Review extracted keywords
3. Use the generated search prompt to find relevant functions
4. Identify RuleFlows impacted

**Example:**
```
analyze_story_blaze_mode with story_id="PROJ-789"
```

**Expected outcome:**
- AI analysis of the requirement
- Extracted keywords: "HolidayPay", "ReserveTrip", "Edd"
- Search prompt optimized for finding Blaze functions
- Guidance on which functions to modify

**Typical Blaze workflow:**
1. Story Analyzer extracts keywords from requirements
2. Search Blaze codebase for functions matching keywords
3. Find specific functions like `fcnCalculateHolidayPayBucketFromReserve`
4. Identify RuleFlows that use these functions
5. Implement changes with confidence

## Troubleshooting

### MCP Server Connection Issues

**Problem:** MCP server won't start or connect

**Symptoms:**
- Error: "Connection refused"
- Server not responding
- Python import errors

**Solutions:**

1. **Verify Python dependencies:**
   ```bash
   pip install mcp jira litellm python-dotenv
   ```

2. **Check Python version:**
   ```bash
   python --version  # Should be 3.8+
   ```

3. **Verify server path in mcp.json:**
   - Ensure `PLACEHOLDER_SERVER_PATH` is replaced with actual path
   - Use absolute path to server.py

4. **Check environment variables:**
   - Verify all required env vars are set
   - Test Jira connection manually

5. **Review logs:**
   - Check Kiro MCP logs for specific errors
   - Look for Python tracebacks

### Jira Connection Errors

**Error:** "Could not connect to Jira"

**Causes:**
- Invalid Jira URL
- Incorrect email or API token
- Network/firewall issues
- Jira instance not accessible

**Solutions:**

1. **Verify Jira credentials:**
   ```bash
   # Test manually
   curl -u email@example.com:api_token https://your-company.atlassian.net/rest/api/3/myself
   ```

2. **Check Jira URL format:**
   - Correct: `https://your-company.atlassian.net`
   - Incorrect: `https://your-company.atlassian.net/` (trailing slash)

3. **Regenerate API token:**
   - Old tokens may expire
   - Create new token at https://id.atlassian.com/manage-profile/security/api-tokens

4. **Check network access:**
   - Verify you can access Jira in browser
   - Check VPN requirements
   - Verify firewall rules

### Acceptance Criteria Not Found

**Problem:** Story fetched but acceptance criteria is empty

**Cause:** Wrong custom field configured

**Solution:**

1. **Find the correct field:**
   - Open Jira story in browser
   - Inspect the page or use Jira API
   - Look for custom fields with acceptance criteria content

2. **Common field names:**
   - `customfield_10054`
   - `customfield_10000`
   - `customfield_10007`

3. **Update mcp.json:**
   ```json
   "JIRA_ACCEPTANCE_CRITERIA_FIELD": "customfield_XXXXX"
   ```

4. **Try multiple fields:**
   - You can specify multiple fields separated by comma
   - Example: `"customfield_10054,customfield_10000"`
   - The tool will try each until it finds content

### AI Analysis Errors

**Error:** "AI analysis failed"

**Causes:**
- Invalid API key
- Rate limit exceeded
- Model not available
- Network issues

**Solutions:**

1. **Verify API key:**
   - Check key is correctly set in environment
   - Test key with provider's API directly
   - Regenerate key if needed

2. **Try different model:**
   - If OpenAI fails, try Groq (free)
   - If rate limited, wait or use different provider

3. **Check model name:**
   - OpenAI: `gpt-4-turbo`, `gpt-4`, `gpt-3.5-turbo`
   - Anthropic: `claude-3-5-sonnet-20241022`
   - Groq: `groq/llama-3.3-70b-versatile`

4. **Verify network:**
   - Check internet connection
   - Verify no proxy issues
   - Test API endpoint directly

### Blaze Mode Not Finding Functions

**Problem:** Blaze mode generates keywords but can't find relevant functions

**Cause:** Keywords too generic or codebase structure different

**Solution:**

1. **Review extracted keywords:**
   - Check if keywords are specific enough
   - Look for compound terms like "HolidayPay" not just "Pay"

2. **Manual search:**
   - Use generated keywords as starting point
   - Search codebase for variations
   - Look for related function names

3. **Refine story description:**
   - Add more specific technical terms
   - Mention exact function names if known
   - Include RuleFlow names

4. **Use standard analysis:**
   - If Blaze mode doesn't help, use regular analyze_story
   - Manually search based on business logic description

## Best Practices

### Using with Kiro

**Natural conversation style:**
- ✅ "Fetch story PROJ-456 for me"
- ✅ "Analyze PROJ-456 and note that it's security critical"
- ✅ "Generate test cases for this story"
- ✅ "Analyze sprint with PROJ-123, PROJ-124, PROJ-125"

**Kiro will automatically:**
- Choose the right tool based on your request
- Pass parameters correctly
- Chain tools when needed

**Flexible workflows:**
- You can fetch first, then analyze (recommended)
- Or analyze directly if you trust the story is complete
- Kiro adapts to your preference

**Adding context:**
- Mention architectural notes in your request
- Example: "Analyze PROJ-456. Note: Must integrate with legacy system, 5s timeout"
- Kiro will pass your notes to the analyzer

### Story Analysis
- Always fetch story first to review completeness
- Add architectural notes for better analysis
- Use specific AI models for different needs (Groq for speed, GPT-4 for quality)
- Review analysis before sprint commitment

**Sprint Planning:**
- Analyze all stories together to find dependencies
- Pay attention to technical dependencies (APIs, services)
- Consider data dependencies (models, schemas)
- Use 4-phase plan as implementation guide

**Test Case Generation:**
- Generate test cases early in the process
- Share with QA team for review
- Use as basis for test automation
- Include in story acceptance criteria

**Blaze Rules Projects:**
- Use Blaze mode for business rules stories
- Review extracted keywords for accuracy
- Search codebase systematically
- Document RuleFlow dependencies

**AI Model Selection:**
- Groq (free): Fast, good quality, no cost
- GPT-4 Turbo: Best balance of speed and quality
- Claude 3.5 Sonnet: Excellent for complex analysis

## MCP Config Placeholders

**IMPORTANT:** Before using this power, replace the following placeholders in `mcp.json` with your actual values:

- **`PLACEHOLDER_SERVER_PATH`**: Full absolute path to the server.py file in this power directory.
  - **How to get it:**
    1. Navigate to the power directory: `cd powers/jira-story-analyzer`
    2. Get absolute path: `pwd` (Linux/Mac) or `cd` (Windows)
    3. Append `/server.py` to the path
    4. Example: `/Users/yourname/workspace/powers/jira-story-analyzer/server.py`

- **`YOUR_JIRA_URL`**: Your Jira instance URL.
  - **How to get it:** Your company's Jira URL (e.g., `https://your-company.atlassian.net`)
  - **Note:** Do not include trailing slash

- **`YOUR_JIRA_EMAIL`**: Your Jira account email.
  - **How to get it:** The email you use to log into Jira

- **`YOUR_JIRA_API_TOKEN`**: Your Jira API token.
  - **How to get it:**
    1. Go to https://id.atlassian.com/manage-profile/security/api-tokens
    2. Click "Create API token"
    3. Copy the generated token
    4. Paste here

- **`OPENAI_API_KEY_ENV_VAR`**: Environment variable name containing your OpenAI API key (or leave as placeholder if not using OpenAI).
  - **How to set it:**
    1. Get API key from https://platform.openai.com
    2. Set environment variable: `export OPENAI_API_KEY=sk-...`
    3. Or replace with actual key value (less secure)

- **`ANTHROPIC_API_KEY_ENV_VAR`**: Environment variable name containing your Anthropic API key (or leave as placeholder if not using Anthropic).
  - **How to set it:**
    1. Get API key from https://console.anthropic.com
    2. Set environment variable: `export ANTHROPIC_API_KEY=sk-ant-...`
    3. Or replace with actual key value (less secure)

- **`GROQ_API_KEY_ENV_VAR`**: Environment variable name containing your Groq API key (or leave as placeholder if not using Groq).
  - **How to set it:**
    1. Get free API key from https://console.groq.com
    2. Set environment variable: `export GROQ_API_KEY=gsk_...`
    3. Or replace with actual key value (less secure)

**After replacing placeholders, your mcp.json should look like:**
```json
{
  "mcpServers": {
    "jira-story-analyzer": {
      "command": "python",
      "args": ["/Users/yourname/workspace/powers/jira-story-analyzer/server.py"],
      "env": {
        "JIRA_URL": "https://your-company.atlassian.net",
        "JIRA_EMAIL": "your.email@company.com",
        "JIRA_API_TOKEN": "ATATT3xFfGF0...",
        "JIRA_ACCEPTANCE_CRITERIA_FIELD": "customfield_10054",
        "OPENAI_API_KEY": "sk-proj-...",
        "ANTHROPIC_API_KEY": "sk-ant-...",
        "GROQ_API_KEY": "gsk_...",
        "AI_MODEL": "gpt-4-turbo",
        "LANGUAGE": "en"
      }
    }
  }
}
```

---

**Package:** Python MCP Server (local)
**MCP Server:** jira-story-analyzer
