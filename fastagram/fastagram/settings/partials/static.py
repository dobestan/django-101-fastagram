import os

from .application import PROJECT_ROOT_DIR


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/


STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_ROOT_DIR, "dist", "static")
MEDIA_ROOT = os.path.join(PROJECT_ROOT_DIR, "dist", "media")

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

PIPELINE = {
    'STYLESHEETS': {
        'application': {
            'source_filenames': (
              'css/*.css',
            ),
            'output_filename': 'css/fastagram.css',
        },
    },
    'JAVASCRIPT': {
    }
}
