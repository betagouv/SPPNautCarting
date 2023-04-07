import re

import requests
from django.core import serializers
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.urls import reverse
from django.views.decorators.http import require_GET
from xsdata.formats.dataclass.parsers import XmlParser

from carting.models import OuvrageSection, S1xyObject, SectionTypology
from carting.s127_models import Dataset


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

    parser = XmlParser()
    # s1xyobjects = S1xyObject.objects.filter(geometry__isnull=False)
    s1xyobjects = S1xyObject.objects.filter(typology="S127:PilotageDistrict")

    s1xyobjects_renderized = []
    for s1xyobject in s1xyobjects:
        dataset = parser.from_string(s1xyobject.content, Dataset)
        pilotage_district = dataset.member[0].pilotage_district
        s1xyobjects_renderized.append(
            {"s1xyobject": s1xyobject, "render": render_to_string(pilotage_district)}
        )

    return render(
        request,
        "carting/index.html",
        {
            "sections": sections,
            "s1xyobjects": s1xyobjects_renderized,
            "geojson": geojson,
            "search_tree_depth": section.tree_depth,
            "search": search,
        },
    )


def camel_to_snake(name):
    name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", name).lower()


def render_to_string(s1xyobject):
    return loader.render_to_string(
        camel_to_snake(s1xyobject.__class__.__name__) + ".html", {"self": s1xyobject}
    )


# Needed until https://github.com/betagouv/SPPNautInterface/issues/185 is closed
@require_GET
def wms_proxy(request, wms_url):
    response = requests.get(url=wms_url, params=request.GET.dict())
    http_response = HttpResponse(response)
    headers_to_forward = ["Content-Type", "Content-Length"]
    for header in headers_to_forward:
        if header in response.headers:
            http_response.headers[header] = response.headers[header]
    return http_response
