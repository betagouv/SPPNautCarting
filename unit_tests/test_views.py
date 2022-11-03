import datetime
from base64 import b64encode

import pytest


@pytest.fixture
def authorization_header(settings):
    GENERATOR_USERNAME, GENERATOR_PASSWORD = list(settings.BASICAUTH_USERS.items())[0]
    return "Basic " + b64encode(
        bytes(
            f"{GENERATOR_USERNAME}:{GENERATOR_PASSWORD}",
            encoding="utf8",
        )
    ).decode("utf8")


class TestOuvragesByDate:
    def test_group_and_desc_sort_by_document_date(
        self, settings, client, authorization_header, requests_mock
    ):
        ouvrage_list_response = {
            "103": {
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
            "2": {
                "document.pdf": {
                    "date": "2022-09-08T14:29:57.340Z",
                    "url": "http://fake.url",
                }
            },
            "g4": {
                "document.pdf": {
                    "date": "2022-09-23T17:22:59.344Z",
                    "url": "http://fake.url",
                },
            },
        }
        requests_mock.get(
            f"{settings.GENERATOR_SERVICE_HOST}/publication/from_production/list",
            json=ouvrage_list_response,
        )

        response = client.get(
            "/ouvrages-by-date/",
            HTTP_AUTHORIZATION=authorization_header,
        )
        assert list(response.context["ouvrages_by_date"].keys()) == [
            "Ouvrages générés le 23/09/2022",
            "Ouvrages générés le 16/09/2022",
            "Ouvrages générés le 08/09/2022",
        ], "The ouvrage date is the document.pdf one"

    def test_sort_by_ouvrage_name(
        self, settings, client, authorization_header, requests_mock
    ):
        ouvrage_list_response = {
            "1": {
                "document.pdf": {
                    "date": "2022-09-16T14:57:18.066Z",
                    "url": "http://fake.url",
                }
            },
            "2": {
                "document.pdf": {
                    "date": "2022-09-23T14:29:57.340Z",
                    "url": "http://fake.url",
                }
            },
            "103": {
                "document.pdf": {
                    "date": "2022-09-16T14:57:18.066Z",
                    "url": "http://fake.url",
                }
            },
            "g4": {
                "document.pdf": {
                    "date": "2022-09-16T17:22:59.344Z",
                    "url": "http://fake.url",
                },
            },
        }
        requests_mock.get(
            f"{settings.GENERATOR_SERVICE_HOST}/publication/from_production/list",
            json=ouvrage_list_response,
        )

        response = client.get(
            "/ouvrages-by-date/",
            HTTP_AUTHORIZATION=authorization_header,
        )
        assert [
            ouvrage.name
            for ouvrage in response.context["ouvrages_by_date"][
                "Ouvrages générés le 16/09/2022"
            ]
        ] == [
            "1",
            "103",
            "g4",
        ]


class TestOuvragesByName:
    def test_sort_by_ouvrage_name(
        self, settings, client, authorization_header, requests_mock
    ):
        ouvrage_list_response = {
            "1": {
                "document.pdf": {
                    "date": "2022-09-16T14:57:18.066Z",
                    "url": "http://fake.url",
                }
            },
            "2": {
                "document.pdf": {
                    "date": "2022-09-23T14:29:57.340Z",
                    "url": "http://fake.url",
                }
            },
            "103": {
                "document.pdf": {
                    "date": "2022-09-16T14:57:18.066Z",
                    "url": "http://fake.url",
                }
            },
            "g4": {
                "document.pdf": {
                    "date": "2022-09-16T17:22:59.344Z",
                    "url": "http://fake.url",
                },
            },
        }
        requests_mock.get(
            f"{settings.GENERATOR_SERVICE_HOST}/publication/from_production/list",
            json=ouvrage_list_response,
        )

        response = client.get(
            "/ouvrages-by-name/",
            HTTP_AUTHORIZATION=authorization_header,
        )
        assert [ouvrage.name for ouvrage in response.context["ouvrages"]] == [
            "1",
            "103",
            "2",
            "g4",
        ]


class TestPublicationDisplay:
    def test_generation_failed(
        self, settings, client, authorization_header, requests_mock
    ):
        requests_mock.get(
            f"{settings.GENERATOR_SERVICE_HOST}/publication/fake_generation_id/",
            status_code=500,
            text="Oh noes!\nMany errors!",
        )

        response = client.get(
            "/publication/fake_generation_id/",
            HTTP_AUTHORIZATION=authorization_header,
        )

        assert response.context["generation_id"] == "fake_generation_id"
        assert response.context["logs"] == "Oh noes!\nMany errors!"

    def test_generation_in_progress(
        self, settings, client, authorization_header, requests_mock
    ):
        requests_mock.get(
            f"{settings.GENERATOR_SERVICE_HOST}/publication/fake_generation_id/",
            status_code=404,
            text="Étape 1 sur 126",
        )

        response = client.get(
            "/publication/fake_generation_id/",
            HTTP_AUTHORIZATION=authorization_header,
        )

        assert response.context["displayable_step"] == "Étape 1 sur 126"

    def test_generation_success(
        self, settings, client, authorization_header, requests_mock
    ):
        requests_mock.get(
            f"{settings.GENERATOR_SERVICE_HOST}/publication/fake_generation_id/",
            status_code=200,
            headers={
                "content-type": "application/pdf",
                "content-length": "123",
                "content-disposition": 'inline; filename="g4p.pdf"',
            },
        )

        response = client.get(
            "/publication/fake_generation_id/",
            HTTP_AUTHORIZATION=authorization_header,
        )

        assert response.headers["content-type"] == "application/pdf"
        assert response.headers["content-length"] == "123"
        assert response.headers["content-disposition"] == 'inline; filename="g4p.pdf"'
