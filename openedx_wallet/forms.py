from credentials.apps.verifiable_credentials.models import IssuanceLine
from django import forms
from django.utils.translation import gettext_lazy as _

from .utils import generate_data_model_choices, perfom_issue_credential


class IssuanceLineForm(forms.ModelForm):
    data_model = forms.ChoiceField(choices=generate_data_model_choices())

    class Meta:
        model = IssuanceLine
        fields = [
            "uuid",
            "issuer_id",
            "subject_id",
            "holder_id",
            "data_model",
            "expiration_date",
        ]
        labels = {
            "uuid": _("UUID"),
            "issuer_id": _("Issuer ID"),
            "subject_id": _("Subject ID"),
            "holder_id": _("Holder ID"),
            "data_model": _("Data model"),
            "expiration_date": _("Expiration date"),
        }
        widgets = {
            'expiration_date': forms.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user  # FIXME: anonymous user
        self.fields["uuid"].widget.attrs["readonly"] = True
        self.fields["issuer_id"].widget.attrs["readonly"] = True
        self.fields["subject_id"].required = True

        for field in self.fields:
            self.fields[field].help_text = ''

    def validate_unique(self):
        # Skip validation
        pass

    def issue_credential(self):
        response = perfom_issue_credential(self.user, self.cleaned_data)
        return str(self.cleaned_data)
