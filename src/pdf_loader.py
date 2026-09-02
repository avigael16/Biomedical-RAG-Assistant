import os
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


def load_pdf_folder(folder_path):
    documents = []
    pdf_files= Path(folder_path).glob("*.pdf")
    

    for pdf_file in pdf_files:
        loader = PyPDFLoader(str(pdf_file))

        docs = loader.load()
        
        documents.extend(docs)

    return documents

def load_single_pdf (pdf_path):

    loader =PyPDFLoader(pdf_path)

    documents = loader.load()

    return documents