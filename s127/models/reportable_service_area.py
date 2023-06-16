from django.contrib.gis.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ValidationError

import s100.models
from carting.fields import ChoiceArrayField
from s127.models.contactable_area import PilotBoardingPlace
from s127.models.feature_type import PilotageDistrict

from .shared import BOOLEAN_CHOICES, ReportableServiceArea


class PilotService(ReportableServiceArea):
    class CategoryOfPilot(models.TextChoices):
        # fmt: off
        PILOT = "pilot" # Pilot licenced to conduct vessels during approach from sea to a specified place which may be a handover place, an anchorage or alongside.
        DEEP_SEA = "deep sea" # Pilot licenced to conduct vessels over extensive sea areas.
        HARBOUR = "harbour" # Pilot who is licenced to conduct vessels from a specified place, such as a handover area or anchorage into a harbour.
        BAR = "bar" # Pilot licensed to conduct vessels over a bar to or from a handover with a river pilot (for example as used in USA).
        RIVER = "river" # Pilot licensed to conduct vessels from and to specified places, along the course of a river (for example as used in Rio Amazonas and Rio de La Plata).
        CHANNEL = "channel" # Pilot licensed to conduct vessels from and to specified places, along the course of a channel. (for example as used in Rio Amazonas and Rio de La Plata).
        LAKE = "lake" # Pilot licensed to conduct vessels from and to specified places on a great lake. (for example as used in the Lago de  Maracaibo in Venezuela).
        # fmt: on

    class PilotQualification(models.TextChoices):
        # fmt: off
        GOVERNMENT_PILOT = "government pilot" # A pilot service carried out by government pilots.
        PILOT_APPROVED_BY_GOVERNMENT = "pilot approved by government" # A pilot service carried out by pilots who are approved by government.
        STATE_PILOT = "state pilot" # A pilot that is licensed by the State (USA) and/or their respective pilot association, required for all foreign vessels and all American vessels under registry, bound for a port with compulsory State pilotage. A federal licence is not sufficient to pilot such vessels into the port.
        FEDERAL_PILOT = "federal pilot" # A pilot who carries a Federal endorsement, offering services to vessels that are not required to obtain compulsory State pilotage. Services are usually contracted for in advance.
        COMPANY_PILOT = "company pilot" # A pilot provided by a commercial company.
        LOCAL_PILOT = "local pilot" # A pilot with local knowledge but who does not hold a qualification as a pilot.
        CITIZEN_WITH_SUFFICIENT_LOCAL_KNOWLEDGE = "citizen with sufficient local knowledge" # A pilot service carried out by a citizen with sufficient local knowledge.
        CITIZEN_WITH_DOUBTFUL_LOCAL_KNOWLEDGE = "citizen with doubtful local knowledge" # A pilot service carried out by a citizen whose local knowledge is uncertain.
        # fmt: on

    pilotage_district = models.ForeignKey(
        PilotageDistrict,
        on_delete=models.CASCADE,
        related_name="pilot_services",
        blank=True,
        null=True,
        help_text="An area within which a pilotage direction exists.",
    )
    pilot_boarding_places = models.ManyToManyField(
        PilotBoardingPlace, through="PilotBoardingPlaceServiceThrough"
    )
    category_of_pilot = ChoiceArrayField(
        base_field=models.CharField(
            max_length=255,
            choices=CategoryOfPilot.choices,
        ),
        default=list,
        blank=True,
        help_text="Classification of pilots and pilot services by type of waterway where piloting services are provided.",
    )
    pilot_qualification = models.CharField(
        max_length=255,
        choices=PilotQualification.choices,
        blank=True,
        null=True,
        help_text="Classification of pilots and pilot services by type of license qualification or type of organization providing services.",
    )
    pilot_request = models.TextField(
        blank=True,
        null=True,
        help_text="Description of the pilot request procedure",
    )
    remote_pilot = models.BooleanField(
        choices=BOOLEAN_CHOICES,
        default=False,
        help_text="Whether remote pilot services are available. "
        "True: remote pilot is available: Pilotage is available remotely from shore or other location remote from the vessel requiring pilotage."
        "False: remote pilot is not available: Remote pilotage is not available.",
    )
    # https://github.com/betagouv/SPPNautInterface/issues/228
    geometry = s100.models.GMMultiSurface(null=True, blank=True)

    def clean(self):
        super().clean()
        # raise ValidationError(
        #     "Unauthorized : A service is linked to another District through itss boarding places",
        #     code="boarding_place_inconsistency",
        # )


