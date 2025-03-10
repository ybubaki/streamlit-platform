import streamlit as st

def company_info_view():
    st.markdown(
        """
        <style>
        .centered-container {
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 1em;
            text-align: center;
            font-size: 20px;
            font-weight: bold;
            background-color: #f0f0f0; /* Light gray background */
            border-radius: 10px;
            margin-bottom: 32px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    with st.container():
        st.markdown('<div class="centered-container">company name</div>', unsafe_allow_html=True)