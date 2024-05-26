import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

#Image
img = Image.open("C:/Users/atif/OneDrive/Data Science NED/Machine Learning/Projects/Streamlit_Tutorial/assets/logo.png")
st.image(img, width=200)

#Title
st.title("Brookes Pharma (Pvt.) Ltd.")

#Header
st.header("Invoice Management System")

#subheader
st.subheader("Mantain Invoices")

#Text
st.text("This is the invoice mangement system")

#Markdown
st.markdown("### This is markdown")

#Success
st.success("Success")

#Info
st.info("Information")

#Warning
st.warning("Warning")

#Error
st.error("Error")

#Exception
exp = ZeroDivisionError("Trying to divide by zero")
st.exception(exp)

#Wrtite Text
st.write("Write text with write")
st.write(range(0,100))

#Check Boxes
if st.checkbox("Show/Hide"):
    st.text("Showing the widget")

#Radio Button
status = st.radio("Select Gender", ("Male", "Female"))
if (status=="Male"):
    st.success("Male")
else:
    st.success("Female")

#Selection Box
hobby = st.selectbox("Hobbies", ["Dancing", "Music", "Cricket"])
st.write("You hobbies is: ", hobby)

#Multi Select Box
hobbies = st.multiselect("Courses", ["Python", "Power Bi", "Data Science", "Machine Learning",
                                     "Deep Learning", 'Neural Network'])

st.write("Your courses are: ", len(hobbies), "hobbies")


#Button
st.button("Click me for no reason")
if (st.button("About")):
    st.text("Welcome to The Brookes Family!")

# Text Input

# save the input text in the variable 'name'
# first argument shows the title of the text input box
# second argument displays a default text inside the text input area
name = st.text_input("Enter Your name", "Welcome, ...")

# display the name when the submit button is clicked
# .title() is used to get the input text string
if(st.button('Submit')):
	result = name.title()
	st.success(result)
     
#Slider
level = st.slider("Select the level", 1, 100)
st.text("Selected {}".format(level))


