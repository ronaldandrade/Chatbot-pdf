import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Define a rota URL para os arquivos na api do Pinata 
PINATA_API_URL = "https://api.pinata.cloud/pinning/pinFileToIPFS"

# keys da API para o Pinata no .env
PINATA_API_KEY = os.getenv("PINATA_API_KEY")
PINATA_SECRET_API_KEY = os.getenv("PINATA_SECRET_API_KEY")

def upload_pdf_to_pinata(file_path):
    """
    Fazer o upload para os serviços de api do Pinata 
    Uploads a PDF file to Pinata's IPFS service.

    Args:
        file_path (str): The path to the PDF file to be uploaded.

    Returns:
        str: The IPFS hash of the uploaded file if successful, None otherwise.
    """
    #API keys do Pinata para criação dos headers
    headers = {
        "pinata_api_key": PINATA_API_KEY,
        "pinata_secret_api_key": PINATA_SECRET_API_KEY
    }

    # Abrir o arquivo em modo leitura binaria -rb- 
    with open(file_path, 'rb') as file:
        # Envia POST request para Pinata API e upload the file
        response = requests.post(PINATA_API_URL, files={'file': file}, headers=headers)

        # Check de status code (200)
        if response.status_code == 200:
            print("File uploaded successfully")
            # Retorna o IPFS hash com response JSON
            return response.json()['IpfsHash']
        else:
            print(f"Error: {response.text}")
            return None 