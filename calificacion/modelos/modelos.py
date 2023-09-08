from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50))
    contrasena = db.Column(db.String(50))
    calificacion = db.Column(db.Integer)

class Preguntas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    enunciado = db.Column(db.String(50))
    opcion1 = db.Column(db.String(50))
    opcion2 = db.Column(db.String(50))
    opcion3 = db.Column(db.String(50))
    opcion4 = db.Column(db.String(50))
    respuesta = db.Column(db.Integer)