import streamlit as st

from retrieve import retrieve
from llm import ask_llm

st.set_page_config(page_title="Mozilla.ai Local RAG")

st.title("📄 Local Document Q&A")

question = st.text_input("Ask a question about the PDF")

if st.button("Submit"):

    context = retrieve(question)

    answer = ask_llm(question, context)

    st.subheader("Retrieved Context")
    st.write(context)

    st.subheader("Answer")
    st.write(answer)