# -*- coding: utf-8 -*-

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'name_db',  #TODO: set name_db
        'USER': 'username_db',  #TODO: set username_db
        'PASSWORD': 'password_user_db', #TODO: set password_user_db
        'HOST': 'localhost',
        'PORT': '',  # Set to empty string for default.
    }
}

ALLOWED_HOSTS = ['*']   #TODO: set like this ['objets-trouves.palexpo.ch', 'objetstrouves.palexpo.ch']

ADMINS = [('Kevin', 'estalella.kevin@gmail.com')]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# One Time Stripe
stripe_keys = {
  'secret_key': 'sk_test_7z5jn6AfgIKAbvpcy41tJqDh',
  'publishable_key': 'pk_test_UbEMwmv3TU0WpoWV6cn462zt'
}