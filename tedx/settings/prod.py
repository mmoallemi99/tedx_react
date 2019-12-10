from .base import *

DEBUG = False
ADMINS = (
    ('Mohammad Moallemi', 'mohammadmoallemi@outlook.com'),
)
ALLOWED_HOSTS = [
    'tedxui.ir',
    'www.tedxui.ir',
    'tedxuniversityofisfahan.ir',
    'www.tedxuniversityofisfahan.ir',
    '185.204.102.163',
]

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tedx',
        'USER': 'tedx',
        'PASSWORD': '4EunuP6D/cD6XWhYERE=',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}


# Production Settings

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
CSRF_USE_SESSIONS = True

# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# CSRF_COOKIE_AGE = None
