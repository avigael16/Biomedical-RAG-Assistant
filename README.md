# 🧬 Biomedical RAG AI Assistant


A biomedical question-answering application built with Python, FAISS and a local LLM.

The goal of this project is to explore how Retrieval-Augmented Generation (RAG) can be used to interact with biomedical documents. Users can upload PDF files and ask questions about their content through a Streamlit chat interface.

I built this project as part of my work on AI and bioinformatics, with a focus on understanding the different components of a RAG pipeline rather than relying entirely on high-level frameworks.

## Features

- Upload biomedical PDF documents
- Extract and split text into smaller chunks
- Generate embeddings with Sentence Transformers
- Store and search embeddings using FAISS
- Retrieve relevant passages for a user question
- Generate answers using a local LLM through Ollama
- Display the conversation in a Streamlit chat interface
- Keep conversation history during the session
- Show the retrieved sources used to generate an answer

Medical image support is currently being added.

## How it works

The application follows a standard RAG pipeline:

```text
Biomedical documents
        |
        v
   Text extraction
        |
        v
     Chunking
        |
        v
    Embeddings
        |
        v
   FAISS index
        |
        v
User question
        |
        v
Similarity search
        |
        v
Relevant chunks
        |
        v
   Local LLM
        |
        v
Answer + sources
```

Instead of asking the language model to answer only from its internal knowledge, the application first searches the uploaded documents for relevant information. These passages are then provided to the model as context.

## Project structure

```text
Biomedical_RAG_Assistant/
│
├── src/
│   ├── conversation.py
│   ├── embedding.py
│   ├── image_analyzer.py
│   ├── image_loader.py
│   ├── knowledge_base.py
│   ├── llm.py
│   ├── pdf_loader.py
│   ├── prompts.py
│   ├── rag_pipeline.py
│   ├── retriever.py
│   ├── storage.py
│   ├── text_splitter.py
│   ├── upload_manager.py
│   ├── utils.py
│   └── vector_store.py
│
├── build_database.py
├── streamlit_app.py
├── config.py
├── requirements.txt
└── README.md
```

## Technologies

- Python
- Streamlit
- FAISS
- Sentence Transformers
- Ollama
- Llama
- NumPy

## Running the project

Clone the repository:

```bash
git clone https://github.com/avigael16/Biomedical-RAG-Assistant.git
cd Biomedical-RAG-Assistant
```

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Make sure Ollama is installed and the required model is available locally.

Then start the application:

```bash
streamlit run streamlit_app.py
```

## Current work

I am currently extending the project to support medical images in addition to text documents.

The next steps are:

- medical image upload and preprocessing
- support for common medical imaging formats
- integration of image analysis into the chat
- improved retrieval and source attribution
- better handling of newly uploaded documents
- evaluation of retrieval quality

## Disclaimer

This project is intended for educational and research purposes. It is not a medical diagnostic tool and should not be used to make clinical decisions.
