from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser ##default output parser

import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv() 
open_api = st.secrets["OPENAI_API_KEY"]
os.environ["OPENAI_API_KEY"] = open_api
#langsmith
os.environ["LANGCHAIN_TRACING_V2"]="true"
langchain_api=os.getenv("LANGCHAIN_API_KEY")

## Prompt template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant.Please respond to the user queries."),
        ("user","Question:{question}")
    ]
)

##streamlit framework

st.title('Langchain Demo With OPENAI API')
input_text=st.text_input("Search the topic you want")

# openAI llm

llm=ChatOpenAI(model_name="gpt-3.5-turbo")
output_parser=StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    try:
        response = chain.invoke({'question': input_text})
        st.write(response)
    except Exception as e:
        import traceback
        st.error("An error occurred.")
        st.code(traceback.format_exc())
