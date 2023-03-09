from credentials.apps.verifiable_credentials.models import IssuanceLine
from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import FormView

from .forms import IssuanceLineForm


class IssuanceSetupView(FormView):
    form_class = IssuanceLineForm
    template_name = "issuance_setup.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        kwargs["instance"] = get_object_or_404(
            IssuanceLine, uuid=self.request.GET.get("issuance_uuid")
        )
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["verifiable_credentials_mfe_url"] = "https://google.com"
        return context


class IssuanceResultView(FormView):
    form_class = IssuanceLineForm
    template_name = "issuance_result.html"

    def form_valid(self, form):
        credential = form.issue_credential()
        return render(
            self.request,
            self.template_name,
            {
                "credential": credential,
                "verifiable_credentials_mfe_url": "https://google.com",
            },
        )
