from django import forms
from django.conf import settings

from . import generator


class UploadFileForm(forms.Form):
    file = forms.FileField(
        error_messages={
            "required": "Vous devez séléctionner un fichier tableau type format XML"
        },
    )

    def clean_file(self):
        file = self.cleaned_data["file"]
        if file.content_type != "text/xml":
            raise forms.ValidationError(
                "Le fichier doit être un fichier tableau type format XML"
            )
        return file


def _get_preparation_ouvrages():
    ouvrages = generator.get(
        f"{settings.GENERATOR_SERVICE_HOST}/publication/from_preparation/list"
    ).json()
    return [(ouvrage, ouvrage) for ouvrage in ouvrages]


class PublicationReferentielPreparationForm(forms.Form):
    ouvrage = forms.ChoiceField(
        choices=_get_preparation_ouvrages,
        widget=forms.Select(attrs={"class": "fr-select"}),
        label="Sélectionnez un ouvrage",
    )


class PublicationReferentielProductionForm(forms.Form):
    ouvrage = forms.CharField()
