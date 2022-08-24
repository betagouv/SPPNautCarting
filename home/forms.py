from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField(
        error_messages={
            "required": "Vous devez séléctionner un fichier tableau type format XML"
        },
    )


class PublicationReferentielForm(forms.Form):
    ouvrage = forms.ChoiceField(
        choices=[("g4p", "g4p")], widget=forms.Select(attrs={"class": "fr-select"})
    )
