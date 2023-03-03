import textwrap
from uuid import uuid4
from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement

import pytest
from django.contrib.gis.geos import GEOSException, GEOSGeometry
from django.core.exceptions import ValidationError

from carting.models import OuvrageSection, SectionTypology


def foo(xml_string):
    return [
        stripped_line
        for line in xml_string.content_html.strip().splitlines()
        if (stripped_line := line.strip())
    ]


# FIXME: Transformer les Arrange en XML fromstring
# FIXME : tester ingestion de deux ouvrages différents. Mais tester quoi ?
# FIXME: assert_num_queries
# FIXME: Tester que si un bpn_id change de place dans le XML, il change de place dans la base ou alors on veut émettre un warning
# FIXME: Tester que si un bpn_id change de topologie, il change de topologie dans la base ou alors on veut émettre un warning
# FIXME: Test "integration" qui absorbe un XML plus représentatif et on vérifiera la hiérarchie retournée par .descendants(). Est-ce qu'on l'écrit au niveau de la commande ?
class TestIngestXMLSubtree:
    @pytest.mark.django_db(transaction=True)
    def test_basic_ouvrage(self):
        fake_bpn_id = uuid4()

        root = ElementTree.fromstring(
            f"""
                <root>
                    <ouvrage bpn_id="{fake_bpn_id}" />
                </root>
            """
        )

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

        root = ElementTree.fromstring(
            f"""
            <root>
                <{tagname} bpn_id="{fake_bpn_id}">
                    <titre>
                        <numero>12.</numero>
                    </titre>
                </{tagname}>
            </root>
        """
        )

        ingested = OuvrageSection.objects.ingest_xml_subtree("g4p", root)

        assert ingested == 1
        ouvrage_sections = OuvrageSection.objects.all()
        assert len(ouvrage_sections) == 1
        assert ouvrage_sections[0].bpn_id == fake_bpn_id
        assert ouvrage_sections[0].typology == typology
        assert ouvrage_sections[0].numero == "12."
        assert (
            textwrap.dedent(ouvrage_sections[0].content)
            == textwrap.dedent(
                """\
            <titre>
                <numero>12.</numero>
            </titre>
        """
            ).strip()
        )
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

        chapitre = SubElement(root, "chapitre", {"bpn_id": str(uuid4())})
        titre = SubElement(chapitre, "titre")

        numero = SubElement(titre, "numero")
        numero.text = "12."

        alinea = SubElement(chapitre, "alinea", {"bpn_id": str(fake_parent_bpn_id)})
        nmrAlinea = SubElement(alinea, "nmrAlinea")
        nmrAlinea.text = "42"

        texte = SubElement(alinea, "texte")
        section = SubElement(texte, tagname, {"bpn_id": str(fake_bpn_id)})

        ingested = OuvrageSection.objects.ingest_xml_subtree("g4p", root)

        assert ingested == 3
        _, alinea_section, section_section = OuvrageSection.objects.all()
        assert section_section.bpn_id == fake_bpn_id
        assert section_section.typology == typology
        assert section_section.numero == "12.0.42"
        assert section_section.content == ElementTree.tostring(section, "unicode")
        assert section_section.ouvrage_name == "g4p"
        assert section_section.geometry == None
        assert section_section.parent == alinea_section

    @pytest.mark.django_db()
    def test_chapter_without_numero_raises_exception(self):
        fake_bpn_id = uuid4()

        root = Element("root")
        section = SubElement(root, "chapitre", {"bpn_id": str(fake_bpn_id)})
        titre = SubElement(section, "titre")
        numero = SubElement(titre, "numero")

        with pytest.raises(ValidationError) as exception:
            OuvrageSection.objects.ingest_xml_subtree("g4p", root)
            # FIXME : vérifier l'erreur de type
            assert len(exception.value) == 1
            assert "numero" in exception.value

    @pytest.mark.django_db()
    def test_ingestion_preserves_geometry(self):
        fake_bpn_id = uuid4()
        OuvrageSection.objects.create(
            bpn_id=fake_bpn_id,
            geometry='{"type": "Point", "coordinates": [-2.04, 48.65]}',
        )

        root = Element("root")
        SubElement(root, "ouvrage", {"bpn_id": str(fake_bpn_id)})
        OuvrageSection.objects.ingest_xml_subtree("g4p", root)

        assert OuvrageSection.objects.get(bpn_id=fake_bpn_id).geometry


class TestGeometry:
    @pytest.mark.django_db()
    def test_geometry_basic(self):
        fake_bpn_id = uuid4()
        section_instance = OuvrageSection(
            bpn_id=fake_bpn_id,
            geometry='{"type": "Point", "coordinates": [-2.04, 48.65]}',
        )
        section_instance.save()
        assert (
            OuvrageSection.objects.get(bpn_id=fake_bpn_id).geojson()
            == '{"type": "FeatureCollection", "crs": {"type": "name", "properties": {"name": "EPSG:4326"}}, "features": [{"type": "Feature", "properties": {}, "geometry": {"type": "Point", "coordinates": [-2.04, 48.65]}}]}'
        )

    def test_unclosed_geometry(self):
        fake_bpn_id = uuid4()
        section_instance = OuvrageSection(
            bpn_id=fake_bpn_id,
            geometry='{"type": "Polygon", "coordinates": [[[-2.977, 48.9098333], [-2.9528333, 48.8383333], [-2.9656666, 48.8025]]] }',
        )

        with pytest.raises(GEOSException):
            section_instance.save()


# FIXME: À tester parce qu'on a trouvé que c'était un comportement de GeoDjango
# section_instance.geometry = None
# section_instance.save()
# assert OuvrageSection.objects.get(bpn_id=fake_bpn_id).geometry == None

# section_instance.geometry = ""
# section_instance.save()
# assert OuvrageSection.objects.get(bpn_id=fake_bpn_id).geometry == None


class TestContentHtml:
    def test_basic(self):
        section = OuvrageSection(content="")
        assert section.content_html == ""

    def test_xslt_basic(self):
        section = OuvrageSection(
            typology=SectionTypology.CHAPTER,
            content="""
                <titre tDate="2018-06-20" tMaj="edition">
                    <nmrAlinea>01</nmrAlinea>
                    <numero>0.2.1.</numero>
                    <texte>
                        <txt>Objet des Instructions Nautiques</txt>
                    </texte>
                </titre>
            """,
        )

        # assert foo(section.content_html) == [
        #     '<h2 class="fr-mt-2w">',
        #     '<span class="sppnaut-bold fr-pr-1w">0.2.1.</span>',
        #     "Objet des Instructions Nautiques",
        #     "</h2>",
        # ]

    def test_xslt_match(self):
        alinea = OuvrageSection(
            typology=SectionTypology.TABLE,
            content="""
                <tableau tDate="2018-06-20" tMaj="edition">
                    <numero>01</numero>
                </tableau>
            """,
        )

        titre = OuvrageSection(
            typology=SectionTypology.ILLUSTRATION,
            content="""
                <illustration tDate="2018-06-20" tMaj="edition">
                    <numero>01</numero>
                </illustration>
            """,
        )

        assert titre.content_html == alinea.content_html
