import streamlit as st
from google import genai
from dotenv import load_dotenv

import os


load_dotenv()

client = genai.Client(api_key="google_gemini_api_key")

st.title("Hello Streamlit!")
st.write("This is a simple streamlit app.")

st.slider("Select Pay Range",0,100,50)
st.button("Click Me!")


st.subheader("Chatbot Form")
user_input = st.text_input("Enter your query: ")

if st.button("Submit"):
    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=user_input
    )
    st.write(response.text)