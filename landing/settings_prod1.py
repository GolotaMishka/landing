DEBUG = False
ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbapp',
        'USER': 'english',
        'PASSWORD': 'misterbean',
        'HOST': 'localhost',
        'PORT':'',
    }
}

