#!/bin/bash

# Crear directorios
mkdir tempdir
mkdir tempdir/templates
mkdir tempdir/static

# Copiar archivos
cp app.py tempdir/.
cp -r templates/* tempdir/templates/.
cp -r static/* tempdir/static/.

# Crear el archivo DockerFile y agregar las instrucciones
echo "FROM python" >> tempdir/DockerFile
echo "RUN pip install flask pymysql" >> tempdir/DockerFile
echo "COPY ./static /home/myapp/static/" >> tempdir/DockerFile
echo "COPY ./templates /home/myapp/templates/" >> tempdir/DockerFile
echo "COPY app.py /home/myapp/" >> tempdir/DockerFile
echo "EXPOSE 5050" >> tempdir/DockerFile
echo "CMD python3 /home/myapp/app.py" >> tempdir/DockerFile

# Cambiar al directorio tempdir
cd tempdir

# Construir la imagen Docker
docker build -t sampleapp .

# Ejecutar el contenedor Docker, mapeando el puerto 5000 para Flask y el puerto 3303 para la base de datos
docker run -t -d -p 5050:5050 -p 3303:3303 --name samplerunning sampleapp

# Mostrar información sobre los contenedores Docker
docker ps -a
