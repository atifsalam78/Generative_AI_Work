import streamlit as st
from PIL import Image

img = Image.open("C:/Users/atif/OneDrive/Data Science NED/Machine Learning/Projects/Streamlit_Tutorial/assets/logo.png")
st.image(img, width=100)

st.title("Brookes Pharma Pvt. Ltd.")


