while True:
    question = input(
        "Enter your question (enter 'exit' if you don't want to continue): "
    )

    if question.lower() == "exit":
        break

    tool = choose_tool(question)

    if tool == "greeting":
        answer = greeting_tool()

    elif tool == "calculator":
        answer = calculator_tool(question)

    elif tool == "rag":
        context = rag_tool(question)

        prompt = f"""<|user|>
Use ONLY the context below to answer the question.

Context:
{context}

Question:
{question}

If the answer is not present, reply exactly:
I couldn't find that information.
<|end|>

<|assistant|>
"""

        result = pipe(
            prompt,
            max_new_tokens=120,
            return_full_text=False,
        )

        answer = result[0]["generated_text"].strip()

    print("\nAnswer:")
    print(answer)
    print("-" * 60)
