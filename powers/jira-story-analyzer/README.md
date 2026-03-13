# Jira Story Analyzer - Kiro Power

AI-powered analysis of Jira user stories to identify gaps, generate technical tasks, and create test cases.

## Quick Start

### Installation Options

**Option 1: Install from GitHub (Recommended)**

1. **Open Kiro Powers UI:**
   - Command Palette (Ctrl+Shift+P) → "Powers: Configure"
   - Or click Powers icon in sidebar

2. **Add Custom Power:**
   - Click "Add Custom Power"
   - Select "GitHub Repository"
   - Enter URL: `https://github.com/mac50503/StoryPromptAnalyzer`
   - Kiro will find the power in `powers/jira-story-analyzer/`

3. **Configure credentials:**
   
   After installation, you need to configure your credentials. Two options:
   
   **Option A: Edit Kiro's MCP config (Recommended)**
   - Open `.kiro/settings/mcp.json` in your workspace
   - Add the server configuration with your real credentials:
   
   ```json
   {
     "mcpServers": {
       "jira-story-analyzer": {
         "command": "python",
         "args": ["<PATH_TO_POWER>/server.py"],
         "env": {
           "JIRA_URL": "https://your-company.atlassian.net",
           "JIRA_EMAIL": "your.email@company.com",
           "JIRA_API_TOKEN": "your_jira_token",
           "JIRA_ACCEPTANCE_CRITERIA_FIELD": "customfield_10054",
           "OPENAI_API_KEY": "your_openai_key",
           "ANTHROPIC_API_KEY": "your_anthropic_key",
           "GROQ_API_KEY": "your_groq_key",
           "AI_MODEL": "gpt-4-turbo",
           "LANGUAGE": "en"
         }
       }
     }
   }
   ```
   
   **Option B: Use environment variables**
   - Set environment variables in your system:
   ```bash
   export JIRA_URL="https://your-company.atlassian.net"
   export JIRA_EMAIL="your.email@company.com"
   export JIRA_API_TOKEN="your_jira_token"
   export OPENAI_API_KEY="your_openai_key"
   # etc...
   ```

4. **Reconnect the MCP server:**
   - Command Palette → "MCP: Reconnect Server"
   - Select "jira-story-analyzer"

5. **Test:**
   ```
   Fetch story YOUR-STORY-ID
   ```

**Option 2: Install from Local Directory**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mac50503/StoryPromptAnalyzer.git
   cd StoryPromptAnalyzer/powers/jira-story-analyzer
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create local config with your credentials:**
   ```bash
   cp mcp.json mcp.local.json
   # Edit mcp.local.json with your real credentials
   ```
   
   **Required replacements in mcp.local.json:**
   - `PLACEHOLDER_SERVER_PATH` → Absolute path to `server.py`
   - `YOUR_JIRA_URL` → Your Jira instance URL
   - `YOUR_JIRA_EMAIL` → Your Jira email
   - `YOUR_JIRA_API_TOKEN` → Your Jira API token
   - `OPENAI_API_KEY_ENV_VAR` → Your OpenAI key (or env var name)
   - `ANTHROPIC_API_KEY_ENV_VAR` → Your Anthropic key (or env var name)
   - `GROQ_API_KEY_ENV_VAR` → Your Groq key (or env var name)

4. **Install in Kiro:**
   - Open Kiro Powers UI
   - Click "Add Custom Power"
   - Select "Local Directory"
   - Point to: `<your-path>/StoryPromptAnalyzer/powers/jira-story-analyzer`
   - When prompted for config, use `mcp.local.json`

5. **Test:**
   ```
   Fetch story YOUR-STORY-ID
   ```

### Getting API Keys

**Jira API Token:**
- Go to https://id.atlassian.com/manage-profile/security/api-tokens
- Click "Create API token"
- Copy the token

**AI Provider (choose at least one):**

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

### Finding Your Acceptance Criteria Field

Different Jira instances use different custom fields. To find yours:

1. Open any Jira story that has acceptance criteria
2. Use the Jira REST API or inspect the story JSON
3. Look for custom fields like `customfield_10054`, `customfield_10000`, etc.
4. Common field names: `customfield_10054`, `customfield_10000`, `customfield_10007`

**Note:** The power will try multiple common fields automatically, but specifying the correct one improves reliability.

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

## Security Note

⚠️ **Never commit real credentials to git!**

- The `mcp.json` in this repo has PLACEHOLDERS only
- When installing from GitHub, configure credentials in `.kiro/settings/mcp.json` or use environment variables
- When installing locally, use `mcp.local.json` for your real credentials (already in .gitignore)
- The `.kiro/` folder (which may contain credentials) is also in .gitignore

## Repository

Part of [StoryPromptAnalyzer](https://github.com/mac50503/StoryPromptAnalyzer) project.
