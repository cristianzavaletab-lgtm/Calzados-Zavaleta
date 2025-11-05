#!/usr/bin/env bash
# Exit on error
set -o errexit

echo "=== Instalando dependencias con pip ==="
pip install --upgrade pip
pip install -r requirements.txt

echo "=== Colectando archivos estáticos ==="
python manage.py collectstatic --no-input

echo "=== Aplicando migraciones ==="
python manage.py migrate

echo "=== Build completado ==="