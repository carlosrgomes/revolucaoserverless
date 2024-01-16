# Importa a classe Flask do módulo Flask
from flask import Flask

# Cria uma instância da classe Flask e atribui à variável app
app = Flask(__name__)

# Define uma rota usando o decorador @app.route()
@app.route("/")
def hello_world():
    # Retorna um parágrafo HTML simples contendo o texto "Exemplo Revolução Serverless"
    return "<p>Exemplo Revolução Serverless</p>"

# Garante que a aplicação só seja executada quando o script for executado diretamente, não quando importado como módulo
if __name__ == "__main__":
    # Inicia o servidor de desenvolvimento Flask com as seguintes configurações:
    # - host="0.0.0.0": Vincula o servidor a todas as interfaces de rede disponíveis, tornando-o acessível de outros dispositivos na rede.
    # - port=8080: Define a porta para ouvir solicitações recebidas, normalmente a porta 8080 para fins de desenvolvimento.
    app.run(host="0.0.0.0", port=8080)