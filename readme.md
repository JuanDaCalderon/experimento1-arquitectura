# EXPERIMENTO DE DISPONIBILIDAD CON MICROSERVICIOS Y COLA DE MENSAJERIA
## Pasos para reproducir el experimento

- Debemos tener instalado redis desde una terminal de WSL (UBUNTU)
    - _sudo apt-get upgrade_
    - _sudo apt-get install redis_

- Clonamos el repositorio [https://github.com/JuanDaCalderon/experimento1-arquitectura](https://github.com/JuanDaCalderon/experimento1-arquitectura)

- Nos dirigimos a la rama Master

- Nos movemos a la carpeta correspondiente al validador
    - _cd validador_

- Instalamos los requirments.txt
    - _pip install -r requirements.txt_

- Creamos tres terminales diferentes sobre el proyecto y a cada una corremos las 3 colas necesarias para ejecutar el experimento con los siguientes comandos:
    - _celery -A tareas worker -Q cola1 -n cola1@worker --pool=solo -l info_
    - _celery -A tareas worker -Q cola2 -n cola2@worker --pool=solo -l info_
    - _celery -A tareas worker -Q cola3 -n cola3@worker --pool=solo -l info_

- Desde la carpeta del validador ejecutamos la aplicación con:
    - _flask run_

- Desde postman consumimos el servicio desde una peticion POST con los siguientes datos:
    - POST: http://localhost:5000/validador
    - BODY: {
                "id_solicitud": 1,
                "usuario": 1,
                "preguntas": [
                    {
                        "id_pregunta": 1,
                        "respuesta": 3
                    },
                    {
                        "id_pregunta": 2,
                        "respuesta": 3
                    },
                    {
                        "id_pregunta": 3,
                        "respuesta": 2
                    },
                    {
                        "id_pregunta": 4,
                        "respuesta": 3
                    },
                    {
                        "id_pregunta": 5,
                        "respuesta": 4
                    }
                ]
            }
