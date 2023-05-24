from django.contrib.gis.db import models
from django.contrib.gis.geos import GeometryCollection, Point, Polygon
from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ValidationError

from carting.fields import ChoiceArrayField

from .shared import CategoryOfVessel, ContactableArea


def validate_point_or_surface(collection: GeometryCollection):
    if not all(isinstance(geometry, Point | Polygon) for geometry in collection):
        raise ValidationError(message="OH MY GOD !", code="point_or_surface")


class PilotBoardingPlace(ContactableArea):
    class CategoryOfPilotBoardingPlace(models.TextChoices):
        # fmt: off
        BOARDING_BY_PILOT_CRUISING_VESSEL = "boarding by pilot-cruising vessel" # Pilot boards from a cruising vessel.
        BOARDING_BY_HELICOPTER = "boarding by helicopter" # Pilot boards by helicopter which comes out from the shore.
        PILOT_COMES_OUT_FROM_SHORE = "pilot comes out from shore" # Pilot boards from a vessel which comes out from the shore on request.
        # fmt: on

    class CategoryOfPreference(models.TextChoices):
        # fmt: off
        PRIMARY = "primary" # The preferred and published pilot boarding place which is used in normal weather conditions.
        ALTERNATE = "alternate" # The pilot boarding place which is used if the primary boarding place is unsuitable, for example because of weather or sea state.
        # fmt: on

    class PilotMovement(models.TextChoices):
        # fmt: off
        EMBARKATION = "embarkation" # The place where vessels not being navigated according to a pilot’s instructions pick up a pilot while in transit from sea to a port or constricted waters for future navigation under pilot instructions.
        DISEMBARKATION = "disembarkation" # The place where vessels being navigated under a pilot’s instructions in transit from sea to a port or constricted waters drop the pilot and proceed without being subject to pilot instructions.
        PILOT_CHANGE = "pilot change" # The place where vessels being navigated under a pilot’s instructions drop off the pilot and pick up a different pilot for future navigation under pilot’s instructions.
        # fmt: on

    class Status(models.TextChoices):
        # fmt: off
        PERMANENT = "permanent" # Intended to last or function indefinitely
        OCCASIONAL = "occasional" # Acting on special occasions; happening irregularly
        RECOMMENDED = "recommended" # Presented as worthy of confidence, acceptance, use, etc.
        NOT_IN_USE = "not in use" # Use has ceased, but the facility still exists intact; disused.
        PERIODIC_INTERMITTENT = "periodic/intermittent" # Recurring at intervals
        RESERVED = "reserved" # Set apart for some specific use
        TEMPORARY = "temporary" # Meant to last only for a time
        PRIVATE = "private" # Administered by an individual or corporation, rather than a State or a public body.
        MANDATORY = "mandatory" # Compulsory; enforced.
        EXTINGUISHED = "extinguished" # No longer lit
        ILLUMINATED = "illuminated" # Lit by floodlights, strip lights, etc.
        HISTORIC = "historic" # Famous in history; of historical interest
        PUBLIC = "public" # Belonging to, available to, used or shared by, the community as a whole and not restricted to private use.
        SYNCHRONISED = "synchronised" # Occur at a time, coincide in point of time, be contemporary or simultaneous
        WATCHED = "watched" # Looked at or observed over a period of time especially so as to be aware of any movement or change.
        UN_WATCHED = "un-watched" # Usually automatic in operation, without any permanently-stationed personnel to superintend it.
        EXISTENCE_DOUBTFUL = "existence doubtful" # A feature that has been reported but has not been definitely determined to exist.
        BUOYED = "buoyed" # Marked by buoys
        # fmt: on

    # We choose to skip this relation as we believe it's implicit through PilotService
    # pilotage_district = models.ForeignKey(PilotageDistrict, on_delete=models.CASCADE)

    call_sign = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="The designated call-sign of a radio station.",
    )
    category_of_pilot_boarding_place = models.CharField(
        max_length=255,
        choices=CategoryOfPilotBoardingPlace.choices,
        blank=True,
        null=True,
        help_text="Classification of pilot boarding place by method used to board pilots.",
    )
    category_of_preference = models.CharField(
        max_length=255,
        choices=CategoryOfPreference.choices,
        blank=True,
        null=True,
        help_text="The selection of one location compared to others.",
    )
    category_of_vessel = models.CharField(
        max_length=255,
        choices=CategoryOfVessel.choices,
        blank=True,
        null=True,
        help_text="Classification of vessels by function or use",
    )

    # https://github.com/betagouv/SPPNautInterface/issues/261
    communication_channel = ArrayField(
        models.CharField(max_length=255),
        default=list,
        blank=True,
        help_text="A channel number assigned to a specific radio frequency, frequencies or frequency band.<br/>"
        "ℹ️ Write comma separated values to define multiple.",
    )
    destination = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="The place or general direction to which a vessel is going or directed. Remarks: In addition to a placename of a port, harbour area or terminal, the place could include generalities such as “The north-west”, or “upriver”.",
    )
    pilot_movement = models.CharField(
        max_length=255,
        choices=PilotMovement.choices,
        blank=True,
        null=True,
        help_text="Classification of pilot activity by arrival, departure, or change of pilot. It may also describe the place where the pilot's advice begins, ends, or is transferred to a different pilot.",
    )
    pilot_vessel = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Description of the pilot vessel. The pilot vessel is a small vessel used by a pilot to go to or from a vessel employing the pilot's services.",
    )
    status = ChoiceArrayField(
        base_field=models.CharField(
            max_length=255,
            choices=Status.choices,
        ),
        default=list,
        blank=True,
        # No description in XSD
    )

    geometry = models.GeometryCollectionField(validators=[validate_point_or_surface])

    # Uncomment when upgrading to django 4.2
    # class Meta:
    #     db_table_comment = "A location offshore where a pilot may board a vessel "
    #     "in preparation to piloting it through local waters."
