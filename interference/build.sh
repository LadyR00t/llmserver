#!/bin/bash
set -e

echo "==== Construyendo contenedores para el Copilot ===="

# Asegurarnos de tener permisos de ejecución en scripts
chmod +x code_runner/start-server.sh

# Forzar reconstrucción completa
docker-compose down --rmi all
docker-compose build --no-cache

# Iniciar el servicio
echo "==== Iniciando servicio en puerto 31337 ===="
docker-compose up 