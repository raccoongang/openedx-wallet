"""
Open edx Wallet verifiable credentials storage backends.
"""
from credentials.apps.verifiable_credentials.composition.verifiable_credentials import VerifiableCredentialsDataModel
from credentials.apps.verifiable_credentials.storages import WebWallet
from crum import get_current_request
from django.urls import reverse
from django.utils.translation import gettext as _


class OpenEdxWallet(WebWallet):
    """
    Learner Credential Wallet by Openedx.
    """

    ID = "openedx_wallet"
    NAME = _("Open edX Wallet")

    PREFERRED_DATA_MODEL = VerifiableCredentialsDataModel

    @classmethod
    def get_deeplink_url(cls, issuance_line, **kwargs):
        """
        Construct URL for initial page.
        """
        request = get_current_request()
        if not request:
            return None
        return request.build_absolute_uri(
            reverse("openedx-wallet:issuance_setup", kwargs={"pk": issuance_line.uuid})
        )
