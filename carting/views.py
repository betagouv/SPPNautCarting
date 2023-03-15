from django.core import serializers
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_GET

from carting.models import OuvrageSection, SectionTypology


# FIXME : Les sections commençant par '0.' ne devraient pas être affichées (pas de géométrie attachée); les illustrations en '0.' sont mal ordonnées
@require_GET
def index(request: HttpRequest) -> HttpResponse:
    search = request.GET.get("search", "")

    if not search:
        return redirect(reverse("carting:index") + "?search=4.1.")

    if not search.endswith("."):
        return redirect(reverse("carting:index") + f"?search={search}.")

    ouvrage, _, numero = search.rpartition("/")
    if not numero:
        return render(
            request,
            "carting/index.html",
        )

    sections = OuvrageSection.objects.exclude(
        typology__in=[
            SectionTypology.ALINEA.name,
            SectionTypology.ILLUSTRATION.name,
            SectionTypology.REFERENCE.name,
            SectionTypology.TABLE.name,
            SectionTypology.TOPONYME.name,
        ]
    ).with_tree_fields()
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
    sections = [*section.ancestors(), *section.descendants(include_self=True)]

    GeoJSONSerializer = serializers.get_serializer("geojson")

    # https://stackoverflow.com/questions/34556679/geodjango-serialize-geojson-skipping-id-field
    class Serializer(GeoJSONSerializer):
        def get_dump_object(self, obj):
            data = super(Serializer, self).get_dump_object(obj)
            data.update(id=obj.pk)
            return data

    geojson = Serializer().serialize(s for s in sections if s.geometry)

    return render(
        request,
        "carting/index.html",
        {
            "sections": sections,
            "geojson": geojson,
            "search_tree_depth": section.tree_depth,
            "search": search,
        },
    )
