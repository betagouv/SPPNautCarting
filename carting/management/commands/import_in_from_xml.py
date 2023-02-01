import xml.etree.ElementTree as ET

import requests
from django.conf import settings
from django.core.management.base import BaseCommand

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
        ouvrage = options["ouvrage"]

        response = generator.get(
            f"{settings.GENERATOR_SERVICE_HOST}/carting/{ouvrage}/"
        )
        print(response.text)
        document_xml = requests.get(response.text)
        content_document_xml = document_xml.content.decode("utf-16")
        print(content_document_xml)
        #        content_root = ET.fromstring(content_document_xml)
        #        print(content_root.tag)
        pass
