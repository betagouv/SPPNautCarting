import xml.etree.ElementTree as ET

import requests
from django.conf import settings
from django.core.management.base import BaseCommand

from core import generator


class INElement:
    element: ET.Element

    def __init__(self, element):
        self.element = element

    def get_bpn_id(self):
        return (
            self.element.attrib["bpn_id"]
            if "bpn_id" in self.element.attrib
            else "not found"
        )

    def get_content(self):
        return ET.fromstring(self.element)


class INChapterElement(INElement):
    def get_content(self):
        titre = self.element.find("titre")
        return ET.tostring(titre, encoding="unicode", method="xml")


class Command(BaseCommand):
    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            "--ouvrage",
            required=True,
            help="Ouvrage name, ex = 12, c22, l1",
        )

    def handle(self, *args, **options):
        def get_bpn_id(element):
            return (
                element.attrib["bpn_id"] if "bpn_id" in element.attrib else "not found"
            )

        ouvrage = options["ouvrage"]
        response = generator.get(
            f"{settings.GENERATOR_SERVICE_HOST}/carting/{ouvrage}/"
        )
        document_xml = requests.get(response.text)
        content_document_xml = document_xml.text  # .content.decode("utf-8")
        content_root = ET.fromstring(content_document_xml)
        ouvrage = content_root.find("ouvrage")
        for chapter in [
            INChapterElement(chapter) for chapter in ouvrage.iter("chapitre")
        ]:

            print(f"Chapter {chapter.get_bpn_id()}")
            print(chapter.get_content())
            for chapter_alinea in chapter.element.findall("alinea"):
                print(f"Alinea {get_bpn_id(chapter_alinea)}")
            for sub_chapter in chapter.element.iter("sChapitre"):
                print(f"SubChapter {get_bpn_id(sub_chapter)}")
