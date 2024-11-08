import google.generativeai as genai
from google.api_core.exceptions import InvalidArgument
from initial_prompt import initialPrompt
import os
import time
import gradio

GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash", system_instruction=initialPrompt)
chat = model.start_chat()

def assemble_prompt(message):
   prompt = [message["text"]]
   uploaded_files = upload_files(message)
   prompt.extend(uploaded_files)
   return prompt

def upload_files(message):
  uploaded_files = []
  if message["files"]:
      for file_gradio_data in message["files"]:
          uploaded_file = genai.upload_file(file_gradio_data)
          while uploaded_file.state.name == "PROCESSING":
              time.sleep(5)
              uploaded_file = genai.get_file(uploaded_file.name)
          uploaded_files.append(uploaded_file)
  return uploaded_files

def gradio_wrapper(message, _history):
  prompt = assemble_prompt(message)
  try:
    response = chat.send_message(prompt)
  except InvalidArgument as error:
    response = chat.send_message(
      f"O usuário te enviou um arquivo para você ler e obteve o erro: {error}. "
      "Pode explicar o que houve e dizer quais tipos de arquivos você "
      "dá suporte? Assuma que a pessoa não sabe programação e "
      "não quer ver o erro original. Explique de forma simples e concisa."
    )
  return response.text

chatInterface = gradio.ChatInterface(
  fn=gradio_wrapper,
  title="Chatbot com suporte a arquivos",
  multimodal=True
)

chatInterface.launch()
