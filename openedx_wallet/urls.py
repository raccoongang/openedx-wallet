"""
URLs for openedx_wallet.
"""
from django.conf import settings
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    # TODO: Fill in URL patterns and views here.
    path('', TemplateView.as_view(
        template_name="openedx_wallet/base.html",
        extra_context={'settings': settings}
    )),
]
