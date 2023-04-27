'''Use this for development'''

from .base import *

ALLOWED_HOSTS += ['127.0.0.1','localhost']
DEBUG = True

WSGI_APPLICATION = 'home.wsgi.dev.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv("POSTGRES_DATABASE", "postgres"),
        'USER' : os.getenv("POSTGRES_USER", "postgres"),
        'PASSWORD' : os.getenv("POSTGRES_PASSWORD", "postgres"),
        'HOST' : os.getenv("POSTGRES_HOST", "db"),
        'PORT' : os.getenv("POSTGRES_PORT", "5432"),
    }
}

CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',
)