from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
from unipath import Path
import dj_database_url
from decouple import config

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

PROJECT_DIR = Path(__file__).parent

DEBUG = config('DEBUG', default=False, cast=bool) 
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': dj_database_url.config(
      default = config('DATABASE_URL'))
}

ALLOWED_HOSTS = ['*']

TIME_ZONE = 'America/Sao_Paulo'
LANGUAGE_CODE = 'en-us'

USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = PROJECT_DIR.parent.child('media')
MEDIA_URL = '/media/'

STATIC_ROOT = PROJECT_DIR.child('static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    PROJECT_DIR.parent.child('static'),
)

SECRET_KEY = config('SECRET_KEY')

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'parsifal.urls'

WSGI_APPLICATION = 'parsifal.wsgi.application'

TEMPLATE_DIRS = (
    PROJECT_DIR.parent.child('templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'south',
    'activities',
    'auth',
    'core',
    'blog',
    'reviews',
    'reviews.planning',
    'reviews.conducting',
    'reviews.reporting',
    'reviews.settings',
    'settings',
    'utils',
)

LOGIN_URL = '/signin/'