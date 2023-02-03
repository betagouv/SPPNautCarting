from django import forms


class XPathSearchForm(forms.Form):
    search_field = forms.CharField(
        label="Rechercher",
        max_length=512,
        # widget=forms.TextInput(attrs={"class": "form-control"}),
        error_messages={
            "required": "Veuillez saisir un xpath à afficher",
            "max_length": "Le xpath ne doit pas dépasser 512 caractères",
        },
    )
