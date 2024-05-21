# Usa una imagen de Python como base
FROM python:3.10

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de tu aplicación Flask al contenedor
COPY . .

# Instala las dependencias de tu aplicación
RUN pip install --no-cache-dir -r requirements.txt

# Instala el cliente MySQL
RUN apt-get update && apt-get install -y mariadb-client

# Expone el puerto en el que se ejecutará tu aplicación
EXPOSE 5000

# Define el comando para ejecutar tu aplicación Flask
CMD ["python", "src/app.py"]
