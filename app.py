import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

chat = client.chats.create(model="gemini-3.5-flash-lite")

print("--- Chat iniciado (digite 'sair' para encerrar) ---")

while True: 
  pergunta = input("\nVocê: ")
  if pergunta.lower() in ["sair", "exit"]:
    break

  response = chat.send_message(pergunta)
  print(f"\nGemini: {response.text}")