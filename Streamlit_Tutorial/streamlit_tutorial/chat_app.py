import streamlit as st
import numpy as np
import random
import time
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

user_name = os.environ.get("db_user")

st.set_page_config(
    page_title = "Bot",
    page_icon="🤖",
    layout="wide"       
)

flag_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Flag_of_Pakistan.svg/1280px-Flag_of_Pakistan.svg.png"
logo = "C:/Users/atif/OneDrive/Data Science NED/Machine Learning/Projects/Streamlit_Tutorial/assets/logo.png"

original_title = '<h1 style="text-align: center; font-family: serif; color:#363030; font-size: 40px;">Personal Bot</h1>'

background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://images.unsplash.com/photo-1709626011483-5bb4b5470ac9?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=900&ixid=MnwxfDB8MXxyYW5kb218MHx8fHx8fHx8MTcxNTYxNDE5Mw&ixlib=rb-4.0.3&q=80&w=1600");
    background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;  
    background-repeat: no-repeat;
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)

st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #7da6b3;
    }
</style>
""", unsafe_allow_html=True)


st.markdown(
    """
<style>
    .stChatMessage {
        text-align: left;
    }
</style>
""",
    unsafe_allow_html=True,
)

with st.sidebar:
    st.sidebar.markdown(original_title, unsafe_allow_html=True)    
    st.image(logo, caption="Llama 13b", width=None, use_column_width="auto", clamp=False, channels="RGB", output_format="auto")
    # st.sidebar.markdown("""This app is using llama 13b for educational purpose""")
    
client = OpenAI(
    api_key = os.environ.get("db_api_key"),
    base_url = os.environ.get("db_url")
)

def response_generator():
    response = random.choice(
        [
            f"Hello {user_name}! How can I assist you today?",
            f"Hi, {user_name}! Is there anything I can help you with?",
            f"{user_name} Do you need help?",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "llama-13b-chat"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input(f"Ask me anything"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    try:
        response = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
        )
        st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})
        with st.chat_message("assistant"):            
            st.markdown(response.choices[0].message.content)
    except Exception as e:
        st.error(f"Error: {e}")        
        st.session_state.messages.append({"role": "assistant", "content": "Error occurred. Please try again."})

# Display assistant response in chat message container
with st.chat_message("assistant"):
    response = st.write_stream(response_generator())
# Add assistant response to chat history
st.session_state.messages.append({"role": "assistant", "content": response})

