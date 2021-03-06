"""
Django settings for example_django_hot project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
REL_SITE_ROOT = os.path.relpath(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=t@sa9iuihc4@0jk=-04woqga%5z0i-0u^dkd18oof2xz@cx8s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_tables2',
    'bootstrapform',
    'HotDisplay',
    'example_app'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'UTC'

USE_I18N = False

USE_L10N = False

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(SITE_ROOT, 'static')


# HotDisplay Settings
DISPLAY_APPS = ('example_app',) # 'HotDisplay'
## ALL or AUTH or list of groups
# HOT_PERMITTED_GROUPS = 'ALL'
# LOGIN_URL = '%s/login/' % SUB_SITE
# LOGIN_EXEMPT_URLS = ['login/']
# LOGIN_REDIRECT_URL = '%s/' % SUB_SITE
# PAGE_BASE = 'page_base.html'
# SK_VIEW_SETTINGS ={'viewname': 'setup', 'args2include': [False, True], 'base_name': 'Setup'}
# 
SITE_TITLE = 'HotDisplay'
INDEX_URL_NAME = 'index'
TOP_MENU = [{'url': 'hot_display', 'name': 'Display', 'glyph': 'cog'}]

# HOT_ID_IN_MODEL_STR = True
