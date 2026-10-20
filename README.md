# 💬 Chat Simples via Terminal com Gemini API

Projeto prático desenvolvido para estudos com o objetivo de demonstrar a integração básica com a API do **Google Gemini** em Python, utilizando a biblioteca oficial `google-genai` e mantendo o histórico de conversação ativo no terminal.

---

## 📌 Sobre o Projeto

Este repositório contém um script Python simples que implementa um chat interativo diretamente pelo terminal. Diferente de chamadas isoladas de geração de texto, este exemplo utiliza sessões de chat (`client.chats.create`), o que permite que a IA lembre das mensagens anteriores dentro da mesma execução.

### 🎯 Objetivos de Aprendizado
- Configuração de credenciais e variáveis de ambiente (`.env`).
- Inicialização do cliente da SDK oficial `google-genai`.
- Criação e gerenciamento de sessões de chat contínuas.
- Criação de um loop interativo no terminal em Python.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **[google-genai](https://pypi.org/project/google-genai/)**: SDK oficial do Google para modelos de IA.
- **[python-dotenv](https://pypi.org/project/python-dotenv/)**: Para carregamento seguro de variáveis de ambiente.

---

## 📂 Estrutura do Projeto

```text
.
├── app.py           # Script principal com a lógica do chat
├── .env             # Arquivo com a chave de API (NÃO subir no GitHub)
├── .env.example     # Modelo de configuração das variáveis de ambiente
├── .gitignore       # Arquivos/pastas ignorados pelo Git
└── README.md        # Documentação do projeto
```

## 🚀 Como Executar o Projeto
1. Pré-requisitos
Certifique-se de ter o Python instalado e de possuir uma chave de API do Gemini, obtida gratuitamente no Google AI Studio.

2. Clonar o Repositório
Bash
git clone [https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git](https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git)
cd NOME-DO-REPOSITORIO
3. Criar e Ativar o Ambiente Virtual (venv)
Windows (Git Bash):

Bash
python -m venv venv
source venv/Scripts/activate
Linux/macOS:

Bash
python3 -m venv venv
source venv/bin/activate
4. Instalar as Dependências
Bash
pip install google-genai python-dotenv
5. Configurar as Variáveis de Ambiente
Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:

Fragmento do código
GEMINI_API_KEY=sua_chave_de_api_aqui
💻 Como Usar
Rode o script no terminal:

Bash
python app.py
Digite sua mensagem e pressione Enter para conversar. Para encerrar a sessão, basta digitar sair ou exit.

📝 Explicação do Código (app.py)
Python
import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

# 1. Carrega o arquivo .env localizado na mesma pasta do script
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

# 2. Inicializa o cliente apontando para a chave guardada na variável de ambiente
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# 3. Cria a sessão de chat (mantém contexto/histórico durante a execução)
chat = client.chats.create(model="gemini-2.5-flash")

print("--- Chat iniciado (digite 'sair' para encerrar) ---")

# 4. Loop contínuo de interação via terminal
while True:
    pergunta = input("\nVocê: ")
    if pergunta.lower() in ["sair", "exit"]:
        break

    # Envia a mensagem para a sessão de chat ativa
    response = chat.send_message(pergunta)
    print(f"\nGemini: {response.text}")
