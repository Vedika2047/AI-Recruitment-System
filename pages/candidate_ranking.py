import streamlit as st
from components.candidate_card import candidate_card


def show():

    st.title("🏆 Candidate Ranking")

    candidate_card(
        name="Rahul Sharma",
        email="rahul@gmail.com",
        score=92,
        status="Shortlisted",
        skills=["Python", "React", "SQL"]
    )

    candidate_card(
        name="Priya Patel",
        email="priya@gmail.com",
        score=85,
        status="Shortlisted",
        skills=["Machine Learning", "TensorFlow"]
    )

    candidate_card(
        name="Amit Verma",
        email="amit@gmail.com",
        score=58,
        status="Rejected",
        skills=["Java", "Spring Boot"]
    )