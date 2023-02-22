from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET

from carting.models import OuvrageSection


# FIXME : Les sections commençant par '0.' ne devraient pas être affichées (pas de géométrie attachée); les illustrations en '0.' sont mal ordonnées
@login_required
@require_GET
def index(request: HttpRequest) -> HttpResponse:
    sections = []
    search = request.GET.get("search", "")

    ouvrage, _, numero = search.rpartition("/")
    if numero:
        sections = OuvrageSection.objects.all()
        if ouvrage:
            sections = sections.filter(ouvrage_name=ouvrage)

        try:
            section = sections.get(numero=numero)
        except OuvrageSection.DoesNotExist:
            raise Http404("No OuvrageSection matches the given query.")
        sections = list(section.ancestors(include_self=True)) + list(
            section.descendants()
        )
    return render(
        request,
        "carting/index.html",
        {
            "sections": sections,
            "search": search,
        },
    )
