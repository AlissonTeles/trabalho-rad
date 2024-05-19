from datetime import date, time
from flask import jsonify, request
from flask_restful import Resource, reqparse
from app.models.missao import Missao

argumentos_get = reqparse.RequestParser()
argumentos_get.add_argument('id', type=int, required=False, ignore=True)
argumentos_get.add_argument('nome', type=str, required=False, ignore=True)
argumentos_get.add_argument('data_lancamento_inicial', type=str, required=False, ignore=True)
argumentos_get.add_argument('data_lancamento_final', type=str, required=False, ignore=True)

argumentos_adicionar = reqparse.RequestParser()
argumentos_adicionar.add_argument('nome', type=str)
argumentos_adicionar.add_argument('data_lancamento', type=str)
argumentos_adicionar.add_argument('destino', type=str)
argumentos_adicionar.add_argument('estado_missao',type=str)
argumentos_adicionar.add_argument('tripulacao', type=str)
argumentos_adicionar.add_argument('carga_util', type=str)
argumentos_adicionar.add_argument('tempo_duracao', type=str)
argumentos_adicionar.add_argument('custo_missao', type=float)
argumentos_adicionar.add_argument('status_missao', type=str)


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

argumentos_delete = reqparse.RequestParser()
argumentos_delete.add_argument('id', type=int, required=True, help="ID não pode estar em branco!")

class ListarMissao(Resource):
    def get(self):
        try:
            # if argumentos_get.args:
            #     datas = argumentos_get.parse_args()
            #     missionList = Missao.list_mission(self, datas['id'],
            #                         datas['nome'],
            #                         datas['data_lancamento_inicial'], 
            #                         datas['data_lancamento_final'])
            #     missionListJson = [missao.to_dict() for missao in missionList]
            # else:
            missionList = Missao.list_mission(self, "", "", "", "")
            missionListJson = [missao.to_dict() for missao in missionList]
            return {"data": missionListJson}, 200
        except Exception as err:
            print(err)
            print("5050050500")
            return jsonify({'status': 500, 'msg': f'{err}'}), 500

class CriarMissao(Resource):
    def post(self):
        try:
            dados = argumentos_adicionar.parse_args()
            print(dados)
            Missao.create_mission(self, 
                dados['nome'], 
                dados['data_lancamento'], 
                dados['destino'], 
                dados['estado_missao'], 
                dados['tripulacao'], 
                dados['carga_util'], 
                dados['tempo_duracao'],
                dados['custo_missao'], 
                dados['status_missao'])
            return {"message": 'Mission create successfully!'}, 200
        
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'deu erro o{e}'}), 500
    
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
        
class Delete(Resource):
    def delete(self):
        try:
            datas = argumentos_delete.parse_args()
            missao_id = datas['id']
            missao = Missao.query.get(missao_id)
            if missao:
                missao.delete_missao(missao_id)
                return {"message": 'Missao deleted sucessfully!'}, 200
            else:
                return {"message": f'Missao with id {missao_id} not found.'}, 404
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500

