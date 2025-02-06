import os
import streamlit as st
from local_rag import get_answer

# working directory of folder LLAMA
working_dir = os.path.dirname(os.path.abspath(__file__))

st.set_page_config(
    page_title="Chat with PDF Doc",
    page_icon="📄",
    layout="centered"
)

st.title("RAG - Llama 3.2 - Ollama")

# File uploader section
uploaded_file = st.file_uploader(label="Upload your file", type=["pdf"])

# Query section
user_query = st.text_input("Ask your question?")

# Read file
if st.button("Run"):
    bytes_data = uploaded_file.read()
    file_name = uploaded_file.name

    # Save the file to the working directory
    file_path = os.path.join(working_dir, file_name)
    with open(file_path, "wb") as f:
        f.write(bytes_data)

    # RAG
    answer = get_answer(file_name, user_query)

    st.success(answer)