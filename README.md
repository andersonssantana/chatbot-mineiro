# Chatbot Zeca

Primeira tentativa de construir um chatbot em Python usando a API do Gemini e a interface com Gradio.

## Visão Geral

O **Chatbot Zeca** é um projeto experimental para construir um chatbot com personalidade mineira, utilizando a API de inteligência artificial Gemini e a interface interativa Gradio. O chatbot responde com expressões típicas de Minas Gerais, trazendo um toque regional ao diálogo.

## Funcionalidades

- **Personalidade Mineira**: O chatbot usa expressões e um tom de linguagem característico do "mineirês", criando uma interação leve e regionalizada.
- **Interface Gradio**: Uma interface gráfica para interação em tempo real, permitindo ao usuário digitar perguntas e receber respostas do chatbot.
- **API de IA Gemini**: Utiliza uma API avançada de inteligência artificial para gerar respostas contextualizadas.

## Estrutura do Projeto

```plaintext
├── main.py                 # Script principal para rodar o chatbot
├── initial_prompt.py       # Definição inicial do prompt para configurar o estilo de resposta do chatbot
├── requirements.txt        # Lista de dependências do projeto
└── README.md               # Documentação do projeto
```

### Arquivo `main.py`

Este é o ponto de entrada do projeto. Aqui, o chatbot é configurado para rodar, estabelecendo conexão com a API Gemini e definindo a interface de interação via Gradio.

### Arquivo `initial_prompt.py`

Este arquivo contém a configuração inicial do prompt, determinando o estilo e a personalidade do chatbot, garantindo respostas no dialeto mineiro.

## Pré-requisitos

Antes de executar o projeto, certifique-se de ter instalado:

- **Python 3.8+**
- **Gradio** (para a interface gráfica)
- **Google AI Python SDK** (para chamadas à API Gemini)

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/andersonssantana/chatbot-mineiro.git
   cd chatbot-mineiro
   ```

2. Crie um ambiente virtual e ative-o:

   ```bash
   python -m venv .env
   source .env/bin/activate  # No Windows: .env\Scripts\activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure a API Gemini com sua chave no `main.py`.

## Como Usar

Execute o chatbot com o comando:

```bash
python main.py
```

Isso abrirá a interface do Gradio no navegador, onde você pode começar a interagir com o Chatbot Zeca.

## Personalização

Para alterar o estilo das respostas, edite o arquivo `initial_prompt.py`, ajustando as expressões e o tom conforme desejado.

## Licença

Este projeto é livre para uso, modificação e distribuição.
