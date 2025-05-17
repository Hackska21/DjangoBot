# Simple djangoBot Implementation powered by OpenAI



## Structure

### api
Based on Django-like basic structure
apps/  \
├─ seller/ (django app) \
│  ├─ migrations/ (all database operations for this app)\
│  ├─ __init__.py\
│  ├─ admin.py (admin model declarations)\
│  ├─ apps.py (app django config)\
│  ├─ models.py (models declarations)\
│  ├─ serializers.py (drf serializers for the app)\
│  ├─ test.py\
│  ├─ urls.py (app urls)\
│  ├─ views.py \
├─ templates/ (django templates)\
├─ DjangoBot/\
│  ├─ __init__.py\
│  ├─ asgi.py\
│  ├─ settings.py  (django main config)\
│  ├─ urls.py   (root of urls)\
│  ├─ wsgi.py\
├─ .env\
├─ __init__.py\
├─ Dockerfile\
├─ Docker-compose\
├─ manage.py\
├─ requirements.txt\





## Prerequisites
To setup your local environment, you need install Docker Engine and docker-compose. You can follow the instructions [here](#How-to-install-Docker) to install.

### How to install Docker

Docker Engine is available on a variety of [MacOS](https://docs.docker.com/docker-for-mac/install/)

### How to install docker-compose

Docker compose is available on [MacOs](https://docs.docker.com/compose/install/)


### Running services

If you have already set up your local environment and have a **.env** file with the development variables set, this command builds the image  services:

```shell
$ docker-compose up -d
```
  - [http://127.0.0.1:8000](http://127.0.0.1:5000) is the Django app



## How to rebuild the docker image

In case you want the changes you have been testing to remain permanently in a new docker image you can rebuild the image, run this command:

```shell
$ docker-compose build
$ docker-compose up -d
```

After the build, you can remove the previous image with:

```shell
$ docker image prune -f
```

## Container shell access 

The docker exec command allows you to run commands inside a Docker container. The following command line will give you a bash shell inside your containers: `docker exec -it <container_name> <command>`



## Services

### Easy bot test
Allows test the 

```http
POST /seller/bot/
{
    "msg": "",
    "user_id": ""
}
```


### TwilioWebhook
Allows test the bot via Whatsapp using twilio 

```http
POST webhook/twilio/
{
    "MessageSid": "",
    "SmsSid": "",
    "AccountSid": "",
    "From": "",
    "To": "",
    "Body": ""
}
```
In order to be used is needed to configure the sandbox from twilio
![img.png](src/img2.png)
Also is important to be accessible via internet, this could be done using [ngrok](https://ngrok.com/use-cases/webhook-testing)


## Arquitectura del Bot 
![img.png](src/img.png)

# Backlog / Roadmap
## Para llevar a producción (Usando AWS)
- Generar registro en ECR para guardar la imagen docker
- Generar Cluster ECS
- Generar CI/CD script (Git hub actions)
	- Build de imagen y push a ECS 
	-  Deploy to ECS Cluster
- Soporte de Datadog o similar para monitoreo


### Roadmap
1. Preparación e Infraestructura
1.1. Configuración de Infraestructura en AWS
- Crear y configurar repositorio en ECR para almacenar imágenes Docker.
- Definir políticas y roles de IAM adecuados para interacción con ECR en el proceso de CI/CD.
- Crear y configurar cluster ECS con servicios y tareas necesarias, ajustando networking (VPC, subnets, security groups).
- Integrar herramientas de monitoreo como Datadog o CloudWatch para registro de métricas, latencia y alertas.

2. Integración Continua y Despliegue (CI/CD)
2.1. Configuración de GitHub Actions
- Programar workflow que construya imagen Docker desde el código en Python/Django.
- Configurar proceso de push automático de la imagen al repositorio ECR.
- Establecer despliegue automatizado al cluster ECS tras cada actualización de código.
- Implementar rollback automático en caso de fallos en el despliegue.
- Integrar notificaciones en canales de comunicación (Slack, email) para alertar sobre errores críticos.
2.2. Pipeline para Pruebas Automatizadas
- Integrar pruebas unitarias en cada commit o pull request.
- Desarrollar tests de integración para validar respuestas del bot en casos de uso reales.

3. Evaluación de Rendimiento y Detección de Regresiones
3.1. Monitoreo del Desempeño
- Implementar captura de logs de latencia de respuesta del bot.
- Configurar métricas para medir velocidad de respuesta y estabilidad bajo carga.
- Incorporar encuestas de NPS en las interacciones para recolectar feedback de usuarios.
- Integrar panel de métricas para análisis del rendimiento en tiempo real.
3.2. Pruebas de Regresión
- Definir conjunto de casos de prueba para evaluar el comportamiento del bot en diferentes escenarios.
- Automatizar tests de regresión para evaluar precisión, velocidad de respuesta y alineación de personalidad.
- Implementar comparación de versiones basada en historial de interacciones del bot.

4. Procesos de Datos y Gestión del Contexto
4.1. Ingesta de Datos y Catálogo de Autos
- Asegurar acceso constante al catálogo de marcas por parte del bot.
- Configurar extracción de modelos disponibles desde base de datos.
- Diseñar mecanismos de filtrado dinámico para generación de listados.
- Incorporar datos de la lista retornada como parte del contexto, junto con número de páginas y página actual.
4.2. Gestión del Contexto en el Bot
- Establecer limpieza automática de ventana de contexto al alcanzar límite de tokens.
- Implementar mecanismo para permitir a usuarios limpiar manualmente la sesión.
- Definir tiempo de vida de sesión configurable (días, semanas, etc.).

5. Seguimiento y Notificaciones
5.1. Sistema de Notificaciones
- Establecer sistema de alertas para eventos clave, como la generación de un plan de financiamiento.
- Integrar notificaciones en herramientas de monitoreo y comunicación interna.
5.2. Mantenimiento y Mejora Continua
- Revisar métricas de rendimiento periódicamente y realizar ajustes según hallazgos.
- Planificar iteraciones en el roadmap basadas en feedback de usuario y análisis de métricas.

