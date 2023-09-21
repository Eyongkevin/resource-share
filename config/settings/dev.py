import os

from .base import *
import environ

env = environ.Env()
env_file = os.path.join(BASE_DIR, '.env-dev')
env.read_env(env_file)

SECRET_KEY = env('DJANGO_SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}
