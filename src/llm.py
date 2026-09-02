import ollama

from src.prompts import build_prompt
from config import LLM_MODEL

def generate_answer(question, context):
    prompt = build_prompt(question,context)

    response=ollama.chat(
        model=LLM_MODEL,
        messages= [
            {"role": "user",
             "content": prompt
             }
            ]
    )
    return response["message"]["content"]