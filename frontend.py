import streamlit as st
import requests

# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------

st.set_page_config(
    page_title="TeachMe Python",
    page_icon=None,
    layout="wide"
)

# ------------------------------------------------
# CUSTOM CSS
# ------------------------------------------------

st.markdown("""

<style>

/* ---------------- FONT ---------------- */
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@300;400;500;600&family=DM+Mono:wght@400;500&display=swap');

/* ---------------- BASE ---------------- */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.main {
    background-color: #0b1220;
}

/* ---------------- HEADER ---------------- */
.header-box {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    padding: 40px;
    border-radius: 16px;
    margin-bottom: 20px;
}

.title-text {
    font-family: 'DM Serif Display', serif;
    font-size: 84px;
    font-weight: 400;
    color: #ffffff;
    letter-spacing: -2px;
    margin: 0;
    line-height: 1;
}

.title-accent {
    color: #60a5fa;
}

.subtitle-text {
    color: #cbd5e1;
    font-size: 18px;
    margin-top: 10px;
}

/* ---------------- DIVIDER ---------------- */
.thin-rule {
    border: none;
    border-top: 1px solid #1f2937;
    margin: 24px 0;
}

/* ---------------- BANNER ---------------- */
.banner-card {
    background: linear-gradient(135deg, #1a1a2e, #0f3460);
    padding: 32px;
    border-radius: 16px;
    margin-bottom: 28px;
}

.banner-card h2 {
    color: #ffffff;
    font-size: 22px;
    margin: 0 0 10px 0;
}

.banner-card p {
    color: #94a3b8;
    font-size: 14px;
}

/* ---------------- INFO CARD ---------------- */
.info-card {
    background: #111827;
    border: 1px solid #1f2937;
    padding: 22px;
    border-radius: 14px;
    margin-bottom: 18px;
}

.info-card .label {
    font-size: 11px;
    font-weight: 700;
    color: #60a5fa;
    text-transform: uppercase;
}

.info-card p {
    color: #e5e7eb;
    font-size: 16px;
}

/* ---------------- CHAT (FIXED - NO CONFLICTS) ---------------- */
[data-testid="stChatMessage"] {
    background: #111827;
    border: 1px solid #1f2937;
    border-radius: 12px;
    padding: 12px 14px;
    margin-bottom: 10px;
}

[data-testid="stChatMessage"] * {
    color: #f9fafb !important;
    font-size: 16px !important;
    line-height: 1.6 !important;
}

/* ---------------- SIDEBAR ---------------- */
[data-testid="stSidebar"] {
    background-color: #0f172a;
    border-right: 1px solid #1f2937;
}

[data-testid="stSidebar"] * {
    color: #e5e7eb !important;
}

/* ---------------- INPUT ---------------- */
.stTextInput input {
    border-radius: 10px;
    background: #0f172a;
    color: white;
    border: 1px solid #1f2937;
}

.stTextInput input:focus {
    border-color: #60a5fa;
}

/* ---------------- BUTTON ---------------- */
.stButton button {
    background-color: #1f2937;
    color: white;
    border-radius: 10px;
    width: 100%;
}

.stButton button:hover {
    background-color: #2563eb;
}

/* ---------------- CODE BLOCK ---------------- */
.stCodeBlock {
    border-radius: 12px;
}

/* ---------------- FOOTER ---------------- */
.footer {
    text-align: center;
    color: #64748b;
    font-size: 12px;
    padding-top: 30px;
}

/* ---------------- SECTION HEADER ---------------- */
.section-header {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.4px;
    text-transform: uppercase;
    color: #94a3b8;
    margin-bottom: 14px;
    margin-top: 30px;
}

</style>
            
""", unsafe_allow_html=True)
st.markdown("""
<div class="header-box">
    <p class="title-text">Teach<span class="title-accent">Me</span> Python</p>
    <p class="subtitle-text">Your interactive Python learning assistant</p>
</div>
""", unsafe_allow_html=True)
# ------------------------------------------------
# SESSION STATE
# ------------------------------------------------

if "page" not in st.session_state:
    st.session_state.page = "login"

if "user" not in st.session_state:
    st.session_state.user = {}

if "history" not in st.session_state:
    st.session_state.history = []

# ------------------------------------------------
# SIDEBAR
# ------------------------------------------------

with st.sidebar:

    st.markdown('<p class="sidebar-title">TeachMe Python</p>', unsafe_allow_html=True)

    if st.session_state.user.get("name"):

        st.markdown('<p class="sidebar-section">Profile</p>', unsafe_allow_html=True)

        st.markdown(
            f"""
            <p class="profile-name">{st.session_state.user['name']}</p>
            <p class="profile-level">Level {st.session_state.user['level']}</p>
            """,
            unsafe_allow_html=True
        )

        st.divider()

        st.markdown('<p class="sidebar-section">Learning Topics</p>', unsafe_allow_html=True)

        topics = [
            "Python Basics",
            "Variables",
            "Loops",
            "Functions",
            "OOP",
            "Projects"
        ]

        for topic in topics:
            st.markdown(f'<p class="topic-item">{topic}</p>', unsafe_allow_html=True)

        st.divider()

        st.markdown('<p class="sidebar-section">Progress</p>', unsafe_allow_html=True)

        progress_value = st.session_state.user["level"] * 20
        st.progress(progress_value)
        st.caption(f"{progress_value}% completed")

        st.divider()

        if st.button("Sign Out"):
            st.session_state.page = "login"
            st.session_state.user = {}
            st.session_state.history = []
            st.rerun()

