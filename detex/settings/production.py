from .base import *

DEBUG = True

ALLOWED_HOSTS = ['45.147.46.199', 'detextools.com', 'www.detextools.com']

CSRF_TRUSTED_ORIGINS = ['https://detextools.com', 'https://www.detextools.com']

DATABASES = {
    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'detex',

        'USER': 'detexuser',

        'PASSWORD': 'detex123',

        'HOST': 'localhost',

        'PORT': '5432',

    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
