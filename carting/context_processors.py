from django.urls import reverse


def menu(request):
    return {
        "menu": {
            "Carting": {
                "Démo": reverse("carting:index"),
            },
        }
    }
