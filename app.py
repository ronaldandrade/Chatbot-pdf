import streamlit as st
import os
import time
from pinata_helper import upload_pdf_to_pinata
from openai_helper import get_openai_response
from PyPDF2 import PdfReader
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Chat with PDFs", layout="centered")

st.title("Chat with PDFs using OpenAI and Pinata")

uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "loading" not in st.session_state:
    st.session_state.loading = False 

if uploaded_file is not None:
    os.makedirs("temp", exist_ok=True)
    # Salva o arquivo na pasta temp
    file_path = os.path.join("temp", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Upload PDF para o Pinata
    st.write("Uploading PDF to Pinata...")
    pdf_cid = upload_pdf_to_pinata(file_path)
    
    if pdf_cid:
        st.write(f"File uploaded to IPFS with CID: {pdf_cid}")
        
        # Extraindo conteudo do PDF
        reader = PdfReader(file_path)
        pdf_text = ""
        for page in reader.pages:
            pdf_text += page.extract_text()

        if pdf_text:
            st.text_area("PDF Content", pdf_text, height=200)
            
            # Input para chatbot buscar no PDF
            user_input = st.text_input("Ask something about the PDF:", disabled=st.session_state.loading)

            if st.button("Send", disabled=st.session_state.loading):
                if user_input:

                    st.session_state.loading = True
                    
                    with st.spinner("AI is thinking..."):
                        # Simulate loading with sleep (remove in production)
                        time.sleep(1)  # Simulate network delay
                        # Get AI response
                        response = get_openai_response(user_input, pdf_text)

                    # Update chat history
                    st.session_state.chat_history.append({"user": user_input, "ai": response})

                    # Limapr o input box depois de enviado
                    st.session_state.input_text = ""
                    
                    # Resetar estados carregados
                    st.session_state.loading = False

            if st.session_state.chat_history:
                for chat in st.session_state.chat_history:
                    st.write(f"**You:** {chat['user']}")
                    st.write(f"**AI:** {chat['ai']}")

                st.write("<style>div.stChat {overflow-y: auto;}</style>", unsafe_allow_html=True)

                if st.session_state.loading:
                    st.write("**AI is typing** ...")

        else:
            st.error("Could not extract text from the PDF.")
    else:
        st.error("Failed to upload PDF to Pinata.")