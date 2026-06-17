import streamlit as st
import pandas as pd
from components.score_card import score_card


def show():
    st.title("📊 Recruitment Dashboard")
    st.markdown("Monitor applications, shortlisted candidates, interviews and selections.")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        score_card("Applications", "125", "📄", "#3B82F6")

    with col2:
        score_card("Shortlisted", "42", "✅", "#10B981")

    with col3:
        score_card("Interviews", "18", "🎤", "#F59E0B")

    with col4:
        score_card("Selected", "8", "🏆", "#8B5CF6")

    st.divider()

    st.subheader("📌 Recruitment Pipeline")
    pipeline_data = pd.DataFrame({
        "Stage": ["Applied", "Screening", "Interview", "Selected"],
        "Candidates": [125, 80, 18, 8]
    })

    st.bar_chart(pipeline_data, x="Stage", y="Candidates")

    st.divider()

    st.subheader("🕒 Recent Activities")
    activities = [
        "Resume uploaded successfully",
        "Candidate ranking generated",
        "Interview scheduled",
        "Candidate shortlisted"
    ]

    for activity in activities:
        st.write(f"✅ {activity}")