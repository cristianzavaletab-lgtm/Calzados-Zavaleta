import os
from pathlib import Path
from datetime import timedelta
import dj_database_url

# ----------------- RUTAS BASE -----------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ----------------- CONFIGURACIÓN PRINCIPAL -----------------
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'clave-secreta-local')
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = ['*']

# ----------------- APLICACIONES INSTALADAS -----------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Apps locales
    'rest_framework',
    'corsheaders',
    'calzados_api',  # <- tu app principal
]

# ----------------- MIDDLEWARE -----------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Para archivos estáticos
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ----------------- CONFIGURACIÓN DE URLS Y WSGI -----------------
ROOT_URLCONF = 'calzados_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # si usas plantillas
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'calzados_project.wsgi.application'

# ----------------- BASE DE DATOS -----------------
# Por defecto (modo local con XAMPP)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME', 'calzados_db'),
        'USER': os.environ.get('DB_USER', 'root'),
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': os.environ.get('DB_HOST', '127.0.0.1'),
        'PORT': os.environ.get('DB_PORT', '3306'),
    }
}

# ----------------- VALIDACIÓN DE CONTRASEÑAS -----------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ----------------- INTERNACIONALIZACIÓN -----------------
LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'America/Lima'
USE_I18N = True
USE_TZ = True

# ----------------- ARCHIVOS ESTÁTICOS -----------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ----------------- CONFIGURACIÓN REST -----------------
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}

# ----------------- CORS -----------------
CORS_ALLOW_ALL_ORIGINS = True

# ----------------- CONFIGURACIÓN PARA PRODUCCIÓN (Render + Aiven) -----------------
if os.environ.get('RENDER'):
    DEBUG = False

    ALLOWED_HOSTS = [
        'calzados-zavaleta.onrender.com',  # tu dominio de Render
        'localhost',
        '127.0.0.1',
    ]

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ.get('DB_NAME', 'defaultdb'),
            'USER': os.environ.get('DB_USER', 'avnadmin'),
            'PASSWORD': os.environ.get('DB_PASSWORD', ''),
            'HOST': os.environ.get('DB_HOST', ''),
            'PORT': os.environ.get('DB_PORT', '3306'),
            'OPTIONS': {
                'ssl': {'ca': '/etc/ssl/certs/ca-certificates.crt'}
            }
        }
    }

    # Archivos estáticos comprimidos
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

    # Middleware WhiteNoise (para Render)
    MIDDLEWARE = list(MIDDLEWARE)
    if 'whitenoise.middleware.WhiteNoiseMiddleware' not in MIDDLEWARE:
        idx = MIDDLEWARE.index('django.middleware.security.SecurityMiddleware') + 1
        MIDDLEWARE.insert(idx, 'whitenoise.middleware.WhiteNoiseMiddleware')

# ----------------- CONFIGURACIÓN FINAL -----------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
