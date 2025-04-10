"""
Django settings for quora project.

Generated by 'django-admin startproject' using Django 4.1.13.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Define the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+ta0w_$ji&+rj3y&&17l4@u*$d=-^xdfbd5j+=yc&tc9x5w9x6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # Set to False in production

ALLOWED_HOSTS = []  # Add domain names or IPs when deploying

LOGIN_URL = 'login'  # Redirect to this URL if user is not logged in

INSTALLED_APPS = [
    'django.contrib.admin',  
    'django.contrib.auth',  
    'django.contrib.contenttypes',
    'django.contrib.sessions', 
    'django.contrib.messages',
    'django.contrib.staticfiles',  
    'app',  #  custom app
    'widget_tweaks',  # For form rendering customization in templates
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Manages sessions across requests
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # Protects against CSRF attacks
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Associates users with requests
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'quora.urls'  # Root URL configuration

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, "templates"],  # Location of template files
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',  # Adds user object to templates
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'quora.wsgi.application'  # WSGI entry point for deployment

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Using PostgreSQL as DB
        'NAME': 'Quora',             
        'USER': 'postgres',           
        'PASSWORD': 'root',  
        'HOST': 'localhost',        
        'PORT': '5433',             
    }
}

# Password validation to enhance security
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # Minimum password length
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'  

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True 

USE_TZ = True  

STATIC_URL = 'static/'  # URL path for static files

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  

