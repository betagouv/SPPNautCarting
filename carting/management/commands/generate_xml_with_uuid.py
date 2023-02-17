import uuid
import xml.etree.ElementTree as ET
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

from carting.models import SectionTypology
from core import generator


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "filepath",
            type=str,
            help="filepath to document.xml file",
        )

    def handle(self, *args, **options):
        filepath = options.get("filepath")

        xml_file = Path(str(filepath))
        content_root = ET.parse(xml_file, parser=ET.XMLParser(encoding="UTF-16"))

        for topology in SectionTypology.labels:
            topology = topology.split("/")[-1]
            for element in content_root.iter(topology):
                element.set("bpn_id", str(uuid.uuid4()))

        for element in content_root.iter("principal"):
            element.set("bpn_id", str(uuid.uuid4()))

        Path(xml_file.name).write_text(
            ET.tostring(content_root.getroot(), encoding="unicode"),
            encoding="UTF-16",
        )
