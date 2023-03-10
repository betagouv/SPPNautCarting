from django.urls import reverse


def menu(request):
    return {
        "menu": {
            "Liste des ouvrages": {
                "Par nom": reverse("spo:ouvrages_by_name"),
                "Par date": reverse("spo:ouvrages_by_date"),
            },
            "Génération": {
                "Génération de tableaux": reverse("spo:tableau"),
                "Génération d'ouvrage en préparation": reverse(
                    "spo:publication_referentiel"
                ),
                "Génération d'ouvrage téléversé": reverse("spo:publication_upload"),
            },
            "Carting": {
                "Démo": reverse("carting:index"),
            },
        }
    }
