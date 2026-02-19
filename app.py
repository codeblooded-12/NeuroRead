import streamlit as st
import PyPDF2
import time
import re

st.set_page_config(page_title="NeuroRead", layout="centered")

st.title("🧠 NeuroRead")
st.subheader("RSVP-Based Speed Reading & Focus Tool")

st.write(
    "Upload a PDF and read one word at a time to improve focus, "
    "concentration, and reading speed using Rapid Serial Visual Presentation (RSVP)."
)

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

wpm = st.slider("Select Reading Speed (Words Per Minute)", 100, 800, 360)

if uploaded_file is not None:
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""

    for page in pdf_reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + " "

    # Clean text
    text = re.sub(r'\s+', ' ', text).strip()

    words = text.split(" ")

    st.success(f"PDF loaded successfully! Total words: {len(words)}")

    if st.button("Start Reading"):
        delay = 60 / wpm
        word_placeholder = st.empty()

        for word in words:
            word_placeholder.markdown(
                f"<h1 style='text-align:center; font-size:60px;'>{word}</h1>",
                unsafe_allow_html=True
            )
            time.sleep(delay)
