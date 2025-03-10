import streamlit as st
from components.tabs import main_tabs

# Configure page title for the homepage.
st.set_page_config(page_title="Addition Intelligence")

# This add side bar to the page.
st.sidebar.title('Addition Intelligence')

with st.form(key='search_form', border=False):
    col1, col2 = st.columns([5, 1])  # Create two columns with a ratio of 4:1
    with col1:
        search_query = st.text_input("", placeholder="Type your search here...", label_visibility='collapsed')
    with col2:
        submit_button = st.form_submit_button(label='search', use_container_width=True)

main_tabs()


