import streamlit as st
import json
import random
from datetime import datetime

# ─── PAGE CONFIG ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="LectureAI – Human–AI Co-Orchestration",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── CUSTOM CSS ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@300;400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}
h1, h2, h3 { font-family: 'DM Serif Display', serif; }

.main { background-color: #f7f5f2; }

.block-container { padding-top: 2rem; padding-bottom: 2rem; }

.card {
    background: white;
    border-radius: 12px;
    padding: 1.4rem 1.6rem;
    margin-bottom: 1rem;
    border-left: 4px solid #2d6a4f;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}

.icap-badge {
    display: inline-block;
    padding: 3px 10px;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.5px;
    margin-left: 8px;
}
.badge-passive  { background: #fde8d8; color: #c0440a; }
.badge-active   { background: #d8f0e8; color: #1a6640; }
.badge-constructive { background: #dce8fd; color: #1a3f80; }
.badge-interactive  { background: #f0d8fd; color: #6a1a80; }

.section-header {
    font-family: 'DM Serif Display', serif;
    font-size: 1.1rem;
    color: #1a1a1a;
    margin-top: 1rem;
    margin-bottom: 0.5rem;
    border-bottom: 2px solid #e8e4de;
    padding-bottom: 0.3rem;
}

.metric-box {
    background: #f0faf4;
    border: 1px solid #b7dfc8;
    border-radius: 8px;
    padding: 0.8rem 1rem;
    text-align: center;
}

.stButton > button {
    background-color: #2d6a4f;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 0.5rem 1.5rem;
    font-weight: 600;
    font-family: 'DM Sans', sans-serif;
}
.stButton > button:hover { background-color: #1e4d38; }

.difficulty-easy   { color: #1a6640; font-weight: 600; }
.difficulty-medium { color: #7a5900; font-weight: 600; }
.difficulty-hard   { color: #c0440a; font-weight: 600; }
</style>
""", unsafe_allow_html=True)


# ─── MOCK TEMPLATE ENGINE ────────────────────────────────────────────────────

ICAP_LABELS = ["Passive", "Active", "Constructive", "Interactive"]

def badge(label):
    cls = f"badge-{label.lower()}"
    return f'<span class="icap-badge {cls}">{label}</span>'


def generate_lesson(topic, objectives, level, duration, style):
    """
    Mock lesson generator – returns a structured lesson plan dict.
    Replace the return value with an LLM API call when ready.
    """

    style_map = {
        "Lecture-based":   "clear, structured explanations with worked examples",
        "Discussion-based":"open questions and guided class discussion",
        "Project-based":   "hands-on mini-tasks and real-world case studies",
        "Flipped":         "pre-class reading prompts and in-class application activities",
    }
    style_desc = style_map.get(style, "balanced instruction")

    intro_min   = max(5, int(duration * 0.12))
    concept_min = max(10, int(duration * 0.35))
    activity_min= max(10, int(duration * 0.30))
    wrapup_min  = max(5, int(duration * 0.12))
    qanda_min   = duration - intro_min - concept_min - activity_min - wrapup_min

    plan = {
        "topic": topic,
        "level": level,
        "duration": duration,
        "style": style,
        "objectives": objectives,
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "outline": [
            {
                "segment": "Introduction & Hook",
                "duration_min": intro_min,
                "description": f"Open with a compelling real-world question or dataset related to '{topic}'. "
                               f"Use {style_desc} to engage students immediately.",
                "icap": "Active",
            },
            {
                "segment": "Core Concept Explanation",
                "duration_min": concept_min,
                "description": f"Explain the foundational ideas of '{topic}' using layered analogies "
                               f"appropriate for {level}-level learners. "
                               f"Present at least two representations (visual + formal).",
                "icap": "Passive",
            },
            {
                "segment": "Guided In-Class Activity",
                "duration_min": activity_min,
                "description": f"Students apply '{topic}' concepts to a structured {style_desc} task. "
                               f"Pairs or small groups encouraged to explain reasoning aloud.",
                "icap": "Constructive",
            },
            {
                "segment": "Peer Discussion & Debate",
                "duration_min": qanda_min,
                "description": f"Pose a conceptual challenge or misconception about '{topic}'. "
                               f"Groups compare answers and defend their reasoning to the class.",
                "icap": "Interactive",
            },
            {
                "segment": "Wrap-Up & Reflection",
                "duration_min": wrapup_min,
                "description": f"Instructor summarises key takeaways. Students write a 2-sentence "
                               f"'exit ticket' explaining the most important idea from '{topic}' in their own words.",
                "icap": "Constructive",
            },
        ],
        "examples_analogies": [
            f"Analogy 1 (Beginner): Think of '{topic}' like sorting a messy drawer – you create rules "
            f"for what goes where before you touch anything.",
            f"Analogy 2 (Visual): Imagine '{topic}' as a flowchart painted on a whiteboard where each "
            f"decision arrow depends on data you observe.",
            f"Analogy 3 (Disciplinary): For social-science students, '{topic}' resembles how a researcher "
            f"codes qualitative interview responses before drawing conclusions.",
        ],
        "activity_prompts": [
            {
                "title": "Think-Pair-Share",
                "prompt": f"Given a small dataset on [your domain], identify one place where '{topic}' "
                          f"would change the result if applied differently. Share with a partner.",
                "icap": "Interactive",
            },
            {
                "title": "Error Spotting",
                "prompt": f"The instructor presents an incorrect application of '{topic}'. "
                          f"Students find the mistake and explain why it is wrong.",
                "icap": "Constructive",
            },
            {
                "title": "Concept Map",
                "prompt": f"In 5 minutes, sketch how '{topic}' connects to at least two other ideas "
                          f"from previous lectures. Be ready to explain one connection.",
                "icap": "Constructive",
            },
        ],
        "reflection_questions": [
            f"What is the single most important idea you learned about '{topic}' today?",
            f"Where did you feel confused, and what would help you clarify that point?",
            f"How might '{topic}' appear in a real dataset or project you care about?",
            f"What question would you still like to ask about '{topic}'?",
        ],
        "student_support": generate_student_support(topic, level),
    }
    return plan


def generate_student_support(topic, level):
    levels_map = {
        "Beginner":      "no prior computing background",
        "Intermediate":  "some programming or statistics experience",
        "Advanced":      "solid technical background",
    }
    desc = levels_map.get(level, "general background")

    return {
        "micro_explanation": (
            f"**{topic} – Plain Language Summary**\n\n"
            f"For a student with {desc}: '{topic}' is the process by which we take raw information "
            f"and apply a systematic rule or method to reach a useful conclusion. "
            f"Think of it as a recipe: you need the right ingredients (data), the right steps (method), "
            f"and a way to check whether the dish turned out correctly (evaluation)."
        ),
        "practice_questions": [
            {
                "difficulty": "Easy",
                "question": f"In one sentence, define '{topic}' in your own words.",
                "hint": "Focus on what it does, not how it works.",
            },
            {
                "difficulty": "Easy",
                "question": f"Give one real-life example where '{topic}' would be useful.",
                "hint": "Think about everyday decisions that rely on patterns in data.",
            },
            {
                "difficulty": "Medium",
                "question": f"Explain one advantage and one limitation of '{topic}'.",
                "hint": "Consider what assumptions it makes about the data.",
            },
            {
                "difficulty": "Medium",
                "question": f"How would you explain '{topic}' to a friend who has never studied data science?",
                "hint": "Use an analogy from everyday life.",
            },
            {
                "difficulty": "Hard",
                "question": f"Design a small experiment to test whether '{topic}' performs well "
                            f"on a dataset of your choice. What metrics would you use?",
                "hint": "Think about what 'success' means for your specific problem.",
            },
            {
                "difficulty": "Hard",
                "question": f"What ethical concerns might arise when applying '{topic}' in a high-stakes "
                            f"setting such as hiring, healthcare, or criminal justice?",
                "hint": "Consider bias, transparency, and accountability.",
            },
        ],
        "srl_prompts": [
            "Before reading: What do I already know about this topic?",
            "During study: Am I understanding this, or just reading the words?",
            "After practice: Can I explain this without looking at my notes?",
            "Reflection: What is my study plan for the parts I found difficult?",
        ],
    }


# ─── SIDEBAR ─────────────────────────────────────────────────────────────────

with st.sidebar:
    st.markdown("## 🎓 LectureAI")
    st.markdown("**Human–AI Co-Orchestration**\n\n*Prototype v0.1 – Mock Mode*")
    st.divider()
    st.markdown("### Navigation")
    page = st.radio("", ["📋 Lesson Builder", "📚 Student Support", "📊 Evaluation Rubric", "📁 Export"], label_visibility="collapsed")
    st.divider()
    st.caption("Based on Jamil (2025) – ACM TOCE\nImplemented by Omolola • Feb 2026")


# ─── SESSION STATE ────────────────────────────────────────────────────────────
if "lesson_plan" not in st.session_state:
    st.session_state.lesson_plan = None
if "approved_segments" not in st.session_state:
    st.session_state.approved_segments = {}
if "instructor_notes" not in st.session_state:
    st.session_state.instructor_notes = {}


# ════════════════════════════════════════════════════════════════════════════
#  PAGE 1 – LESSON BUILDER
# ════════════════════════════════════════════════════════════════════════════
if page == "📋 Lesson Builder":
    st.markdown("# Lesson Builder")
    st.markdown("Fill in the form below and click **Generate Lesson Plan** to create an AI-assisted lecture outline.")

    with st.form("lesson_form"):
        col1, col2 = st.columns(2)
        with col1:
            topic      = st.text_input("Topic *", placeholder="e.g., Linear Regression")
            level      = st.selectbox("Class Level *", ["Beginner", "Intermediate", "Advanced"])
            duration   = st.slider("Class Duration (minutes) *", 30, 180, 75, step=5)
        with col2:
            objectives = st.text_area("Learning Objectives *", placeholder="e.g.\n1. Understand what linear regression is\n2. Interpret coefficients\n3. Evaluate model fit", height=120)
            style      = st.selectbox("Teaching Style *", ["Lecture-based", "Discussion-based", "Project-based", "Flipped"])

        submitted = st.form_submit_button("✨ Generate Lesson Plan", use_container_width=True)

    if submitted:
        if not topic or not objectives:
            st.error("Please fill in Topic and Learning Objectives.")
        else:
            with st.spinner("Generating lesson plan…"):
                st.session_state.lesson_plan = generate_lesson(topic, objectives, level, duration, style)
                st.session_state.approved_segments = {i: True for i in range(5)}
                st.session_state.instructor_notes  = {i: "" for i in range(5)}
            st.success("Lesson plan generated! Review and approve each segment below.")

    # ── Display plan ──────────────────────────────────────────────────────────
    if st.session_state.lesson_plan:
        plan = st.session_state.lesson_plan

        st.divider()
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Topic",    plan["topic"])
        col2.metric("Level",    plan["level"])
        col3.metric("Duration", f"{plan['duration']} min")
        col4.metric("Style",    plan["style"])

        # ICAP Summary bar
        icap_counts = {}
        for seg in plan["outline"]:
            icap_counts[seg["icap"]] = icap_counts.get(seg["icap"], 0) + 1
        for act in plan["activity_prompts"]:
            icap_counts[act["icap"]] = icap_counts.get(act["icap"], 0) + 1

        st.markdown("#### ICAP Coverage Summary")
        cols = st.columns(4)
        for i, label in enumerate(ICAP_LABELS):
            count = icap_counts.get(label, 0)
            cols[i].markdown(f'<div class="metric-box">{badge(label)}<br><b style="font-size:1.4rem">{count}</b><br><small>items</small></div>', unsafe_allow_html=True)

        # Outline segments
        st.markdown('<p class="section-header">📐 Lecture Outline</p>', unsafe_allow_html=True)
        for i, seg in enumerate(plan["outline"]):
            with st.expander(f"**{i+1}. {seg['segment']}** ({seg['duration_min']} min)", expanded=(i == 0)):
                st.markdown(f"{seg['description']}")
                st.markdown(f"ICAP Level: {badge(seg['icap'])}", unsafe_allow_html=True)
                st.session_state.instructor_notes[i] = st.text_input(
                    "Instructor notes / edits:", value=st.session_state.instructor_notes.get(i, ""),
                    key=f"note_{i}", placeholder="Add your own notes or override here…"
                )
                st.session_state.approved_segments[i] = st.checkbox(
                    "✅ Approve this segment", value=st.session_state.approved_segments.get(i, True), key=f"approve_{i}"
                )

        # Examples & Analogies
        st.markdown('<p class="section-header">💡 Examples & Analogies</p>', unsafe_allow_html=True)
        for ex in plan["examples_analogies"]:
            st.markdown(f'<div class="card">{ex}</div>', unsafe_allow_html=True)

        # Activity Prompts
        st.markdown('<p class="section-header">🎯 In-Class Activity Prompts</p>', unsafe_allow_html=True)
        for act in plan["activity_prompts"]:
            st.markdown(
                f'<div class="card"><b>{act["title"]}</b> {badge(act["icap"])}<br><br>{act["prompt"]}</div>',
                unsafe_allow_html=True
            )

        # Reflection Questions
        st.markdown('<p class="section-header">🪞 Reflection Questions</p>', unsafe_allow_html=True)
        for rq in plan["reflection_questions"]:
            st.markdown(f"- {rq}")


# ════════════════════════════════════════════════════════════════════════════
#  PAGE 2 – STUDENT SUPPORT
# ════════════════════════════════════════════════════════════════════════════
elif page == "📚 Student Support":
    st.markdown("# Student Support Module")

    if not st.session_state.lesson_plan:
        st.info("Generate a lesson plan first in the **Lesson Builder** tab.")
    else:
        plan = st.session_state.lesson_plan
        ss   = plan["student_support"]

        st.markdown(f"### Topic: {plan['topic']}  |  Level: {plan['level']}")
        st.divider()

        # Micro-explanation
        st.markdown('<p class="section-header">📖 Plain-Language Micro-Explanation</p>', unsafe_allow_html=True)
        st.markdown(ss["micro_explanation"])

        # Practice Questions
        st.markdown('<p class="section-header">✏️ Practice Questions</p>', unsafe_allow_html=True)
        diff_filter = st.multiselect("Show difficulty:", ["Easy", "Medium", "Hard"], default=["Easy", "Medium", "Hard"])

        for q in ss["practice_questions"]:
            if q["difficulty"] in diff_filter:
                diff_color = {"Easy": "difficulty-easy", "Medium": "difficulty-medium", "Hard": "difficulty-hard"}[q["difficulty"]]
                with st.expander(f'[{q["difficulty"]}] {q["question"]}'):
                    st.markdown(f'<span class="{diff_color}">{q["difficulty"]}</span>', unsafe_allow_html=True)
                    st.markdown(f"**Question:** {q['question']}")
                    st.markdown(f"💡 *Hint: {q['hint']}*")

        # SRL Prompts
        st.markdown('<p class="section-header">🧠 Self-Regulated Learning Prompts</p>', unsafe_allow_html=True)
        for srl in ss["srl_prompts"]:
            st.markdown(f'<div class="card">🔹 {srl}</div>', unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════
#  PAGE 3 – EVALUATION RUBRIC
# ════════════════════════════════════════════════════════════════════════════
elif page == "📊 Evaluation Rubric":
    st.markdown("# Evaluation Rubric")
    st.markdown("Score your prototype's output quality across five pedagogical criteria.")

    if not st.session_state.lesson_plan:
        st.info("Generate a lesson plan first in the **Lesson Builder** tab.")
    else:
        plan = st.session_state.lesson_plan
        st.markdown(f"**Evaluating:** {plan['topic']} | Generated: {plan['generated_at']}")
        st.divider()

        criteria = [
            ("Relevance",          "Does output match the topic and stated learning objectives?"),
            ("Clarity",            "Is the language understandable for the target student level?"),
            ("Pedagogical Value",  "Does it support active / constructive / interactive engagement (ICAP)?"),
            ("Correctness",        "Are concepts and examples technically accurate?"),
            ("Usability",          "Is the workflow easy and intuitive for instructors to use?"),
        ]

        scores = {}
        for criterion, description in criteria:
            st.markdown(f"**{criterion}** – *{description}*")
            scores[criterion] = st.slider("", 1, 5, 3, key=f"rubric_{criterion}")
            st.divider()

        total = sum(scores.values())
        pct   = round(total / (len(criteria) * 5) * 100, 1)

        col1, col2, col3 = st.columns(3)
        col1.metric("Total Score",   f"{total} / {len(criteria)*5}")
        col2.metric("Percentage",    f"{pct}%")
        col3.metric("Rating",        "Excellent" if pct >= 80 else "Good" if pct >= 60 else "Needs Work")

        if st.button("💾 Save Rubric Scores"):
            rubric_record = {
                "topic": plan["topic"],
                "evaluated_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "scores": scores,
                "total": total,
                "percentage": pct,
            }
            st.session_state["rubric_record"] = rubric_record
            st.success("Rubric scores saved! They will be included in the export.")
            st.json(rubric_record)


# ════════════════════════════════════════════════════════════════════════════
#  PAGE 4 – EXPORT
# ════════════════════════════════════════════════════════════════════════════
elif page == "📁 Export":
    st.markdown("# Export Lesson Plan")

    if not st.session_state.lesson_plan:
        st.info("Generate a lesson plan first in the **Lesson Builder** tab.")
    else:
        plan = st.session_state.lesson_plan

        # Build export package
        export_data = {
            "lesson_plan": plan,
            "instructor_notes": st.session_state.instructor_notes,
            "approved_segments": st.session_state.approved_segments,
        }
        if "rubric_record" in st.session_state:
            export_data["rubric_scores"] = st.session_state["rubric_record"]

        # JSON export
        json_str = json.dumps(export_data, indent=2)
        st.download_button(
            label="⬇️ Download as JSON",
            data=json_str,
            file_name=f"lesson_{plan['topic'].replace(' ', '_')}_{plan['generated_at'][:10]}.json",
            mime="application/json",
            use_container_width=True,
        )

        # Plain text export
        txt_lines = [
            f"LESSON PLAN: {plan['topic']}",
            f"Generated: {plan['generated_at']}",
            f"Level: {plan['level']} | Duration: {plan['duration']} min | Style: {plan['style']}",
            "",
            "LEARNING OBJECTIVES",
            plan["objectives"],
            "",
            "LECTURE OUTLINE",
        ]
        for i, seg in enumerate(plan["outline"]):
            note = st.session_state.instructor_notes.get(i, "")
            approved = "✅" if st.session_state.approved_segments.get(i, True) else "⛔"
            txt_lines.append(f"{approved} {i+1}. {seg['segment']} ({seg['duration_min']} min) [{seg['icap']}]")
            txt_lines.append(f"   {seg['description']}")
            if note:
                txt_lines.append(f"   [INSTRUCTOR NOTE]: {note}")
            txt_lines.append("")

        txt_lines += ["", "EXAMPLES & ANALOGIES"]
        for ex in plan["examples_analogies"]:
            txt_lines.append(f"- {ex}")

        txt_lines += ["", "IN-CLASS ACTIVITY PROMPTS"]
        for act in plan["activity_prompts"]:
            txt_lines.append(f"[{act['icap']}] {act['title']}: {act['prompt']}")

        txt_lines += ["", "REFLECTION QUESTIONS"]
        for rq in plan["reflection_questions"]:
            txt_lines.append(f"- {rq}")

        ss = plan["student_support"]
        txt_lines += ["", "STUDENT SUPPORT – MICRO EXPLANATION", ss["micro_explanation"], "", "PRACTICE QUESTIONS"]
        for q in ss["practice_questions"]:
            txt_lines.append(f"[{q['difficulty']}] {q['question']}")
            txt_lines.append(f"  Hint: {q['hint']}")

        txt_lines += ["", "SRL PROMPTS"]
        for srl in ss["srl_prompts"]:
            txt_lines.append(f"- {srl}")

        txt_content = "\n".join(txt_lines)
        st.download_button(
            label="⬇️ Download as Plain Text",
            data=txt_content,
            file_name=f"lesson_{plan['topic'].replace(' ', '_')}_{plan['generated_at'][:10]}.txt",
            mime="text/plain",
            use_container_width=True,
        )

        st.divider()
        st.markdown("### Preview")
        st.text_area("Export preview (text format):", txt_content, height=400)
