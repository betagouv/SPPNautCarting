from django.urls import reverse


def menu(request):
    return {
        "menu": {
            "Carting": {
                "Recherche texte": reverse("carting:search_by_text"),
                "Recherche position": reverse("carting:search_by_position"),
            },
            "Pilotage": {
                "Recherche": reverse("carting:pilotage_search"),
            },
        }
    }
