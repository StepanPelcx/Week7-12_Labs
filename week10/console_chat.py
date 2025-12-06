from openai import OpenAI
client = OpenAI(api_key="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")

print("ChatGPT Console Chat")
print("Type 'quit' to exit\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Goodbye!")
        break
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": user_input}]
    )
    answer = response.choices[0].message.content
    print(f"AI: {answer}\n")
