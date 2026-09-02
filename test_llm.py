from src.llm import generate_answer


response = generate_answer(
    "Explain BRCA1 in simple words."
)


print(response)