from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

#langsmith
os.environ["LANGCHAIN_TRACING_V2"]="true"
langchain_api=os.getenv("LANGCHAIN_API_KEY")
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant.Please respond to the user queries."),
        ("user","Question:{question}")
    ]
)
st.title('Langchain Demo With Ollama')
input_text=st.text_input("Search the topic you want")
llm=Ollama(model="gemma:2b-instruct")
output_parser=StrOutputParser()
chain = prompt | llm | output_parser
if input_text:
    response = chain.invoke({"question",input_text})
    st.write(response)
    