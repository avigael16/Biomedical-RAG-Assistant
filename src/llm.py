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




def rewrite_question_with_history(question, history):
    if not history:
        return question

    conversation = ""

    for message in history[-6:]:
        role = message["role"]
        content = message["content"]

        conversation += f"{role}: {content}\n"

    prompt = f"""
You are given a conversation between a user and a biomedical AI assistant.

Conversation history:
{conversation}

Current user question:
{question}

Rewrite the current question as a complete standalone question.

Resolve references such as:
- it
- this
- that
- they
- this disease
- this gene
- this treatment

using the conversation history.

Do not answer the question.
Only return the rewritten question.

If the question is already standalone, return it unchanged.
"""

    response = ollama.chat(
        model="llama3.1:8b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"].strip()