import streamlit as st


def score_card(title, value, icon="📊", color="#2563EB"):
    st.markdown(
        f"""
        <div style="
            background: white;
            padding: 20px;
            border-radius: 15px;
            border-left: 6px solid {color};
            box-shadow: 0px 2px 10px rgba(0,0,0,0.08);
            margin-bottom: 10px;
        ">
            <div style="
                font-size: 18px;
                color: #64748B;
                font-weight: 600;
            ">
                {icon} {title}
            </div>

            <div style="
                font-size: 32px;
                font-weight: bold;
                color: #0F172A;
                margin-top: 10px;
            ">
                {value}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )