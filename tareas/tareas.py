from celery import Celery
from aiohttp import ClientSession
import asyncio
import requests

celery_app = Celery(__name__, broker='redis://localhost:6379/0')

"""@celery_app.task()
def enviarSolicitudACalificacion(body): 
    calificacion1 = requests.post("http://localhost:5001/calificacion", json=body)
    calificacion2 = requests.post("http://localhost:5002/calificacion", json=body)
    calificacion3 = requests.post("http://localhost:5003/calificacion", json=body)
    
    return [calificacion1, calificacion2, calificacion3]"""

def solicitudes(body):
    enviarSolicitudACalificacion(body)
    
@celery_app.task()
async def enviarSolicitudACalificacion(body): 
    async with ClientSession() as session:
        tasks=[]
        for i in range(1,4):
            url = f'http://localhost:500{i}/calificacion'
            print("### url " , url)
            tasks.append(asyncio.create_task(enviarSolicitud(session, url=url)))
            
        response = await asyncio.gather(*tasks)
        print("++++++ respuesta ++++ ", response)
        
         
async def enviarSolicitud(session, url:str):
    response = await session.post(url)
    calificacion = await response.json()
    return calificacion['calificacion']
