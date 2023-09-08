import requests
from datetime import datetime
from flask import request
from flask_restful import Resource
from ..modelos import db, Usuario, Preguntas
import random


class VistaValidador(Resource):
    def post(self):
        print('Se envio la peticion ' + str(datetime.utcnow()))
        # primer log 
        flagError1 = False
        flagError2 = False
        flagError3 = False
        body = request.json
        calificacion1 = requests.post(
            "http://localhost:5001/calificacion", json=body)
        calificacion2 = requests.post(
            "http://localhost:5002/calificacion", json=body)
        calificacion3 = requests.post(
            "http://localhost:5003/calificacion", json=body)

        if calificacion1.json()['calificacion'] < 0:
            flagError1 = True
            # primer log de error
            print("hubo un error en el microservicio 1 -> " + str(calificacion1.json()['calificacion']) + " el valor esperado 3" + str(datetime.utcnow()) )

        if calificacion2.json()['calificacion'] < 0:
            flagError2 = True
            print('hubo un error en el microservicio 2')

        if calificacion3.json()['calificacion'] < 0:
            flagError3 = True
            print('hubo un error en el microservicio 3')
            
            
        respuesta = { }
        
        if flagError1 == True:
            respuesta = {
                "Calificacion del servicio 2": calificacion2.json(),
                "Calificacion del servicio 3": calificacion3.json()
            }
        if flagError2 == True:
            respuesta = {
                "Calificacion del servicio 1": calificacion1.json(),
                "Calificacion del servicio 3": calificacion3.json()
            }
        if flagError3 == True:
            respuesta = {
                "Calificacion del servicio 1": calificacion1.json(),
                "Calificacion del servicio 2": calificacion2.json()
            }
        if flagError1 == False and flagError2 == False and flagError3 == False:
            respuesta = {
                "Calificacion del servicio 1": calificacion1.json(),
                "Calificacion del servicio 2": calificacion2.json(),
                "Calificacion del servicio 3": calificacion3.json()
            }

        return respuesta
