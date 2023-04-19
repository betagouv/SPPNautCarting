from unittest.mock import patch

import pytest
from lxml import etree

from carting.models import S1xyObject


class TestS1xyObjectManagerIngestFromXML:
    @pytest.fixture(params=["member", "imember"])
    def tmp_xml_file(self, request, tmp_path):
        with open(tmp_path / "test.xml", "w") as f:
            f.write(
                f"""
<Dataset xmlns:gml="http://www.opengis.net/gml/3.2">
    <{request.param}>
        <XMLTag gml:id="GML.ID" />
    </{request.param}>
</Dataset>
"""
            )
        return tmp_path / "test.xml"

    @pytest.mark.django_db()
    def test_ingest_basic_i_member(self, tmp_xml_file):
        S1xyObject.objects.inject_from_xml_file(tmp_xml_file)

        s1xy_object = S1xyObject.objects.get(id="GML.ID")
        assert s1xy_object.typology == "XMLTag"
        assert s1xy_object.geometry is None
        assert s1xy_object.content == etree.tostring(
            etree.parse(tmp_xml_file),
            method="xml",
            encoding="unicode",
            pretty_print=True,
        )

    @pytest.mark.django_db()
    def test_ingest_linked_object(self, tmp_path):
        with open(tmp_path / "test.xml", "w") as f:
            f.write(
                f"""
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
    <member>
        <XMLTag1 gml:id="XLINK.ID1" />
    </member>
    <member>
        <XMLTag2 gml:id="XLINK.ID2" />
    </member>
</Dataset>
"""
            )
        S1xyObject.objects.inject_from_xml_file(tmp_path / "test.xml")

        xml_tag_0_xml_expected = """
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
        s1xy_object = S1xyObject.objects.get(id="GML.ID")
        assert s1xy_object.typology == "XMLTag"
        assert s1xy_object.geometry is None
        assert s1xy_object.content == etree.tostring(
            etree.fromstring(xml_tag_0_xml_expected),
            method="xml",
            encoding="unicode",
            pretty_print=True,
        )

        xml_tag_1_xml_expected = """
<Dataset
    xmlns:gml="http://www.opengis.net/gml/3.2"
    xmlns:xlink="http://www.w3.org/1999/xlink"
>
    <member>
        <XMLTag1 gml:id="XLINK.ID1" />
    </member>
    </Dataset>
"""
        s1xy_object = S1xyObject.objects.get(id="XLINK.ID1")
        assert s1xy_object.typology == "XMLTag1"
        assert s1xy_object.geometry is None
        assert s1xy_object.content == etree.tostring(
            etree.fromstring(xml_tag_1_xml_expected),
            method="xml",
            encoding="unicode",
            pretty_print=True,
        )

        xml_tag_2_xml_expected = """
<Dataset
    xmlns:gml="http://www.opengis.net/gml/3.2"
    xmlns:xlink="http://www.w3.org/1999/xlink"
>
    <member>
        <XMLTag2 gml:id="XLINK.ID2" />
    </member>
</Dataset>
"""
        s1xy_object = S1xyObject.objects.get(id="XLINK.ID2")
        assert s1xy_object.typology == "XMLTag2"
        assert s1xy_object.geometry is None
        assert s1xy_object.content == etree.tostring(
            etree.fromstring(xml_tag_2_xml_expected),
            method="xml",
            encoding="unicode",
            pretty_print=True,
        )

    @pytest.mark.django_db()
    def test_ingest_linked_object2(self, tmp_path):
        with open(tmp_path / "test.xml", "w") as f:
            f.write(
                f"""
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
    <member>
        <XMLTag1 gml:id="XLINK.ID1" />
    </member>
    <member>
        <XMLTag2 gml:id="XLINK.ID2" />
    </member>
</Dataset>
"""
            )
        with patch("carting.models.S1xyObject.inject_from_xml") as mock:
            S1xyObject.objects.inject_from_xml_file(tmp_path / "test.xml")
            assert mock.call_count == 3
            assert (
                etree.tostring(
                    mock.mock_calls[0].args[0], method="xml", encoding="unicode"
                )
                == """<Dataset xmlns:gml="http://www.opengis.net/gml/3.2" xmlns:xlink="http://www.w3.org/1999/xlink">
    <member>
        <XMLTag1 gml:id="XLINK.ID1"/>
    </member>
    </Dataset>"""
            )
            assert (
                etree.tostring(
                    mock.mock_calls[1].args[0], method="xml", encoding="unicode"
                )
                == """<Dataset xmlns:gml="http://www.opengis.net/gml/3.2" xmlns:xlink="http://www.w3.org/1999/xlink">
    <member>
        <XMLTag2 gml:id="XLINK.ID2"/>
    </member>
</Dataset>"""
            )
            assert (
                etree.tostring(
                    mock.mock_calls[2].args[0], method="xml", encoding="unicode"
                )
                == """<Dataset xmlns:gml="http://www.opengis.net/gml/3.2" xmlns:xlink="http://www.w3.org/1999/xlink">
    <imember>
        <XMLTag gml:id="GML.ID">
            <linkedObject xlink:href="#XLINK.ID1"/>
            <linkedObject xlink:href="#XLINK.ID2"/>
        </XMLTag>
    </imember>
    </Dataset>"""
            )
