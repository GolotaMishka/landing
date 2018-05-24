DEBUG = False
ALLOWED_HOSTS = ['206.189.123.93']


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