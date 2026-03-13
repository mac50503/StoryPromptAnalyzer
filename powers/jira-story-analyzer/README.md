# Jira Story Analyzer - Kiro Power

AI-powered analysis of Jira user stories to identify gaps, generate technical tasks, and create test cases.

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure credentials (IMPORTANT):**
   
   The `mcp.json` file in this repo contains PLACEHOLDERS only. To use this power:
   
   **Option A: Create local config (recommended for security)**
   ```bash
   # Copy template to local config (not tracked by git)
   cp mcp.json mcp.local.json
   
   # Edit mcp.local.json with your real credentials
   # Then use mcp.local.json when installing the power in Kiro
   ```
   
   **Option B: Edit mcp.json directly (less secure)**
   ```bash
   # Edit mcp.json with your credentials
   # WARNING: Don't commit real credentials to git!
   ```
   
   **Required replacements:**
   - `PLACEHOLDER_SERVER_PATH` → Absolute path to `server.py`
   - `YOUR_JIRA_URL` → Your Jira instance URL
   - `YOUR_JIRA_EMAIL` → Your Jira email
   - `YOUR_JIRA_API_TOKEN` → Your Jira API token
   - `OPENAI_API_KEY_ENV_VAR` → Your OpenAI key (or env var name)
   - `ANTHROPIC_API_KEY_ENV_VAR` → Your Anthropic key (or env var name)
   - `GROQ_API_KEY_ENV_VAR` → Your Groq key (or env var name)

3. **Install in Kiro:**
   - Open Kiro Powers UI
   - Click "Add Custom Power"
   - Select "Local Directory"
   - Point to this directory
   - When prompted for config, use `mcp.local.json` (if you created it)

4. **Test:**
   ```
   Use fetch_story with story_id="YOUR-STORY-ID"
   ```

## Security Note

⚠️ **Never commit real credentials to git!**

- The `mcp.json` in this repo has PLACEHOLDERS only
- Use `mcp.local.json` for your real credentials (already in .gitignore)
- Or use environment variables for API keys

## Features

- ✅ Fetch Jira stories with all details
- ✅ AI-powered gap analysis
- ✅ Generate test cases in Gherkin format
- ✅ Sprint analysis with dependency detection
- ✅ Blaze Rules Context mode for business rules projects
- ✅ Support for OpenAI, Anthropic, and Groq (free)

## Documentation

See [POWER.md](POWER.md) for complete documentation including:
- Onboarding and setup
- All available tools
- Common workflows
- Troubleshooting guide
- Best practices

## Requirements

- Python 3.8+
- Jira account with API access
- At least one AI provider API key (OpenAI, Anthropic, or Groq)

## Author

Miguel Angel Cervantes Juarez

## License

MIT
