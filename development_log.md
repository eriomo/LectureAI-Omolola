# LectureAI – Development Log
**For use in Project Report – Section 6 (Results) and Section 7 (Discussion)**
Omolola | University of Idaho | Feb 2026

---

## Challenge 1: Python Installation Delay
**What happened:**
During Week 1 setup, Python took an unexpectedly long time to install on the development machine, blocking initial testing of the Streamlit app.

**Impact:**
Delayed local testing of the core prototype by approximately 1–2 hours.

**How it was resolved:**
Switched to a pure HTML/JavaScript implementation that runs directly in any browser — no installation required. This actually improved the prototype's accessibility since it works on phones, tablets, and laptops without any setup.

**What this teaches (for report):**
This reflects a real engineering trade-off: Streamlit is more powerful but requires a Python environment. An HTML file is more portable and immediately testable. For a prototype meant to demonstrate a concept, portability often matters more than power.

---

## Challenge 2: API Access Blocked by Browser (CORS Error)
**What happened:**
When connecting the prototype to the Claude AI API directly from the browser, the app returned:
> "Error: Invalid response format"
This appeared in the browser console on mobile (iPhone).

**Technical cause:**
Browsers enforce a security policy called CORS (Cross-Origin Resource Sharing). When a webpage tries to call an external API directly, the browser blocks it unless the API explicitly allows it. The Anthropic API does not allow direct browser-to-API calls for security reasons.

**Impact:**
The AI-powered version of the app (lectureai_ai_powered.html) failed to generate any lesson plans on mobile and would similarly fail in most standard browser environments.

**How it was resolved:**
Replaced the external API call with a smart topic-aware content engine built entirely inside the app. The engine:
- Detects the category of topic entered (statistics, machine learning, data cleaning, visualization, programming, ethics)
- Generates content that is specific and relevant to that category
- Produces different analogies, activities, practice questions, and micro-explanations depending on topic type
- Simulates a realistic AI loading experience with sequential status messages

**What this teaches (for report):**
This is a common challenge in web-based AI prototyping. The standard solution in production systems is to route API calls through a backend server (e.g. Flask or FastAPI) which is not subject to browser CORS restrictions. For this prototype stage, a sophisticated template engine achieves the same demonstrative purpose without requiring server infrastructure. Future work should implement a proper backend to enable live LLM integration.

---

## Challenge 3: Output Repetitiveness (Identified, Not Yet Resolved)
**What happened:**
Early versions of the mock output engine produced nearly identical content regardless of the topic entered. For example, "Linear Regression" and "Decision Trees" returned structurally identical lesson plans with only the topic name swapped in.

**Impact:**
This weakens the prototype's pedagogical value — a key claim of the paper is that AI can generate *differentiated* content tailored to the specific topic and learner profile. If all outputs look the same, this claim cannot be demonstrated.

**How it was resolved:**
Built a topic detection system that identifies 6 subject categories and generates category-specific content for each section of the lesson plan. This means "Data Cleaning" now produces genuinely different analogies, activities and questions than "Neural Networks."

**What this teaches (for report):**
Even without a live LLM, a well-designed template system can demonstrate the *principle* of personalization. However, this also highlights a key limitation: true AI-generated content would be unique for every topic, every run, and every learner profile — something templates cannot fully replicate. This is the strongest argument for integrating a real LLM in future iterations.

---

## Challenge 4: Scope Management (Ongoing)
**What happened:**
The original paper describes three layers of co-orchestration: pre-lecture design, in-class real-time adaptation, and post-lecture personalization. Building all three in a prototype within 6 weeks is unrealistic.

**How it was resolved:**
Prototype scope was limited to Layer 1 (pre-lecture design) and Layer 3 (post-lecture student support). Layer 2 (real-time in-class adaptation) is noted as future work.

**What this teaches (for report):**
Scope decisions are a legitimate part of software development and research. Clearly stating what was built AND what was intentionally excluded — and why — demonstrates research maturity. It is better to build two layers well than three layers poorly.

---

## Key Design Decisions (also worth mentioning in report)

| Decision | Chosen Approach | Alternative Considered | Reason |
|---|---|---|---|
| Frontend framework | HTML/CSS/JS | Streamlit (Python) | Portability — works on any device without installation |
| AI integration | Smart template engine | Live LLM API | Browser CORS restrictions; no backend server available |
| Data storage | In-memory (session only) | SQLite / JSON files | Simplicity for MVP; no server required |
| ICAP labelling | Hardcoded per segment type | AI-generated labels | Ensures pedagogical accuracy in prototype |
| Export format | Plain text + JSON | PDF | Simpler to implement; sufficient for prototype evaluation |

---

## Prototype Versions (track these for report appendix)

| Version | File | What Changed |
|---|---|---|
| v0.1 | lectureai_demo.html | Basic mock — same output for every topic |
| v0.2 | lectureai_ai_powered.html | Connected to Claude API — blocked by CORS |
| v0.3 | lectureai_fixed.html | Topic-aware engine — works on all devices, no errors |

---

*This log should be referenced in Report Sections 4 (Implementation), 6 (Results), and 7 (Discussion/Limitations).*
