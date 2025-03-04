"""
Django settings for comp project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5qq=e42p8%$^yc!yyy6e#((x#*813@-%m2$ix$28ebq1b&)xuz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['www.spacemate.in','127.0.0.1', 'localhost']

import os
# Application definition








INSTALLED_APPS = [
    # 'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "rest_framework",
    'rest_framework.authtoken',
    'djoser',
    "api",
    "app",
    "corsheaders",
    "django_filters",
]
CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:5173",
    "http://localhost:3000",
    "https://spacemate.pythonanywhere.com",
    "https://www.spacemate.in"
]
CORES_ORIGIN_WHITELIST = [
    "http://127.0.0.1:5173",
    "http://localhost:3000",
    "https://spacemate.pythonanywhere.com",
    "https://www.spacemate.in"
]
# from django.core.mail import send_mail

# send_mail(
#     'Test Email',
#     '{uid}{token}',
#     'x2.prateeksonar2002@gmail.com',
#     ['xprateek.2002@gmail.com'],
#     fail_silently=False,
# )






MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = 'comp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'build1')],
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

WSGI_APPLICATION = 'comp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'spacemate$default',
#         'USER': 'spacemate',
#         'PASSWORD': 'Space@123',
#         'HOST': 'spacemate.mysql.pythonanywhere-services.com',
#         'OPTIONS': {
#             'autocommit': True,
#             }
#     }
# }

#  'PASSWORD': 'Interior@mate#765',





# EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_HOST_USER='x2.prateeksonar2002@gmail.com'
EMAIL_HOST_PASSWORD='zhkaiodrfmtiegyi'
EMAIL_USE_TLS=True


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',

    ),
    # 'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.PageNumberPagination',
    # 'PAGE_SIZE':10
}

DJOSER = {
    "LOGIN_FIELD":'username',
    "USER_CREATE_PASSWORD_RETYPE":True,
    "USERNAME_CHANGED_EMAIL_CONFIRMATION":True,
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION":True,
    "SEND_CONFIRMATION_EMAIL":True,
    "SET_USERNAME_RETYPE":True,
    "SET_PASSWORD_RETYPE":True,
    "PASSWORD_RESET_CONFIRM_URL":"password/reset/confirm/{uid}/{token}",
    "USERNAME_RESET_CONFIRM_URL":"username/reset/confirm/{uid}/{token}",
    "ACTIVATION_URL":"activate/{uid}/{token}",
    'SEND_ACTIVATION_EMAIL': True,
    "PASSWORD_RESET_CONFIRM_RETYPE":True,
    "PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND":True,


    "SERIALIZERS":{

        # 'user_create':'app.serializers.UserCreateSerializer',
        # 'user':'app.serializers.UserCreateSerializer',
        # 'password_reset': 'djoser.email.PasswordResetEmail',
        'current_user':'app.serializers.UserCreateSerializer',
        'user_delete':'djoser.serializers.UserDeleteSerializer',
        'password_reset': 'app.serializers.SendEmailResetSerializer',
    },
    'EMAIL': {
        # 'password_reset': 'djoser.email.PasswordResetEmail'
        # 'password_reset': 'app.email.CustomPasswordResetView'
    }
}


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]
from datetime import timedelta

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('Bearer',),
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),

}
# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# rpmkprzjjcmrleja

# zhkaiodrfmtiegyi
# EMAIL_HOST_USER='x2.prateeksonar2002@gmail.com'
# EMAIL_HOST_PASSWORD='zhkaiodrfmtiegyi'
# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'


MEDIA_URL = '/image/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'image')

STATICFILES_DIRS = (
    # os.path.join(BASE_DIR, 'build1/static'),
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'








DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# AUTH_USER_MODEL = 'app.UserAccount'


# AUTH_USER_MODEL="app.UserAccount"

