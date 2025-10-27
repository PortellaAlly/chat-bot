from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"), 
    base_url="https://api.groq.com/openai/v1"
)

def chat_with_ai(prompt):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile", 
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=1024
    )
    
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    print("Digite 'sair' para encerrar\n")
    
    while True:
        user_input = input("Você: ")
        if user_input.lower() in ["sair", "exit", "quit", "tchau", "até mais"]:
            print("Encerrando o chat. Até mais!")
            break
        
        if not user_input.strip():
            continue
            
        try:
            response = chat_with_ai(user_input)
            print(f"IA: {response}\n")
        except Exception as e:
            print(f"Erro: {e}\n")