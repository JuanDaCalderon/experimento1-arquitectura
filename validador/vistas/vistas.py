import requests
from datetime import datetime
from flask import request
from flask_restful import Resource
from ..modelos import db, Usuario, Preguntas
import random
from time import gmtime, strftime


class VistaValidador(Resource):
    def post(self):
        horaEnvio = datetime.utcnow()
        body = request.json
        solicitud = body['id_solicitud']
        
        with open('log_resultados.txt', 'a+') as file:
            file.write('solicitud: ' + str(solicitud) + ', envio solicitud, ' + str(horaEnvio) + '\n') 
        
       
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
            horaRespuesta = datetime.utcnow()
            with open('log_resultados.txt', 'a+') as file:
                file.write('solicitud: ' + str(solicitud) + ', error microservicio1, ' + str(datetime.utcnow()) + '\n') 

        if calificacion2.json()['calificacion'] < 0:
            flagError2 = True
            print('hubo un error en el microservicio 2')
            horaRespuesta = datetime.utcnow()
            with open('log_resultados.txt', 'a+') as file:
                file.write('solicitud: ' + str(solicitud) + ', error microservicio2, ' + str(datetime.utcnow()) + '\n') 

        if calificacion3.json()['calificacion'] < 0:
            flagError3 = True
            print('hubo un error en el microservicio 3')
            horaRespuesta = datetime.utcnow()
            with open('log_resultados.txt', 'a+') as file:
                file.write('solicitud: ' + str(solicitud) + ', error microservicio3, ' + str(datetime.utcnow()) + '\n') 
            
            
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
            horaRespuesta = datetime.utcnow()
            with open('log_resultados.txt', 'a+') as file:
                file.write('solicitud: ' + str(solicitud) + ', exitosa, ' + str(datetime.utcnow()) + "\n")             
            respuesta = {
                "Calificacion del servicio 1": calificacion1.json(),
                "Calificacion del servicio 2": calificacion2.json(),
                "Calificacion del servicio 3": calificacion3.json()
            }

        tiempoRespuesta = horaRespuesta - horaRespuesta
        
        print(tiempoRespuesta.total_seconds()*1000)
        
        with open('log_resultados.txt', 'a+') as file:
                file.write('solicitud: ' + str(solicitud) + ', tiempo de respuesta, ' + str(tiempoRespuesta) + "\n")        

        return respuesta
