import streamlit as st

from src.vector_store import load_vector_store
from src.storage import load_chunks
from src.rag_pipeline import ask_rag

from config import FAISS_PATH, CHUNKS_PATH

from src.upload_manager import save_uploaded_pdf
from src.pdf_loader import load_single_pdf

st.title("🧬Biomedical RAG Assistant ")

st.subheader("📄 Upload your documents")

uploaded_pdf= st.file_uploader(
    "Choose a PDF file",
    type=["pdf"]
)

if uploaded_pdf:

    pdf_path = save_uploaded_pdf(uploaded_pdf)

    st.success(
        f"PDF saved successfully:{pdf_path}"
    )
    documents= load_single_pdf(pdf_path)
    st.write(
        "Number of pages:",
        len(documents)

    )

if "messages" not in st.session_state:
        st.session_state.messages= []

for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
   

# Load database

index=load_vector_store(FAISS_PATH)

chunks = load_chunks(CHUNKS_PATH)

# ---------------------------------------------------
# CHAT
# ---------------------------------------------------

st.write( 
    "Ask question about your biomedical documents."
)

question = st.chat_input(
     "Enter your biomedical question"
)


if question :

#save user question to session state

    st.session_state.messages.append(
        {"role":"user",
         "content":question
         }
    )

    # Display user question in chat message container
    with st.chat_message("user"):
        st.markdown(question)

    #Previous conversation
    history = st.session_state.messages[:-1]


    #Generate answer using RAG pipeline
    with st.spinner("Searching documents and generating answer..."):
        answer ,sources = ask_rag(
            question,
            index,
            chunks,
            history=history
        )
        
    
    #Save  assistant answer 
    st.session_state.messages.append(
        {"role":"assistant",
         "content":answer
         }
    )


    # Display assistant answer
    with st.chat_message("assistant"):
         st.markdown(answer)


    # Display sources     
    st.subheader("Sources")
    for i, doc in enumerate(sources):

        st.write(
            f"Source {i+1}:",
            doc.metadata
        )

    
