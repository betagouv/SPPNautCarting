from django import forms
from django.conf import settings

from . import generator


class UploadFileForm(forms.Form):
    file = forms.FileField(
        error_messages={
            "required": "Vous devez séléctionner un fichier tableau type format XML"
        },
    )


def _get_ouvrages():
    ouvrages = generator.get(
        f"{settings.GENERATOR_SERVICE_HOST}/publication/from_preparation/list"
    ).json()
    return [(ouvrage, ouvrage) for ouvrage in ouvrages]


class PublicationReferentielForm(forms.Form):
    ouvrage = forms.ChoiceField(
        choices=_get_ouvrages,
        widget=forms.Select(attrs={"class": "fr-select"}),
        label="Sélectionnez un ouvrage",
    )
