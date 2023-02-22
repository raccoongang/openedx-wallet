"""
openedx_wallet Django application initialization.
"""

import logging

from django.apps import AppConfig

APP_NAME = 'openedx_wallet'

logger = logging.getLogger(APP_NAME)


class OpenedxWalletConfig(AppConfig):
    """
    Configuration for the `openedx_wallet` Django application.
    """

    name = APP_NAME
    verbose_name = 'Open edX Wallet'

    plugin_app = {
        'url_config': {
            'credentials.djangoapp': {
                'namespace': 'openedx-wallet',
                'regex': r'^openedx-wallet/',
                'relative_path': 'urls',
            },
        },
        'settings_config': {
            'credentials.djangoapp': {
                'common': {
                    'relative_path': 'settings.common',
                },
                'devstack': {
                    'relative_path': 'settings.devstack',
                },
            },
        },
        'signals_config': {
            'credentials.djangoapp': {
                'relative_path': 'handlers',
                'receivers': [],
            },
        },
    }

    def ready(self):
        """
        Inform plugin is initiated.
        """
        logger.warning("%s plugin is ready!", self.verbose_name)
