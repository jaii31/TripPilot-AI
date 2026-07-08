from pathlib import Path
import streamlit as st


STYLE_DIR = Path(__file__).parent / "styles"


def load_styles():

    css = ""

    for file in sorted(STYLE_DIR.glob("*.css")):
        css += file.read_text(encoding="utf-8")

    st.markdown(

        f"""
        <style>

        {css}

        </style>
        """,

        unsafe_allow_html=True

    )