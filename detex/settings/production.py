from .base import *

DEBUG = False

ALLOWED_HOSTS = ['45.147.46.199', 'detextools.com', 'www.detextools.com']

CORS_ALLOWED_ORIGINS = ["http://detextools.com", "http://www.detextools.com", 'http://45.147.46.199']

CORS_ORIGIN_WHITELIST = (

    'detextools.com',
    'www.detextools.com',
    '45.147.46.199',
)

CSRF_TRUSTED_ORIGINS = ['http://detextools.com']

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
