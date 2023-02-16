import logging
from xml.etree import ElementTree

import requests
from django.conf import settings
from django.core.management.base import BaseCommand

from carting.models import INSection, SectionTypology
from core import generator

count = 0


def create_children(parent_in_section, parent_element):
    for typology in SectionTypology:
        for element in parent_element.iterfind(typology.label):
            in_section = INSection.from_xml(
                element,
                parent_in_section,
                typology,
            )
            # FIXME : check if in_section is new or has been updated
            global count
            count += 1
            in_section.save()
            create_children(in_section, element)


class Command(BaseCommand):
    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            "--ouvrage",
            required=True,
            help="Ouvrage name, ex = 12, c22, l1",
        )

    def handle(self, *args, **options):

        ouvrage_name = options.get("ouvrage")
        response = generator.get(
            f"{settings.GENERATOR_SERVICE_HOST}/url-for/{ouvrage_name}/xml/document.xml"
        )
        document_xml = requests.get(response.text)
        content_root = ElementTree.fromstring(document_xml.text)

        typology = SectionTypology.OUVRAGE
        ouvrage_element = content_root.find(typology.label)
        bpn_id = ouvrage_element.attrib["bpn_id"]
        ouvrage = INSection(
            bpn_id=bpn_id,
            numero=ouvrage_name,
            typology=typology,
            ouvrage_name=ouvrage_name,
        )
        ouvrage.save()
        create_children(ouvrage, ouvrage_element)
        logging.warning(count)
        # todo : Compteur du nombre d'éléments créés / mis à jour
