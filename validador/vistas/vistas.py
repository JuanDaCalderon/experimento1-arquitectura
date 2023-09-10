from datetime import datetime
from flask import request
from flask_restful import Resource
from tareas import enviarSolicitudACalificacion1, enviarSolicitudACalificacion2, enviarSolicitudACalificacion3

class VistaValidador(Resource):
    def post(self):
        horaEnvio = datetime.utcnow()
        body = request.json
        solicitud = body['id_solicitud']

        with open('../log_resultados.txt', 'a+') as file:
            file.write('solicitud: ' + str(solicitud) +
                       ', envio solicitud, HORA ENVIO: ' + str(horaEnvio) + '\n')
            file.close()

        # primer log
        body = request.json

        calificacion1 = enviarSolicitudACalificacion1.delay(body, horaEnvio)
        calificacion2 = enviarSolicitudACalificacion2.delay(body, horaEnvio)
        calificacion3 = enviarSolicitudACalificacion3.delay(body, horaEnvio)

        respuestas = [calificacion1.get(), calificacion2.get(),
                      calificacion3.get()]

        respuesta = {
            'calificacion': 0
        }

        concurrencias = set()

        calificacion = [x for x in respuestas if x in concurrencias or (
            concurrencias.add(x) or False)]

        if len(calificacion) > 0:
            respuesta['calificacion'] = calificacion[0]
        else:
            respuesta = {
                'mensaje': 'Tus preguntas estan siendo calificadas, gracias'
            }

        return respuesta
