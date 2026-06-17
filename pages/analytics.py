import streamlit as st

from components.charts import (
    recruitment_pipeline_chart,
    candidate_score_chart,
    application_status_chart,
    monthly_applications_chart
)


def show():
    st.title("📈 Recruitment Analytics")
    st.markdown("Analyze recruitment progress, candidate scores and application trends.")

    st.write("")

    col1, col2 = st.columns(2)

    with col1:
        recruitment_pipeline_chart()

    with col2:
        application_status_chart()

    st.divider()

    candidate_score_chart()

    st.divider()

    monthly_applications_chart()

    st.divider()

    st.subheader("📌 Analytics Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.success("Highest Score: 92%")

    with col2:
        st.info("Average Score: 77.75%")

    with col3:
        st.warning("Pending Applications: 48")

    st.info(
        "Backend integration pending: later these charts will use real data "
        "from database/API instead of dummy values."
    )