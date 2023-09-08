from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbcalificacion.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app