from src.pdf_loader import load_pdf_folder 
from src.image_loader import load_images
from src.text_splitter import split_documents
from src.embedding import create_embedding
from src.vector_store import create_vector_store,save_vector_store
from src.embedding import create_query_embedding 
from src.storage import save_chunks
from config import PDF_FOLDER


print("Starting database construction...")


# 1/ Load PDF documents from the specified folder

documents = PDF_FOLDER

print ("Documents loaded:", len(documents))

# 2/ Split the loaded documents in chunks

chunks = split_documents(documents)
print("Chunks created:", len(chunks))

# 3/ Create embeddings for the chunks

embeddings = create_embedding(chunks)
print("Embeddings created")

# 4/ Create a FAISS vector store from the embeddings

index= create_vector_store(embeddings)
print("FAISS index created:", index.ntotal)

# 5/ Save the FAISS index to disk
save_vector_store(index, "data/faiss_index.index")

save_chunks(
    chunks,"storage/chunks.pkl"
)

print ("Database succcessfully saved!")
    