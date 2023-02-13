# Microservicio De usuarios
Este microservicio se encarga de brindar las operaciones de creación, login y obtención de información de los usuarios.
#Operaciones Disponibles
## creación de usuarios
Permite la creación de nuevos usuarios
## Login
Permite la generación de tokens de autenticación mediante la validación de un usuario y contraseña
## información de usuario
Permite la consulta de los datos de un usuario, requiere token de autenticación
## ping
Permite validar si la aplicación está en ejecución
## Tecnologias usadas
- Python : 3.11.1-bullseye
- Postgresql:15.1
- Framework Flask para python
- Orm SQL Alchemy
- Docker

## Dockerfile
En el dockerfile se encuentra la implementación de la imagen de python , se uso el directorio /app como directorio de trabajo ,los archivos de la aplicación se copiaron al directorios /app,luego se ejecuta el archivo requeriments.txt para instalar las dependencias de la aplicación, se expone el puerto 5000 por el cual escuchara la aplicación y por último se ejecuta flask con el comando flask run (el host 0.0.0.0 se usa para que flask sea visible por toda la red del contenedor)

  dsaddasdassss dsada