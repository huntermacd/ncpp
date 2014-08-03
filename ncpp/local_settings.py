import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ncpp',
        'USER': 'huntermacd',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

DEBUG = True