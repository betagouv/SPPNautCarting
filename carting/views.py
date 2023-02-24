from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET

from carting.models import OuvrageSection


# FIXME : Les sections commençant par '0.' ne devraient pas être affichées (pas de géométrie attachée); les illustrations en '0.' sont mal ordonnées
@login_required
@require_GET
def index(request: HttpRequest) -> HttpResponse:
    search = request.GET.get("search", "")

    ouvrage, _, numero = search.rpartition("/")
    if not numero:
        return render(
            request,
            "carting/index.html",
        )

    sections = OuvrageSection.objects.all().with_tree_fields()
    if ouvrage:
        sections = sections.filter(ouvrage_name=ouvrage)
    try:
        # FIXME: 4.2. get() returned more than one OuvrageSection -- it returned 2!
        section = sections.get(numero=numero)
    except OuvrageSection.DoesNotExist:
        raise Http404(
            "Probably we won't fix it : No OuvrageSection matches the given query."
        )
    except OuvrageSection.MultipleObjectsReturned:
        raise Http404(
            "Probably we won't fix it : Multiple OuvrageSections match the given query."
        )
    sections = list(section.ancestors()) + list(section.descendants(include_self=True))

    return render(
        request,
        "carting/index.html",
        {
            "sections": sections,
            "search_tree_depth": section.tree_depth,
            "search": search,
        },
    )
