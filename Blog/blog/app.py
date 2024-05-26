import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers

# Function to get reponse from Llama 2 model

def get_llama_reponse(input_text,no_words,blog_style):

    ## Llama2 model
    llm=CTransformers(model="models\llama-2-7b-chat.ggmlv3.q8_0.bin",model_type="llama",config={'max_new_tokens':256,"temperature":0.01})

    #model = AutoModelForCausalLM.from_pretrained(
    #model_name,
    #quantization_config=bnb_config,
    #device_map=device_map,
    #local_files_only = True)
    
    # Prompt Template

    template=f"Write a blog for {blog_style} job profile for a topic {input_text} within {no_words} words."

    prompt = PromptTemplate(input_variables=["blog_style", "input_text", "no_words"],
                            template=template)
    
    # Generate the reponse from llama 2 model

    response = llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    print(response)
    return response


st.set_page_config(page_title="Generate Blogs",
                   page_icon="👋🏻",
                   layout="centered",
                   initial_sidebar_state="collapsed")

st.header("Generate My Blogs 👋🏻")
input_text = st.text_input("Enter the blog topic")

# creating two more columns for additional 2 fields

col1, col2 = st.columns([5,5])
with col1:
    no_words=st.text_input("No of Words")

with col2:
    blog_style=st.selectbox("Writing the blog for",
                            ("Researchers", "DataScientisit", "Common People"),index=0)

submit=st.button("Generate")

# Final Response
st.write(get_llama_reponse(input_text,no_words,blog_style))

