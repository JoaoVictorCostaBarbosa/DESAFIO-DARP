#!/bin/bash
set -e

echo "Aguardando o banco de dados ficar pronto..."

while ! nc -z db 5432; do
  sleep 1
done

echo "Banco de dados está pronto!"

echo "🚀 Aplicando migrações..."
alembic upgrade head

echo "Iniciando a aplicação..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
