import logging
import xml.etree.ElementTree as ET

import requests
from django.conf import settings
from django.core.management.base import BaseCommand

from carting.models import Element, ElementTypology
from core import generator

# from django.db.utils import IntegrityError


class INElement:
    element: ET.Element
    xpath: str

    def __init__(
        self,
        element: ET.Element,
        *,
        typology: ElementTypology,
        xpath_prefix: str | None = None,
        ouvrage_name: str,
    ):
        self.element = element
        self.typology = typology
        self.xpath = f"{xpath_prefix}/" if xpath_prefix else ""
        self.xpath += self.typology.label
        self.xpath += f"[@bpn_id='{self.bpn_id}']" if self.bpn_id else ""
        self.ouvrage_name = ouvrage_name

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
        if self.bpn_id:
            # try:
            (_, created) = Element.objects.update_or_create(
                bpn_id=self.bpn_id,
                typology=self.typology,
                ouvrage_name=self.ouvrage_name,
                defaults={
                    "content": self.get_content(),
                    "xpath": self.xpath,
                },
            )
            logging.warning(
                "Element %s %s avec l'id %s",
                self.typology.label,
                ("créé" if created else "mis à jour"),
                self.bpn_id,
            )
        # except IntegrityError:
        #     logging.error("Element avec bpn_id %s existe déjà", self.bpn_id)

    def create_children(self):
        for typology in ElementTypology:
            for element in self.element.findall(typology.label):
                in_element = INElement(
                    element,
                    typology=typology,
                    xpath_prefix=self.xpath,
                    ouvrage_name=self.ouvrage_name,
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
            ouvrage_name=ouvrage_name,
        )
        ouvrage.update_or_create()
        ouvrage.create_children()
        # todo : Compteur du nombre d'éléments créés / mis à jour
