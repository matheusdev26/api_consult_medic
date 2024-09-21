from flask import Flask, jsonify, request

app = Flask(__name__)

profissionais = []
consultas = []

# Cadastrar um profissional
@app.route('/profissionais', methods=['POST'])
def cadastrar_profissional():
    dados = request.get_json()
    profissional_id = len(profissionais) + 1
    profissionais.append({**dados, 'id': profissional_id})
    return jsonify(profissionais[-1]), 201

# Cadastrar uma consulta
@app.route('/consultas', methods=['POST'])
def cadastrar_consulta():
    dados = request.get_json()
    consulta_id = len(consultas) + 1
    consultas.append({**dados, 'id': consulta_id})
    return jsonify(consultas[-1]), 201

# Pesquisar consultas por ID do profissional
@app.route('/consultas/profissionais/<int:profissional_id>', methods=['GET'])
def pesquisar_consultas_profissionais(profissional_id):
    resultado = [consulta for consulta in consultas if consulta['profissional_id'] == profissional_id]
    return jsonify(resultado), 200

if __name__ == '__main__':
    app.run(debug=True)
