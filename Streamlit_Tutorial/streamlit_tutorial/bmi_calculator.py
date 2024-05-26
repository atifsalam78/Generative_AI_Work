import streamlit as st
from PIL import Image

img = Image.open("C:/Users/atif/OneDrive/Data Science NED/Machine Learning/Projects/Streamlit_Tutorial/assets/logo.png")
st.image(img, width=150)

st.title("Welcom to BMI Calculator")

weight = st.number_input("Enter your weight (in Kgs)")

status = st.radio("Select your height format", ("cms", "meters", "feet"))
if (status=="cms"):
    height = st.number_input("Centimeters")

    try:
        bmi = weight / ((height/100)**2)
    except:
        st.text("Enter some value of height")

elif (status=="meters"):
    height = st.number_input("Meters")

    try:
        bmi = weight / (height**2)
    except:
        st.text("Enter some value of height")

else:
    height = st.number_input("Feet")

    try:
        bmi = weight / (((height/3.28))**2)
    except:
        st.text("Enter some value of height")

if (st.button("Calculate BMI")):
    st.text("Your BMI Index is {}".format(bmi))

    if (bmi<16):
        st.error("You are extremely underweight")

    elif (bmi >= 16 and bmi < 18.5):
        st.warning("You are underweight")

    elif (bmi >=18.5 and bmi < 25):
        st.success("You are healthy")

    elif (bmi >= 25 and bmi < 30):
        st.warning("You are overweight")

    elif (bmi >= 30):
        st.error("You are extremely overweight")
