from pathlib import Path
import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# Informações do sistema
SYSTEM_NAME = "Beach Time"  
SYSTEM_VERSION = "0.1.0"
SYSTEM_DESCRIPTION = "API para o Beach Time" 
API_DOC_URL = "/docs"

# Segurança
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "unsafe-key")
DEBUG = os.getenv("DEBUG", "True") == "True"
ALLOWED_HOSTS = []

# Arquivos de mídia
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Django apps
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Terceiros
THIRD_PARTY_APPS = [
    'ninja',
    'ninja_jwt',
    'ninja_extra',
]

# Núcleo do projeto
CORE_APPS = [
    'core',
]

# Apps internos do projeto
LOCAL_INTERNAL_APPS = [
    'modules.users',
    'modules.tokens',
    'modules.sports',
]

# Apps externos (ex: plugins locais ou libs customizadas)
LOCAL_EXTERNAL_APPS = []

# Registro final de apps
INSTALLED_APPS = (
    DJANGO_APPS
    + THIRD_PARTY_APPS
    + CORE_APPS
    + LOCAL_INTERNAL_APPS
    + LOCAL_EXTERNAL_APPS
)

# Middlewares padrão
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URLs e Templates
ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'
ASGI_APPLICATION = 'core.asgi.application'

# Banco de dados
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'beach_time_db'),
        'USER': os.getenv('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'postgres'),
        'HOST': os.getenv('POSTGRES_HOST', 'localhost'),
        'PORT': os.getenv('POSTGRES_PORT', '5432'),
    }
}
# Autenticação

# Modelo de usuário
AUTH_USER_MODEL = 'users.CustomUser'

# Autenticação com JWT (se for usar)
NINJA_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=18),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}

# Validação de senha
AUTH_PASSWORD_VALIDATORS = []

# Internacionalização
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Fortaleza'
USE_I18N = True
USE_TZ = True

# Arquivos estáticos
STATIC_URL = 'static/'

# ID padrão
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
