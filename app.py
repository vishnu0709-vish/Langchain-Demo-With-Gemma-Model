import os 
from dotenv import load_dotenv

from langchain_ollama import ChatOllama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACKING_V2"]="True"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")



### Prompt template 
prompt =ChatPromptTemplate.from_messages(
[
    ("system","You are a helpful assistant. Please respond to the question asked"),
    ("human","Question:{question}")

]
)



### Streamlit Framework

st.title("Langchain Demo With Gemma Model")
input_text = st.text_input("Ask about something you want")


### Ollama Model

llm=ChatOllama(model="gemma:2b")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))