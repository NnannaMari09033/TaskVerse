from .base import *
import os


DEBUG = False


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('TaskVerse'),
        'USER': os.environ.get('Mari'),
        'PASSWORD': os.environ.get('@mari09033'),
        'HOST': os.environ.get('pgdb'),
        'PORT': os.environ.get('5432'),
    }
}


ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'yourdomain.com').split(',')


SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True


FLOWER_PORT = 5555
FLOWER_URL_PREFIX = 'flower'
FLOWER_BASIC_AUTH = os.environ.get('FLOWER_BASIC_AUTH', 'admin:password')


STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'


SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-688bz4^++t4zvch&6l0d6l0-fn_^l6$wyk%hk867bo=d#4u(f+')