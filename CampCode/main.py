from app_teste import app  # Importa a aplicação Flask criada no pacote `app_teste`.

if __name__ == '__main__':  # Verifica se o arquivo está sendo executado diretamente (não importado como módulo).
    app.run(debug=True)  # Inicia o servidor Flask com o modo de depuração ativado.

