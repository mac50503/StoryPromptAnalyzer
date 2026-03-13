#!/usr/bin/env python3
"""MCP Server for Jira Story Analyzer."""

import asyncio
import sys
import os
from typing import Any

# Add parent directory to path to import from src
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from mcp.server import Server
from mcp.types import Tool, TextContent
from src.jira_client import JiraClient
from src.ai_analyzer import AIAnalyzer

# Initialize server
app = Server("jira-story-analyzer")

# Global clients (initialized on first use)
jira_client = None
ai_analyzer = None


def get_jira_client():
    """Get or create Jira client."""
    global jira_client
    if jira_client is None:
        jira_client = JiraClient.from_env()
    return jira_client


def get_ai_analyzer(model: str = None):
    """Get or create AI analyzer."""
    global ai_analyzer
    if ai_analyzer is None or (model and ai_analyzer.model != model):
        ai_analyzer = AIAnalyzer(
            model=model or os.getenv("AI_MODEL", "gpt-4-turbo"),
            language=os.getenv("LANGUAGE", "en")
        )
    return ai_analyzer


@app.list_tools()
async def list_tools() -> list[Tool]:
    """List available tools."""
    return [
        Tool(
            name="fetch_story",
            description="Fetch a Jira user story with all details including description, acceptance criteria, and comments",
            inputSchema={
                "type": "object",
                "properties": {
                    "story_id": {
                        "type": "string",
                        "description": "Jira story ID (e.g., PROJ-123)"
                    }
                },
                "required": ["story_id"]
            }
        ),
        Tool(
            name="analyze_story",
            description="Analyze a Jira story using AI to identify gaps, generate technical tasks, and provide recommendations. Returns structured 5-section analysis.",
            inputSchema={
                "type": "object",
                "properties": {
                    "story_id": {
                        "type": "string",
                        "description": "Jira story ID (e.g., PROJ-123)"
                    },
                    "model": {
                        "type": "string",
                        "description": "AI model to use (gpt-4-turbo, claude-3-5-sonnet-20241022, groq/llama-3.3-70b-versatile)",
                        "default": "gpt-4-turbo"
                    },
                    "user_notes": {
                        "type": "string",
                        "description": "Optional additional context or notes from the user"
                    }
                },
                "required": ["story_id"]
            }
        ),
        Tool(
            name="analyze_story_blaze_mode",
            description="Analyze a Jira story for Blaze Rules projects. Extracts specific keywords and generates a prompt optimized for searching Blaze codebase.",
            inputSchema={
                "type": "object",
                "properties": {
                    "story_id": {
                        "type": "string",
                        "description": "Jira story ID (e.g., PROJ-123)"
                    },
                    "model": {
                        "type": "string",
                        "description": "AI model to use",
                        "default": "gpt-4-turbo"
                    }
                },
                "required": ["story_id"]
            }
        ),
        Tool(
            name="generate_blaze_prompt",
            description="Generate ONLY the Kiro search prompt for Blaze Rules projects without AI analysis. Fast and free - just extracts story info and formats it for Kiro to analyze the codebase.",
            inputSchema={
                "type": "object",
                "properties": {
                    "story_id": {
                        "type": "string",
                        "description": "Jira story ID (e.g., PROJ-123)"
                    }
                },
                "required": ["story_id"]
            }
        ),
        Tool(
            name="generate_test_cases",
            description="Generate comprehensive test cases in Gherkin format (Given-When-Then) for a Jira story",
            inputSchema={
                "type": "object",
                "properties": {
                    "story_id": {
                        "type": "string",
                        "description": "Jira story ID (e.g., PROJ-123)"
                    },
                    "model": {
                        "type": "string",
                        "description": "AI model to use",
                        "default": "gpt-4-turbo"
                    }
                },
                "required": ["story_id"]
            }
        ),
        Tool(
            name="analyze_sprint",
            description="Analyze multiple Jira stories together to identify dependencies, conflicts, and generate implementation plan",
            inputSchema={
                "type": "object",
                "properties": {
                    "story_ids": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of Jira story IDs (e.g., ['PROJ-123', 'PROJ-124'])"
                    },
                    "model": {
                        "type": "string",
                        "description": "AI model to use",
                        "default": "gpt-4-turbo"
                    }
                },
                "required": ["story_ids"]
            }
        )
    ]


