from flask import Flask, render_template
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
    

from app.view.reso_missao import IndexAll, Update, Delete, CriarMissao
api.add_resource(IndexAll, "/getAllMissions")
api.add_resource(Update, "/atualizar")
api.add_resource(Delete, "/delete")
api.add_resource(CriarMissao,'/criar')
@app.route('/')

def index():
    index_all = IndexAll()
    return render_template('index.html', missao=index_all)


