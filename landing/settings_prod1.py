DEBUG = False
ALLOWED_HOSTS = ['shychkina.com']

#settings for db on server
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db1',
        'USER': 'landing',
        'PASSWORD': 'misterbean101',
        'HOST': 'localhost',
        'PORT': '',                      # Set to empty string for default.
    }
}