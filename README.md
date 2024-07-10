# ProyectoELO321
 
Proyecto de investigación basado en el estudio de contenedores y su uso.

Descripción de los Archivos

`3.1. server/server.py`
Este archivo contiene el código del servidor HTTP. Aquí se usa el módulo http.server para manejar las peticiones HTTP y threading para gestionar la concurrencia mediante un semáforo. También utilizamos el módulo logging para registrar mensajes de log.

`3.2. server/Dockerfile`
Este archivo define cómo construir la imagen Docker para el servidor. Utiliza una imagen base de Python y copia el script del servidor al contenedor.

`3.3. client/client.py`
Este archivo contiene el código del cliente que realiza una petición GET al servidor y muestra la respuesta recibida.

`3.4. client/Dockerfile`
Este archivo define cómo construir la imagen Docker para el cliente. Utiliza una imagen base de Python, copia el script del cliente e instala las dependencias necesarias.

`3.5. docker-compose.yml`
Este archivo define los servicios necesarios para el proyecto utilizando Docker Compose. Orquesta la construcción y ejecución de los contenedores del servidor y los clientes.

