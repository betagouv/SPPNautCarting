import datetime
import logging
from base64 import b64encode

import pytest
import requests
import requests_mock
from django.urls import reverse

from home.views import PublicationProd


@pytest.fixture
def authorization_header(settings):
    GENERATOR_USERNAME, GENERATOR_PASSWORD = list(settings.BASICAUTH_USERS.items())[0]
    return "Basic " + b64encode(
        bytes(
            f"{GENERATOR_USERNAME}:{GENERATOR_PASSWORD}",
            encoding="utf8",
        )
    ).decode("utf8")


class TestGenerateFromProduction:
    def test_get_publication_prod(self, settings, client, authorization_header):
        with requests_mock.Mocker() as m:
            ouvrage_list_response = {
                "103": {
                    "document.pdf": {
                        "date": "2022-09-16T14:57:18.066Z",
                        "url": "https://cellar-fr-north-hds-c1.services.clever-cloud.com/sppnaut-generated-production/103/document.pdf?AWSAccessKeyId=C02LQ3V10SBVQXHW9U37&Signature=PvYIAwIsnUDpa97%2FmgdLSJ%2Bvdtg%3D&Expires=1664357893",
                    }
                },
            }
            m.get(
                f"{settings.GENERATOR_SERVICE_HOST}/publication/from_production/list",
                json=ouvrage_list_response,
            )

            response = client.get(
                reverse("home:publication_prod"),
                HTTP_AUTHORIZATION=authorization_header,
            )
            assert list(response.context["ouvrages"].keys()) == [
                datetime.date(2022, 9, 16)
            ]

    def test_get_publication_prod_sort_by_date(
        self, settings, client, authorization_header
    ):
        with requests_mock.Mocker() as m:
            ouvrage_list_response = {
                "103": {
                    "document.pdf": {
                        "date": "2022-09-16T14:57:18.066Z",
                        "url": "https://cellar-fr-north-hds-c1.services.clever-cloud.com/sppnaut-generated-production/103/document.pdf?AWSAccessKeyId=C02LQ3V10SBVQXHW9U37&Signature=PvYIAwIsnUDpa97%2FmgdLSJ%2Bvdtg%3D&Expires=1664357893",
                    }
                },
                "2": {
                    "document.pdf": {
                        "date": "2022-09-08T14:29:57.340Z",
                        "url": "https://cellar-fr-north-hds-c1.services.clever-cloud.com/sppnaut-generated-production/2/document.pdf?AWSAccessKeyId=C02LQ3V10SBVQXHW9U37&Signature=mnvOvbFrAitEmSgAtAbPegGe3c4%3D&Expires=1664357893",
                    }
                },
                "g4": {
                    "document.pdf": {
                        "date": "2022-09-23T17:22:59.344Z",
                        "url": "https://cellar-fr-north-hds-c1.services.clever-cloud.com/sppnaut-generated-production/g4/document.pdf?AWSAccessKeyId=C02LQ3V10SBVQXHW9U37&Signature=d8sol0mJNW%2FlaT%2BRd7zW8roQKbc%3D&Expires=1664357893",
                    },
                },
            }
            m.get(
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

    def test_get_publication_prod_filter_on_document_pdf(
        self, settings, client, authorization_header
    ):
        with requests_mock.Mocker() as m:
            ouvrage_list_response = {
                "103": {
                    "document.pdf": {
                        "date": "2022-09-16T14:57:18.066Z",
                        "url": "https://cellar-fr-north-hds-c1.services.clever-cloud.com/sppnaut-generated-production/103/document.pdf?AWSAccessKeyId=C02LQ3V10SBVQXHW9U37&Signature=PvYIAwIsnUDpa97%2FmgdLSJ%2Bvdtg%3D&Expires=1664357893",
                    }
                },
                "2": {
                    "document.pdf": {
                        "date": "2022-09-08T14:29:57.340Z",
                        "url": "https://cellar-fr-north-hds-c1.services.clever-cloud.com/sppnaut-generated-production/2/document.pdf?AWSAccessKeyId=C02LQ3V10SBVQXHW9U37&Signature=mnvOvbFrAitEmSgAtAbPegGe3c4%3D&Expires=1664357893",
                    }
                },
                "g4": {
                    "document2.pdf": {
                        "date": "2022-09-23T17:22:59.344Z",
                        "url": "https://cellar-fr-north-hds-c1.services.clever-cloud.com/sppnaut-generated-production/g4/document.pdf?AWSAccessKeyId=C02LQ3V10SBVQXHW9U37&Signature=d8sol0mJNW%2FlaT%2BRd7zW8roQKbc%3D&Expires=1664357893",
                    },
                },
            }
            m.get(
                f"{settings.GENERATOR_SERVICE_HOST}/publication/from_production/list",
                json=ouvrage_list_response,
            )

            response = client.get(
                reverse("home:publication_prod"),
                HTTP_AUTHORIZATION=authorization_header,
            )
            assert list(response.context["ouvrages"].keys()) == [
                datetime.date(2022, 9, 16),
                datetime.date(2022, 9, 8),
            ]

    def test_get_publication_prod_group_by_date_order_by_label(
        self, settings, client, authorization_header
    ):
        with requests_mock.Mocker() as m:
            ouvrage_list_response = {
                "1": {
                    "document.pdf": {
                        "date": "2022-09-16T14:57:18.066Z",
                        "url": "https://cellar-fr-north-hds-c1.services.clever-cloud.com/sppnaut-generated-production/103/document.pdf?AWSAccessKeyId=C02LQ3V10SBVQXHW9U37&Signature=PvYIAwIsnUDpa97%2FmgdLSJ%2Bvdtg%3D&Expires=1664357893",
                    }
                },
                "2": {
                    "document.pdf": {
                        "date": "2022-09-16T14:29:57.340Z",
                        "url": "https://cellar-fr-north-hds-c1.services.clever-cloud.com/sppnaut-generated-production/2/document.pdf?AWSAccessKeyId=C02LQ3V10SBVQXHW9U37&Signature=mnvOvbFrAitEmSgAtAbPegGe3c4%3D&Expires=1664357893",
                    }
                },
                "103": {
                    "document.pdf": {
                        "date": "2022-09-16T14:57:18.066Z",
                        "url": "https://cellar-fr-north-hds-c1.services.clever-cloud.com/sppnaut-generated-production/103/document.pdf?AWSAccessKeyId=C02LQ3V10SBVQXHW9U37&Signature=PvYIAwIsnUDpa97%2FmgdLSJ%2Bvdtg%3D&Expires=1664357893",
                    }
                },
                "g4": {
                    "document.pdf": {
                        "date": "2022-09-16T17:22:59.344Z",
                        "url": "https://cellar-fr-north-hds-c1.services.clever-cloud.com/sppnaut-generated-production/g4/document.pdf?AWSAccessKeyId=C02LQ3V10SBVQXHW9U37&Signature=d8sol0mJNW%2FlaT%2BRd7zW8roQKbc%3D&Expires=1664357893",
                    },
                },
            }
            m.get(
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
                dict(response.context["ouvrages"][datetime.date(2022, 9, 16)]).keys()
            ) == [
                "1",
                "103",
                "2",
                "g4",
            ]
