from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField(
        error_messages={
            "required": "Vous devez séléctionner un fichier tableau type format XML"
        },
    )
