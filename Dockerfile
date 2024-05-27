FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ /app/
COPY itl.sql /app/
COPY init-db.sh /app/

RUN chmod +x /app/init-db.sh

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
