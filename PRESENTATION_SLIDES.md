---
marp: true
theme: default
paginate: true
backgroundColor: #fff
---

# Story Prompt Analyzer
## AI-Powered User Story Analysis

Miguel Angel Cervantes Juarez
Software Architect

---

# What It Does

Analyzes Jira user stories using AI to:
- Identify gaps and ambiguities
- Generate technical tasks
- Create test cases
- Detect dependencies in sprints

**Built with Kiro AI Assistant**

---

# System Architecture

```
┌─────────────────────────────────────────────────────┐
│                  GUI Layer (Tkinter)                 │
│                                                      │
│  Single Story Tab  |  Sprint Analysis  |  Settings  │
└──────────────────────┬──────────────────────────────┘
                       │
┌──────────────────────┼──────────────────────────────┐
│            Business Logic Layer                      │
│                                                      │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────┐ │
│  │ AIAnalyzer   │  │ JiraClient   │  │   I18n   │ │
│  │ (1478 lines) │  │ (180 lines)  │  │(200 lines│ │
│  └──────┬───────┘  └──────┬───────┘  └──────────┘ │
└─────────┼──────────────────┼──────────────────────┘
          │                  │
          ▼                  ▼
┌─────────────────┐  ┌─────────────────┐
│   LiteLLM API   │  │   Jira REST API │
│ OpenAI/Anthropic│  │                 │
│ Groq (Free)     │  │                 │
└─────────────────┘  └─────────────────┘
```

---

# Module Structure

```
src/
├── main.py                 # Entry point
├── gui.py                  # Main UI (1508 lines)
├── ai_analyzer.py          # AI engine (1478 lines)
├── jira_client.py          # Jira integration (180 lines)
├── jira_formatter.py       # Markdown → Jira (100 lines)
├── settings_window.py      # Config UI (200 lines)
├── i18n.py                 # Translations (200 lines)
├── export_utils.py         # PDF/DOCX export (200 lines)
└── rich_text_viewer.py     # Enhanced display (100 lines)

Total: 2000+ lines of production code
```

---

# Flow Diagram: Single Story Analysis

```
┌─────────────┐
│ User Input  │
│ Story ID    │
└──────┬──────┘
       │
       ▼
┌─────────────────────────┐
│ 1. Fetch from Jira      │
│    - Get story data     │
│    - Get AC fields      │
│    - Get comments       │
└──────┬──────────────────┘
       │
       ▼
┌─────────────────────────┐
│ 2. Display Story Info   │
│    - User reviews       │
│    - Add notes          │
└──────┬──────────────────┘
       │
       ▼
┌─────────────────────────┐
│ 3. AI Analysis          │
│    - Build prompt       │
│    - Call AI (stream)   │
│    - Parse response     │
└──────┬──────────────────┘
       │
       ▼
┌─────────────────────────┐
│ 4. Generate Output      │
│    - 5 sections         │
│    - Technical tasks    │
│    - Test cases         │
└──────┬──────────────────┘
       │
       ▼
┌─────────────────────────┐
│ 5. Export/Publish       │
│    - PDF/DOCX           │
│    - Post to Jira       │
└─────────────────────────┘
```

---

# Flow Diagram: Blaze Rules Context Mode

```
┌─────────────────────────┐
│ User Story (Blaze)      │
└──────┬──────────────────┘
       │
       ▼
┌─────────────────────────┐
│ AI Analysis             │
│ (Standard)              │
└──────┬──────────────────┘
       │
       ▼
┌─────────────────────────┐
│ Extract Keywords        │
│ "holiday pay" →         │
│ "HolidayPay"            │
└──────┬──────────────────┘
       │
       ▼
┌─────────────────────────┐
│ Generate Kiro Prompt    │
│ - Story details         │
│ - Keywords              │
│ - Search instructions   │
└──────┬──────────────────┘
       │
       ▼
┌─────────────────────────┐
│ Copy to Clipboard       │
└──────┬──────────────────┘
       │
       ▼
┌─────────────────────────┐
│ Paste in Kiro           │
│ (Blaze Java Project)    │
└──────┬──────────────────┘
       │
       ▼
┌─────────────────────────┐
│ Kiro Finds Functions    │
│ fcnCalculateHoliday...  │
└─────────────────────────┘
```

---

# Key Features

**1. Jira Integration**
- Direct API connection
- Flexible custom field support
- Debug tool for field discovery

**2. AI Analysis**
- OpenAI (GPT-4) or Anthropic (Claude)
- Streaming responses
- 5-section structured output

**3. Blaze Rules Context**
- Auto-extract keywords
- Generate Kiro prompts
- Search Blaze codebase

---

# Tech Stack

```
Frontend:  Python Tkinter
Backend:   Python 3.8+
AI:        LiteLLM (OpenAI + Anthropic)
APIs:      Jira REST API
Export:    python-docx, reportlab
Config:    python-dotenv
```

---

# Demo

Live demonstration of:
1. Fetch story from Jira
2. Analyze with AI
3. Generate Kiro prompt (Blaze mode)
4. Export to PDF

---

# Results

**Time Savings:**
- Story review: 15-20 min → 3-5 min (70% faster)
- Sprint planning: 4 hours → 2 hours (50% faster)

**Development:**
- Built in 1 session with Kiro (vs 2-3 weeks)
- 2000+ lines of production code
- 10-15x faster development

---

# Q&A

Questions?

**GitHub:** https://github.com/mac50503/StoryPromptAnalyzer
**Contact:** Miguel Angel Cervantes Juarez

---

# Thank You!

**Built with ❤️ using Kiro AI Assistant**
