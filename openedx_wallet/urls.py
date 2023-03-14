"""
URLs for openedx_wallet.
"""
from django.urls import path

from .views import ResultView, SetupView

urlpatterns = [
    path("issuance-setup/<uuid:pk>", SetupView.as_view(), name="issuance_setup"),
    path("issuance-result/<uuid:pk>", ResultView.as_view(), name="issuance_result"),
]
