import streamlit as st

st.title("Irrigation Predicting System")
tab1 = st.tabs("Tab 1")
st.subheader("This is an irrigation predictor system it gives an approx answer")
st.image("C:/Users/syeds/OneDrive/Pictures/rpo/aggri.avif")

tab1 = st.sidebar.radio("MENU :", [ "statistics", "crops data" ])



