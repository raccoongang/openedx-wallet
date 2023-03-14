"""
openedx_wallet UI forms.
"""
from datetime import datetime, timedelta

from credentials.apps.verifiable_credentials.models import IssuanceLine, generate_data_model_choices
from django import forms
from django.utils.translation import gettext_lazy as _


class IssuanceLineForm(forms.ModelForm):
    """
    Verifiable credential issuance request setup.
    """

    data_model_id = forms.ChoiceField(
        choices=generate_data_model_choices(), required=True, label=_("Data model")
    )

    class Meta:
        """
        Form's meta.
        """

        model = IssuanceLine
        fields = [
            "data_model_id",
            "subject_id",
            "expiration_date",
        ]
        help_texts = {
            "subject_id": _("Required. Valid DID value."),
            "expiration_date": _("Optional. Should be future date."),
        }
        widgets = {
            "expiration_date": forms.DateTimeInput(
                attrs={
                    "type": "datetime-local",
                    "min": (datetime.today() + timedelta(days=1)).strftime(
                        "%Y-%m-%dT%H:%M"
                    ),
                },
            )
        }
