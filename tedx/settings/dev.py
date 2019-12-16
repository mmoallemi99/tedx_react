from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'tedx',
#         'USER': 'tedx',
#         'PASSWORD': '4EunuP6D/cD6XWhYERE=',
#         'HOST': 'localhost',
#         'PORT': 5432,
#     }
# }

INSTALLED_APPS += [
    'corsheaders',
]
MIDDLEWARE = [
                 'corsheaders.middleware.CorsMiddleware',
             ] + MIDDLEWARE

# CORS Settings Section
# https://github.com/adamchainz/django-cors-headers
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',

    'Access-Control-Allow-Origin',
]
