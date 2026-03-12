---
marp: true
theme: default
paginate: true
backgroundColor: #fff
---

# Story Prompt Analyzer
## AI-Powered User Story Analysis Tool

**Miguel Angel Cervantes Juarez**
Software Architect

---

## 🎯 The Problem

**Before:**
- ⏱️ Manual story review: 15-20 minutes per story
- ❌ Inconsistent analysis quality
- 🐛 Missing requirements discovered late
- 🚧 Architects bottlenecked reviewing every story

---

## ✅ The Solution

**After:**
- ⚡ Automated analysis: 3-5 minutes (70% faster)
- ✓ Consistent, thorough analysis every time
- 🎯 Early gap detection before development
- 📈 Scales architect expertise across all stories

---

## 🔑 Three Core Features

1. **Jira Integration**
2. **AI Analysis Engine**
3. **Blaze Rules Context Mode**

---

# 1️⃣ Jira Integration
## Direct connection to your Jira workspace

- ✅ Fetch stories with one click
- ✅ Automatic field detection
- ✅ Post analysis back to Jira as comments
- ✅ Supports child issues and sprint analysis

**Demo:** Enter story ID → Instant fetch → All data ready

---

# 2️⃣ AI Analysis Engine
## Powered by GPT-4 Turbo & Claude 3.5 Sonnet

**5-Section Analysis:**
1. Quick Summary (complexity, business value)
2. What to Build (core features breakdown)
3. Critical Gaps (blockers, risks, questions)
4. Technical Tasks (backend, frontend, DB, testing)
5. Next Steps (ready to start? yes/no)

---

## AI Analysis - Advanced Features

- 📊 Sprint analysis with dependency detection
- 🧪 Test case generation (Gherkin format)
- ⚡ Real-time streaming responses
- 🌍 Bilingual (English/Spanish)

**Demo:** Analyze story → Structured output → Copy tasks to Jira

---

# 3️⃣ Blaze Rules Context Mode
## For IBM Blaze Advisor projects

**The Challenge:**
- 500+ business rule functions in codebase
- Finding the right function is time-consuming
- Need to understand RuleFlow dependencies

---

## Blaze Mode - The Solution

**Workflow:**
1. Analyze story in our app
2. App auto-extracts keywords
   - Example: "HolidayPay", "ReserveTrip", "Edd"
3. Generates optimized prompt for Kiro AI
4. Copy → Paste in Kiro (Blaze Java project)
5. Kiro finds exact functions to modify

---

## Blaze Mode - Example

**Story:**
> "Holiday pay for S labeled reserve trips with EDD"

**Generated Keywords:**
`Edd, ReserveTrip, HolidayPay, Bucket`

**Kiro Finds:**
`fcnCalculateHolidayPayBucketFromReserve`

---

## 💡 Real-World Impact

**Time Savings:**
- Single story: 15-20 min → 3-5 min
- Sprint planning: 4 hours → 2 hours
- **~12 hours/week saved per architect**

**Quality:**
- 30% fewer defects
- 40% less rework
- Early dependency detection

---

## 🛠️ Technical Highlights

- Python + Tkinter GUI
- LiteLLM (OpenAI + Anthropic)
- Jira REST API integration
- Export to PDF/DOCX

**Prompt Engineering:**
- XML-structured prompts
- Chain-of-thought reasoning
- Few-shot learning
- Anti-hallucination guidelines

---

## 📊 Live Demo

**Demo 1: Standard Analysis (2 min)**
1. Fetch from Jira
2. AI Analysis (real-time streaming)
3. Post back to Jira

**Demo 2: Blaze Rules Context (2 min)**
1. Select Blaze mode
2. Generate Kiro prompt
3. Copy to clipboard

---

## 🎯 Key Takeaways

1. **Jira Integration** = Seamless workflow
2. **AI Analysis** = 70% time savings
3. **Blaze Prompt** = Bridge to implementation

**Result:** Architects scale expertise, developers get clarity, teams ship faster.

---

## 🚀 Getting Started

```bash
git clone https://github.com/mac50503/StoryPromptAnalyzer.git
cd StoryPromptAnalyzer
pip install -r requirements.txt
python src/main.py
```

**GitHub:** [github.com/mac50503/StoryPromptAnalyzer](https://github.com/mac50503/StoryPromptAnalyzer)

---

# Questions?

**Thank you!**

Miguel Angel Cervantes Juarez
[@mac50503](https://github.com/mac50503)
