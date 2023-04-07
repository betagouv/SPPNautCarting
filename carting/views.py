import requests
from django.core import serializers
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_GET

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

    # S1xyObject information display
    from io import BytesIO, StringIO

    from lxml import etree

    # s1xyobjects = S1xyObject.objects.filter(geometry__isnull=False)
    s1xyobjects = S1xyObject.objects.filter(typology="S127:PilotageDistrict")
    for s1xyobject in s1xyobjects:
        from xsdata.formats.dataclass.parsers import XmlParser

        parser = XmlParser()
        dataset = parser.from_string(s1xyobject.content, Dataset)
        print(dataset.member[0].pilotage_district.feature_name[1].name)

        # linked_objects = {x.id: x for x in s1xyobject.link_to.all()}
        # content = "Typology : " + s1xyobject.typology + "<br/>"
        # content += "Id : " + s1xyobject.id + "<br/>"

        # root = etree.XML(s1xyobject.content)
        # root_element = root.xpath(
        #     './/*[local-name()="' + s1xyobject.typology.split(":")[1] + '"]'
        # )

        # for element in root_element[0]:
        #     href = element.get("{http://www.w3.org/1999/xlink}href")
        #     if href is not None:
        #         linked_id = href.replace("#", "")
        #         try:
        #             linked_object = linked_objects[linked_id]
        #         except KeyError:
        #             linked_object = None
        #         if linked_object is not None:
        #             content += (
        #                 linked_object.typology
        #                 + " : <a href='#"
        #                 + linked_object.id
        #                 + "'>"
        #                 + linked_object.id
        #                 + "</a><br/>"
        #             )
        #     elif element.tag != "geometry":
        #         # Il doit forcement y avoir moins degolasse à faire
        #         for event, elmt in etree.iterparse(
        #             BytesIO(etree.tostring(element)),
        #             events=("start", "end"),
        #         ):
        #             if event == "start":
        #                 content += "<ul>"
        #                 content += "<li>" + etree.QName(elmt).localname
        #                 if elmt.text.isspace():
        #                     content += "</li>"
        #                 else:
        #                     content += " : " + elmt.text + "</li>"
        #             else:
        #                 content += "</ul>"

        # s1xyobject.content = content

    return render(
        request,
        "carting/index.html",
        {
            "sections": sections,
            "s1xyobjects": s1xyobjects,
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
