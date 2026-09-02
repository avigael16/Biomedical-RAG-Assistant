from sentence_transformers import SentenceTransformer

# load the model only one time for all futures uses, using
#  HuggingFace
model = SentenceTransformer ("BAAI/bge-base-en-v1.5")

def create_embedding(chunks):
    """
    transforms chunks to embeddings.
    
    """

    texts = [chunk.page_content for chunk in chunks]

    embeddings = model.encode(
        texts,
        show_progress_bar=True
        )
    return embeddings

def create_query_embedding(query):
        embedding=model.encode([query])

        return embedding 