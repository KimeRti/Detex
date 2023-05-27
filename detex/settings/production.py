from .base import *

DEBUG = False

ALLOWED_HOSTS = ['45.147.46.199', 'detextools.com', 'www.detextools.com']

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

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True