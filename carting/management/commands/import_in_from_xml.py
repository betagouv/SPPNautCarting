import logging
import xml.etree.ElementTree as ET

import requests
from django.conf import settings
from django.core.management.base import BaseCommand

from carting.models import Element, ElementTypology
from core import generator


class INElement:
    element: ET.Element
    xpath: str

    def __init__(
        self,
        element,
        typology: ElementTypology,
        xpath_prefix="/document",
    ):
        self.element = element
        self.typology = typology
        self.xpath = f"{xpath_prefix}/{self.typology.label}[@bpn_id={self.bpn_id}]"

    @property
    def bpn_id(self):
        return self.element.attrib["bpn_id"] if "bpn_id" in self.element.attrib else ""

    def get_content(self):
        if self.typology == ElementTypology.OUVRAGE:
            return ""
        if self.typology in [
            ElementTypology.CHAPTER,
            ElementTypology.SUBCHAPTER,
            ElementTypology.PARAGRAPH,
            ElementTypology.SUBPARAGRAPH,
            ElementTypology.SUBSUBPARAGRAPH,
        ]:
            titre = self.element.find("titre")
            return ET.tostring(titre, encoding="unicode", method="xml")
        return ET.tostring(self.element, encoding="unicode", method="xml")

    def iter(self, tag):
        return self.element.iter(tag)

    def update_or_create(
        self,
    ):
        Element.objects.update_or_create(
            bpn_id=self.bpn_id,
            typology=self.typology,
            defaults={
                "content": self.get_content(),
                "xpath": self.xpath,
            },
        )
        logging.warning(
            "Element %s créé avec l'id %s", self.typology.label, self.bpn_id
        )

    def create_children(self):
        for typology in ElementTypology:
            for element in self.element.findall(typology.label):
                in_element = INElement(
                    element, typology=typology, xpath_prefix=self.xpath
                )
                in_element.update_or_create()
                in_element.create_children()


class Command(BaseCommand):
    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            "--ouvrage",
            required=True,
            help="Ouvrage name, ex = 12, c22, l1",
        )

    def handle(self, *args, **options):

        ouvrage_name = options["ouvrage"]
        response = generator.get(
            f"{settings.GENERATOR_SERVICE_HOST}/carting/{ouvrage_name}/"
        )
        document_xml = requests.get(response.text)
        content_document_xml = document_xml.text  # .content.decode("utf-8")

        content_root = ET.fromstring(content_document_xml)
        ouvrage = INElement(
            content_root.find(ElementTypology.OUVRAGE.label),
            typology=ElementTypology.OUVRAGE,
            xpath_prefix="/document",
        )
        ouvrage.update_or_create()
        ouvrage.create_children()
        # todo : Compteur du nombre d'éléments créés / mis à jour
