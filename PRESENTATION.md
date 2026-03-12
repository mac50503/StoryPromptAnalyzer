# Story Prompt Analyzer
## AI-Powered User Story Analysis Tool

---

## 🎯 What Problem Does It Solve?

**Before:**
- Manual story review takes 15-20 minutes per story
- Inconsistent analysis quality
- Missing requirements discovered late
- Architects bottlenecked reviewing every story

**After:**
- Automated analysis in 3-5 minutes (70% faster)
- Consistent, thorough analysis every time
- Early gap detection before development starts
- Scales architect expertise across all stories

---

## 🔑 Three Core Features

### 1️⃣ Jira Integration
**Direct connection to your Jira workspace**

- Fetch stories with one click
- Automatic field detection (custom fields, acceptance criteria)
- Post analysis back to Jira as comments
- Supports child issues and sprint analysis

**Demo:** Enter story ID → Instant fetch → All data ready

---

### 2️⃣ AI Analysis Engine
**Powered by GPT-4 Turbo & Claude 3.5 Sonnet**

**What it analyzes:**
- ✅ Quick Summary (complexity, business value)
- ✅ What to Build (core features breakdown)
- ✅ Critical Gaps (blockers, risks, questions)
- ✅ Technical Tasks (backend, frontend, DB, testing)
- ✅ Next Steps (ready to start? yes/no)

**Advanced Features:**
- Sprint analysis with dependency detection
- Test case generation (Gherkin format)
- Real-time streaming responses
- Bilingual (English/Spanish)

**Demo:** Analyze story → See structured output → Copy technical tasks to Jira

---

### 3️⃣ Blaze Rules Context Mode
**Special mode for IBM Blaze Advisor projects**

**The Challenge:**
- Blaze codebases have 500+ business rule functions
- Finding the right function to modify is time-consuming
- Need to understand RuleFlow dependencies

**The Solution:**
1. Analyze story in our app (understand requirements)
2. App auto-extracts specific keywords (e.g., "HolidayPay", "ReserveTrip", "Edd")
3. Generates optimized prompt for Kiro AI
4. Copy prompt → Paste in Kiro when opening Blaze Java project
5. Kiro searches codebase and finds exact functions to modify

**Example:**
```
Story: "Holiday pay for S labeled reserve trips with EDD"

Generated Keywords: Edd, ReserveTrip, HolidayPay, Bucket

Kiro finds: fcnCalculateHolidayPayBucketFromReserve
```

**Demo:** Blaze mode → Analyze → Copy Kiro Prompt → Ready to paste

---

## 💡 Real-World Impact

**Time Savings:**
- Single story review: 15-20 min → 3-5 min
- Sprint planning: 4 hours → 2 hours
- **Total: ~12 hours/week saved per architect**

**Quality Improvements:**
- 30% fewer defects from ambiguous requirements
- 40% less architectural rework
- Early dependency detection prevents blockers

**Developer Experience:**
- Clear, actionable analysis in <1 minute read
- Technical tasks ready to copy to Jira
- No more "where do I start?" confusion

---

## 🛠️ Technical Highlights

**Architecture:**
- Python + Tkinter GUI
- LiteLLM (unified OpenAI + Anthropic interface)
- Jira REST API integration
- Export to PDF/DOCX

**Prompt Engineering:**
- XML-structured prompts for better AI parsing
- Chain-of-thought reasoning (5-step methodology)
- Few-shot learning (Good vs Bad examples)
- Anti-hallucination guidelines
- Temperature optimization (0.2 for consistency)

**Built with Kiro AI Assistant:**
- 2000+ lines of production code
- Complete in 1 session vs 2-3 weeks traditional coding
- 10-15x faster development

---

## 📊 Live Demo Flow

### Demo 1: Standard Analysis (2 minutes)
1. **Fetch from Jira**
   - Enter story ID: `PROJ-123`
   - Click "Fetch from Jira"
   - Show: Description, Acceptance Criteria, Comments

2. **AI Analysis**
   - Click "Analyze Story"
   - Watch real-time streaming
   - Show 5-section output:
     - Quick Summary
     - What to Build
     - Critical Gaps
     - Technical Tasks
     - Next Steps

3. **Post to Jira**
   - Click "Post to Jira"
   - Edit comment if needed
   - Publish → Analysis appears in Jira story

### Demo 2: Blaze Rules Context (2 minutes)
1. **Select Blaze Mode**
   - Radio button: "Blaze Rules Context"
   - Enter story about holiday pay/reserve trips

2. **Generate Kiro Prompt**
   - Click "Analyze Story"
   - Show analysis + extracted keywords
   - Show "PROMPT FOR KIRO" section

3. **Copy to Clipboard**
   - Click "📋 Copy Kiro Prompt"
   - Show prompt includes:
     - Story details
     - Suggested keywords
     - Search strategy for Kiro

4. **Explain Next Step**
   - Paste in Kiro when opening Blaze Java project
   - Kiro searches and finds specific functions
   - Kiro explains what changes are needed

---

## 🎯 Key Takeaways

1. **Jira Integration** = Seamless workflow, no context switching
2. **AI Analysis** = Consistent, thorough, fast (70% time savings)
3. **Blaze Prompt** = Bridge between story analysis and code implementation

**Result:** Architects scale their expertise, developers get clear direction, teams ship faster with fewer defects.

---

## 🚀 Getting Started

```bash
# Clone and setup
git clone https://github.com/mac50503/StoryPromptAnalyzer.git
cd StoryPromptAnalyzer
pip install -r requirements.txt

# Configure .env
JIRA_URL=https://your-company.atlassian.net
JIRA_EMAIL=your-email@company.com
JIRA_API_TOKEN=your-token
OPENAI_API_KEY=your-key

# Run
python src/main.py
```

**Questions?**

GitHub: [github.com/mac50503/StoryPromptAnalyzer](https://github.com/mac50503/StoryPromptAnalyzer)
