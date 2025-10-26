from openai import OpenAI
import os

client = OpenAI(api_key="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")

def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("Você: ")
        if user_input.lower() in ["sair", "exit", "quit", "tchau", "até mais"]:
            print("Encerrando o chat. Até mais!")
            break

        response = chat_with_gpt(user_input)
        print("ChatGPT: ", response)