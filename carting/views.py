from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render
from django.views.decorators.http import require_GET

from carting.models import INSection


@login_required
@require_GET
def index(request):
    elements = []
    search = ""

    if "search" in request.GET:
        search = request.GET["search"]
        ouvrage, _, numero = search.rpartition("/")
        elements = INSection.objects.filter(numero__startswith=numero).order_by(
            "numero"
        )

        if ouvrage:
            elements = elements.filter(ouvrage_name=ouvrage)

    return render(
        request,
        "carting/index.html",
        {
            "elements": elements,
            "search": search,
        },
    )
