import json
import requests

from django import forms
from django.conf import settings

class UploadFileForm(forms.Form):
    file = forms.FileField(
        error_messages={
            "required": "Vous devez séléctionner un fichier tableau type format XML"
        },
    )


def get_ouvrages():
    username, password = list(settings.BASICAUTH_USERS.items())[0]

    response = requests.get(
        f"{settings.GENERATOR_SERVICE_HOST}/publication/ouvrages/list",
        auth=(username, password),
    )

    ouvrages = response.json()
    return [(ouvrage, ouvrage) for ouvrage in ouvrages]


class PublicationReferentielForm(forms.Form):
    ouvrage = forms.ChoiceField(
        choices=get_ouvrages, widget=forms.Select(attrs={"class": "fr-select"})
    )
