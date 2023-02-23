from uuid import uuid4
from xml.etree import ElementTree
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

    @pytest.mark.parametrize(
        "tagname,typology",
        [
            ("chapitre", SectionTypology.CHAPTER),
            ("sChapitre", SectionTypology.SUBCHAPTER),
            ("para", SectionTypology.PARAGRAPH),
            ("sPara", SectionTypology.SUBPARAGRAPH),
            ("ssPara", SectionTypology.SUBSUBPARAGRAPH),
        ],
    )
    @pytest.mark.django_db(transaction=True)
    def test_paragraph_ingester(self, tagname, typology):
        fake_bpn_id = uuid4()

        root = Element("root")
        section = SubElement(root, tagname, {"bpn_id": str(fake_bpn_id)})
        titre = SubElement(section, "titre")
        numero = SubElement(titre, "numero")
        numero.text = "12."

        ingested = OuvrageSection.objects.ingest_xml_subtree("g4p", root)

        assert ingested == 1
        ouvrage_sections = OuvrageSection.objects.all()
        assert len(ouvrage_sections) == 1
        assert ouvrage_sections[0].bpn_id == fake_bpn_id
        assert ouvrage_sections[0].typology == typology
        assert ouvrage_sections[0].numero == "12."
        assert ouvrage_sections[0].content == ElementTree.tostring(titre, "unicode")
        assert ouvrage_sections[0].ouvrage_name == "g4p"
        assert ouvrage_sections[0].geometry == None

    @pytest.mark.django_db(transaction=True)
    def test_alinea_ingester(self):
        fake_parent_bpn_id = uuid4()
        fake_bpn_id = uuid4()

        root = Element("root")
        # FIXME: Doit on parametriser ?
        section = SubElement(root, "chapitre", {"bpn_id": str(fake_parent_bpn_id)})
        titre = SubElement(section, "titre")
        numero = SubElement(titre, "numero")
        numero.text = "12."

        alinea = SubElement(section, "alinea", {"bpn_id": str(fake_bpn_id)})
        nmrAlinea = SubElement(alinea, "nmrAlinea")
        nmrAlinea.text = "42"

        ingested = OuvrageSection.objects.ingest_xml_subtree("g4p", root)
        assert ingested == 2
        ouvrage_sections = OuvrageSection.objects.all()
        assert len(ouvrage_sections) == 2
        section_section, alinea_section = ouvrage_sections
        assert alinea_section.bpn_id == fake_bpn_id
        assert alinea_section.typology == SectionTypology.ALINEA
        assert alinea_section.numero == "12.0.42"
        assert alinea_section.content == ElementTree.tostring(alinea, "unicode")
        assert alinea_section.ouvrage_name == "g4p"
        assert alinea_section.parent == section_section
        assert alinea_section.geometry == None

    @pytest.mark.parametrize(
        "tagname,typology",
        [
            ("tableau", SectionTypology.TABLE),
            ("illustration", SectionTypology.ILLUSTRATION),
        ],
    )
    @pytest.mark.django_db(transaction=True)
    def test_figure_ingester(self, tagname, typology):
        fake_bpn_id = uuid4()

        root = Element("root")
        section = SubElement(root, tagname, {"bpn_id": str(fake_bpn_id)})
        numero = SubElement(section, "numero")
        numero.text = "12."

        ingested = OuvrageSection.objects.ingest_xml_subtree("g4p", root)

        assert ingested == 1
        ouvrage_sections = OuvrageSection.objects.all()
        assert len(ouvrage_sections) == 1
        assert ouvrage_sections[0].bpn_id == fake_bpn_id
        assert ouvrage_sections[0].typology == typology
        assert ouvrage_sections[0].numero == "12."
        assert ouvrage_sections[0].content == ElementTree.tostring(section, "unicode")
        assert ouvrage_sections[0].ouvrage_name == "g4p"
        assert ouvrage_sections[0].geometry == None

    @pytest.mark.parametrize(
        "tagname,typology",
        [
            ("principal", SectionTypology.TOPONYME),
            ("reference", SectionTypology.REFERENCE),
        ],
    )
    @pytest.mark.django_db(transaction=True)
    def test_section_ingester(self, tagname, typology):
        fake_parent_bpn_id = uuid4()
        fake_bpn_id = uuid4()

        root = Element("root")

        alinea = SubElement(root, "alinea", {"bpn_id": str(fake_parent_bpn_id)})
        nmrAlinea = SubElement(alinea, "nmrAlinea")
        nmrAlinea.text = "42"

        texte = SubElement(alinea, "texte")
        section = SubElement(texte, tagname, {"bpn_id": str(fake_bpn_id)})
        numero = SubElement(section, "numero")
        numero.text = "12."

        ingested = OuvrageSection.objects.ingest_xml_subtree("g4p", root)

        assert ingested == 1
        ouvrage_sections = OuvrageSection.objects.all()
        assert len(ouvrage_sections) == 1
        assert ouvrage_sections[0].bpn_id == fake_bpn_id
        assert ouvrage_sections[0].typology == typology
        assert ouvrage_sections[0].numero == "12."
        assert ouvrage_sections[0].content == ElementTree.tostring(section, "unicode")
        assert ouvrage_sections[0].ouvrage_name == "g4p"
        assert ouvrage_sections[0].geometry == None


# FIXME: Veut-on tester les contraintes Django?
# django.core.exceptions.ValidationError: {'numero': ['Ce champ ne peut pas contenir la valeur nulle.']}
