import streamlit as st


def show():
    st.title("📤 Upload Resume")
    st.markdown("Upload candidate resumes and enter job details for AI-based screening.")

    st.write("")

    with st.container(border=True):
        st.subheader("📝 Job Details")

        job_title = st.text_input("Job Title", placeholder="Example: Frontend Developer")
        job_description = st.text_area(
            "Job Description",
            placeholder="Enter required skills, experience, responsibilities...",
            height=150
        )

    st.write("")

    with st.container(border=True):
        st.subheader("📄 Upload Resume Files")

        uploaded_files = st.file_uploader(
            "Choose resume files",
            type=["pdf", "docx"],
            accept_multiple_files=True
        )

        if uploaded_files:
            st.success(f"{len(uploaded_files)} resume(s) uploaded successfully.")

            for file in uploaded_files:
                st.write(f"✅ {file.name}")

    st.write("")

    analyze_button = st.button("🚀 Analyze Resume", use_container_width=True)

    if analyze_button:
        if not job_title:
            st.warning("Please enter the job title.")

        elif not job_description:
            st.warning("Please enter the job description.")

        elif not uploaded_files:
            st.warning("Please upload at least one resume.")

        else:
            st.success("Resume analysis started successfully!")

            st.info(
                "Backend integration pending: later this button will send resumes "
                "and job description to the resume parser / AI ranking backend."
            )

            st.subheader("Preview Data Sent to Backend")

            st.write("**Job Title:**", job_title)
            st.write("**Job Description:**", job_description)

            st.write("**Uploaded Files:**")
            for file in uploaded_files:
                st.write(f"- {file.name}")