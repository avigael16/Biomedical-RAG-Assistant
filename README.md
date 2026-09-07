# 🧬 Biomedical RAG AI Assistant

A local Retrieval-Augmented Generation (RAG) application designed to answer questions from biomedical documents using semantic search and a locally hosted Large Language Model.

The project combines document processing, vector search, local LLM inference and an interactive Streamlit interface.

## 🎯 Project Goal

Biomedical literature can contain large amounts of complex information distributed across multiple documents.

The goal of this project is to build an AI assistant capable of:

- processing biomedical PDF documents;
- retrieving relevant information using semantic search;
- answering questions based on retrieved evidence;
- providing document sources for generated answers;
- running an LLM locally;
- eventually integrating medical image analysis.

## 🏗️ Architecture

```text
PDF Documents
      │
      ▼
PDF Loader
      │
      ▼
Text Chunking
      │
      ▼
Embeddings
      │
      ▼
FAISS Vector Database
      │
      │
User Question
      │
      ▼
Question Embedding
      │
      ▼
Semantic Retrieval
      │
      ▼
Top Relevant Chunks
      │
      ▼
Context Builder
      │
      ▼
Local LLM (Llama / Ollama)
      │
      ▼
Answer + Sources
```

## ✨ Current Features

### Document processing

- PDF loading with LangChain / PyPDFLoader
- Automatic document chunking
- Metadata preservation
- Page and source tracking

### Semantic search

- Sentence Transformer embeddings
- FAISS vector indexing
- Persistent FAISS storage
- Top-K semantic retrieval

### Retrieval-Augmented Generation

- Context construction from retrieved passages
- Biomedical-oriented prompting
- Answers grounded in retrieved documents
- Source/page attribution
- Fallback when the answer cannot be found in the provided context

### Local AI

The language model runs locally through Ollama, allowing the RAG pipeline to operate without sending the document context to a hosted LLM API.

### User Interface

An interactive Streamlit interface allows users to ask questions through a web interface instead of using the command line.

### Document Upload

PDF upload support is being integrated so users can build a knowledge base from their own documents without manually modifying local project folders.

## 🧠 RAG Workflow

### 1. Indexing

Documents are loaded and split into smaller chunks.

Each chunk is transformed into a numerical embedding and stored inside a FAISS vector index.

### 2. Retrieval

When a user asks a question, the question is converted into an embedding using the same embedding model.

FAISS searches for the most semantically similar document chunks.

### 3. Generation

The most relevant chunks are assembled into a context and sent together with the user's question to the local LLM.

The model is instructed to answer using the retrieved evidence rather than relying only on its internal knowledge.

## 📁 Project Structure

```text
Biomedical_RAG_Assistant/
│
├── streamlit_app.py
├── build_database.py
├── config.py
│
├── src/
│   ├── pdf_loader.py
│   ├── image_loader.py
│   ├── text_splitter.py
│   ├── embedding.py
│   ├── vector_store.py
│   ├── storage.py
│   ├── retriever.py
│   ├── prompts.py
│   ├── llm.py
│   ├── rag_pipeline.py
│   └── upload_manager.py
│
├── uploads/
│   ├── pdfs/
│   └── images/
│
└── storage/
```

## 🛠️ Technologies

- Python
- Streamlit
- LangChain
- Sentence Transformers
- Hugging Face
- FAISS
- Ollama
- Llama

## 🚀 Running the Application

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

Make sure Ollama is installed and the configured Llama model is available.

Build the document index when required:

```bash
python build_database.py
```

Run the Streamlit application:

```bash
streamlit run streamlit_app.py
```

## 🗺️ Roadmap

Planned improvements include:

- dynamic PDF upload and indexing;
- multi-document knowledge bases;
- conversational memory;
- medical image analysis;
- multimodal RAG;
- retrieval confidence/relevance scoring;
- document comparison;
- automatic document summarization;
- improved citation handling;
- RAG evaluation;
- automated tests;
- Docker deployment;
- persistent database/storage;
- production-ready API.

## ⚠️ Disclaimer

This project is intended for educational, research and software engineering purposes.

It is not a medical device and should not be used for diagnosis, treatment decisions, or other clinical decision-making without appropriate validation and regulatory review.
