from google_sheets import log_response
import streamlit as st
from datetime import datetime

# --- App Config ---
st.set_page_config(
    page_title="Cyber Sentinel",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- Dark Mode Styling ---
st.markdown(
    """
    <style>
    body {
        background-color: #1e1e1e;
        color: #f0f0f0;
    }
    .css-18e3th9 {
        background-color: #2e2e2e;
    }
    .css-1d391kg, .css-1v3fvcr {
        color: #f0f0f0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Welcome Message ---
st.title("🛡️ Cyber Sentinel")
st.markdown("""
**Welcome, student.**

You've summoned Cyber Sentinel — a mysteriously cool cybersecurity professor with a shadowy past and a ridiculous knowledge of everything from phishing kits to zero-day exploits.

Let's get your mind sharp and your defenses sharper.
""")

# --- Study Session Launcher ---
st.subheader("📚 Start a Study Session")
# Set up session state variable to track if session started
if "show_question" not in st.session_state:
    st.session_state.show_question = False

# Button to start study session
if st.button("Ask Me Questions"):
    st.session_state.show_question = True

# If session started, show question and form
if st.session_state.show_question:

    topic = "Access Control"
    subtopic = "Least Privilege"
    question = "What does the principle of 'least privilege' refer to in cybersecurity?"

    st.markdown(f"**{question}**\n\n"
                "A. Giving users all access  \n"
                "B. Granting only necessary permissions  \n"
                "C. Assigning access based on seniority  \n"
                "D. Letting users choose their access level")

    answer = st.radio("Your answer:", ["A", "B", "C", "D"], key="answer_radio")

    if st.button("Submit Answer"):
        if answer == "B":
            st.success("Correct. You're on fire 🔥")
            correct = "✅"
            notes = "Understood principle clearly."
        else:
            st.error("Incorrect. Let's revisit that concept in our next round.")
            correct = "❌"
            notes = "Needs review."

        # Log to Google Sheets
        log_response(topic, subtopic, question, answer, correct, notes)
        st.session_state.show_question = False  # Reset for next session

st.markdown("---")
st.caption("Cyber Sentinel · Powered by Rossovic Group")