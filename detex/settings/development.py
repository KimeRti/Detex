from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'detexnew',

        'USER': 'postgres',

        'PASSWORD': '123',

        'HOST': 'localhost',

        'PORT': '5432',

    }
}

STATICFILES_DIRS = [
     os.path.join(BASE_DIR, '../../static')
     ]
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')