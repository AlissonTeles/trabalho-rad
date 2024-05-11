from flask import jsonify
from flask_restful import Resource, reqparse
from app.models.missao import Missao

class IndexAll(Resource):
    def get(self):
        return jsonify("Teste")