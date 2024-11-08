import google.generativeai as genai
from google.api_core.exceptions import InvalidArgument
from initial_prompt import initialPrompt
import os
import time
import gradio

# Configuração do modelo Gemini com a chave de API
GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]
genai.configure(api_key=GEMINI_API_KEY)

gemini_model = genai.GenerativeModel("gemini-1.5-flash", system_instruction=initialPrompt)
gemini_chat_session = gemini_model.start_chat()

def build_chat_prompt(user_input):
    #Monta o prompt com base no texto e arquivos enviados pelo usuário.
    prompt_parts = [user_input["text"]]
    processed_files = process_and_upload_files(user_input)
    prompt_parts.extend(processed_files)
    return prompt_parts

def process_and_upload_files(user_input):
    #Faz o upload de arquivos e retorna uma lista de identificadores de arquivos.
    processed_files = []
    if user_input.get("files"):
        for file_data in user_input["files"]:
            uploaded_file = genai.upload_file(file_data)
            while uploaded_file.state.name == "PROCESSING":
                time.sleep(5)
                uploaded_file = genai.get_file(uploaded_file.name)
            processed_files.append(uploaded_file)
    return processed_files

def handle_chat_response(user_input, _history):
    #Processa o input do usupario e retorna a resposta do chatbot.
    prompt = build_chat_prompt(user_input)
    try:
        response = gemini_chat_session.send_message(prompt)
    except InvalidArgument as error:
        response = gemini_chat_session.send_message(
            f"O usuário enviou um arquivo que causou o erro: {error}. "
            "Explique quais tipos de arquivos são suportados de forma simples e concisa, "
            "assumindo que o usuário não tem conhecimentos técnicos."
        )
    return response.text

# Configuração da interface Gradio
chat_interface = gradio.ChatInterface(
    fn=handle_chat_response,
    title="Chatbot com suporte a arquivos",
    multimodal=True
)

chat_interface.launch()
