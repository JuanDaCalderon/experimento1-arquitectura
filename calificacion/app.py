from calificacion import create_app
from .modelos import db
from flask_restful import Api
from .vistas import VistaCalificacion

app = create_app()
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(VistaCalificacion, '/calificacion')