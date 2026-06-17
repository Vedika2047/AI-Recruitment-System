import streamlit as st


def show():

    st.title("📊 Recruitment Dashboard")
    st.markdown("Monitor hiring activities, candidate performance and recruitment progress.")

    st.write("")

    # KPI Cards
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="Total Applications",
            value="125",
            delta="+12"
        )

    with col2:
        st.metric(
            label="Shortlisted",
            value="42",
            delta="+5"
        )

    with col3:
        st.metric(
            label="Interviews Scheduled",
            value="18",
            delta="+3"
        )

    with col4:
        st.metric(
            label="Selected Candidates",
            value="8",
            delta="+2"
        )

    st.divider()

    # Candidate Pipeline
    st.subheader("📌 Recruitment Pipeline")

    pipeline_col1, pipeline_col2, pipeline_col3, pipeline_col4 = st.columns(4)

    pipeline_col1.info("Applications\n\n125")
    pipeline_col2.warning("Screening\n\n80")
    pipeline_col3.success("Interview\n\n18")
    pipeline_col4.success("Hired\n\n8")

    st.divider()

    # Recent Activities
    st.subheader("🕒 Recent Activities")

    activities = [
        "Resume uploaded for Software Engineer position",
        "AI ranking completed for Data Analyst role",
        "Interview scheduled for candidate Rahul Sharma",
        "Candidate Priya Patel shortlisted",
        "Recruitment analytics generated"
    ]

    for activity in activities:
        st.write(f"✅ {activity}")

    st.divider()

    # Upcoming Interviews
    st.subheader("📅 Upcoming Interviews")

    interview_data = {
        "Candidate": [
            "Rahul Sharma",
            "Priya Patel",
            "Amit Verma",
            "Sneha Shah"
        ],
        "Role": [
            "Software Engineer",
            "Data Analyst",
            "AI Engineer",
            "Frontend Developer"
        ],
        "Date": [
            "18-06-2026",
            "18-06-2026",
            "19-06-2026",
            "19-06-2026"
        ],
        "Time": [
            "10:00 AM",
            "11:30 AM",
            "02:00 PM",
            "04:00 PM"
        ]
    }

    st.dataframe(
        interview_data,
        use_container_width=True
    )

    st.divider()

    st.subheader("📈 Recruitment Insights")

    chart_data = {
        "Stage": [
            "Applied",
            "Screening",
            "Interview",
            "Selected"
        ],
        "Candidates": [
            125,
            80,
            18,
            8
        ]
    }

    st.bar_chart(
        data=chart_data,
        x="Stage",
        y="Candidates"
    )