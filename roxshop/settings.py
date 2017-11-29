"""
Django settings for roxshop project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w#bv&)i@g95fb#@wuenj(n#avok6d+)68&_*a8a%+c4t=5nk0k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shopstore',
    'easy_thumbnails',
    'filer',
    'mptt',
    'cart',
]




MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'roxshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'roxshop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/kurt/django/roxshop/media'


THUMBNAIL_HIGH_RESOLUTION = True

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
    )

FILER_STORAGES = {
    'public':{
        'main':{
            'ENGINE':'filer.storage.PublicFileSystemStorage',
            'OPTIONS':{
                'location': '/home/kurt/django/roxshop/media/filer',
                'base_url': '/media/filer/',
            },
            'UPLOAD_TO':'filer.utils.generate_filename.randomized',
            'UPLOAD_TO_PREFIX':'filer_public',
        },
        'thumbnails':{
            'ENGINE':'filer.storage.PublicFileSystemStorage',
            'OPTIONS':{
                'location': '/home/kurt/django/roxshop/media/filer_thumbnails',
                'base_url': '/media/filer_thumbnails/',
            },

        },
    },
    'private':{
        'main':{
            'ENGINE':'filer.storage.PublicFileSystemStorage',
            'OPTIONS':{
                'location': '/home/kurt/django/roxshop/smedia/filer',
                'base_url': '/smedia/filer/',
            },
            'UPLOAD_TO':'filer.utils.generate_filename.randomized',
            'UPLOAD_TO_PREFIX':'filer_public',
        },
        'thumbnails':{
            'ENGINE':'filer.storage.PublicFileSystemStorage',
            'OPTIONS':{
                'location': '/home/kurt/django/roxshop/smedia/filer_thumbnails',
                'base_url': '/smedia/filer_thumbnails/',
            },

        },
    },
}

SESSION_EXPIRE_AT_BROWSER_CLOSE = True