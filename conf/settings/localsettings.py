from conf.settings.default import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'jworld_db',
        'USER': 'jovani',
        'PASSWORD': 'galapagos',
        'HOST': 'localhost',
    }
}
