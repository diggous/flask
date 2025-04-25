from app_teste import app  # Importa o objeto `app` do pacote `app_teste`, que é a instância do Flask.
from flask import render_template, url_for  # Importa funções do Flask para renderizar templates e gerar URLs.

@app.route('/')  # Define uma rota para a URL raiz ('/').
def homepage():  # Função que será executada quando a rota '/' for acessada.
    return render_template('index.html')  # Renderiza o arquivo HTML chamado 'index.html' e o retorna como resposta.

@app.route('/nova/')  # Define uma rota para a URL '/nova/'.
def newpage():  # Função que será executada quando a rota '/nova/' for acessada.
    return 'Outra view'  # Retorna uma string simples como resposta para a rota '/nova/'.