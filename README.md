# LectureAI – Human–AI Co-Orchestration Demo

A Streamlit prototype implementing the framework from:

> Jamil, H. M. (2025). *Human–AI Co-Orchestration in Data Science Education: Interactive, Adaptive, and Personalized Lecture Design for Diverse Learners.* ACM Transactions on Computing Education. https://doi.org/10.1145/3785369

**Implemented by:** Omolola  
**Supervised by:** Prof. Hasan Jamil, University of Idaho  
**Date:** February 2026

---

## What This Prototype Does

| Feature | Description |
|---|---|
| 📋 Lesson Builder | Instructor inputs topic, objectives, level, duration & style → generates full lecture outline |
| 🏷️ ICAP Tagging | Every segment and activity is tagged as Passive / Active / Constructive / Interactive |
| ✏️ Human Override | Instructor can add notes and approve/reject each segment |
| 📚 Student Support | Micro-explanations, practice questions (Easy/Medium/Hard), SRL prompts |
| 📊 Evaluation Rubric | Score output on 5 pedagogical criteria (1–5 scale) |
| 📁 Export | Download lesson plan as JSON or plain text |

## How to Run

```bash
# 1. Clone or unzip the project
cd lesson_demo

# 2. Install dependencies (Python 3.9+ recommended)
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

The app will open at `http://localhost:8501` in your browser.

## Project Structure

```
lesson_demo/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md           # This file
└── (future folders)
    ├── prompts/        # Prompt templates (for API version)
    ├── data/           # Sample test topics & saved outputs
    ├── tests/          # Evaluation sheets
    ├── screenshots/    # For report figures
    └── report/         # Report drafts
```

## Current Status: Mock Mode
All outputs are generated from intelligent templates — **no API key required**.  
When ready to switch to real AI: replace the `generate_lesson()` function body in `app.py` with an OpenAI or Gemini API call using the same input parameters.

## Three-Layer Framework (from Jamil 2025)

| Layer | When | ChatGPT Role in Paper | This Prototype |
|---|---|---|---|
| Pre-lecture | Before class | Co-designer | ✅ Lesson Builder |
| In-lecture | During class | Real-time orchestrator | ⬜ Future work |
| Post-lecture | After class | Personalization engine | ✅ Student Support |

## Test Topics to Try
- Linear Regression
- Decision Trees
- Data Cleaning and Missing Values
- SQL Joins
- Probability and Distributions
- Neural Networks (Intro)

## Weekly Progress Log
| Week | Status | Notes |
|---|---|---|
| 1 | ✅ Done | Paper read, prototype built (mock mode) |
| 2 | ⬜ | Design doc, wireframes, prompt library |
| 3 | ⬜ | Core API integration |
| 4 | ⬜ | Evaluation + student support expansion |
| 5 | ⬜ | Testing + iteration |
| 6 | ⬜ | Final report |
