#!/bin/bash
set -e

echo "Esperando a MySQL..."

until mysqladmin ping -h "db" --silent; do
  echo "Esperando a MySQL..."
  sleep 2
done

echo "MySQL está arriba - ejecutando comandos"

mysql -h "db" -u root < /app/itl.sql