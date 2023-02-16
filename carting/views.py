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
        elements = INSection.objects.filter(numero__startswith=search).order_by(
            "numero"
        )

    return render(
        request,
        "carting/index.html",
        {
            "elements": elements,
            "search": search,
        },
    )
