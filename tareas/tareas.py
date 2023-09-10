from datetime import datetime
from celery import Celery
import requests

celery_app = Celery(__name__, broker='redis://localhost:6379/0', backend='redis://localhost:6379/0',)


@celery_app.task(queue="cola1")
def enviarSolicitudACalificacion1(body, horaEnvio):
    calificacion1 = requests.post("http://localhost:5001/calificacion", json=body)  
    tiempoRespuesta = datetime.utcnow() - horaEnvio
    if calificacion1.json()['calificacion'] < 0:
        with open('log_resultados.txt', 'a+') as file:
            file.write('desde worker -> solicitud: ' + str(body['id_solicitud']) + ', ERROR EN EL MICROSERVICIO 1 CON TIEMPO DE RESPUESTA DE: ' + str(tiempoRespuesta.total_seconds()) + ' Seg' + "\n")  
            file.close()  
            
    return calificacion1.json()['calificacion']

@celery_app.task(queue="cola2")
def enviarSolicitudACalificacion2(body, horaEnvio):
    calificacion2 = requests.post("http://localhost:5002/calificacion", json=body)
    tiempoRespuesta = datetime.utcnow() - horaEnvio
    if calificacion2.json()['calificacion'] < 0:
        with open('log_resultados.txt', 'a+') as file:
            file.write('desde worker -> solicitud: ' + str(body['id_solicitud']) + ', ERROR EN EL MICROSERVICIO 2 CON TIEMPO DE RESPUESTA DE: ' + str(tiempoRespuesta.total_seconds()) + ' Seg' + "\n")  
            file.close()
    return calificacion2.json()['calificacion']
    
@celery_app.task(queue="cola3")
def enviarSolicitudACalificacion3(body, horaEnvio):
    calificacion3 = requests.post("http://localhost:5003/calificacion", json=body)
    tiempoRespuesta = datetime.utcnow() - horaEnvio
    if calificacion3.json()['calificacion'] < 0:
        with open('log_resultados.txt', 'a+') as file:
            file.write('desde worker -> solicitud: ' + str(body['id_solicitud']) + ', ERROR EN EL MICROSERVICIO 3 CON TIEMPO DE RESPUESTA DE: ' + str(tiempoRespuesta.total_seconds()) + ' Seg' + "\n")  
            file.close()
    return calificacion3.json()['calificacion']