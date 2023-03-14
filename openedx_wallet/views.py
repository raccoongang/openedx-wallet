"""
openedx_wallet page views.
"""
import json
import logging
from urllib.parse import urljoin

from credentials.apps.verifiable_credentials.models import IssuanceLine
from credentials.apps.verifiable_credentials.rest_api.v1.views import IssueCredentialView
from django.conf import settings
from django.urls import reverse
from django.utils.translation import gettext as _
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView

from .forms import IssuanceLineForm

logger = logging.getLogger(__name__)


class SetupView(UpdateView):
    """
    Verifiable credential issuance request setup.
    """

    form_class = IssuanceLineForm
    template_name = "issuance_setup.html"
    model = IssuanceLine

    extra_context = {
        "learner_record_mfe_verifiable_credentials_url": urljoin(
            settings.LEARNER_RECORD_MFE_RECORDS_PAGE_URL, "verifiable-credentials"
        ),
    }

    def get_success_url(self):
        """
        Construct URL to redirect when form submission succeeded.
        """
        return reverse(
            "openedx-wallet:issuance_result", kwargs={"pk": self.kwargs["pk"]}
        )

    def post(self, request, *args, **kwargs):
        """
        Extend processing logic with a side effect - verifiable credential issuance.
        """
        super().post(request, *args, **kwargs)

        form = self.get_form()
        if not form.is_valid():
            return self.form_invalid(form)

        verifiable_credential = self.request_verifiable_credential(form)
        # now form may include extra errors from issuer:
        if not form.is_valid():
            return self.form_invalid(form)

        self.put_to_session(verifiable_credential)
        return self.form_valid(form)

    def request_verifiable_credential(self, form):
        """
        Make additional direct request to verifiable credentials issuance API view.

        NOTE:
            The backend uses its special position to make internal request using seamless session.
            External backends have to authorize via OAuth2.
        """
        failure_msg = _("Something went wrong...")
        verifiable_credential = {"result": failure_msg}

        try:
            # call Verifiable Credentials issuance directly:
            response = IssueCredentialView.as_view()(
                self.request, issuance_line_uuid=self.object.uuid
            )
            if response.status_code == 400:
                for error, message in response.data.items():
                    form.add_error(error if error in form.fields else None, message)
        except Exception:  # pylint: disable=broad-except
            msg = f"Verifiable credential issuance request failed: [{self.object.uuid}]"
            logger.exception(msg)
            form.add_error(None, msg)
        else:
            verifiable_credential = response.data.get(
                "verifiableCredential", verifiable_credential
            )

        return json.dumps(verifiable_credential)

    def put_to_session(self, value):
        """
        Store issued verifiable credential in session's issuance context.
        """
        session_context = self.request.session.get("issuance_context", {})
        session_context[str(self.kwargs["pk"])] = value
        self.request.session["issuance_context"] = session_context


class ResultView(TemplateView):
    """
    Issued verifiable credential result.
    """

    template_name = "issuance_result.html"

    extra_context = {
        "learner_record_mfe_verifiable_credentials_url": urljoin(
            settings.LEARNER_RECORD_MFE_RECORDS_PAGE_URL, "verifiable-credentials"
        ),
    }

    def get_context_data(self, **kwargs):
        """
        Extend render context with needed data.
        """
        context = super().get_context_data(**kwargs)
        verifiable_credential_json = self.get_from_session()
        prettyfied = self.prettify_json(verifiable_credential_json)

        context.update(
            {
                "verifiable_credential": verifiable_credential_json,
                "formatted_verifiable_credential": prettyfied,
                "setup_page_url": reverse(
                    "openedx-wallet:issuance_setup",
                    kwargs={"pk": kwargs["pk"]},
                ),
                "json_file_name": f"{kwargs['pk']}.json",
            }
        )
        return context

    def get_from_session(self, default="{}"):
        """
        Pull stored verifiable credential from session's issuance context.
        """
        issuance_context = self.request.session.get("issuance_context", {})
        return issuance_context.get(str(self.kwargs["pk"]), default)

    @staticmethod
    def prettify_json(json_str):
        """
        Format JSON for rendering.
        """
        loaded = json.loads(json_str)
        return json.dumps(loaded, indent=4)
