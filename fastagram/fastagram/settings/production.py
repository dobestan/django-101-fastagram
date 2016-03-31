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
