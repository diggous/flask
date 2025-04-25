from flask import Flask  # Importa a classe Flask do módulo flask para criar a aplicação.

app = Flask(__name__)  # Cria uma instância da aplicação Flask. O argumento __name__ indica o nome do módulo atual.

from app_teste.views import homepage  # Importa as rotas definidas no arquivo views.py para registrar as rotas na aplicação.
