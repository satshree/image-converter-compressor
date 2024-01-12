"""
Django settings for image_converter project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path


def get_heroku_var():
    var = os.environ.get("USE_HEROKU")
    return str(var).lower() == "true"


def get_staging_var():
    var = os.environ.get("STAGING")
    return str(var).lower() == "true"


# def get_allowed_hosts_var():
#     var = os.environ.get("ALLOWED_HOSTS", list([]))

#     if isinstance(var, list):
#         return var

#     allowed = var.split(",")
#     allowed.append('.vercel.app')

#     return allowed


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&kp(ulc8m%fbak!73h-enrnsbulqin@srn8_syn)8%s)%m9t38'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# ALLOWED_HOSTS = get_allowed_hosts_var()
ALLOWED_HOSTS = ['.vercel.app']

USE_HEROKU = get_heroku_var()

STAGING = get_staging_var()

# Application definition

INSTALLED_APPS = [
    # CLOUDINARY
    'cloudinary_storage',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    # THIRD PARTY LIBRARIES (ONLY REQUIRED APPS)
    'corsheaders',
    'cloudinary',
    # 'whitenoise.runserver_nostatic',

    # PROJECT APPS
    'main',
    'compressor',
    'converter',
]

MIDDLEWARE = [
    # DJANGO MIDDLEWARES
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # THIRD PARTY MIDDLEWARES
    'corsheaders.middleware.CorsMiddleware',
    # "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = 'image_converter.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/"templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'image_converter.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/imageconvertercompressor/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = (BASE_DIR / 'static',)
# STATICFILES_DIR = (
#     (BASE_DIR / "static"),
# (BASE_DIR / "main/static"),
# )
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = '/media/'
# MEDIA_DIR = "media"
MEDIA_ROOT = BASE_DIR / "media"
MEDIAFILES_DIR = (
    (BASE_DIR / "media"),
)

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CLOUDINARY_CLOUD_NAME = ""
CLOUDINARY_API_KEY = ""
CLOUDINARY_API_SECRET = ""

# CORS SETTINGS
try:
    from .cors_settings import *
except Exception as e:
    print("-" * 100)
    print("Unable to import CORS Settings.")
    print(str(e))
    print("-" * 100)

# LOCAL SETTINGS
try:
    from .local_settings import *
except:
    pass

# CLOUDINARY SETTINGS
try:
    # CLOUDINARY_STORAGE = {}
    # CLOUDINARY_URL = ""

    from .cloudinary_settings import *
except Exception as e:
    print("-" * 100)
    print("Unable to import Cloudinary Settings.")
    print(str(e))
    print("-" * 100)


# HEROKU SETTINGS
# try:
#     if USE_HEROKU:
#         import django_heroku
#         django_heroku.settings(locals())

#         from .heroku_settings import *
# except Exception as e:
#     print("-" * 100)
#     print("Unable to import Heroku Settings.")
#     print(str(e))
#     print("-" * 100)
