from uuid import uuid4
from xml.etree.ElementTree import Element, SubElement

import pytest

from carting.models import OuvrageSection, SectionTypology


class TestIngestXMLSubtree:
    @pytest.mark.django_db(transaction=True)
    def test_basic_ouvrage(self):
        fake_bpn_id = uuid4()

        root = Element("root")
        SubElement(root, "ouvrage", {"bpn_id": str(fake_bpn_id)})

        ingested = OuvrageSection.objects.ingest_xml_subtree("g4p", root)

        assert ingested == 1
        ouvrage_sections = OuvrageSection.objects.all()
        assert len(ouvrage_sections) == 1
        assert ouvrage_sections[0].bpn_id == fake_bpn_id
        assert ouvrage_sections[0].typology == SectionTypology.OUVRAGE
        assert ouvrage_sections[0].numero == "g4p"
        assert ouvrage_sections[0].content == ""
        assert ouvrage_sections[0].ouvrage_name == "g4p"
        assert ouvrage_sections[0].geometry == None

    # FIXME Parametrize tagname
    @pytest.mark.django_db(transaction=True)
    def test_basic_paragraph(self):
        fake_bpn_id = uuid4()

        root = Element("root")
        SubElement(root, "chapter", {"bpn_id": str(fake_bpn_id)})

        ingested = OuvrageSection.objects.ingest_xml_subtree("g4p", root)

        assert ingested == 1
        ouvrage_sections = OuvrageSection.objects.all()
        assert len(ouvrage_sections) == 1
        assert ouvrage_sections[0].bpn_id == fake_bpn_id
        assert ouvrage_sections[0].typology == SectionTypology.OUVRAGE
        assert ouvrage_sections[0].numero == "g4p"
        assert ouvrage_sections[0].content == ""
        assert ouvrage_sections[0].ouvrage_name == "g4p"
        assert ouvrage_sections[0].geometry == None
