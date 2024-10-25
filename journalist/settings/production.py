from .base import *

ALLOWED_HOSTS = ["cosi.medtoon.co.tz, 'localhost"]
DEBUG = False

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
CSRF_TRUSTED_ORIGINS = [
    'https://cosi.medtoon.co.tz',
]

try:
    from .local import *
except ImportError:
    pass
