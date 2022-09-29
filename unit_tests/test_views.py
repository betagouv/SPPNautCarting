import datetime
from base64 import b64encode

import pytest
from django.urls import reverse


@pytest.fixture
def authorization_header(settings):
    GENERATOR_USERNAME, GENERATOR_PASSWORD = list(settings.BASICAUTH_USERS.items())[0]
    return "Basic " + b64encode(
        bytes(
            f"{GENERATOR_USERNAME}:{GENERATOR_PASSWORD}",
            encoding="utf8",
        )
    ).decode("utf8")


class TestPublicationProd:
    def test_get(self, settings, client, authorization_header, requests_mock):
        ouvrage_list_response = {
            "103": {
                "document.pdf": {
                    "date": "2022-09-16T14:57:18.066Z",
                    "url": "http://fake.url",
                }
            },
        }
        requests_mock.get(
            f"{settings.GENERATOR_SERVICE_HOST}/publication/from_production/list",
            json=ouvrage_list_response,
        )
        response = client.get(
            reverse("home:publication_prod"),
            HTTP_AUTHORIZATION=authorization_header,
        )
        assert list(response.context["ouvrages"].keys()) == [datetime.date(2022, 9, 16)]

    def test_group_and_desc_sort_by_date(
        self, settings, client, authorization_header, requests_mock
    ):
        ouvrage_list_response = {
            "103": {
                "document.pdf": {
                    "date": "2022-09-16T14:57:18.066Z",
                    "url": "http://fake.url",
                }
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
            reverse("home:publication_prod"),
            HTTP_AUTHORIZATION=authorization_header,
        )
        assert list(response.context["ouvrages"].keys()) == [
            datetime.date(2022, 9, 23),
            datetime.date(2022, 9, 16),
            datetime.date(2022, 9, 8),
        ]

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
                    "date": "2022-09-16T14:29:57.340Z",
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
            reverse("home:publication_prod"),
            HTTP_AUTHORIZATION=authorization_header,
        )
        assert list(response.context["ouvrages"].keys()) == [
            datetime.date(2022, 9, 16),
        ]
        assert list(
            response.context["ouvrages"][datetime.date(2022, 9, 16)].keys()
        ) == [
            "1",
            "103",
            "2",
            "g4",
        ]
