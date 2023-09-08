from flask import request
from flask_restful import Resource
from modelos import db, Usuario, UsuarioSchema, Preguntas, PreguntasSchema 

usuario_schema = UsuarioSchema()
pregunta_schema = PreguntasSchema()
    
class VistaCalificacion(Resource):
    def post(self):
        usuario = Usuario.query.filter(Usuario.id == request.json["usuario"]).first()
        calificacion = 0
        preguntas = Preguntas.query.all()
        for index in range(len(preguntas)):
            if request.json["preguntas"][index]['respuesta'] == preguntas[index].respuesta:
                calificacion += 1
        
        usuario.calificacion = calificacion
        db.session.commit()
        return { "calificacion": calificacion }