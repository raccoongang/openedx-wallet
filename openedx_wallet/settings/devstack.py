"""
Devstack settings for the openedx_wallet app.
"""


def plugin_settings(settings):
    """
    Defines completion-specific settings when app is used as a plugin to edx-platform.
    See: https://github.com/edx/edx-platform/blob/master/openedx/core/djangoapps/plugins/README.rst
    """
    settings.OPENEDX_WALLET_TYPE = 'web'
