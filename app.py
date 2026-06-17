import streamlit as st

from components.navbar import navbar


st.set_page_config(
    page_title="AI Recruitment System",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


def load_global_css():
    st.markdown(
        """
        <style>
        .main {
            background-color: #F8FAFC;
        }

        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }

        .page-heading {
            font-size: 34px;
            font-weight: 800;
            color: #0F172A;
            margin-bottom: 5px;
        }

        .page-subheading {
            font-size: 16px;
            color: #64748B;
            margin-bottom: 25px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


def show_page_title(title, subtitle):
    st.markdown(f'<div class="page-heading">{title}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="page-subheading">{subtitle}</div>', unsafe_allow_html=True)


def main():
    load_global_css()

    page = navbar()

    try:
        if page == "Dashboard":
            from pages import dashboard
            dashboard.show()

        elif page == "Upload Resume":
            from pages import upload_resume
            upload_resume.show()

        elif page == "Candidate Ranking":
            from pages import candidate_ranking
            candidate_ranking.show()

        elif page == "Interview Scheduler":
            from pages import interview_scheduler
            interview_scheduler.show()

        elif page == "Analytics":
            from pages import analytics
            analytics.show()

        else:
            show_page_title("AI Recruitment System", "Welcome to the smart hiring dashboard.")

    except ModuleNotFoundError as e:
        st.error("Some page/component file is missing.")
        st.code(str(e))

    except AttributeError:
        st.error("Every page file must contain a show() function.")

    except Exception as e:
        st.error("Something went wrong while loading the page.")
        st.code(str(e))


if __name__ == "__main__":
    main()