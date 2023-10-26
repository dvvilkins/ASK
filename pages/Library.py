import datetime
import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="ASK Library", initial_sidebar_state="collapsed")


st.markdown( """ <style> [data-testid="collapsedControl"] { display: none } </style> """, unsafe_allow_html=True, )

st.title("//ASK Auxiliary Source of Knowledge")
st.write("  ")

want_to_contribute = st.button("Return to the App")
if want_to_contribute:
    switch_page('ASK_chatstyle')