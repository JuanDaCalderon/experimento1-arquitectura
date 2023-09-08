from flask import Flask
from modelos import db
from flask_restful import Api
from vistas import VistaUsuarios, VistaPreguntas, VistaCalificacion

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbcalificacion.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(VistaCalificacion, '/calificacion')