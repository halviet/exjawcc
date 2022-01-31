import os.path
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = False


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'NAME': BASE_DIR / 'exjawcc.sqlite3',
        'USER': 'exjawadmin',
        'PASSWORD': 'y*D65rJsDMaUqk%Q',
        'HOST': '127.0.0.1',
        'PORT': '8000',
        'TEST': {
            'NAME': 'test_db',
        },
    },
}


STATIC_URL = 'static/'
STATIC_DIR = os.path.join(BASE_DIR, 'static')
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [STATIC_DIR, ]
