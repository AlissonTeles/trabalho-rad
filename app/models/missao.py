from app import db
from datetime import datetime

class Missao(db.Model):
    __tablename__ = "missao"
    __table_args__ = {'sqlite_autoincrement': True} 
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    data_lancamento = db.Column(db.Date) 
    destino = db.Column(db.String)
    estado_missao = db.Column(db.String)
    tripulacao = db.Column(db.String)
    carga_util = db.Column(db.String)
    tempo_duracao = db.Column(db.String)
    custo_missao = db.Column(db.Float)
    status_missao = db.Column(db.String)

    def __init__(self, nome, data_lancamento, destino, estado_missao, tripulacao, carga_util, tempo_duracao, custo_missao, status_missao):
        self.nome = nome
        self.data_lancamento = data_lancamento
        self.destino = destino
        self.estado_missao = estado_missao
        self.tripulacao = tripulacao
        self.carga_util = carga_util
        self.tempo_duracao = tempo_duracao
        self.custo_missao = custo_missao
        self.status_missao = status_missao


    def Adicionar_Missao(self, nome, data_lancamento, destino, estado_missao, tripulacao, carga_util, tempo_duracao, custo_missao, status_missao):
        try:
            data_obj = datetime.strptime(data_lancamento, "%Y-%m-%d").date()
            add_banco = Missao(nome, data_obj, destino, estado_missao, tripulacao, carga_util, tempo_duracao, custo_missao, status_missao)
            #db.session.add(add_banco) 
            #db.session.commit()
        except Exception as error:
            print(error)


    def missao_update(self, id, nome, data_lancamento, destino, estado_missao, tripulacao, carga_util, tempo_duracao, custo_missao, status_missao):
        try:
            db.session.query(Missao).filter(Missao.id==id).update({"nome":nome, "data_lancamento":data_lancamento, "destino":destino, "estado_missao":estado_missao, "tripulacao":tripulacao, "carga_util":carga_util, "tempo_duracao":tempo_duracao, "custo_missao":custo_missao, "status_missao":status_missao})
            db.session.commit()
        except Exception as e:
            print(e)
    def delete_missao(self, id):
        try:
            missao = db.session.query(Missao).get(id)
            if missao: 
                db.session.delete(missao)
                db.session.commit()
            else:
                print(f"Missão com id {id} não encontrada.")
        except Exception as e:
            print(e)
            db.session.rollback()        

