ChatBot OpenAI
Este projeto é um chatbot utilizando a API da OpenAI. Aqui, você encontrará um modelo de chatbot que pode ser integrado a diferentes sistemas.

Pré-requisitos
Antes de começar, você precisará ter o Python instalado em sua máquina. Você também vai precisar de uma chave de API da OpenAI, que pode ser obtida aqui.

Instalação
1. Clonar o repositório
Primeiro, clone este repositório para sua máquina local:
git clone https://github.com/rodriguesgui/ChatBot-openai.git


2. Acessar a pasta do projeto
Depois de clonar o repositório, navegue até a pasta do projeto:
cd ChatBot-openai

3. Criar um ambiente virtual (opcional, mas recomendado)
Crie um ambiente virtual para isolar as dependências do projeto:
python -m venv venv

4. Ativar o ambiente virtual
Para ativar o ambiente virtual:

Windows:

bash
Copiar
Editar
.\venv\Scripts\activate
Mac/Linux:

bash
Copiar
Editar
source venv/bin/activate
5. Instalar as dependências
Com o ambiente virtual ativado, instale as dependências necessárias para rodar o projeto:

bash
Copiar
Editar
pip install -r requirements.txt
6. Configurar sua chave da API
Para interagir com a API da OpenAI, você precisará configurar sua chave de API:

Crie um arquivo chamado .env na pasta raiz do projeto.

No arquivo .env, insira sua chave de API da OpenAI da seguinte forma:

bash
Copiar
Editar
OPENAI_API_KEY=sua-chave-aqui
7. Rodar o projeto
Depois de configurar a chave da API, você pode rodar o chatbot com o seguinte comando:

bash
Copiar
Editar
python chatbot.py
