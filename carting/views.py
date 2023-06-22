import json
from uuid import UUID

import requests
from django.contrib.gis import geos
from django.core.serializers import serialize
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_GET

from carting.models import OuvrageSection, SectionTypology
from s127.models import PilotageDistrict, PilotBoardingPlace

SAINT_MALO_BBOX = "-3.15, 47.32, -1.65, 49.14"


@require_GET
def pilotage_search(request: HttpRequest) -> HttpResponse:
    qs_bbox = request.GET.get("bbox", SAINT_MALO_BBOX)
    qs_bbox = [float(coordinate) for coordinate in qs_bbox.split(",")]
    bbox = geos.Polygon.from_bbox(qs_bbox)

    pilotage_districts = PilotageDistrict.objects.filter(geometry__bboverlaps=bbox)
    boarding_places = PilotBoardingPlace.objects.filter(
        pilotservice__pilotage_district__in=pilotage_districts
    )
    geojson = serialize(
        "geojson", (*pilotage_districts, *boarding_places), id_field="geojson_id"
    )

    return render(
        request,
        "carting/pilotage_search.html",
        {
            "scroll_snap": True,
            "geojson": geojson,
            "bbox": json.dumps(qs_bbox),
            "pilotage_districts": pilotage_districts,
        },
    )


@require_GET
def search_by_position(request: HttpRequest) -> HttpResponse:
    zoom_level = float(request.GET.get("zoom", 1))

    qs_bbox = request.GET.get("bbox", SAINT_MALO_BBOX)
    qs_bbox = [float(coordinate) for coordinate in qs_bbox.split(",")]
    bbox = geos.Polygon.from_bbox(qs_bbox)

    allowed_typologies = SectionTypology.paragraph_likes
    if zoom_level < 7:
        allowed_typologies = [SectionTypology.CHAPTER]

    sections = (
        OuvrageSection.objects.filter(geometry__bboverlaps=bbox)
        # FIXME : A geometry is not excluded by filter below 75f7dbbd-c0b4-456f-bc10-19f72f89608b
        .exclude(geometry__contains_properly=bbox).filter(
            typology__in=[x.name for x in allowed_typologies]
        )
    )

    geojson = serialize("geojson", (s for s in sections if s.geometry))

    return render(
        request,
        "carting/search_by_position.html",
        {
            "scroll_snap": True,
            "geojson": geojson,
            "bbox": json.dumps(qs_bbox),
            "zoom_level": zoom_level,
            "sections": sections,
        },
    )


@require_GET
def search_by_position_details(
    request: HttpRequest, root_expanded: UUID, expanded: UUID
) -> HttpResponse:
    zoom_level = float(request.GET.get("zoom", 1))

    qs_bbox = request.GET.get("bbox", SAINT_MALO_BBOX)
    qs_bbox = [float(coordinate) for coordinate in qs_bbox.split(",")]

    expanded_section = OuvrageSection.objects.prefetch_related("children").get(
        pk=expanded
    )

    to_serialize = [expanded_section, *expanded_section.children.all()]
    geojson = serialize("geojson", (s for s in to_serialize if s.geometry))

    return render(
        request,
        "carting/search_by_position.html",
        {
            "scroll_snap": True,
            "geojson": geojson,
            "bbox": json.dumps(qs_bbox),
            "zoom_level": zoom_level,
            "root_expanded": root_expanded,
            "expanded": expanded,
            "expanded_section": expanded_section,
        },
    )


# FIXME : Les sections commençant par '0.' ne devraient pas être affichées (pas de géométrie attachée); les illustrations en '0.' sont mal ordonnées
@require_GET
def search_by_text(request: HttpRequest) -> HttpResponse:
    search = request.GET.get("search", "")

    if not search:
        return redirect(reverse("carting:search_by_text") + "?search=4.1.")

    if not search.endswith("."):
        return redirect(reverse("carting:search_by_text") + f"?search={search}.")

    ouvrage, _, numero = search.rpartition("/")
    if not numero:
        return render(
            request,
            "carting/search_by_text.html",
        )
    allowed_typologies = SectionTypology.paragraph_likes.union(
        {SectionTypology.OUVRAGE}
    )
    sections = OuvrageSection.objects.filter(
        typology__in=[x.name for x in allowed_typologies]
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

    geojson = serialize("geojson", (s for s in sections if s.geometry))
    return render(
        request,
        "carting/search_by_text.html",
        {
            "sections": sections,
            "geojson": geojson,
            "search_tree_depth": section.tree_depth,
            "search": search,
        },
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
