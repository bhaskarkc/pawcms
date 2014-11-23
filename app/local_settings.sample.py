from logging import config
import sys

LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
        }
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO'
    }
}
config.dictConfig(LOGGING)

SITE_ID = 1
SECRET_KEY = '<3m$sl+g__*0bcbyinv1@<3q$#h-@=y6!r<3nf*x#dm*f0_8<3'

DEBUG = True
TEMPLATE_DEBUG = True
THUMBNAIL_DEBUG = True

ALLOWED_HOSTS = []

STATIC_URL = '/static/'
STATIC_ROOT = '/var/www/html/static/paw/'
MEDIA_ROOT = '/var/www/html/static/paw/media'
MEDIA_URL = 'http://localhost/static/paw/media/'

from settings import *

INSTALLED_APPS += (
    # 'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'paw',
        'USER': 'paw',
        'PASSWORD': 'paw',
        'HOST': 'localhost',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',  # Set to empty string for default.
    }
}

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': '127.0.0.1:6379:3',
        'OPTIONS': {
            # 'PASSWORD': 'secretpassword',  # Optional
        }
    }
}

CACHEOPS_REDIS = {
    'host': 'localhost',  # redis-server is on same machine
    'port': 6379,  # default redis port
    'db': 1,  # SELECT non-default redis database
    # using separate redis db or redis instance
    # is highly recommended
    'socket_timeout': 3,
}
