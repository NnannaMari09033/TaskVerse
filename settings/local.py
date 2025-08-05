from .base import *


DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'TaskVerse',
        'USER': 'Mari',
        'PASSWORD': '@mari09033',
        'HOST': 'pgdb',
        'PORT': '5432',
    }
}



ALLOWED_HOSTS = ['localhost', '127.0.0.1']


FLOWER_PORT = 5555
FLOWER_URL_PREFIX = 'flower'


SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False