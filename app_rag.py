
from src.vector_store import load_vector_store
from src.storage import load_chunks
from src.rag_pipeline import ask_rag
from config import FAISS_PATH ,CHUNKS_PATH

 


# 1/ load FAISS memory index from disk
index = FAISS_PATH

# 2 load associated texts

chunks= CHUNKS_PATH



# 4.a User question

while True: 

    question= input("Question:")
    if  question.lower() == 'exit':
            break



    answer, sources =ask_rag(question,index,chunks)

    print(answer)

