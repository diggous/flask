from app_teste import app  # Importa o objeto `app` do pacote `app_teste`, que é a instância do Flask.
from flask import render_template, url_for  # Importa funções do Flask para renderizar templates e gerar URLs.

@app.route('/')  # Define uma rota para a URL raiz ('/').
def homepage():  # Função que será executada quando a rota '/' for acessada.
    usuario = 'Diego Irigoyen' #variavel com o nome do usuario
    idade = 33 #variavel com o a idade do usuario

    context = { #dicionário com as informações do usuário, no return é utilizado apenas o dicionário, ao invés do nome de cada váriavel.
        'usuario': usuario,
        'idade': idade
    }

    return render_template('index.html', context = context)  # Renderiza o arquivo HTML chamado 'index.html' e o retorna como resposta.

@app.route('/contatos/')  # Define uma rota para a URL '/nova/'.
def newpage():  # Função que será executada quando a rota '/nova/' for acessada.
    return 'Outra pagina'  # Retorna uma string simples como resposta para a rota '/nova/'.