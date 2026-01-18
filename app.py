from __future__ import annotations
import streamlit as st

st.set_page_config(page_title="OVGU Explorer v1", layout="wide")
st.title("OVGU Explorer v1")

st.write("Use the sidebar to open a view:")
st.page_link("pages/3_🔬_Thematic_Overview.py", label="🔬_Thematic_Overview")
st.page_link("pages/4_🔎_Thematic_Drilldown.py", label="🔎_Thematic_Drilldown")