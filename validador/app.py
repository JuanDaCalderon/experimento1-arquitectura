from validador import create_app
from .modelos import db
from flask_restful import Api
from .vistas import VistaValidador

app = create_app()
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
# ruta para consumir el validador 
api.add_resource(VistaValidador, '/validador')