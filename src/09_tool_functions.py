def rag_tool(question):
    question_embedding = embedding_model.encode([question])
    results = collection.query(
        query_embeddings=question_embedding.tolist(),
        n_results=3
    )
    retrieved_chunks = results['documents'][0]
    context = "\n\n".join(retrieved_chunks)
    return context


def calculator_tool(question):
    expression = question.lower()
    expression = expression.replace("what is", "")
    expression = expression.replace("calculate", "")
    expression = expression.replace("=", "")
    expression = expression.replace("×", "*")
    expression = expression.replace("x", "*")
    expression = expression.replace("÷", "/")
    expression = expression.strip()
    answer = eval(expression)
    return answer


def greeting_tool():
    return """
Hello!

I can help you with:

1. Answering questions from your PDF documents.
2. Solving mathematical calculations.

How can I help you today?
"""


def choose_tool(question):
    question = question.lower().strip()

    if question in ["hi", "hello", "hey", "good morning", "good evening"]:
        return "greeting"

    elif any(operator in question for operator in ["+", "-", "*", "/", "×", "÷"]):
        return "calculator"

    else:
        return "rag"
