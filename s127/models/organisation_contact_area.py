from django.contrib.gis.db import models
from django.contrib.postgres.fields import ArrayField

from .shared import CategoryOfVessel, ChoiceArrayField, S127OrganisationContactArea


class S127PilotBoardingPlace(S127OrganisationContactArea):
    class CategoryOfPilotBoardingPlace(models.TextChoices):
        """
        Classification of pilot boarding place by method used to board pilots.

        :cvar BOARDING_BY_PILOT_CRUISING_VESSEL: Pilot boards from a
            cruising vessel.
        :cvar BOARDING_BY_HELICOPTER: Pilot boards by helicopter which comes
            out from the shore.
        :cvar PILOT_COMES_OUT_FROM_SHORE: Pilot boards from a vessel which
            comes out from the shore on request.
        """

        BOARDING_BY_PILOT_CRUISING_VESSEL = "boarding by pilot-cruising vessel"
        BOARDING_BY_HELICOPTER = "boarding by helicopter"
        PILOT_COMES_OUT_FROM_SHORE = "pilot comes out from shore"

    class CategoryOfPreference(models.TextChoices):
        """
        The selection of one location compared to others.

        :cvar PRIMARY: The preferred and published pilot boarding place
            which is used in normal weather conditions.
        :cvar ALTERNATE: The pilot boarding place which is used if the
            primary boarding place is unsuitable, for example because of
            weather or sea state.
        """

        PRIMARY = "primary"
        ALTERNATE = "alternate"

    class PilotMovement(models.TextChoices):
        """Classification of pilot activity by arrival, departure, or change of
        pilot.
        It may also describe the place where the pilot's advice begins,
        ends, or is transferred to a different pilot.

        :cvar EMBARKATION: The place where vessels not being navigated
            according to a pilot’s instructions pick up a pilot while in
            transit from sea to a port or constricted waters for future
            navigation under pilot instructions.
        :cvar DISEMBARKATION: The place where vessels being navigated under
            a pilot’s instructions in transit from sea to a port or
            constricted waters drop the pilot and proceed without being
            subject to pilot instructions.
        :cvar PILOT_CHANGE: The place where vessels being navigated under a
            pilot’s instructions drop off the pilot and pick up a different
            pilot for future navigation under pilot’s instructions.
        """

        EMBARKATION = "embarkation"
        DISEMBARKATION = "disembarkation"
        PILOT_CHANGE = "pilot change"

    class Status(models.TextChoices):
        """
        Definition required.

        :cvar PERMANENT: Intended to last or function indefinitely
        :cvar OCCASIONAL: Acting on special occasions; happening irregularly
        :cvar RECOMMENDED: Presented as worthy of confidence, acceptance,
            use, etc.
        :cvar NOT_IN_USE: Use has ceased, but the facility still exists
            intact; disused.
        :cvar PERIODIC_INTERMITTENT: Recurring at intervals
        :cvar RESERVED: Set apart for some specific use
        :cvar TEMPORARY: Meant to last only for a time
        :cvar PRIVATE: Administered by an individual or corporation, rather
            than a State or a public body.
        :cvar MANDATORY: Compulsory; enforced.
        :cvar EXTINGUISHED: No longer lit
        :cvar ILLUMINATED: Lit by floodlights, strip lights, etc.
        :cvar HISTORIC: Famous in history; of historical interest
        :cvar PUBLIC: Belonging to, available to, used or shared by, the
            community as a whole and not restricted to private use.
        :cvar SYNCHRONISED: Occur at a time, coincide in point of time, be
            contemporary or simultaneous
        :cvar WATCHED: Looked at or observed over a period of time
            especially so as to be aware of any movement or change.
        :cvar UN_WATCHED: Usually automatic in operation, without any
            permanently-stationed personnel to superintend it.
        :cvar EXISTENCE_DOUBTFUL: A feature that has been reported but has
            not been definitely determined to exist.
        :cvar BUOYED: Marked by buoys
        """

        PERMANENT = "permanent"
        OCCASIONAL = "occasional"
        RECOMMENDED = "recommended"
        NOT_IN_USE = "not in use"
        PERIODIC_INTERMITTENT = "periodic/intermittent"
        RESERVED = "reserved"
        TEMPORARY = "temporary"
        PRIVATE = "private"
        MANDATORY = "mandatory"
        EXTINGUISHED = "extinguished"
        ILLUMINATED = "illuminated"
        HISTORIC = "historic"
        PUBLIC = "public"
        SYNCHRONISED = "synchronised"
        WATCHED = "watched"
        UN_WATCHED = "un-watched"
        EXISTENCE_DOUBTFUL = "existence doubtful"
        BUOYED = "buoyed"

    # FIXME: We choose to skip this relation as we believe it's implicit through PilotService
    # pilotage_district = models.ForeignKey(
    #     PilotageDistrict, on_delete=models.CASCADE, related_name="pilot_boarding_places"
    # )

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
        help_text="The place or general direction to which a vessel is going or directed. Remarks: In addition to a placename of a port, harbour area or terminal, the place could include generalities such as “The north-west”, or “upriver”.",
    )
    category_of_preference = models.CharField(
        max_length=255,
        choices=CategoryOfPreference.choices,
        blank=True,
        null=True,
    )
    # FIXME: In XSD : simpleType with Union = choice or other string
    category_of_vessel = models.CharField(
        max_length=255,
        choices=CategoryOfVessel.choices,
        blank=True,
        null=True,
    )
    # FIXME : Mettre un joli widget
    communication_channel = ArrayField(
        models.CharField(max_length=255), blank=True, null=True
    )
    destination = models.CharField(max_length=255, blank=True, null=True)
    pilot_movement = models.CharField(
        max_length=255,
        choices=PilotMovement.choices,
        blank=True,
        null=True,
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
            blank=True,
            null=True,
        ),
        default=list,
        blank=True,
        null=True,
    )
    geometry = models.GeometryField()

    # Uncomment when upgrading to django 4.2
    # class Meta:
    #     db_table_comment = "A location offshore where a pilot may board a vessel "
    #     "in preparation to piloting it through local waters."
