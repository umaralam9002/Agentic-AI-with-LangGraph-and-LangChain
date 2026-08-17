import os
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")
# LangSmith Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANG_SMITH_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the question asked"),
        ("user", "Question:{question}")
    ]
)

## streamlit framework
st.title("Langchain Demo With Google Gemini 2.5")
input_text = st.text_input("What question you have in mind?")

## Ollama Llama2 model
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash",google_api_key=os.environ["GEMINI_API_KEY"])
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))