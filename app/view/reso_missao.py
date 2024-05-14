from datetime import date, time
from flask import jsonify
from flask_restful import Resource, reqparse
from app.models.missao import Missao

argumentos_update = reqparse.RequestParser()
argumentos_update.add_argument('id', type=int)
argumentos_update.add_argument('nome', type=str)
argumentos_update.add_argument('data_lancamento', type=date)
argumentos_update.add_argument('destino', type=str)
argumentos_update.add_argument('estado_missao', type=str)
argumentos_update.add_argument('tripulacao', type=str)
argumentos_update.add_argument('carga_util', type=str)
argumentos_update.add_argument('tempo_duracao', type=time)
argumentos_update.add_argument('custo_missao', type=float)
argumentos_update.add_argument('status_missao', type=str)

class IndexAll(Resource):
    def get(self):
        return jsonify("Teste")
    
class Update(Resource):
    def put(self):
        try:
            datas=argumentos_update.parse_args()
            Missao.missao_update(self, datas['id'],
                                 datas['nome'],
                                 datas['data_lancamento'],
                                 datas['destino'],
                                 datas['estado_missao'],
                                 datas['data_missao'],
                                 datas['tripulacao'],
                                 datas['carga_util'],
                                 datas['tempo_duracao'],                               
                                 datas['custo_missao'],
                                 datas['status_missao'],)
            return {"message": 'Missao update successfully!'}, 200
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500