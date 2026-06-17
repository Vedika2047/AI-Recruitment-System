import streamlit as st


def load_navbar_styles():
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0F172A, #1E293B);
        }

        [data-testid="stSidebar"] h1,
        [data-testid="stSidebar"] h2,
        [data-testid="stSidebar"] h3,
        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] label {
            color: white !important;
        }

        .main-title {
            font-size: 26px;
            font-weight: 800;
            color: #38BDF8;
            margin-bottom: 5px;
        }

        .sub-title {
            font-size: 14px;
            color: #CBD5E1;
            margin-bottom: 25px;
        }

        .nav-footer {
            position: fixed;
            bottom: 20px;
            color: #94A3B8;
            font-size: 13px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


def navbar():
    load_navbar_styles()

    with st.sidebar:
        st.markdown('<div class="main-title">AI Recruitment</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-title">Smart Hiring Dashboard</div>', unsafe_allow_html=True)

        page = st.radio(
            "Go to",
            [
                "Dashboard",
                "Upload Resume",
                "Candidate Ranking",
                "Interview Scheduler",
                "Analytics"
            ],
            label_visibility="collapsed"
        )

        st.markdown("---")

        st.info("Member 3: Frontend Engineer")

        st.markdown(
            """
            <div class="nav-footer">
                Built with Streamlit
            </div>
            """,
            unsafe_allow_html=True
        )

    return page