!pip install streamlit PyPDF2 pyngrok
%%writefile app.py
import streamlit as st
import PyPDF2
import time
import re

st.set_page_config(page_title="Focus Reading App", layout="centered")

st.title("🧠 Focus Reading / Speed Reading App")

st.write("Upload a PDF and read one word at a time to improve focus and speed.")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

wpm = st.slider("Select Reading Speed (Words Per Minute)", 100, 800, 360)

if uploaded_file is not None:
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""

    for page in pdf_reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + " "

    # Clean text
    text = re.sub(r'\s+', ' ', text)

    words = text.split(" ")

    st.success(f"PDF Loaded Successfully! Total Words: {len(words)}")

    if st.button("Start Reading"):
        delay = 60 / wpm
        word_placeholder = st.empty()

        for word in words:
            word_placeholder.markdown(
                f"<h1 style='text-align:center; font-size:60px;'>{word}</h1>",
                unsafe_allow_html=True
            )
            time.sleep(delay)
from pyngrok import ngrok
import os

# Set your ngrok auth token (get it from https://dashboard.ngrok.com/get-started/your-authtoken)
ngrok.set_auth_token("33nHw9sC2PcmXQYPUAoavEHXuAU_88qivG7MNbgUaAPgH3jGH")

# Start streamlit
!streamlit run app.py &>/dev/null &

# Open public URL
public_url = ngrok.connect(8501)
public_url
