import requests
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
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
        elements = Element.objects.filter(xpath__startswith=search_field)
        return render(
            self.request,
            "display_in_with_map.html",
            {
                "elements": elements,
                "form": form,
            },
        )


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
