import uuid
import xml.etree.ElementTree as ET

import requests
from django.conf import settings
from django.core.management.base import BaseCommand

from carting.models import Element, ElementTypology
from core import generator

# from django.db.utils import IntegrityError


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

        for topology in ElementTypology:
            for element in content_root.iter(topology.label):
                element.set("bpn_id", str(uuid.uuid4()))

        open(f"{ouvrage_name}.xml", "w").write(
            ET.tostring(content_root, encoding="unicode")
        )
