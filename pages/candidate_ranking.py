import streamlit as st
from components.candidate_card import candidate_card


def show():
    st.title("🏆 Candidate Ranking")
    st.markdown("View AI-ranked candidates based on resume-job matching score.")

    candidates = [
        {
            "name": "Rahul Sharma",
            "email": "rahul@gmail.com",
            "score": 92,
            "status": "Shortlisted",
            "skills": ["Python", "React", "SQL"]
        },
        {
            "name": "Priya Patel",
            "email": "priya@gmail.com",
            "score": 85,
            "status": "Shortlisted",
            "skills": ["Machine Learning", "Python"]
        },
        {
            "name": "Amit Verma",
            "email": "amit@gmail.com",
            "score": 58,
            "status": "Rejected",
            "skills": ["Java", "Spring Boot"]
        }
    ]

    candidates = sorted(candidates, key=lambda x: x["score"], reverse=True)

    for candidate in candidates:
        candidate_card(
            candidate["name"],
            candidate["email"],
            candidate["score"],
            candidate["status"],
            candidate["skills"]
        )