# ------------------------------------------------
# LOGIN PAGE
# ------------------------------------------------

if st.session_state.page == "login":

    col1, col2 = st.columns([4, 1])

    with col1:
        st.markdown(
            """
            <p class="title-text">Teach<span class="title-accent">Me</span> Python</p>
            <p class="subtitle-text">Your interactive Python learning assistant</p>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.image("python_nobg.png", width=200)

    st.markdown('<hr class="thin-rule">', unsafe_allow_html=True)

    st.markdown("""
    <div class="banner-card">
        <h2>Start Your Learning Journey</h2>
        <p>
            Enter your name and select your current skill level.
            We'll tailor your experience to match where you are right now.
        </p>
    </div>
    """, unsafe_allow_html=True)

    left, center, right = st.columns([1, 2, 1])

    with center:

        with st.form("login_form"):

            name = st.text_input("Your name", placeholder="e.g. Alex")

            level = st.slider(
                "Skill level (1 = beginner, 5 = advanced)",
                1,
                5,
                1
            )

            submit = st.form_submit_button("Begin Learning")

        if submit and name:

            try:

                response = requests.post(
                    "http://127.0.0.1:8000/login",
                    json={
                        "name": name,
                        "level": level
                    }
                )

                response.raise_for_status()

                data = response.json()

                st.session_state.user["id"] = data["user_id"]
                st.session_state.user["name"] = name
                st.session_state.user["level"] = level

                st.session_state.page = "chat"

                st.success("Logged in successfully.")

                st.rerun()

            except Exception as e:
                st.error(f"Could not connect: {e}")

# ------------------------------------------------
# CHAT PAGE
# ------------------------------------------------

elif st.session_state.page == "chat":

    name = st.session_state.user["name"]
    level = st.session_state.user["level"]

    col1, col2 = st.columns([4, 1])

    with col1:
        st.markdown(
            f"""
            <p class="title-text">Teach<span class="title-accent">Me</span> Python</p>
            <p class="subtitle-text">Welcome back, {name}</p>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.image("python_nobg.png", width=200)

    st.markdown('<hr class="thin-rule">', unsafe_allow_html=True)

    # Dashboard Banner
    st.markdown(f"""
    <div class="banner-card">
        <h2>Your Dashboard</h2>
        <p>
            You are currently at level <strong style="color:#93c5fd">{level}</strong>.
            Keep practicing and asking questions to sharpen your Python skills.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Recommended Topic
    st.markdown('<p class="section-header">Recommended Topic</p>', unsafe_allow_html=True)

    topic_map = {
        1: ("Python Fundamentals", "Start with variables, the print() function, and accepting user input with input(). These are the building blocks of every Python program."),
        2: ("Control Flow", "Learn how to branch your logic with if / elif / else statements, and repeat actions using for and while loops."),
        3: ("Functions & Collections", "Practice writing reusable functions, and work with lists, tuples, and comprehensions to handle groups of data."),
        4: ("OOP & Dictionaries", "Explore object-oriented programming — classes, attributes, methods — and master dictionaries for structured data."),
        5: ("APIs & Advanced Projects", "Build REST APIs with FastAPI, work with async code, and tackle real-world projects that pull everything together."),
    }

    topic_title, topic_desc = topic_map.get(level, ("", ""))

    st.markdown(f"""
    <div class="info-card">
        <div class="label">Level {level} — {topic_title}</div>
        <p>{topic_desc}</p>
    </div>
    """, unsafe_allow_html=True)

    # Example Code
    st.markdown('<p class="section-header">Example</p>', unsafe_allow_html=True)

    greet_code = f'''def greeting(name):
    print(f"Hello {{name}}, welcome to TeachMe Python!")

greeting("{name}")'''

    st.code(greet_code, language="python")

    st.markdown('<hr class="thin-rule">', unsafe_allow_html=True)

    # ------------------------------------------------
    # CHAT INPUT
    # ------------------------------------------------

    question = st.chat_input("Ask a Python question...")

    if question:

        with st.chat_message("user"):
            st.write(question)

        try:

            with st.spinner("Thinking..."):

                response = requests.post(
                    "http://127.0.0.1:8000/ask",
                    json={
                        "question": question,
                        "user_id": st.session_state.user["id"]
                    }
                )

                response.raise_for_status()

                answer = response.json()["answer"]

        except Exception as e:

            answer = f"Error: {e}"

        with st.chat_message("assistant"):
            st.write(answer)

        st.session_state.history.append((question, answer))

    # ------------------------------------------------
    # CHAT HISTORY
    # ------------------------------------------------

    if st.session_state.history:

        st.markdown('<p class="section-header">Conversation History</p>', unsafe_allow_html=True)

        for q, a in reversed(st.session_state.history):

            st.markdown(f"""
            <div class="history-card">
                <div class="speaker-label">You</div>
                <div class="from-user">{q}</div>
                <div class="speaker-label">Assistant</div>
                <p class="from-bot">{a}</p>
            </div>
            """, unsafe_allow_html=True)

    # ------------------------------------------------
    # FOOTER
    # ------------------------------------------------

    st.markdown("""
    <div class="footer">
        <hr style="border-color: #e8e8e3; margin-bottom: 16px;">
        Built with Streamlit
    </div>
    """, unsafe_allow_html=True)