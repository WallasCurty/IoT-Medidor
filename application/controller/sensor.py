from application import app
from flask import jsonify, request
import datetime

from application.model.entity.medicao import Medicao
from application.model.dao.sens_DAO import Qualidade



qualidade_list = Qualidade().listar_todos()

@app.route('/medicao', methods=['GET'])
def listar_medicao():
    medicao_dict = []
    for medicao in qualidade_list:
        medicao_dict.append(medicao.toDict())
    return jsonify(medicao_dict)

@app.route('/medicao', methods=['POST'])
def adicionar_medicao():
    id = len(qualidade_list) + 1
    dispositivo_id = request.json.get('Id_dispositivo', None)
    materia_particulada = float(request.json.get('materiaParticulada', None))
    gas = float(request.json.get('gas', None))
    nitrogenio = float(request.json.get('nitrogenio', None))
    ozonio = float(request.json.get('ozonio', None))
    temperatura = float(request.json.get('temperatura', None))
    umidade = float(request.json.get('umidade', None))
    data = datetime(request.json.get('data', None))

    medicao = Medicao(id, dispositivo_id, materia_particulada, gas, nitrogenio, ozonio, temperatura, umidade, data)
    Qualidade().inserir(medicao)
    return medicao.toDict(), 201

@app.route('/medicao/dispositivo/<int:id>', methods=['GET'])
def buscarMedicaoDispositivo(id):
    medicao_dispositivo = []
    for medicao in qualidade_list:
        if id == medicao._dispositivo_id:
            medicao_dispositivo.append(medicao.toDict())
    return jsonify(medicao_dispositivo)

@app.route('/medicao/data/<int:data>', methods=['GET'])
def data_medicao(data):
    medir_data = []
    for medicao in qualidade_list:
        if data == medicao._data:
            medir_data.append(medicao.toDict())
    return jsonify(medir_data)