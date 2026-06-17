import streamlit as st
from datetime import date, time


def show():
    st.title("📅 Interview Scheduler")
    st.markdown("Schedule interviews for shortlisted candidates.")

    st.write("")

    with st.container(border=True):
        st.subheader("👤 Candidate Details")

        candidate_name = st.text_input(
            "Candidate Name",
            placeholder="Example: Rahul Sharma"
        )

        candidate_email = st.text_input(
            "Candidate Email",
            placeholder="Example: rahul@gmail.com"
        )

        job_role = st.text_input(
            "Job Role",
            placeholder="Example: Frontend Developer"
        )

    st.write("")

    with st.container(border=True):
        st.subheader("🕒 Interview Details")

        interview_date = st.date_input(
            "Interview Date",
            min_value=date.today()
        )

        interview_time = st.time_input(
            "Interview Time",
            value=time(10, 0)
        )

        interview_mode = st.selectbox(
            "Interview Mode",
            ["Online", "Offline"]
        )

        if interview_mode == "Online":
            meeting_link = st.text_input(
                "Meeting Link",
                placeholder="Example: Google Meet / Zoom link"
            )
            location = "Online"
        else:
            location = st.text_input(
                "Interview Location",
                placeholder="Example: HR Cabin / Office Room 101"
            )
            meeting_link = ""

    st.write("")

    with st.container(border=True):
        st.subheader("📝 Additional Notes")

        notes = st.text_area(
            "Notes for Interviewer",
            placeholder="Example: Focus on React, Python, communication skills...",
            height=120
        )

    st.write("")

    if st.button("✅ Schedule Interview", use_container_width=True):
        if not candidate_name:
            st.warning("Please enter candidate name.")

        elif not candidate_email:
            st.warning("Please enter candidate email.")

        elif "@" not in candidate_email:
            st.warning("Please enter a valid email address.")

        elif not job_role:
            st.warning("Please enter job role.")

        elif interview_mode == "Online" and not meeting_link:
            st.warning("Please enter meeting link for online interview.")

        elif interview_mode == "Offline" and not location:
            st.warning("Please enter interview location.")

        else:
            st.success("Interview scheduled successfully!")

            st.subheader("📌 Interview Summary")

            st.write("**Candidate Name:**", candidate_name)
            st.write("**Candidate Email:**", candidate_email)
            st.write("**Job Role:**", job_role)
            st.write("**Date:**", interview_date)
            st.write("**Time:**", interview_time)
            st.write("**Mode:**", interview_mode)

            if interview_mode == "Online":
                st.write("**Meeting Link:**", meeting_link)
            else:
                st.write("**Location:**", location)

            if notes:
                st.write("**Notes:**", notes)

            st.info(
                "Backend integration pending: later this data will be saved "
                "in the database and an interview email can be sent to the candidate."
            )