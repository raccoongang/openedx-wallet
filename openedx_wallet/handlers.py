"""
Open edX Wallet signal handlers.
"""
from .apps import OpenedxWalletConfig, logger

logger.warning("%s signal handlers were registered!", OpenedxWalletConfig.verbose_name)
