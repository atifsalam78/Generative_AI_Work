import streamlit as st
import numpy as np
import random
import time
from openai import OpenAI

st.title("Advance Personal Bot")

with st.sidebar:
	st.write("Personal Bot")

user_name = "Atif Salam"

# Set OpenAI API key from Streamlit secrets
client = OpenAI(
    api_key="LL-6FkcZT9McvrsfRj6s3RO3dpWfS3xt95FsOwbTZ2WJSBwmKx9x77iDWG7JJ1QAzrM",
    base_url="https://api.llama-api.com"
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


if prompt := st.chat_input("Ask me anything"):
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