@app.call_tool()
async def call_tool(name: str, arguments: Any) -> list[TextContent]:
    """Handle tool calls."""
    
    try:
        if name == "fetch_story":
            story_id = arguments["story_id"]
            client = get_jira_client()
            story_data = client.get_user_story(story_id)
            
            result = f"""Story: {story_data['key']}
Title: {story_data['title']}
Status: {story_data['status']}
Priority: {story_data['priority']}
Labels: {', '.join(story_data['labels']) if story_data['labels'] else 'None'}

Description:
{story_data['description'] or 'No description'}

Acceptance Criteria:
{story_data['acceptance_criteria'] or 'No acceptance criteria'}

Comments ({len(story_data['comments'])}):
{chr(10).join(f'- {c}' for c in story_data['comments']) if story_data['comments'] else 'No comments'}
"""
            return [TextContent(type="text", text=result)]
        
        elif name == "analyze_story":
            story_id = arguments["story_id"]
            model = arguments.get("model", "gpt-4-turbo")
            user_notes = arguments.get("user_notes")
            
            client = get_jira_client()
            story_data = client.get_user_story(story_id)
            
            if user_notes:
                story_data['user_notes'] = user_notes
            
            analyzer = get_ai_analyzer(model)
            analysis = analyzer.analyze_story(story_data, use_kb_context=False)
            
            return [TextContent(type="text", text=analysis)]
        
        elif name == "analyze_story_blaze_mode":
            story_id = arguments["story_id"]
            model = arguments.get("model", "gpt-4-turbo")
            
            client = get_jira_client()
            story_data = client.get_user_story(story_id)
            
            analyzer = get_ai_analyzer(model)
            
            # Perform analysis
            analysis = analyzer.analyze_story(story_data, use_kb_context=False)
            
            # Generate Kiro prompt
            kiro_prompt = analyzer._generate_kiro_prompt(story_data, analysis)
            
            result = f"""ANALYSIS:
{analysis}

{'='*80}

KIRO PROMPT FOR BLAZE CODEBASE:
{kiro_prompt}
"""
            return [TextContent(type="text", text=result)]
        
        elif name == "generate_blaze_prompt":
            story_id = arguments["story_id"]
            
            client = get_jira_client()
            story_data = client.get_user_story(story_id)
            
            # Generate prompt without AI analysis (fast and free)
            kiro_prompt = f"""I need help implementing this Blaze Rules user story:

STORY: {story_data['title']}

DESCRIPTION:
{story_data['description'] or 'No description'}

ACCEPTANCE CRITERIA:
{story_data['acceptance_criteria'] or 'No acceptance criteria'}

YOUR TASK:
1. Search in the knowledge-base folder for relevant Blaze functions (fcn*) or rulesets (rs*)
2. Identify the MOST SPECIFIC functions that need modification based on the business logic
3. For each function found:
   - Explain what changes are needed
   - Identify which RuleFlows use it
   - Suggest specific test cases
4. Identify potential regression risks

SEARCH STRATEGY:
- Look for functions related to the business logic described above
- Check function implementations to confirm they handle the exact scenario
- Prioritize functions that match the acceptance criteria requirements

Start by searching the knowledge-base and show me the top 3-5 most relevant functions.
"""
            
            return [TextContent(type="text", text=kiro_prompt)]
        
        elif name == "generate_test_cases":
            story_id = arguments["story_id"]
            model = arguments.get("model", "gpt-4-turbo")
            
            client = get_jira_client()
            story_data = client.get_user_story(story_id)
            
            analyzer = get_ai_analyzer(model)
            test_cases = analyzer.generate_test_cases(story_data)
            
            return [TextContent(type="text", text=test_cases)]
        
        elif name == "analyze_sprint":
            story_ids = arguments["story_ids"]
            model = arguments.get("model", "gpt-4-turbo")
            
            client = get_jira_client()
            stories_data = []
            for sid in story_ids:
                story_data = client.get_user_story(sid)
                stories_data.append(story_data)
            
            analyzer = get_ai_analyzer(model)
            sprint_analysis = analyzer.analyze_sprint(stories_data)
            
            return [TextContent(type="text", text=sprint_analysis)]
        
        else:
            return [TextContent(type="text", text=f"Unknown tool: {name}")]
    
    except Exception as e:
        return [TextContent(type="text", text=f"Error: {str(e)}")]


async def main():
    """Run the MCP server."""
    from mcp.server.stdio import stdio_server
    
    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )


if __name__ == "__main__":
    asyncio.run(main())
