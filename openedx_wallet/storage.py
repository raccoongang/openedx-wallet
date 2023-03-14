"""
openedx_wallet verifiable credentials storage backends.
"""
from credentials.apps.verifiable_credentials.composition.verifiable_credentials import VerifiableCredentialsDataModel
from credentials.apps.verifiable_credentials.storages import WebWallet
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
        request = kwargs['request']
        return request.build_absolute_uri(
            reverse("openedx-wallet:issuance_setup", kwargs={"pk": issuance_line})
        )
