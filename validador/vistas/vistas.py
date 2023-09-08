from ..env import INTRODUCE_ERROR
from flask import request
from flask_restful import Resource
from ..modelos import db, Usuario, Preguntas
import random

    
class VistaValidador(Resource):
    def post(self):
        return { "request": request.json }