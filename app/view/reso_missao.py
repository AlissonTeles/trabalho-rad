from flask import jsonify, request, make_response
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
argumentos_update.add_argument('data_lancamento', type=str)
argumentos_update.add_argument('destino', type=str)
argumentos_update.add_argument('estado_missao', type=str)
argumentos_update.add_argument('tripulacao', type=str)
argumentos_update.add_argument('carga_util', type=str)
argumentos_update.add_argument('tempo_duracao', type=str)
argumentos_update.add_argument('custo_missao', type=float)
argumentos_update.add_argument('status_missao', type=str)

argumentos_delete = reqparse.RequestParser()
argumentos_delete.add_argument('id', type=int, required=True, help="ID não pode estar em branco!")

class ListarMissao(Resource):
    def get(self):
        try:
            id = request.args.get('id')
            name = request.args.get('nome')
            data_lancamento_inicial = request.args.get('data_lancamento_inicial')
            data_lancamento_final = request.args.get('data_lancamento_final')
            
            missionList, error = Missao.list_mission(self, id, name, data_lancamento_inicial,data_lancamento_final)
            if error != "":
                return {"status": 400, "error": error}, 400
            missionListJson = [missao.to_dict() for missao in missionList]
            return {"data": missionListJson}, 200
        except Exception as err:
            print(err)
            response = jsonify({'status': 500, 'error': f'{err}'})
            return make_response(response, 500)

class CriarMissao(Resource):
    def post(self):
        try:
            dados = argumentos_adicionar.parse_args()
            error = Missao.create_mission(self, 
                dados['nome'], 
                dados['data_lancamento'], 
                dados['destino'], 
                dados['estado_missao'], 
                dados['tripulacao'], 
                dados['carga_util'], 
                dados['tempo_duracao'],
                dados['custo_missao'], 
                dados['status_missao'])
            if error != "":
                return {"status": 400, "error": error}, 400
            
            return {"msg": 'Missão criada com sucesso!'}, 200
        
        except Exception as err:
            print(err)
            response = jsonify({'status': 500, 'error': f'{err}'})
            return make_response(response, 500)
    
class Update(Resource):
    def put(self):
        try:
            datas=argumentos_update.parse_args()
            error = Missao.update_mission(self, datas['id'],
                                 datas['nome'],
                                 datas['data_lancamento'],
                                 datas['destino'],
                                 datas['estado_missao'],
                                 datas['tripulacao'],
                                 datas['carga_util'],
                                 datas['tempo_duracao'],                               
                                 datas['custo_missao'],
                                 datas['status_missao'],)
            if error != "":
                return {"status": 400, "error": error}, 400
            
            return {"msg": 'Missão atualizada com sucesso!'}, 200
        except Exception as err:
            print(err)
            response = jsonify({'status': 500, 'error': f'{err}'})
            return make_response(response, 500)
        
class Delete(Resource):
    def delete(self):
        try:
            datas = argumentos_delete.parse_args()
            error = Missao.delete_mission(self, datas['id'])
            if error != "":
                return {"status": 400, "error": error}, 400
    
            return {"msg": 'Missão apagada com sucesso!'}, 200

        except Exception as err:
            print(err)
            response = jsonify({'status': 500, 'error': f'{err}'})
            return make_response(response, 500)
