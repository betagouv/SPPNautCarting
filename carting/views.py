import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.views.decorators.http import require_GET
from django.views.generic import FormView

from carting.forms import XPathSearchForm
from carting.models import Element
from core import generator


@login_required
@require_GET
def display_in_with_map(request):
    elements = []
    search = ""

    if "search" in request.GET:
        search = request.GET["search"]
        elements = Element.objects.filter(
            Q(xpath__icontains=search) | Q(numero__startswith=search)
        ).order_by("numero", "xpath")

    for element in elements:
        element.content_html = mark_safe(diplay_xml_as_text(element.content))

    return render(
        request,
        "display_in_with_map.html",
        {
            "elements": elements,
            "search": search,
        },
    )


def diplay_xml_as_text(content):
    import lxml.etree as ET

    if not content:
        return ""

    content_root = ET.fromstring(content)
    content_xslt = ET.parse("carting/document.xslt")
    transform = ET.XSLT(content_xslt)
    transform_content = transform(content_root)
    return transform_content


# Create your views here.
def display_document_xml(request, ouvrage):

    response = generator.get(f"{settings.GENERATOR_SERVICE_HOST}/carting/{ouvrage}/")
    document_xml = requests.get(response.text)
    content_document_xml = document_xml.content
    import lxml.etree as ET

    content_root = ET.fromstring(content_document_xml)
    content_xslt = ET.parse("carting/document.xslt")
    transform = ET.XSLT(content_xslt)

    paragraphe = None
    for spara in content_root.iter("sPara"):
        if spara.find("titre").find("numero").text == "4.1.1.1.":
            paragraphe = spara

    transform_spara = transform(paragraphe)

    return render(
        request,
        "display_document_xml.html",
        {
            "presigned_url": response.text,
            "document_xml": ET.tounicode(transform_spara, pretty_print=True),
        },
    )
