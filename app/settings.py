# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'froala_editor',
    'dbsettings',
    'linaro_django_pagination',
    'sorl.thumbnail',
    'sitetree',

    'notice',
    'college',
    'file',
    'gallery',
    'news',
    'snippet',
    'core',
    'users',
    'page',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'core.middleware.SelectiveSessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'linaro_django_pagination.middleware.PaginationMiddleware',
)

ROOT_URLCONF = 'app.urls'

WSGI_APPLICATION = 'app.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kathmandu'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'core.loader.ThemeLoader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader',
    'core.loader.ThemeLoader',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

try:
    from .local_settings import *  # noqa
except ImportError:
    pass

AUTH_USER_MODEL = 'users.User'
# LOGIN_REDIRECT_URL = '/'
# LOGIN_URL = '/user/login/'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.i18n',
    'django.contrib.messages.context_processors.messages',
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# DISABLE_SESSIONS_FOR = [
#     '/',
# ]
