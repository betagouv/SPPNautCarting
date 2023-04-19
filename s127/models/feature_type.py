from django.contrib.gis.db import models
from django.contrib.postgres.fields import ArrayField

import s100.models


class PilotageDistrict(s100.models.FeatureType):
    # FIXME : Mettre un joli widget
    communication_channel = ArrayField(
        models.CharField(max_length=255, blank=True, null=True),
        blank=True,
        null=True,
        help_text="ℹ️ Write comma separated values to define multiple.",
    )

    # FIXME: GM_Surface ? 0..* ?
    geometry = models.MultiPolygonField()

    # Uncomment when upgrading to django 4.2
    # class Meta:
    #     db_table_comment = "An area within which a pilotage direction exists. "
    #     "Such directions are regulated by a competent harbour authority which "
    #     "dictates circumstances under which they apply."
