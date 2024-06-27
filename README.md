# KorokRecipes

## Descrição

Um site para visualizaçao de receitas culinárias.

## Tecnologias

- Django: Framework web utilizado para desenvolver o site.
- Pytest: Biblioteca de testes unitários do Python para testar o código.
- GitHub Actions: Utilizado para configurar a integração contínua e entrega contínua (CI/CD).
- Banco de Dados SQL: Banco de dados padrao do Django.

## Como rodar o projeto

1. Clone o repositório
2. Instale o Python 3.12.2
3. Crie um virtualenv com o comando `python -m venv venv`
4. Ative o virtualenv com o comando `venv\Scripts\activate`
5. Instale as dependências com o comando `pip install -r requirements.txt`
6. Rode as migrações com o comando `python manage.py migrate`
7. Rode o servidor com o comando `python manage.py runserver`
8. Acesse o site em `http://127.0.0.0:8000/`

## Como rodar os testes

1. Instale as dependências com o comando `pip install -r requirements.txt`
2. Rode os testes com o comando `pytest -html=report.html`
