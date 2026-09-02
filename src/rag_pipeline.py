from src.embedding import create_query_embedding
from src.retriever import search_faiss
from src.llm import generate_answer


def ask_rag(
        question,
        index,
        chunks
):
    
    # 1. Create question embedding


    query_embedding = create_query_embedding(question)



    # 2. Retrieve relevant chunks

    results = search_faiss(
        query_embedding,
        index,
        chunks,
        k=3
    )

    # 3. Build context

    context = "\n\n".join(
        [
            doc.page_content
            for doc in results
        ]
    )

    
    



    # 4. Generate answer

    answer = generate_answer(
       question,
       context
       )
        
        
    return answer,results
