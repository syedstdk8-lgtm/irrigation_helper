import streamlit as st
import pypdf as pd2
from sentence_transformers import sentence_transformer, util
import torch

st.set_page_config (page_title = "simple AI", layout = "wide")
st.title("simple AI")
st.caption("please enter the meaning you want to find")

file = pd2.read("local_path")

@st.cache_resources
def load_model():
    return sentence_transformer("ALL-MiniLM-L6-V2")

model = load_model()
