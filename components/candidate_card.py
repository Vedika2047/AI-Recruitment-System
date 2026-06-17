import streamlit as st


def candidate_card(
    name,
    email,
    score,
    status,
    skills=None
):

    if skills is None:
        skills = []

    if status == "Shortlisted":
        border_color = "#10B981"
        badge_color = "#DCFCE7"
        text_color = "#166534"

    elif status == "Rejected":
        border_color = "#EF4444"
        badge_color = "#FEE2E2"
        text_color = "#991B1B"

    else:
        border_color = "#F59E0B"
        badge_color = "#FEF3C7"
        text_color = "#92400E"

    skills_html = ""

    for skill in skills:
        skills_html += f"""
        <span style="
            background:#E2E8F0;
            padding:5px 10px;
            border-radius:15px;
            margin-right:5px;
            font-size:12px;
        ">
            {skill}
        </span>
        """

    st.markdown(
        f"""
        <div style="
            background:white;
            padding:20px;
            border-radius:15px;
            border-left:6px solid {border_color};
            box-shadow:0px 2px 10px rgba(0,0,0,0.08);
            margin-bottom:15px;
        ">

            <h3 style="margin:0;color:#0F172A;">
                👤 {name}
            </h3>

            <p style="color:#64748B;margin-top:5px;">
                📧 {email}
            </p>

            <div style="margin-top:10px;">
                <strong>Match Score:</strong>
                {score}%
            </div>

            <div style="
                margin-top:10px;
                display:inline-block;
                background:{badge_color};
                color:{text_color};
                padding:6px 12px;
                border-radius:20px;
                font-weight:bold;
            ">
                {status}
            </div>

            <div style="margin-top:15px;">
                {skills_html}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )