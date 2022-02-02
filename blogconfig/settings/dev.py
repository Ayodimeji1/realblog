from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4x&ys-hp(wqveql+%48p_i0rbr+*&9fi$dr9nf2^@3kgzp(*h&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / 'staticfiles/'

STATICFILES_DIRS = [
     os.path.join(BASE_DIR, 'static'),
]

MEDIA_URL = 'media/'

MEDIA_ROOT = BASE_DIR / 'media'
