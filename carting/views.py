import requests
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.views.generic import FormView

from carting.forms import XPathSearchForm
from carting.models import Element
from core import generator


def display_in_with_map(request):

    return render(
        request,
        "display_in_with_map.html",
    )


class DisplayINWithMap(LoginRequiredMixin, FormView):
    form_class = XPathSearchForm
    template_name = "display_in_with_map.html"
    # success_url = reverse_lazy("display_in_with_map")

    def form_valid(self, form):
        search_field = form.cleaned_data["search_field"]
        elements = Element.objects.filter(xpath__icontains=search_field).order_by(
            "numero"
        )
        for element in elements:
            element.content_html = mark_safe(diplay_xml_as_text(element.content))

        return render(
            self.request,
            "display_in_with_map.html",
            {
                "elements": elements,
                "form": form,
            },
        )


def diplay_xml_as_text(content):
    import lxml.etree as ET

    content_root = ET.fromstring(content.encode("utf-16"))
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
