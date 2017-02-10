# -*- coding: utf-8 -*-

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'myproject',  #TODO: set name_db
        'USER': 'postgres',  #TODO: set username_db
        'PASSWORD': 'a1t9t8!7la2', #TODO: set password_user_db
        'HOST': 'localhost',
        'PORT': '',  # Set to empty string for default.
    }
}

# mailhog
EMAIL_HOST = '0.0.0.0'
EMAIL_PORT = '1025'
EMAIL_HOST_USER = 'estalella.kevin@gmail.com'

MEDIA_URL = "/media/"

# One Time Stripe
STRIPE_KEYS = {
  'secret_key': 'sk_test_7z5jn6AfgIKAbvpcy41tJqDh',
  'publishable_key': 'pk_test_UbEMwmv3TU0WpoWV6cn462zt'
}