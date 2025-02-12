## 📄 Chat with PDF 🚀

O poder dos modelos da [OpenAI](https://openai.com/) usados para compreender o texto extraído de PDFs e gerar respostas.

![chatbot-pdf.png](/assets/chatbot-pdf.png)

## 📋 Índice
- [Visão Geral](#visão-geral)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Funcionalidades](#-funcionalidades)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação](#-instalação)
- [Como Usar](#-como-usar)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Contribuições](#-contribuições)
- [Licença](#-licença)


## Visão Geral

O Chatbot PDF permite que os usuários façam upload de arquivos PDF e façam perguntas diretamente sobre o conteúdo desses arquivos. A aplicação extrai o texto do PDF, o armazena na Pinata (IPFS) e usa o modelo de linguagem da OpenAI para responder às perguntas dos usuários sobre o conteúdo do documento. É uma ótima solução quem precisa análisar documentos diáriamente.

## 🚀 Tecnologias Utilizadas

* **Python**: Principal Linguagem para desenvolvimento.
* **Streamlit**: Framework para a criação da interface interativa.
* **Pinata API**: Upload de PDFs e armazenamento em IPFS.
* **OpenAI API**: Interações com o modelo GPT e geração de respostas.
* **PyPDF2**: Extração de texto de arquivos PDF.
* **dotenv**:  Carregar variáveis de ambiente de forma segura.

## ✨ Funcionalidades
 
* Upload de arquivos PDF para o IPFS usando a API do Pinata.
* Extração de texto de PDFs para análise e geração de respostas.
* Chatbot integrado usando OpenAI para responder perguntas sobre o conteúdo do PDF.
* Interface interativa e amigável criada com Streamlit.

## 📦 Pré-requisitos

Certifique-se de ter os seguintes itens instalados no seu ambiente:

* Python 3.8 ou superior
* Pip (Python package installer)
* Conta na OpenAI
* Conta na Pinata

## ⚙️ Instalação

* **1 - Clone este repositório:**

``` bash
git clone https://github.com/ronaldandrade/Chatbot-pdf.git

cd chabot-pdf
```
* **2 - Crie e ative um ambiente virtual (recomendado):**
```bash
python -m venv venv

source venv/bin/activate # No Windows: venv\Scripts\activate
  
```

* **3 - Instale as dependências:**
```bash
pip install -r requirements.txt
```
* **4 - Configure as variáveis de ambiente:**

Crie um arquivo ``.env ``no diretório raiz e adicione suas chaves de API:

```env
OPENAI_API_KEY=your_openai_api_key

PINATA_API_KEY=your_pinata_api_key

PINATA_SECRET_API_KEY=your_pinata_secret_key
```

# ▶️ Como Usar


* **1 - Execute a aplicação:**

  
```python
streamlit run app.py
```
  

* **2 - Abra o navegador e acesse o endereço:**

```python
http://localhost:8501
```
* **3 - Carregue um arquivo PDF e faça perguntas sobre seu conteúdo usando o chatbot!**

  

## 📂 Estrutura do Projeto

  
```bash
chatbot-pdf/
├── .env.exemplo            # Variáveis de ambiente (exemplo)
├── .gitignore              # Arquivos não commitados
├── app.py                  # Código principal da aplicação Streamlit
├── pinata_helper.py        # Funções para upload usando a API do Pinata
├── openai_helper.py        # Funções para interagir com a API da OpenAI
└── README.md               # Documentação do projeto
├── requirements.txt        # Dependências do projeto

```
  
## 🤝 Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir Issues e Pull Requests para adicionar melhorias.

## 📜 Licença
Este projeto é licenciado sob a licença MIT. Consulte o arquivo LICENSE para obter mais detalhes.

🎉 Aproveite a aplicação! Se você achou útil, não se esqueça de deixar uma ⭐ no repositório!

