from ..env import INTRODUCE_ERROR
from flask import request
from flask_restful import Resource
from ..modelos import db, Usuario, Preguntas
import random

    
class VistaCalificacion(Resource):
    def post(self):
        error = random.randint(1, 50)
        usuario = Usuario.query.filter(Usuario.id == request.json["usuario"]).first()
        calificacion = 0
        preguntas = Preguntas.query.all()
        for index in range(len(preguntas)):
            if request.json["preguntas"][index]['respuesta'] == preguntas[index].respuesta:
                calificacion += 1
        
        if INTRODUCE_ERROR == True and 10 <= error <= 25:
            calificacion = -error
            
        usuario.calificacion = calificacion
        db.session.commit()
        return { "calificacion": calificacion }