# Uncomment when upgrading to django 4.2
# class Meta:
#     db_table_comment = "The service provided by a person who directs the movements of a vessel through pilot waters, "
#     "usually a person who has demonstrated extensive knowledge of channels, aids to navigation, dangers to navigation, etc., "
#     "in a particular area and is licensed for that area."


class PilotBoardingPlaceServiceThrough(models.Model):
    pilot_service = models.ForeignKey(PilotService, on_delete=models.CASCADE)
    pilot_boarding_place = models.ForeignKey(
        PilotBoardingPlace, on_delete=models.CASCADE
    )

    def clean(self):
        super().clean()
        if (
            self.pilot_boarding_place.pilotage_district
            and self.pilot_service.pilotage_district
            and self.pilot_boarding_place.pilotage_district
            != self.pilot_service.pilotage_district
        ):
            raise ValidationError(
                "At least one of the related pilot boarding place has a connection with another Pilotage District",
                code="boarding_place_inconsistency",
            )


class NoticeTime(s100.models.ComplexAttributeType):
    class Operation(models.TextChoices):
        """
        Remarks: OPERAT is intended to be used in conjunction with other attributes (or sub-attributes of a complex attribute) to indicate how their values must be combined in order to describe a condition. Null attributes are ignored.
        Example: Complex attribute underkeelAllowance with UKCFIX=2.5, UKCVAR=10.00, OPERAT=1 inicates that the under-keel allowance required is the greater of 2.5 metres or 10% of the ship's draught.
        """

        # fmt: off
        LARGEST_VALUE = "largest value" # The numerically largest value computed from the applicable attributes or sub-attributes
        SMALLEST_VALUE = "smallest value" # The numerically smallest value computed from the applicable attributes or sub-attributes
        # fmt: on

    pilot_service = models.OneToOneField(
        PilotService,
        on_delete=models.CASCADE,
        related_name="notice_time",
        help_text="The service provided by a person who directs the movements of a vessel through pilot waters",
    )

    # https://github.com/betagouv/SPPNautInterface/issues/234
    # https://github.com/betagouv/SPPNautInterface/issues/235
    notice_time_hours = ArrayField(
        models.DurationField(),
        default=list,
        blank=True,
        help_text="Format : hh:mm:ss <br/>"
        "Separate multiple values with a comma.<br/>"
        "The time duration prior to the time the service is needed, when notice must be provided to the service provider.<br/>",
    )
    notice_time_text = models.TextField(
        blank=True,
        null=True,
        help_text="Text string qualifying the notice time specified in NTCHRS."
        "This may explain the time specification in NTCHRS (e.g., “3 working days” for a NTCHRS value of “72” where NTCTIM is supposed to be “3 working days”)"
        " or consist of other language qualifying the time, e.g., “On departure from last port” or “On passing reporting line XY”)",
    )
    operation = models.CharField(
        max_length=255,
        choices=Operation.choices,
        blank=True,
        null=True,
        help_text="Indicates whether the minimum or maximum value should be used to describe a condition or in application processing",
    )


class FullPilotServiceProxy(PilotService):
    class Meta:
        proxy = True
        verbose_name = "Pilot service (full form)"
        verbose_name_plural = "Pilot services (full form)"
