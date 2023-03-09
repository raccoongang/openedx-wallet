"""
URLs for openedx_wallet.
"""
from django.conf import settings
from django.urls import path
from django.views.generic import TemplateView

from .views import IssuanceResultView, IssuanceSetupView

urlpatterns = [
    path("issuance-setup", IssuanceSetupView.as_view(), name="issuance_setup"),
    path("issuance-result", IssuanceResultView.as_view(), name="issuance_result"),
    path(
        "",
        TemplateView.as_view(
            template_name="openedx_wallet/base.html",
            extra_context={"settings": settings},
        ),
    ),
]
