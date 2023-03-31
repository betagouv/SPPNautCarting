from pathlib import Path

import pytest
from django.core.files.uploadedfile import SimpleUploadedFile

from spo.forms import UploadFileForm


class TestUploadFileForm:
    def test_xml_file_ok(self):
        xml_file = SimpleUploadedFile("file.xml", b"fake", content_type="text/xml")
        form = UploadFileForm({}, {"file": xml_file})
        assert form.errors == {}
        assert form.is_valid()

    def test_upload_conte_form_extension_xml_file_ko(self):
        wrong_xml_file = SimpleUploadedFile(
            "file.ods", b"fake", content_type="text/xml"
        )
        form = UploadFileForm({}, {"file": wrong_xml_file})
        assert form.errors["file"] == [
            "Le fichier doit être un fichier tableau type format XML"
        ]
        assert not form.is_valid()
