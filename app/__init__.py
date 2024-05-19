from flask import Flask, render_template, jsonify
from flask_restful import Api 
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify

# Variaveis
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///space.db"

api = Api(app)
db = SQLAlchemy(app)

from app.models.missao import Missao
with app.app_context(): 
    db.create_all()
    

# Rotas
from app.view.reso_missao import ListarMissao, Update, Delete, CriarMissao
api.add_resource(ListarMissao, "/listar")
api.add_resource(CriarMissao,'/criar')
api.add_resource(Update, "/atualizar")
api.add_resource(Delete, "/delete")

@app.route('/')
def index():
    # response, status_code = ListarMissao().get()
    # if status_code == 500:
    #     return render_template('index.html', error=response["msg"])
    return render_template('index.html')


