import os

import raven

from .partials import *


DEBUG = False

ALLOWED_HOSTS = [
    "*",
]


INSTALLED_APPS += [
    'raven.contrib.django.raven_compat',
]


RAVEN_CONFIG = {
    'dsn': 'https://4f2bb88d49f345e88f63bb8066cdccb9:3d6fe481eee24ec58186509440d6a7ff@app.getsentry.com/72479',
}


STATICFILES_STORAGE = 'fastagram.storage.S3PipelineCachedStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")

AWS_S3_CUSTOM_DOMAIN = 'd643ns7eahkdr.cloudfront.net'
AWS_S3_URL_PROTOCOL = 'https'

STATIC_URL = "https://d643ns7eahkdr.cloudfront.net/"
