from src.embedding import create_query_embedding
from src.retriever import search_faiss
from src.llm import generate_answer
from src.llm import generate_answer,rewrite_question_with_history

def ask_rag(
        question,
        index,
        chunks,
        history=None
):
    if history is None:
        history = []

    # 1. Rewrite question with history
    standalone_question = rewrite_question_with_history(
        question,
        history
    )    

    # 1.bis Create question embedding


    query_embedding = create_query_embedding(standalone_question)



    # 2. Retrieve relevant chunks

    results = search_faiss(
        query_embedding,
        index,
        chunks,
        k=3
    )

    # 4. Build document context
    context_parts = []

    for doc in results:

        source = doc.metadata.get("source", "Unknown source")
        page = doc.metadata.get("page", "Unknown page")

        context_parts.append(
            f"""
    Source: {source}
    Page: {page}

    {doc.page_content}
     """
        )

    document_context = "\n\n".join(context_parts)

    # 5. Build recent conversation history
    conversation_context = ""

    for message in history[-6:]:
        conversation_context += (
            f'{message["role"]}: {message["content"]}\n'
        )

    # 6. Give both the conversation and documents to the LLM
    final_context = f"""
RECENT CONVERSATION:

{conversation_context}

RETRIEVED BIOMEDICAL DOCUMENTS:

{document_context}
"""

    # Important:
    # We keep the user's original question for the final answer
    answer = generate_answer(
        question,
        final_context
    )

    return answer, results