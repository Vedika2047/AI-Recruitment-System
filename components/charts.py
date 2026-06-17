import streamlit as st
import pandas as pd


def recruitment_pipeline_chart(data=None):
    if data is None:
        data = {
            "Stage": ["Applied", "Screening", "Interview", "Selected"],
            "Candidates": [125, 80, 18, 8]
        }

    df = pd.DataFrame(data)

    st.markdown("### 📊 Recruitment Pipeline")
    st.bar_chart(df, x="Stage", y="Candidates", use_container_width=True)


def candidate_score_chart(candidates=None):
    if candidates is None:
        candidates = [
            {"Candidate": "Rahul", "Score": 92},
            {"Candidate": "Priya", "Score": 85},
            {"Candidate": "Amit", "Score": 58},
            {"Candidate": "Sneha", "Score": 76}
        ]

    df = pd.DataFrame(candidates)

    st.markdown("### 🏆 Candidate Match Scores")
    st.bar_chart(df, x="Candidate", y="Score", use_container_width=True)


def application_status_chart(data=None):
    if data is None:
        data = {
            "Status": ["Shortlisted", "Rejected", "Pending"],
            "Count": [42, 35, 48]
        }

    df = pd.DataFrame(data)

    st.markdown("### 📌 Application Status")
    st.bar_chart(df, x="Status", y="Count", use_container_width=True)


def monthly_applications_chart(data=None):
    if data is None:
        data = {
            "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
            "Applications": [20, 35, 45, 60, 90, 125]
        }

    df = pd.DataFrame(data)

    st.markdown("### 📈 Monthly Applications")
    st.line_chart(df, x="Month", y="Applications", use_container_width=True)