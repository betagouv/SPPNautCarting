import requests
from django.conf import settings
from django.shortcuts import render

from core import generator


# Create your views here.
def display_document_xml(request, ouvrage):

    response = generator.get(f"{settings.GENERATOR_SERVICE_HOST}/carting/{ouvrage}/")
    document_xml = requests.get(response.text)
    content_document_xml = document_xml.content
    import lxml.etree as ET

    content_root = ET.fromstring(content_document_xml)
    content_xslt = ET.parse("home/document.xslt")
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
