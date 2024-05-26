from flask import Flask, render_template
from flask_restful import Api 
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS # autorizar o acesso

# Variaveis
app = Flask(__name__)
CORS(app)
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
    return render_template('index.html')


