import streamlit as st
import requests

API_URL = "http://backend:8085/todos/"

def get_todos():
    response = requests.get(API_URL)
    return response.json()

def create_todo():
    todo = {"title": st.session_state["new_todo"], "description": st.session_state.get("new_desc", "")}
    response = requests.post(API_URL, json=todo)
    if response.status_code == 200:
        st.success("ToDo created successfully!")
    else:
        st.error("Error creating ToDo")

st.title("ToDo App")
todos = get_todos()

for todo in todos:
    st.write(f"{todo['title']} - {todo['description']}")

st.text_input("Title", key="new_todo")
st.text_input("Description", key="new_desc")
st.button("Add ToDo", on_click=create_todo)


if __name__ == "__main__":
    #st.set_page_config(layout="wide")
    st.write("Hello, Streamlit!")