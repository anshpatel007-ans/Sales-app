import streamlit as st
import pandas as pd
from reportlab.lib.units import mm
def print_header():
    # Header section
    # below CSS is for managing default padding from the top and bottom of page
    st.markdown("""<style>.block-container{padding-top:40px;padding-bottom:10px;background-color:;}</style>""",unsafe_allow_html=True)
    col_logo, col_title = st.columns([1, 4])
    with col_logo:
        st.image("images/logo.png", width=140)
    with col_title:
        st.title(" Sales Analytics Dashboard ")
        st.markdown("""<style>.block-container{padding-top:70px;padding-bottom:20px;background:hsl(210, 5%, 90%);}📊 Kamadgiri Software Solution</style>""",
                    unsafe_allow_html=True)

