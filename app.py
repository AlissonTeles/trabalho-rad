from flask import Flask
from flask_restful import Api 
from flask_sqlalchemy import SQLAlchemy

# Variaveis
app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///space.db"

# Rotas
api.add_resource("/")
