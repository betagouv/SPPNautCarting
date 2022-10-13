import datetime

from home.ouvrages import Ouvrage, OuvrageFile


class TestOuvrage:
    def test_one_document_pdf(self):
        ouvrage = Ouvrage.from_json(
            "103",
            {
                "document.pdf": {
                    "date": "2022-09-16T14:57:18.066Z",
                    "url": "http://fake.url",
                }
            },
        )
        assert ouvrage == Ouvrage(
            "103",
            OuvrageFile("document.pdf", "http://fake.url", datetime.date(2022, 9, 16)),
        )

    def test_document_pdf_with_vignette_and_metadata(self):
        ouvrage = Ouvrage.from_json(
            "103",
            {
                "document.pdf": {
                    "date": "2022-09-16T14:57:18.066Z",
                    "url": "http://fake.url",
                },
                "vignette.jpg": {
                    "date": "2022-10-22T14:57:18.066Z",
                    "url": "http://fake_vignette.url",
                },
                "OUVNAUT_IN_G4.xml": {
                    "date": "2022-09-10T14:57:18.066Z",
                    "url": "http://fake_metadata.url",
                },
            },
        )

        assert ouvrage == Ouvrage(
            "103",
            OuvrageFile("document.pdf", "http://fake.url", datetime.date(2022, 9, 16)),
            OuvrageFile(
                "vignette.jpg",
                "http://fake_vignette.url",
                datetime.date(2022, 10, 22),
            ),
            OuvrageFile(
                "OUVNAUT_IN_G4.xml",
                "http://fake_metadata.url",
                datetime.date(2022, 9, 10),
            ),
        )

    def test_document_pdf_with_unknown_files(self):
        ouvrage = Ouvrage.from_json(
            "103",
            {
                "document.pdf": {
                    "date": "2022-09-16T14:57:18.066Z",
                    "url": "http://fake.url",
                },
                "vignette.jpeg": {
                    "date": "2022-10-22T14:57:18.066Z",
                    "url": "http://fake_vignette.url",
                },
                "OUVNAU_IN_G4.xml": {
                    "date": "2022-09-10T14:57:18.066Z",
                    "url": "http://fake_metadata.url",
                },
                "OUVNAUT_IN_G4.yml": {
                    "date": "2022-09-10T14:57:18.066Z",
                    "url": "http://fake_metadata.url",
                },
            },
        )
        assert ouvrage == Ouvrage(
            "103",
            OuvrageFile("document.pdf", "http://fake.url", datetime.date(2022, 9, 16)),
        ), "metadata and vignette should be named OUVNAUT*.xml and vignette.jpg"

    def test_document_pdf_with_2_metadata_files(self):
        ouvrage = Ouvrage.from_json(
            "103",
            {
                "document.pdf": {
                    "date": "2022-09-16T14:57:18.066Z",
                    "url": "http://fake.url",
                },
                "OUVNAUT_IN_G4.xml": {
                    "date": "2022-09-10T14:57:18.123Z",
                    "url": "http://fake_metadata1.url",
                },
                "OUVNAUT_OUT_G4.xml": {
                    "date": "2022-09-10T14:57:18.456Z",
                    "url": "http://fake_metadata2.url",
                },
            },
        )
        assert ouvrage == Ouvrage(
            "103",
            OuvrageFile("document.pdf", "http://fake.url", datetime.date(2022, 9, 16)),
        ), "both metadata are ignored"

    def test_ouvrage_ignored_if_no_document_pdf(self):
        ouvrage = Ouvrage.from_json(
            "103",
            {
                "document.fake": {
                    "date": "2022-09-16T14:57:18.066Z",
                    "url": "http://fake.url",
                },
                "vignette.jpg": {
                    "date": "2022-10-22T14:57:18.066Z",
                    "url": "http://fake_vignette.url",
                },
                "OUVNAUT_IN_G4.xml": {
                    "date": "2022-09-10T14:57:18.066Z",
                    "url": "http://fake_metadata.url",
                },
            },
        )
        assert not ouvrage

    def test_files_all_file_types(self):
        ouvrage = Ouvrage.from_json(
            "103",
            {
                "document.pdf": {
                    "date": "2022-09-16T14:57:18.066Z",
                    "url": "http://fake.url",
                },
                "vignette.jpg": {
                    "date": "2022-10-22T14:57:18.066Z",
                    "url": "http://fake_vignette.url",
                },
                "OUVNAUT_IN_G4.xml": {
                    "date": "2022-09-10T14:57:18.066Z",
                    "url": "http://fake_metadata.url",
                },
            },
        )

        assert ouvrage.files == {
            "PDF": OuvrageFile(
                "document.pdf", "http://fake.url", datetime.date(2022, 9, 16)
            ),
            "Métadonnées": OuvrageFile(
                "OUVNAUT_IN_G4.xml",
                "http://fake_metadata.url",
                datetime.date(2022, 9, 10),
            ),
            "Vignette": OuvrageFile(
                "vignette.jpg",
                "http://fake_vignette.url",
                datetime.date(2022, 10, 22),
            ),
        }

    def test_files_one_document_pdf(self):
        ouvrage = Ouvrage.from_json(
            "103",
            {
                "document.pdf": {
                    "date": "2022-09-16T14:57:18.066Z",
                    "url": "http://fake.url",
                }
            },
        )
        assert ouvrage.files == {
            "PDF": OuvrageFile(
                "document.pdf", "http://fake.url", datetime.date(2022, 9, 16)
            ),
            "Métadonnées": None,
            "Vignette": None,
        }
