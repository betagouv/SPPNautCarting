from base64 import b64encode

import pytest
from decouple import config
from django.contrib.gis.geos import GeometryCollection, MultiPolygon, Point, Polygon

from s127.admin import AccumulatedInlines
from s127.models import PilotageDistrict, PilotBoardingPlace


@pytest.fixture
def authorization_header():
    TEST_USERNAME = config("TEST_USERNAME")
    TEST_PASSWORD = config("TEST_PASSWORD")
    return "Basic " + b64encode(
        bytes(
            f"{TEST_USERNAME}:{TEST_PASSWORD}",
            encoding="utf8",
        )
    ).decode("utf8")


class TestAccumulatedInlines:
    class ParentInline(AccumulatedInlines):
        inlines = [1, 2]

    class ChildInline(ParentInline):
        pass

    class GrandChildInline(ChildInline):
        inlines = [1, 3]

    def test_get_inlines(self):
        assert self.ParentInline().get_inlines() == [1, 2]

    def test_get_inlines_on_inherited_inline(self):
        assert self.ChildInline().get_inlines() == [1, 2]

    def test_get_inlines_with_accumulated_inlines(self):
        assert self.GrandChildInline().get_inlines() == [1, 3, 2]


# class TestPilotServiceAdd:
#     def test_http(self, client, authorization_header):
#         pilot_boarding_place = PilotBoardingPlace.objects.create(
#             geometry=GeometryCollection(Point(0, 0))
#         )
#         pilotage_district = PilotageDistrict.objects.create(
#             geometry=MultiPolygon(Polygon.from_bbox((0, 0, 0, 0)))
#         )

#         parameters = {
#             "boardingplaceserviceprovider_set-0-id": "",
#             "boardingplaceserviceprovider_set-0-pilot_boarding_place": pilot_boarding_place,
#             "boardingplaceserviceprovider_set-0-pilot_service": "",
#             "csrfmiddlewaretoken": "elDP5uBnq6xZLtXDDbiXRTYCvfYlFeNBAP5aWHBCI4qnfNUQFuKrAFbVL3jEltSK",
#             "pilotage_district": pilotage_district,
#             "remote_pilot": "False",
#             "s100-featurename-content_type-object_id-0-id": "",
#             "s100-featurename-content_type-object_id-0-language": "fra",
#             "s100-featurename-content_type-object_id-0-name": "Pilot Service 1",
#         }

#         response = client.post(
#             "/admin/s127/fullpilotserviceproxy/add/",
#             parameters,
#             HTTP_AUTHORIZATION=authorization_header,
#         )
#         assert response.status_code == 202
#         assert "pilotservice_id" in response.json()
