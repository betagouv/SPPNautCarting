from django.contrib.gis.db import models

from carting.models.s100 import FeatureType, GMLObject


class PilotageDistrict(FeatureType):
    communication_channel = models.CharField(max_length=255, blank=True, null=True)
    geometry = models.MultiPolygonField()
