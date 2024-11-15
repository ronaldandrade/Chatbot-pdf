import os
from openai import OpenAI
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Iniciar o client da OpenAI com a chave da API
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

def get_openai_response(text, pdf_text):
    try:
        # Create chat request
        print("User Input:", text)
        print("PDF Content:", pdf_text) 

        # Contextualiza o conteudo do pdf com request do user
        messages = [
            {"role": "system", "content": "You are a helpful assistant for answering questions about the PDF."},
            {"role": "user", "content": pdf_text},  #Conteudo do PDF
            {"role": "user", "content": text}  # Request do usuário
        ]

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Usar o tipo de gpt de acordo com limite de acesso -gpt 4 - turbo gpt-4-min
            messages=messages,
            max_tokens=400, #Quantide de tokens de resposta
            temperature=0.7 
        )

        return response.choices[0].message.content  # Métodod de acesso
    except Exception as e:
        return f"Error: {str(e)}"
