from .base import *

DEBUG = False

ALLOWED_HOSTS = ['detextools.com','www.detextools.com']

DATABASES = {
    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'detexnew',

        'USER': 'postgres1',

        'PASSWORD': '123',

        'HOST': 'localhost',

        'PORT': '5432',

    }
}

STATIC_ROOT = os.path.join(BASE_DIR,'static/')