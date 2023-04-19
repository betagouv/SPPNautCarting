import lxml
import pytest
from django.contrib.gis.geos import Point
from lxml import etree

from carting.models import S1xyObject


class TestS1xyObjectIngestFromXML:
    @pytest.fixture(params=["member", "imember"])
    def xml_member(self, request):
        return f"""
<Dataset xmlns:gml="http://www.opengis.net/gml/3.2">
    <{request.param}>
        <XMLTag gml:id="GML.ID" />
    </{request.param}>
</Dataset>
"""

    @pytest.mark.django_db()
    def test_ingest_basic_imember(self, xml_member):
        s1xy_object = S1xyObject.inject_from_xml_str(xml_member)

        assert s1xy_object.typology == "XMLTag"
        assert s1xy_object.id == "GML.ID"
        assert s1xy_object.geometry is None
        assert s1xy_object.content == etree.tostring(
            etree.fromstring(xml_member),
            method="xml",
            encoding="unicode",
            pretty_print=True,
        )

    @pytest.mark.django_db()
    def test_ingest_xml_missing_main_namespace(self):
        xml_block = """
<Dataset xmlns:gml="http://www.opengis.net/gml/3.2">
    <imember>
        <S127:XMLTag gml:id="GML.ID" />
    </imember>
</Dataset>
        """

        with pytest.raises(lxml.etree.XMLSyntaxError):
            S1xyObject.inject_from_xml_str(xml_block)

    @pytest.mark.django_db()
    def test_ingest_xml_missing_gml_namespace(self):
        xml_block = """
<Dataset>
    <imember>
        <XMLTag gml:id="GML.ID" />
    </imember>
</Dataset>
        """

        with pytest.raises(lxml.etree.XMLSyntaxError):
            S1xyObject.inject_from_xml_str(xml_block)

    @pytest.mark.django_db()
    def test_ingest_with_xlinks(self):
        xml_block = """
<Dataset
    xmlns:gml="http://www.opengis.net/gml/3.2"
    xmlns:xlink="http://www.w3.org/1999/xlink"
>
    <imember>
        <XMLTag gml:id="GML.ID">
            <linkedObject xlink:href="#XLINK.ID1"/>
            <linkedObject xlink:href="#XLINK.ID2"/>
        </XMLTag>
    </imember>
</Dataset>
"""

        s1xy_object = S1xyObject.inject_from_xml_str(xml_block)

        assert s1xy_object.typology == "XMLTag"
        assert s1xy_object.id == "GML.ID"
        assert s1xy_object.geometry is None
        assert s1xy_object.content == etree.tostring(
            etree.fromstring(xml_block),
            method="xml",
            encoding="unicode",
            pretty_print=True,
        )
        assert s1xy_object.link_to.count() == 2
        for linked_object in s1xy_object.link_to.all():
            assert linked_object.id in ("XLINK.ID1", "XLINK.ID2")
            assert linked_object.geometry is None
            assert linked_object.content == ""

    @pytest.mark.django_db()
    def test_ingest_member_with_geometry(self):
        xml_block = """
<Dataset
    xmlns:gml="http://www.opengis.net/gml/3.2"
    xmlns:xlink="http://www.w3.org/1999/xlink"
    xmlns:S100="http://www.iho.int/s100gml/1.0"
>
    <imember>
        <XMLTag gml:id="GML.ID">
            <geometry>
                <S100:pointProperty>
                    <S100:Point gml:id="GML.POINT" srsDimension="2" srsName="urn:ogc:def:crs:EPSG::4326">
                        <gml:pos>-2.2 48.48</gml:pos>
                    </S100:Point>
                </S100:pointProperty>
            </geometry>
        </XMLTag>
    </imember>
</Dataset>
"""

        s1xy_object = S1xyObject.inject_from_xml_str(xml_block)

        assert s1xy_object.typology == "XMLTag"
        assert s1xy_object.id == "GML.ID"
        assert s1xy_object.geometry is not None
        assert s1xy_object.content == etree.tostring(
            etree.fromstring(xml_block),
            method="xml",
            encoding="unicode",
            pretty_print=True,
        )
        assert s1xy_object.geometry == Point(-2.2, 48.48, srid=4326)

    @pytest.mark.django_db()
    def test_ingest_incremental(self):
        xml_block = """
<Dataset
    xmlns:gml="http://www.opengis.net/gml/3.2"
    xmlns:xlink="http://www.w3.org/1999/xlink"
>
    <imember>
        <XMLTag gml:id="GML.ID.1">
            <linkedObject xlink:href="#GML.ID.2"/>
        </XMLTag>
    </imember>
</Dataset>
"""

        s1xy_object = S1xyObject.inject_from_xml_str(xml_block)

        assert s1xy_object.id == "GML.ID.1"
        linked_object = S1xyObject.objects.get(id="GML.ID.2")
        assert linked_object.geometry is None
        assert linked_object.content == ""

        xml_block2 = """
<Dataset
    xmlns:gml="http://www.opengis.net/gml/3.2"
    xmlns:xlink="http://www.w3.org/1999/xlink"
    xmlns:S100="http://www.iho.int/s100gml/1.0"
>
    <imember>
        <XMLTag2 gml:id="GML.ID.2">
            <geometry>
                <S100:pointProperty>
                    <S100:Point gml:id="GML.POINT" srsDimension="2" srsName="urn:ogc:def:crs:EPSG::4326">
                        <gml:pos>-2.2 48.48</gml:pos>
                    </S100:Point>
                </S100:pointProperty>
            </geometry>
        </XMLTag2>
    </imember>
</Dataset>
"""

        S1xyObject.inject_from_xml_str(xml_block2)

        second_object = S1xyObject.objects.get(id="GML.ID.2")
        assert second_object.geometry == Point(-2.2, 48.48, srid=4326)
        assert second_object.content == etree.tostring(
            etree.fromstring(xml_block2),
            method="xml",
            encoding="unicode",
            pretty_print=True,
        )
