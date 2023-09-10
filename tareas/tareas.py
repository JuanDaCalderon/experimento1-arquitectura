from celery import Celery
import requests

celery_app = Celery(__name__, broker='redis://localhost:6379/0')

@celery_app.task()
def enviarSolicitudACalificacion(body): 
    calificacion1 = requests.post("http://localhost:5001/calificacion", json=body)
    calificacion2 = requests.post("http://localhost:5002/calificacion", json=body)
    calificacion3 = requests.post("http://localhost:5003/calificacion", json=body)
    
    return [calificacion1, calificacion2, calificacion3]
    
