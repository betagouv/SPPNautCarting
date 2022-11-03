from django.urls import reverse


def menu(request):
    return {
        "menu": {
            "Liste des ouvrages": {
                "Par nom": reverse("home:ouvrages_by_name"),
                "Par date": reverse("home:ouvrages_by_date"),
            },
            "Génération": {
                "Génération de tableaux": reverse("home:tableau"),
                "Génération d'ouvrage en préparation": reverse(
                    "home:publication_referentiel"
                ),
                "Génération d'ouvrage téléversé": reverse("home:publication_upload"),
            },
        }
    }
