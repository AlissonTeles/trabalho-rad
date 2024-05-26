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
    tempo_duracao = db.Column(db.Date)
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
    
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'data_lancamento': self.data_lancamento.strftime("%d/%m/%Y"),
            'destino': self.destino,
            'estado_missao': self.estado_missao,
            'tripulacao': self.tripulacao,
            'carga_util': self.carga_util,
            'tempo_duracao': f"{(self.tempo_duracao - self.data_lancamento).days * 24} Horas",
            'custo_missao': self.custo_missao,
            'status_missao': self.status_missao
        }    
    
    def checkValuesAreNotNull(self):
        if not self.nome or self.nome.strip() == "":
            return "Nome da missão não pode ser vazio!"
        if not self.data_lancamento:
            return "Data de lançamento da missão não pode ser vazia!"
        if not self.destino or self.destino.strip() == "":
            return "O Destino da missão não pode ser vazio!"
        if not self.estado_missao or self.estado_missao.strip() == "":
            return "O Estado da missão não pode ser vazio!"
        if not self.tripulacao or self.tripulacao.strip() == "":
            return "A Tripulação da missão não pode ser vazio!"
        if not self.carga_util or self.carga_util.strip() == "":
            return "A Carga útil da missão não pode ser vazia!"
        if not self.tempo_duracao:
            return "O Tempo de duração da missão não pode ser vazio!"
        if not self.custo_missao:
            return "O Custo da missão não pode ser vazio!"
        if self.custo_missao < 0:
            return "O Custo da missão não pode ser vazio!"
        if not self.status_missao or self.status_missao.strip() == "":
            return "O Status da missão não pode ser vazio!"
        if self.data_lancamento > self.tempo_duracao:
            return "A data de lançamento não pode ser maior que o tempo de duração da missão!"
        return ""

    def list_mission(self, id, name, data_lancamento_inicial, data_lancamento_final): 
        try:
            query = Missao.query
            if id:
                query = query.filter(Missao.id == id)
            if name:
                query = query.filter(Missao.nome.like(f'%{name}%'))
                
            if data_lancamento_inicial and data_lancamento_final:
                data_lancamento_inicial = datetime.strptime(data_lancamento_inicial, '%d/%m/%Y').date()
                data_lancamento_final = datetime.strptime(data_lancamento_final, '%d/%m/%Y').date()
                if data_lancamento_final < data_lancamento_inicial:
                    return [{}, "Data de lançamento final é menor que a data de lançamento inicial"]
                query = query.filter(Missao.data_lancamento.between(data_lancamento_inicial, data_lancamento_final))
                
            missionList = query.order_by(Missao.data_lancamento.desc()).all()
            return [missionList, ""]
        except Exception as error:
            print(error)
            raise Exception(str(error))
            
    def create_mission(self, nome, data_lancamento, destino, estado_missao, tripulacao, carga_util, tempo_duracao, custo_missao, status_missao):
        try:
            new_missao = Missao(nome, data_lancamento, destino, estado_missao, tripulacao, carga_util, tempo_duracao, custo_missao, status_missao)
            
            error = new_missao.checkValuesAreNotNull()
            if error != "":
                return error

            new_missao.data_lancamento = datetime.strptime(data_lancamento, "%d/%m/%Y").date()
            new_missao.tempo_duracao = datetime.strptime(tempo_duracao, "%d/%m/%Y").date()

            db.session.add(new_missao) 
            db.session.commit()
            return ""
        except Exception as error:
            print(error)
            db.session.rollback()
            raise Exception(str(error))
            
    def update_mission(self, id, nome, data_lancamento, destino, estado_missao, tripulacao, carga_util, tempo_duracao, custo_missao, status_missao):
        try:
            queryMission = Missao.query.get(id)
            if not queryMission:
                return f"Missão com id {id} não foi encontrada."
            
            data_lancamento_date = datetime.strptime(data_lancamento, "%d/%m/%Y").date()
            tempo_duracao_date = datetime.strptime(tempo_duracao, "%d/%m/%Y").date()
            
            missao = Missao(nome, data_lancamento_date, destino, estado_missao, tripulacao, carga_util, tempo_duracao_date, custo_missao, status_missao)
            error = missao.checkValuesAreNotNull()
            if error:
                return error
            
            db.session.query(Missao).filter(Missao.id==id).update({"nome":nome, "data_lancamento":data_lancamento_date, "destino":destino, "estado_missao":estado_missao, "tripulacao":tripulacao, "carga_util":carga_util, "tempo_duracao":tempo_duracao_date, "custo_missao":custo_missao, "status_missao":status_missao})
            db.session.commit()
            return ""
        except Exception as error:
            print(error)
            db.session.rollback() 
            raise Exception(str(error))
            
    def delete_mission(self, id):
        try:
            missao = Missao.query.get(id)
            if missao: 
                db.session.delete(missao)
                db.session.commit()
                return ""
            else:
                return f"Missão com id {id} não foi encontrada."
        except Exception as error:
            print(error)
            db.session.rollback()
            raise Exception(str(error))
