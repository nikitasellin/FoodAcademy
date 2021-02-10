# Production settings
import os

from .base import *

SECRET_KEY = os.environ.get('SECRET_KEY'),

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('PG_DB'),
        'USER': os.environ.get('PG_USER'),
        'PASSWORD': os.environ.get('PG_PASSWORD'),
        'HOST': os.environ.get('PG_HOST'),
        'PORT': '5432'
    }
}

# Change it with real backend
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = 'tmp/contactus/email/'
