# Settings that are unique to production go here
from .base import *  # noqa
import os

DEBUG = False

# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())

ALLOWED_HOSTS += [ 'sfba-wlt.herokuapp.com' ]

INSTALLED_APPS += ['storages']

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'sfba-wlt'

MEDIA_URL = 'http://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_FILE_OVERWRITE = False
