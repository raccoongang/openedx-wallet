"""
Common settings for the openedx_wallet app.
"""

from os.path import abspath, dirname, join


def root(*args):
    """
    Get the absolute path of the given path relative to the project root.
    """
    return join(abspath(dirname(__file__)), *args)


USE_TZ = True

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'waffle',
    'openedx_wallet',
)

LOCALE_PATHS = [
    root('openedx_wallet', 'conf', 'locale'),
]

ROOT_URLCONF = 'openedx_wallet.urls'

SECRET_KEY = 'insecure-secret-key'


def plugin_settings(settings):
    """
    Defines completion-specific settings when app is used as a plugin to edx-platform.
    See: https://github.com/edx/edx-platform/blob/master/openedx/core/djangoapps/plugins/README.rst
    """
    # plugin setting
    settings.OPENEDX_WALLET_TYPE = 'web'
