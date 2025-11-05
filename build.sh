#!/usr/bin/env bash
set -o errexit

echo "=== Instalando dependencias con pip ==="
pip install --upgrade pip
pip install -r requirements.txt

echo "=== Colectando archivos estáticos ==="
python manage.py collectstatic --no-input

echo "=== Aplicando migraciones ==="
python manage.py migrate

echo "=== Creando superusuario si no existe ==="
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'admin123')" | python manage.py shell

echo "=== Build completado ==="