from credentials.apps.verifiable_credentials.settings import vc_settings
from django.http import HttpRequest, QueryDict


def perfom_issue_credential(user, data):
    from credentials.apps.verifiable_credentials.rest_api.v1.views import IssueCredentialView

    def _build_request(user, data):
        request = HttpRequest()
        request.method = "POST"
        request.user = user
        request.POST = QueryDict(mutable=True)
        request.POST.update(data)
        return request

    response = IssueCredentialView.as_view()(request=_build_request(user, data))
    return response


def generate_data_model_choices():
    if vc_settings.FORCE_DATA_MODEL:
        return ((vc_settings.FORCE_DATA_MODEL.ID, vc_settings.FORCE_DATA_MODEL.ID),)
    else:
        return [
            (data_model.ID, data_model.ID)
            for data_model in vc_settings.DEFAULT_DATA_MODELS
        ]
