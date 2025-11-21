#!/bin/sh
set -e

echo "==============================================="
echo "  Inicializando container Django"
echo "==============================================="

#  Aguardar PostgreSQL
echo "Aguardando PostgreSQL em ${DB_HOST}:${DB_PORT}..."

python << 'EOF'
import socket, time, os

host = os.getenv("DB_HOST")
port = int(os.getenv("DB_PORT"))

while True:
    try:
        s = socket.create_connection((host, port), timeout=2)
        s.close()
        print("✔ Banco de dados disponível!")
        break
    except OSError:
        print("… ainda esperando o banco subir…")
        time.sleep(1)
EOF

# Makemigrations (opcional)
echo "Rodando makemigrations..."
python manage.py makemigrations

# Migrate
echo "Rodando migrations..."
python manage.py migrate

echo "Iniciando Django (WSGI modo desenvolvimento)"
exec "$@"