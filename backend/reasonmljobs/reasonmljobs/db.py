# -*- coding: utf-8 -*-
import os

DATABASE_NAME = os.environ.get('DATABASE_NAME')
USERNAME = os.environ.get('USERNAME')
PASSWORD = os.environ.get('PASSWORD')
HOST = os.environ.get('HOST')
PORT = os.environ.get('PORT')

DB_CONFIG = {
    'default': {
        'NAME': DATABASE_NAME,
        'ENGINE': 'django.db.backends.mysql',
        'USER': USERNAME,
        'PASSWORD': PASSWORD,
        'HOST': HOST,
        'PORT': PORT
    }
}