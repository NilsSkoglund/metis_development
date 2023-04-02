import streamlit as st
from PIL import Image

with st.sidebar:
    image = Image.open(f"pages/tågstation ddimer v2.png")
    st.image(image)

st.subheader("D-dimer")