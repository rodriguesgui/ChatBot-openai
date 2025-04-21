import openai
import os
import time
from dotenv import load_dotenv

# Carregar a chave do OpenAI
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Criar uma função para interagir com o GPT-3.5
def perguntar(mensagem):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente gaúcho bem gente boa. Responde com clareza e educação."},
                {"role": "user", "content": mensagem}
            ]
        )
        return response.choices[0].message['content'].strip()
    except openai.error.RateLimitError:
        print("Cota excedida. Tente novamente mais tarde.")
        return None

# Loop de interação com o usuário
print("🤖 Digita tua pergunta. Escreve 'sair' pra encerrar.")
while True:
    msg = input("Tu: ")
    if msg.lower() in ["sair", "exit", "quit"]:
        print("Bot: Tchê, foi tri massa falar contigo! Até mais ver.")
        break
    
    resp = perguntar(msg)
    if resp:  # Se a resposta for válida, imprime
        print("Bot:", resp)
    else:
        print("Bot: Não consegui te responder agora. Tente novamente em breve.")
        
    # Implementando um intervalo para evitar exceder a cota rapidamente
    time.sleep(2)  # Espera 2 segundos antes de permitir outra interação

