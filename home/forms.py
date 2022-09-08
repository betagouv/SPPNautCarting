from functools import partial

from django import forms
from django.conf import settings

from . import generator


class UploadFileForm(forms.Form):
    file = forms.FileField(
        error_messages={
            "required": "Vous devez séléctionner un fichier tableau type format XML"
        },
    )


def _get_ouvrages(source):
    ouvrages = generator.get(
        f"{settings.GENERATOR_SERVICE_HOST}/publication/from_{source}/list"
    ).json()
    return [(ouvrage, ouvrage) for ouvrage in ouvrages]


class PublicationReferentielPreparationForm(forms.Form):
    ouvrage = forms.ChoiceField(
        choices=partial(_get_ouvrages, "preparation"),
        widget=forms.Select(attrs={"class": "fr-select"}),
        label="Sélectionnez un ouvrage",
    )


class PublicationReferentielProductionForm(forms.Form):
    ouvrage = forms.CharField()
