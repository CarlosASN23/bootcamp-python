"""Criação de uma API para cadastro de programadores contendo os
   campos (Nome, Habilidade, ID).
   API criada atráves da utilização do framework Flask"""

from flask import Flask, jsonify, request
import json

# Inicialização da aplicação
app = Flask(__name__)

# Inserção de dados dos programadores
desenvolvedores = [

    {'nome': 'Carlos',
     'Habilidades': ['Python', 'Flask', 'Django', 'Java']},

    {'nome': 'Rafael',
     'Habilidade': ['Python', 'Flask', 'Django']}
]

# Lista programadores através do ID
@app.route('/dev/<int:identificacao>/', methods=['GET', 'PUT', 'DELETE'])
def programador(identificacao):

    if request.method == 'GET':

        try:
            response = desenvolvedores[identificacao]

        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(identificacao)
            response = {'status': 'Erro', 'mensagem': mensagem}

        except Exception:
            mensagem = 'Erro desconhecido.'
            response = {'status': 'Erro', 'mensagem': mensagem}

        return jsonify(response)

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[identificacao] = dados
        return jsonify(dados)

    elif request.method == 'DELETE':
        desenvolvedores.pop(identificacao)
        return jsonify({'status': 'Suscesso', 'mensagem': 'Registro excluido'})

# Lista dos programadores cadastrados e registro de novos programadores
@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedor():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['identificacao'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])

    elif request.method == 'GET':
        return jsonify(desenvolvedores)

# Finalização e execução da aplicação
if __name__ == '__main__':
    app.run(debug=True)

