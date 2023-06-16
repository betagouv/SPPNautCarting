from xml.etree import ElementTree
from pathlib import Path

import requests
from django.conf import settings
from django.core.management.base import BaseCommand

from carting.models import OuvrageSection


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "ouvrage",
            help="Ouvrage xml file, ex = ./12.xml, ./c22.xml, ./l1.xml",
        )

    def handle(self, *args, **options):
        ouvrage_location = options.get("ouvrage")

        document_path = Path(str(ouvrage_location))
        content_root = ElementTree.parse(document_path)
        # FIXME: Valider bpn_id uniques
        ingested = OuvrageSection.objects.ingest_xml_subtree(
            document_path.name, content_root
        )
        self.stdout.write(self.style.SUCCESS(f"✨ {ingested} sections ingérées"))
