import logging
from xml.etree import ElementTree

import requests
from django.conf import settings
from django.core.management.base import BaseCommand

from carting.models import INSection, SectionTypology
from core import generator


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
        INSection.objects.create_children(ouvrage, ouvrage_element)
        # todo : Compteur du nombre d'éléments créés / mis à jour
