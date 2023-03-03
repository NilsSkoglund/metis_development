import streamlit as st
from PIL import Image

with st.sidebar:
    image = Image.open(f"pages/tågstationer ddimer.png")
    st.image(image)

st.subheader("D-dimer")