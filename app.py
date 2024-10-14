from dotenv import load_dotenv
import streamlit as st
import os
import textwrap
import google.generativeai as genai

load_dotenv()  # Load environment variables from .env file

# Configure API key for Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get response from Gemini model
def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-1.5-flash')  # Ensure the correct model is used
    response = model.generate_content(question)
    return response.text

# Initialize Streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Austin's LLM Application")

# User input
input_text = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

# Handle submit button click
if submit:
    response = get_gemini_response(input_text)
    st.subheader("The Response is")
    st.write(response)
