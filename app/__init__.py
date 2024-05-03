from flask import Flask
from flask_restful import Api 
from flask_sqlalchemy import SQLAlchemy

# Variaveis
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///space.db"

api = Api(app)
db = SQLAlchemy(app)
    
# Rotas
from app.models.missao import Missao
# api.add_resource(Missao, "/")
