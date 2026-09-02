def search_faiss(query_embedding, index, chunk,k=3):

    distance, indices = index.search(
        query_embedding, k  
    )

    results=[]
    for idx in indices[0]:
        results.append(chunk[idx])

    return results