# StoryPromptAnalyzer

Service that converts Jira user stories into structured AI prompts and generates requirement analysis reports to detect ambiguities, gaps, and potential improvements.

## Features

- **Jira Integration**: Connect to Jira and read complete user stories
- **Multi-Provider AI Support**: OpenAI and Anthropic models
- **Bilingual Interface**: Full support for English and Spanish
- **Real-time Streaming**: See analysis results as they're generated
- **Advanced Prompt Engineering**: State-of-the-art prompting techniques
- **Comprehensive Analysis**: Identifies ambiguities, missing requirements, and risks

## Advanced Prompt Engineering Techniques

This application implements cutting-edge prompt engineering best practices:

### 1. **Structured Prompting with XML Tags**
```xml
<task>...</task>
<input_data>...</input_data>
<analysis_methodology>...</analysis_methodology>
<output_format>...</output_format>
```
- Improves model parsing and understanding
- Clear separation of concerns
- Better structured outputs

### 2. **Chain-of-Thought (CoT) Reasoning**
```
1. UNDERSTAND → 2. DECOMPOSE → 3. IDENTIFY GAPS → 4. ASSESS QUALITY → 5. FORMULATE QUESTIONS
```
- Explicit reasoning steps
- Improves analysis depth and quality
- Reduces hallucinations

### 3. **Context-Aware Dynamic Prompting**
- Analyzes what information is present/missing
- Adapts instructions based on story completeness
- Priority-aware analysis (high-priority items get extra scrutiny)

### 4. **Few-Shot Learning with Quality Examples**
```
Good: "The error handling for invalid user input is not specified..."
Bad: "Error handling needs work."
```
- Shows the model what good analysis looks like
- Improves output quality and specificity

### 5. **System Role with Expertise Definition**
```
"You are a senior software architect and QA engineer specialized in 
analyzing Jira user stories and identifying missing requirements and test cases."
```
- Sets expert persona
- Includes instruction to reason before answering
- Bilingual role definitions

### 6. **Structured Output Format**
- Predefined sections with clear templates
- Consistent formatting across analyses
- Easy to parse and present

### 7. **Story Parsing and Context Extraction**
```python
def _parse_story_context(story_data):
    # Extracts structured context
    # Identifies what's present/missing
    # Enables context-aware prompting
```

### 8. **Temperature and Token Optimization**
- **Temperature: 0.2** - More deterministic, consistent analysis
- **Max Tokens: 1200** - Balanced between completeness and conciseness
- **Streaming: True** - Real-time feedback

### 9. **Bilingual Prompt Templates**
- Separate optimized prompts for English and Spanish
- Maintains quality across languages
- Cultural and linguistic adaptation

### 10. **Explicit Guidelines and Constraints**
```
- Be specific and actionable
- Prioritize critical issues
- Provide concrete examples
- Focus on gaps, not what's already clear
```

## Analysis Output Structure

The AI generates a comprehensive 6-section analysis:

1. **Requirement Summary**
   - User story reformulation (As a... I want... So that...)
   - Business value identification
   - Core functionality description

2. **Requirement Structure**
   - Actors involved
   - Main workflow
   - Technical and business dependencies

3. **Detected Ambiguities**
   - Critical ambiguities (blocking)
   - Minor ambiguities (non-blocking)
   - Vague terms requiring definition

4. **Missing Information**
   - Acceptance criteria gaps
   - Unaddressed edge cases
   - Non-functional requirements (performance, security, scalability, accessibility)
   - Data requirements

5. **Clarification Questions**
   - For Product Owner (business logic, UX, priorities)
   - For Technical Team (implementation, integration, constraints)
   - For QA/Testing (test scenarios, error handling, validation)

6. **Recommendations**
   - Immediate actions before development
   - Quality improvements
   - Risk mitigation strategies
   - Alternative approaches

## Project Structure

```
.
├── src/
│   ├── __init__.py
│   ├── main.py              # Entry point
│   ├── gui.py               # GUI with streaming support
│   ├── jira_client.py       # Jira API integration
│   ├── ai_analyzer.py       # Advanced prompt engineering
│   ├── i18n.py              # Internationalization
│   └── settings_window.py   # Configuration UI
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   ├── test_jira_client.py
│   └── test_ai_analyzer.py
├── .env.example             # Configuration template
├── .gitignore
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository and navigate to the directory

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements-dev.txt
```

4. Configure credentials:
```bash
cp .env.example .env
```

5. Edit `.env` file with your credentials:
   - **JIRA_URL**: Your Jira instance URL (e.g., https://your-company.atlassian.net)
   - **JIRA_EMAIL**: Your Jira email
   - **JIRA_API_TOKEN**: Jira API token ([How to get it](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/))
   - **OPENAI_API_KEY**: Your OpenAI API key
   - **ANTHROPIC_API_KEY**: Your Anthropic API key
   - **AI_MODEL**: Model to use (gpt-4, gpt-3.5-turbo, claude-3-opus-20240229, etc.)
   - **LANGUAGE**: Interface language (en or es)

## Usage

### Run the application

```bash
python src/main.py
```

Or alternatively:

```bash
python -m src.gui
```

### Using the interface

1. Enter a Jira Story ID (e.g., PROJ-123)
2. Select AI Provider (OpenAI / Anthropic)
3. Choose the model
4. Click "Analyze Story"
5. Watch the analysis appear in real-time

### Available Models

- **OpenAI**: gpt-4, gpt-4-turbo, gpt-3.5-turbo
- **Anthropic**: claude-3-opus-20240229, claude-3-sonnet-20240229, claude-3-haiku-20240307

## Configuration

Access settings via **File → Settings** to configure:
- Jira connection details
- OpenAI API key
- Anthropic API key
- Default model

Change language via **Language** menu (English/Español)

## Development

### Run tests
```bash
pytest
```

### Format code
```bash
black src/ tests/
```

### Lint code
```bash
flake8 src/ tests/
```

### Type checking
```bash
mypy src/
```

## Prompt Engineering Best Practices Applied

This application demonstrates enterprise-grade prompt engineering:

✅ **Structured Prompting** - XML tags for clear sections  
✅ **Chain-of-Thought** - Explicit reasoning methodology  
✅ **Context-Aware** - Dynamic prompts based on input  
✅ **Few-Shot Learning** - Quality examples included  
✅ **Role Definition** - Expert persona with clear instructions  
✅ **Output Formatting** - Structured, parseable responses  
✅ **Temperature Control** - Optimized for consistency (0.2)  
✅ **Token Management** - Balanced completeness (1200 tokens)  
✅ **Streaming** - Real-time user feedback  
✅ **Bilingual Support** - Optimized prompts per language  

## Security

- Credentials stored in `.env` file (excluded from Git)
- Never share your `.env` file or commit credentials
- Use API tokens with minimum required permissions

## License

MIT
