import streamlit as st

from src.vector_store import load_vector_store
from src.storage import load_chunks
from src.rag_pipeline import ask_rag

from config import FAISS_PATH, CHUNKS_PATH

from src.upload_manager import saved_uploaded_pdf,load_single_pdf

st.title("🧬Biomedical RAG Assistant ")

st.subheader("📄 Upload your documents")

uploaded_pdf= st.file_uploader(
    "Choose a PDF file",
    type=["pdf"]
)

if uploaded_pdf:

    pdf_path = saved_uploaded_pdf(uploaded_pdf)

    st.success(
        f"PDF saved successfully:{pdf_path}"
    )
    documents= load_single_pdf(pdf_path)
    st.write(
        "Number of pages:",
        len(documents)

    )

# Load database

index=FAISS_PATH

chunks = CHUNKS_PATH

st.write( 
    "Ask question about your biomedical documents."
)

question = st.text_input(
     "Enter your medical question"
)


if question :

    with st.spinner("Searching documents and generating answer..."):
        answer ,sources = ask_rag(
            question,
            index,
            chunks
        )
        
    st.subheader("Answer")

    st.write(answer)

    st.subheader("Sources")

    st.subheader("Sources")

    for i, doc in enumerate(sources):

        st.write(
            f"Source {i+1}:",
            doc.metadata
        )

