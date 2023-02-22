from xml.etree import ElementTree

import requests
from django.conf import settings
from django.core.management.base import BaseCommand

from carting.models import OuvrageSection
from home import generator


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "ouvrage",
            help="Ouvrage name, ex = 12, c22, l1",
        )

    def handle(self, *args, **options):
        ouvrage_name = options.get("ouvrage")
        response = generator.get(
            f"{settings.GENERATOR_SERVICE_HOST}/url-for/{ouvrage_name}/xml/document.xml"
        )
        document_xml = requests.get(response.text)
        content_root = ElementTree.fromstring(document_xml.text)
        # FIXME: Valider bpn_id uniques
        ingested = OuvrageSection.objects.ingest_xml_subtree(ouvrage_name, content_root)
        self.stdout.write(self.style.SUCCESS(f"✨ {ingested} sections ingérées"))
