import streamlit as st
import numpy as np
import pandas as pd
import time

import base64

@st.cache_resource()
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("/Streamlit_Tutorial/assets/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_png_as_page_bg("C:/Users/atif/OneDrive/Data Science NED/Machine Learning/Projects/Streamlit_Tutorial/assets/background.png")


st.title("Personal Bot")


# with st.sidebar:
# 	st.write("About")
# 	st.text("""
# 		This app is created for the educational purpose not for 
# 		the professional and business purposes

# 		""")
	

# dataframe = pd.DataFrame(
# 	np.random.randn(10,20),
# 	columns=("col %d" % i for i in range(20))
# )

# # st.dataframe(dataframe.style.highlight_max(axis=0))
# st.table(dataframe)

# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [24.86080000, 67.01040000],
#     columns=['lat', 'lon'])

# st.map(map_data)


# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
#     })

# option = st.selectbox(
#     'Which number do you like best?',
#      df['first column'])

# 'You selected: ', option

# Add a selectbox to the sidebar:
# add_selectbox = st.sidebar.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone')
# )

# # Add a slider to the sidebar:
# add_slider = st.sidebar.slider(
#     'Select a range of values',
#     0.0, 100.0, (25.0, 75.0)
# )

# left_column, right_column = st.columns(2)
# # You can use a column just like st.sidebar:
# left_column.button('Press me!')

# # Or even better, call Streamlit functions inside a "with" block:
# with right_column:
#     chosen = st.radio(
#         'Sorting hat',
#         ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
#     st.write(f"You are in {chosen} house!")

# 'Starting a long computation...'

# # Add a placeholder
# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(100):
#   # Update the progress bar with each iteration.
#   latest_iteration.text(f'Iteration {i+1}')
#   bar.progress(i + 1)
#   time.sleep(0.1)

# '...and now we\'re done!'