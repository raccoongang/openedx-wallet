from credentials.apps.verifiable_credentials.composition.verifiable_credentials import VerifiableCredentialsDataModel
from credentials.apps.verifiable_credentials.serializers import IssuanceLineSerializer
from credentials.apps.verifiable_credentials.storages import WebWallet
from django.urls import reverse


class OpenEdxWallet(WebWallet):
    """
    Learner Credential Wallet by Openedx.
    """

    ID = "openedxwallet"
    DEEP_LINK_URL = reverse("openedx-wallet:issuance_setup")
    ISSUANCE_REQUEST_SERIALIZER = IssuanceLineSerializer
    PREFERRED_DATA_MODEL = VerifiableCredentialsDataModel

    @classmethod
    def get_deeplink_url(cls, issuance_uuid):
        return f"{cls.DEEP_LINK_URL}?issuance_uuid={issuance_uuid}"
