import uuid
import xml.etree.ElementTree as ET
from pathlib import Path

import requests
from django.conf import settings
from django.core.management.base import BaseCommand

from carting.models import SectionTypology
from core import generator


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--ouvrage",
            required=True,
            help="Ouvrage name, ex = 12, c22, l1",
        )

    def handle(self, *args, **options):

        ouvrage_name = options["ouvrage"]
        response = generator.get(
            f"{settings.GENERATOR_SERVICE_HOST}/url-for/{ouvrage_name}/xml/document.xml"
        )
        document_xml = requests.get(response.text)

        content_root = ET.fromstring(document_xml.text)

        for topology in SectionTypology:
            for element in content_root.iter(topology.label):
                element.set("bpn_id", str(uuid.uuid4()))

        Path(f"{ouvrage_name}.xml").write_text(
            ET.tostring(content_root, encoding="unicode")
        )
