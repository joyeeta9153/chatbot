from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser ##default output parser

import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv() 

open_api =  os.getenv("OPENAI_API_KEY") or st.secrets["OPENAI_API_KEY"]
print("Loaded API Key:", open_api)  
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

llm=ChatOpenAI(model_name="gpt-3.5-turbo",openai_api_key=open_api)
output_parser=StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
        response = chain.invoke({'question': input_text})
        st.write(response)
   
