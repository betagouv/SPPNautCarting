from django import forms
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.contrib.gis.db import models
from django.contrib.postgres.fields import ArrayField

from carting.models import s100


class ChoiceArrayField(ArrayField):
    def formfield(self, **kwargs):
        defaults = {
            "form_class": forms.MultipleChoiceField,
            "choices": self.base_field.choices,
        }
        defaults.update(kwargs)

        return super(ArrayField, self).formfield(**defaults)


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


class CategoryOfVessel(models.TextChoices):
    """
    :cvar GENERAL_CARGO_VESSEL: a vessel designed to carry general cargo
    :cvar CONTAINER_CARRIER: a vessel designed to carry ISO containers
    :cvar TANKER: a vessel designed to carry bulk liquid or gas,
        including LPG and LNG
    :cvar BULK_CARRIER: a vessel designed to carry bulk solid material
    :cvar PASSENGER_VESSEL: a vessel designed to carry passengers; often
        a cruise ship
    :cvar ROLL_ON_ROLL_OFF: a vessel designed to allow road vehicles to
        be driven on and off; often a ferry
    :cvar REFRIGERATED_CARGO_VESSEL: a vessel designed to carry
        refrigerated cargo
    :cvar FISHING_VESSEL: a vessel designed to catch or hunt fish
    :cvar SERVICE: a vessel which provides a service such as a tug,
        anchor handler, survey or supply vessel
    :cvar WARSHIP: a vessel designed for the conduct of military
        operations
    :cvar TOWED_OR_PUSHED_COMPOSITE_UNIT: either a tug and tow, or any
        combination of a tug providing propulsion to barges or vessels
        secured ahead or alongside
    :cvar TUG_AND_TOW: a combination of tug(s) and non-powered tow(s)
    :cvar LIGHT_RECREATIONAL: A pleasure boat or watercraft, or an
        excursion vessel used for short cruises such as whale watching
    :cvar SEMI_SUBMERSIBLE_OFFSHORE_INSTALLATION: An installation which
        is designed to float at all times and which is normally anchored
        in position when deployed in the offshore gas and oil industry.
    :cvar JACKUP_EXPLORATION_OR_PROJECT_INSTALLATION: An exploration or
        project installation with legs which can be raised and lowered.
        The legs are raised when the installation is repositioned. When
        stationary the legs are lowered to the sea floor and the working
        platform is raised clear of the sea surface
    :cvar LIVESTOCK_CARRIER: A vessel designed to carry large quantities
        of live animals.
    :cvar SPORT_FISHING: A vessel used in fishing for pleasure or
        competition.
    """

    GENERAL_CARGO_VESSEL = "general cargo vessel"
    CONTAINER_CARRIER = "container carrier"
    TANKER = "tanker"
    BULK_CARRIER = "bulk carrier"
    PASSENGER_VESSEL = "passenger vessel"
    ROLL_ON_ROLL_OFF = "roll-on roll-off"
    REFRIGERATED_CARGO_VESSEL = "refrigerated cargo vessel"
    FISHING_VESSEL = "fishing vessel"
    SERVICE = "service"
    WARSHIP = "warship"
    TOWED_OR_PUSHED_COMPOSITE_UNIT = "towed or pushed composite unit"
    TUG_AND_TOW = "tug and tow"
    LIGHT_RECREATIONAL = "light recreational"
    SEMI_SUBMERSIBLE_OFFSHORE_INSTALLATION = "semi-submersible offshore installation"
    JACKUP_EXPLORATION_OR_PROJECT_INSTALLATION = (
        "jackup exploration or project installation"
    )
    LIVESTOCK_CARRIER = "livestock carrier"
    SPORT_FISHING = "sport fishing"


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


class CategoryOfCargo(models.TextChoices):
    """
    Classification of the different types of cargo that a ship may be carrying.

    :cvar BULK: Normally dry cargo which is transported to and from the
        vessel on conveyors or grabs
    :cvar CONTAINER: One of a number of standard sized cargo carrying
        units, secured using standard corner attachments and bars
    :cvar GENERAL: Break bulk cargo normally loaded by crane
    :cvar LIQUID: Any cargo loaded by pipeline
    :cvar PASSENGER: A fee paying traveller
    :cvar LIVESTOCK: Live animals carried in bulk
    :cvar DANGEROUS_OR_HAZARDOUS: Dangerous or hazardous cargo as
        described by the IMO International Maritime Dangerous Goods code
    :cvar HEAVY_LIFT:
    :cvar BALLAST:
    """

    BULK = "bulk"
    CONTAINER = "container"
    GENERAL = "general"
    LIQUID = "liquid"
    PASSENGER = "passenger"
    LIVESTOCK = "livestock"
    DANGEROUS_OR_HAZARDOUS = "dangerous or hazardous"
    HEAVY_LIFT = "heavy lift"
    BALLAST = "ballast"


class CategoryOfVesselRegistry(models.TextChoices):
    """
    The locality of vessel registration or enrolment relative to the
    nationality of a port, territorial sea, administrative area, exclusive zone
    or other location.

    :cvar DOMESTIC: The vessel is registered or enrolled under the same
        national flag as the port, harbour, territorial sea, exclusive
        economic zone, or administrative area in which the object that
        possesses this attribute applies or is located.
    :cvar FOREIGN: The vessel is registered or enrolled under a national
        flag different from the port, harbour, territorial sea,
        exclusive economic zone, or other administrative area in which
        the object that possesses this attribute applies or is located.
    """

    DOMESTIC = "domestic"
    FOREIGN = "foreign"


class LogicalConnectives(models.TextChoices):
    """
    :cvar LOGICAL_CONJUNCTION: all the conditions described by the other
        attributes of the object, or sub-attributes of the same complex
        attribute, are true
    :cvar LOGICAL_DISJUNCTION: at least one of the conditions described
        by the other attributes of the object, or sub-attributes of the
        same complex attributes, is true
    """

    LOGICAL_CONJUNCTION = "logical conjunction"
    LOGICAL_DISJUNCTION = "logical disjunction"


class ComparisonOperator(models.TextChoices):
    """Remarks: The definition of COMPOP provides the relation between the value given in the model and the real ship's value.

    :cvar GREATER_THAN: The value of the left value is greater than that
        of the right.(http://en.wikipedia.org/wiki/Logical_connective)
    :cvar GREATER_THAN_OR_EQUAL_TO: The value of the left expression is
        greater than or equal to that of the right.
        (http://en.wikipedia.org/wiki/Logical_connective)
    :cvar LESS_THAN: The value of the left expression is less than that
        of the right. (http://en.wikipedia.org/wiki/Logical_connective)
    :cvar LESS_THAN_OR_EQUAL_TO: The value of the left expression is
        less than or equal to that of the right.
        (http://en.wikipedia.org/wiki/Logical_connective)
    :cvar EQUAL_TO: The two values are equivalent. (adapted
        http://en.wikipedia.org/wiki/Logical_connective)
    :cvar NOT_EQUAL_TO: The two values are not equivalent. (adapted
        http://en.wikipedia.org/wiki/Logical_connective)
    """

    GREATER_THAN = "greater than"
    GREATER_THAN_OR_EQUAL_TO = "greater than or equal to"
    LESS_THAN = "less than"
    LESS_THAN_OR_EQUAL_TO = "less than or equal to"
    EQUAL_TO = "equal to"
    NOT_EQUAL_TO = "not equal to"


class CategoryOfPilot(models.TextChoices):
    """
    Classification of pilots and pilot services by type of waterway where
    piloting services are provided.

    :cvar PILOT: Pilot licenced to conduct vessels during approach from
        sea to a specified place which may be a handover place, an
        anchorage or alongside.
    :cvar DEEP_SEA: Pilot licenced to conduct vessels over extensive sea
        areas.
    :cvar HARBOUR: Pilot who is licenced to conduct vessels from a
        specified place, such as a handover area or anchorage into a
        harbour.
    :cvar BAR: Pilot licensed to conduct vessels over a bar to or from a
        handover with a river pilot (for example as used in USA).
    :cvar RIVER: Pilot licensed to conduct vessels from and to specified
        places, along the course of a river (for example as used in Rio
        Amazonas and Rio de La Plata).
    :cvar CHANNEL: Pilot licensed to conduct vessels from and to
        specified places, along the course of a channel. (for example as
        used in Rio Amazonas and Rio de La Plata).
    :cvar LAKE: Pilot licensed to conduct vessels from and to specified
        places on a great lake. (for example as used in the Lago de
        Maracaibo in Venezuela.
    """

    PILOT = "pilot"
    DEEP_SEA = "deep sea"
    HARBOUR = "harbour"
    BAR = "bar"
    RIVER = "river"
    CHANNEL = "channel"
    LAKE = "lake"


class PilotQualification(models.TextChoices):
    """
    Classification of pilots and pilot services by type of license
    qualification or type of organization providing services.

    :cvar GOVERNMENT_PILOT: A pilot service carried out by government
        pilots.
    :cvar PILOT_APPROVED_BY_GOVERNMENT: A pilot service carried out by
        pilots who are approved by government.
    :cvar STATE_PILOT: A pilot that is licensed by the State (USA)
        and/or their respective pilot association, required for all
        foreign vessels and all American vessels under registry, bound
        for a port with compulsory State pilotage. A federal licence is
        not sufficient to pilot such vessels into the port.
    :cvar FEDERAL_PILOT: A pilot who carries a Federal endorsement,
        offering services to vessels that are not required to obtain
        compulsory State pilotage. Services are usually contracted for
        in advance.
    :cvar COMPANY_PILOT: A pilot provided by a commercial company.
    :cvar LOCAL_PILOT: A pilot with local knowledge but who does not
        hold a qualification as a pilot.
    :cvar CITIZEN_WITH_SUFFICIENT_LOCAL_KNOWLEDGE: A pilot service
        carried out by a citizen with sufficient local knowledge.
    :cvar CITIZEN_WITH_DOUBTFUL_LOCAL_KNOWLEDGE: A pilot service carried
        out by a citizen whose local knowledge is uncertain.
    """

    GOVERNMENT_PILOT = "government pilot"
    PILOT_APPROVED_BY_GOVERNMENT = "pilot approved by government"
    STATE_PILOT = "state pilot"
    FEDERAL_PILOT = "federal pilot"
    COMPANY_PILOT = "company pilot"
    LOCAL_PILOT = "local pilot"
    CITIZEN_WITH_SUFFICIENT_LOCAL_KNOWLEDGE = "citizen with sufficient local knowledge"
    CITIZEN_WITH_DOUBTFUL_LOCAL_KNOWLEDGE = "citizen with doubtful local knowledge"


class Operation(models.TextChoices):
    """Indicates whether the minimum or maximum value should be used to describe a condition or in application processing
    Remarks: OPERAT is intended to be used in conjunction with other attributes (or sub-attributes of a complex attribute) to indicate how their values must be combined in order to describe a condition. Null attributes are ignored.
    Example: Complex attribute underkeelAllowance with UKCFIX=2.5, UKCVAR=10.00, OPERAT=1 inicates that the under-keel allowance required is the greater of 2.5 metres or 10% of the ship's draught.

    :cvar LARGEST_VALUE: The numerically largest value computed from the
        applicable attributes or sub-attributes
    :cvar SMALLEST_VALUE: The numerically smallest value computed from
        the applicable attributes or sub-attributes
    """

    LARGEST_VALUE = "largest value"
    SMALLEST_VALUE = "smallest value"


class PilotageDistrict(s100.FeatureType):
    # FIXME : Mettre un joli widget
    communication_channel = ArrayField(
        models.CharField(max_length=255, blank=True, null=True),
        blank=True,
        null=True,
        help_text="ℹ️ Saisissez des valeurs séparées par une virgule pour en définir plusieurs.",
    )

    # FIXME: GM_Surface ? 0..* ?
    geometry = models.MultiPolygonField()

    # Uncomment when upgrading to django 4.2
    # class Meta:
    #     db_table_comment = "An area within which a pilotage direction exists. "
    #     "Such directions are regulated by a competent harbour authority which "
    #     "dictates circumstances under which they apply."


class OrganisationContactArea(s100.FeatureType):
    class Meta:
        abstract = True


class SupervisedArea(OrganisationContactArea):
    class Meta:
        abstract = True


class ReportableServiceArea(SupervisedArea):
    class Meta:
        abstract = True


class PilotService(ReportableServiceArea):
    pilotage_district = models.ForeignKey(
        PilotageDistrict,
        on_delete=models.CASCADE,
        related_name="pilot_service",
        blank=True,
        null=True,
    )
    category_of_pilot = ChoiceArrayField(
        base_field=models.CharField(
            max_length=255,
            choices=CategoryOfPilot.choices,
        ),
        default=list,
        blank=True,
        null=True,
    )
    pilot_qualification = models.CharField(
        max_length=255,
        choices=PilotQualification.choices,
        blank=True,
        null=True,
        help_text="",
    )
    pilot_request = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Description of the pilot request procedure",
    )
    remote_pilot = models.BooleanField(
        null=True,
        blank=True,
        help_text="Whether remote pilot services are available. "
        "True: remote pilot is available: Pilotage is available remotely from shore or other location remote from the vessel requiring pilotage."
        "False: remote pilot is not available: Remote pilotage is not available.",
    )
    # FIXME: GM_OrientableSurface ? 0..* ?
    geometry = models.MultiPolygonField()

    # Uncomment when upgrading to django 4.2
    # class Meta:
    #     db_table_comment = "The service provided by a person who directs the movements of a vessel through pilot waters, "
    #     "usually a person who has demonstrated extensive knowledge of channels, aids to navigation, dangers to navigation, etc., "
    #     "in a particular area and is licensed for that area."


class NoticeTime(models.Model):
    pilot_service = models.ForeignKey(
        PilotService, on_delete=models.CASCADE, related_name="notice_time"
    )
    notice_time_hours = ArrayField(
        models.FloatField(),
        help_text="The time duration prior to the time the service is needed, when notice must be provided to the service provider.",
    )
    notice_time_text = models.CharField(
        max_length=255,
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


class PilotBoardingPlace(OrganisationContactArea):
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


class Applicability(models.Model):
    class CategoryOfDangerousOrHazardousCargo(models.TextChoices):
        """
        :cvar IMDG_CODE_CLASS_1_DIV_1_1: Explosives, Division 1: substances
            and articles which have a mass explosion hazard
        :cvar IMDG_CODE_CLASS_1_DIV_1_2: Explosives, Division 2: substances
            and articles which have a projection hazard but not a mass
            explosion hazard
        :cvar IMDG_CODE_CLASS_1_DIV_1_3: Explosives, Division 3: substances
            and articles which have a fire hazard and either a minor blast
            hazard or a minor projection hazard or both, but not a mass
            explosion hazard
        :cvar IMDG_CODE_CLASS_1_DIV_1_4: Explosives, Division 4: substances
            and articles which present no significant hazard
        :cvar IMDG_CODE_CLASS_1_DIV_1_5: Explosives, Division 5: very
            insensitive substances which have a mass explosion hazard
        :cvar IMDG_CODE_CLASS_1_DIV_1_6: Explosives, Division 6: extremely
            insensitive articles which do not have a mass explosion hazard
        :cvar IMDG_CODE_CLASS_2_DIV_2_1: Gases, flammable gases
        :cvar IMDG_CODE_CLASS_2_DIV_2_2: Gases, non-flammable, non-toxic
            gases
        :cvar IMDG_CODE_CLASS_2_DIV_2_3: Gases, toxic gases
        :cvar IMDG_CODE_CLASS_3: flammable liquids
        :cvar IMDG_CODE_CLASS_4_DIV_4_1: flammable solids, self-reactive
            substances and desensitized explosives
        :cvar IMDG_CODE_CLASS_4_DIV_4_2: substances liable to spontaneous
            combustion
        :cvar IMDG_CODE_CLASS_4_DIV_4_3: substances which, in contact with
            water, emit flammable gases
        :cvar IMDG_CODE_CLASS_5_DIV_5_1: oxidizing substances
        :cvar IMDG_CODE_CLASS_5_DIV_5_2: organic peroxides
        :cvar IMDG_CODE_CLASS_6_DIV_6_1: toxic substances
        :cvar IMDG_CODE_CLASS_6_DIV_6_2: infectious substances
        :cvar IMDG_CODE_CLASS_7: Radioactive material
        :cvar IMDG_CODE_CLASS_8: Corrosive substances
        :cvar IMDG_CODE_CLASS_9: Miscellaneous dangerous substances and
            articles
        :cvar HARMFUL_SUBSTANCES_IN_PACKAGED_FORM: Harmful substances are
            those substances which are identified as marine pollutants in
            the International Maritime Dangerous Goods Code (IMDG Code).
            Packaged form is defined as the forms of containment specified
            for harmful substances in the IMDG Code. (MARPOL (73/78) Annex
            III)
        """

        IMDG_CODE_CLASS_1_DIV_1_1 = "IMDG Code Class 1 Div. 1.1"
        IMDG_CODE_CLASS_1_DIV_1_2 = "IMDG Code Class 1 Div. 1.2"
        IMDG_CODE_CLASS_1_DIV_1_3 = "IMDG Code Class 1 Div. 1.3"
        IMDG_CODE_CLASS_1_DIV_1_4 = "IMDG Code Class 1 Div. 1.4"
        IMDG_CODE_CLASS_1_DIV_1_5 = "IMDG Code Class 1 Div. 1.5"
        IMDG_CODE_CLASS_1_DIV_1_6 = "IMDG Code Class 1 Div. 1.6"
        IMDG_CODE_CLASS_2_DIV_2_1 = "IMDG Code Class 2 Div. 2.1"
        IMDG_CODE_CLASS_2_DIV_2_2 = "IMDG Code Class 2 Div. 2.2"
        IMDG_CODE_CLASS_2_DIV_2_3 = "IMDG Code Class 2 Div. 2.3"
        IMDG_CODE_CLASS_3 = "IMDG Code Class 3"
        IMDG_CODE_CLASS_4_DIV_4_1 = "IMDG Code Class 4 Div. 4.1"
        IMDG_CODE_CLASS_4_DIV_4_2 = "IMDG Code Class 4 Div. 4.2"
        IMDG_CODE_CLASS_4_DIV_4_3 = "IMDG Code Class 4 Div. 4.3"
        IMDG_CODE_CLASS_5_DIV_5_1 = "IMDG Code Class 5 Div. 5.1"
        IMDG_CODE_CLASS_5_DIV_5_2 = "IMDG Code Class 5 Div. 5.2"
        IMDG_CODE_CLASS_6_DIV_6_1 = "IMDG Code Class 6 Div. 6.1"
        IMDG_CODE_CLASS_6_DIV_6_2 = "IMDG Code Class 6 Div. 6.2"
        IMDG_CODE_CLASS_7 = "IMDG Code Class 7"
        IMDG_CODE_CLASS_8 = "IMDG Code Class 8"
        IMDG_CODE_CLASS_9 = "IMDG Code Class 9"
        HARMFUL_SUBSTANCES_IN_PACKAGED_FORM = "Harmful Substances in packaged form"

    BOOLEAN_CHOICES = ((None, "---------"), (True, "Yes"), (False, "No"))

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.BigIntegerField()
    information_type = GenericForeignKey()
    in_ballast = models.BooleanField(
        null=True,
        blank=True,
        help_text="Whether the vessel is in ballast.",
        choices=BOOLEAN_CHOICES,
    )
    category_of_cargo = ChoiceArrayField(
        base_field=models.CharField(
            max_length=255,
            choices=CategoryOfCargo.choices,
        ),
        default=list,
        blank=True,
        null=True,
        help_text="Classification of the different types of cargo that "
        "a ship may be carrying <br/>"
        "If item 7 is used, the nature of dangerous or hazardous cargoes can"
        " be amplified with category of dangerous or hazardous cargo.",
        # TODO : à la validation vérifier la condition :
        # If item 7 is used, the nature of dangerous or hazardous cargoes can be amplified with category of dangerous or hazardous cargo.
    )
    category_of_dangerous_or_hazardous_cargo = ChoiceArrayField(
        base_field=models.CharField(
            max_length=255,
            choices=CategoryOfDangerousOrHazardousCargo.choices,
        ),
        default=list,
        blank=True,
        null=True,
        help_text="Classification of dangerous goods or hazardous materials based on "
        "the International Maritime Dangerous Goods Code"
        # FIXME : vérifier avec Anthony si on a bien besoin des deux valeur du rel
        " (<a href='https://www.imo.org/fr/OurWork/Safety/Pages/DangerousGoods-default.aspx' target='_blank' rel='noreferrer noopener'>IMDG Code</a>)",
    )
    # FIXME: In XSD : simpleType with Union = choice or other string
    category_of_vessel = models.CharField(
        max_length=255,
        choices=CategoryOfVessel.choices,
        blank=True,
        null=True,
    )
    category_of_vessel_registry = models.CharField(
        max_length=255,
        choices=CategoryOfVesselRegistry.choices,
        blank=True,
        null=True,
    )
    logical_connectives = models.CharField(
        max_length=255,
        choices=LogicalConnectives.choices,
        blank=True,
        null=True,
    )
    thickness_of_ice_capability = models.IntegerField(null=True, blank=True)
    vessel_performance = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    information = GenericRelation(s100.Information)

    class Meta:
        verbose_name_plural = "Applicabilities"


class VesselsMeasurements(models.Model):
    class VesselsCharacteristicsUnit(models.TextChoices):
        """
        :cvar METRE: The metre (or meter) is the base unit of length in the
            International System of Units (SI). It is defined as the
            distance travelled by light in vacuum in 1/299,792,458 of a
            second.
        :cvar FOOT: A foot (plural: feet) is a non-SI unit of length in a
            number of different systems including English units, Imperial
            units, and United States customary units. The most commonly used
            foot today is the international foot. There are three feet in a
            yard and 12 inches in a foot.
        :cvar METRIC_TON: The tonne or metric ton (U.S.), often redundantly
            referred to as a metric tonne, is a unit of mass equal to 1,000
            kg (2,205 lb) or approximately the mass of one cubic metre of
            water at four degrees Celsius. It is sometimes abbreviated as mt
            in the United States, but this conflicts with other SI symbols.
            The tonne is not a unit in the International System of Units
            (SI), but is accepted for use with the SI. In SI units and
            prefixes, the tonne is a megagram (Mg). The Imperial and US
            customary units comparable to the tonne are both spelled ton in
            English, though they differ in mass. Pronunciation of tonne (the
            word used in the UK) and ton is usually identical, but is not
            too confusing unless accuracy is important as the tonne and UK
            long ton differ by only 1.6%.
        :cvar TON: Long ton (weight ton or imperial ton) is the name for the
            unit called the "ton" in the avoirdupois or Imperial system of
            measurements, as used in the United Kingdom and several other
            Commonwealth countries. It has been mostly replaced by the
            tonne, and in the United States by the short ton. One long ton
            is equal to 2,240 pounds (1,016 kg) or 35 cubic feet (0.9911 m3)
            of salt water with a density of 64 lb/ft³ (1.025 g/ml). It has
            some limited use in the United States, most commonly in
            measuring the displacement of ships, and was the unit prescribed
            for warships by the Washington Naval Treaty—for example
            battleships were limited to a mass of 35,000 long tons (36,000
            t; 39,000 ST).
        :cvar SHORT_TON: The short ton is a unit of weight equal to 2,000
            pounds (907.18474 kg). In the United States it is often called
            simply ton without distinguishing it from the metric ton (tonne,
            1,000 kilograms) or the long ton (2,240 pounds / 1,016.0469088
            kilograms); rather, the other two are specifically noted. There
            are, however, some U.S. applications for which unspecified tons
            normally means long tons (for example, Navy ships) or metric
            tons (world grain production figures). Both the long and short
            ton are defined as 20 hundredweights, but a hundredweight is 100
            pounds (45.359237 kg) in the U.S. system (short or net
            hundredweight) and 112 pounds (50.80234544 kg) in the Imperial
            system (long or gross hundredweight).
        :cvar GROSS_TON: Gross tonnage (GT) is a function of the volume of
            all ship's enclosed spaces (from keel to funnel) measured to the
            outside of the hull framing. There is a sliding scale factor. So
            GT is a kind of capacity-derived index that is used to rank a
            ship for purposes of determining manning, safety and other
            statutory requirements and is expressed simply as GT, which is a
            unitless entity, even though its derivation is tied to the cubic
            meter unit of volumetric capacity. Tonnage measurements are now
            governed by an IMO Convention (International Convention on
            Tonnage Measurement of Ships, 1969 (London-Rules)), which
            applies to all ships built after July 1982. In accordance with
            the Convention, the correct term to use now is GT, which is a
            function of the moulded volume of all enclosed spaces of the
            ship.
        :cvar NET_TON: Net tonnage (NT) is based on a calculation of the
            volume of all cargo spaces of the ship. It indicates a vessel’s
            earning space and is a function of the moulded volume of all
            cargo spaces of the ship.
        :cvar PANAMA_CANAL_UNIVERSAL_MEASUREMENT_SYSTEM_NET_TONNAGE: The
            Panama Canal/Universal Measurement System (PC/UMS) is based on
            net tonnage, modified for Panama Canal purposes. PC/UMS is based
            on a mathematical formula to calculate a vessel's total volume;
            a PC/UMS net ton is equivalent to 100 cubic feet of capacity.
        :cvar SUEZ_CANAL_NET_TONNAGE: The Suez Canal Net Tonnage (SCNT) is
            derived with a number of modifications from the former net
            register tonnage of the Moorsom System and was established by
            the International Commission of Constantinople in its Protocol
            of 18 December 1873. It is still in use, as amended by the Rules
            of Navigation of the Suez Canal Authority, and is registered in
            the Suez Canal Tonnage Certificate.
        :cvar NONE: Can be used for net and gross tonnages, including Panama
            Canal/Universal Measurement System net tonnage and The Suez
            Canal Net Tonnage.
        :cvar CUBIC_METRES: cubic metres
        :cvar SUEZ_CANAL_GROSS_TONNAGE: The Suez Canal Gross Tonnage (SCGT)
            is derived with a number of modifications from the former net
            register tonnage of the Moorsom System and was established by
            the International Commission of Constantinople in its Protocol
            of 18 December 1873. It is still in use, as amended by the Rules
            of Navigation of the Suez Canal Authority, and is registered in
            the Suez Canal Tonnage Certificate.
        """

        METRE = "metre"
        FOOT = "foot"
        METRIC_TON = "metric ton"
        TON = "ton"
        SHORT_TON = "short ton"
        GROSS_TON = "gross ton"
        NET_TON = "net ton"
        PANAMA_CANAL_UNIVERSAL_MEASUREMENT_SYSTEM_NET_TONNAGE = (
            "Panama Canal/Universal Measurement System net tonnage"
        )
        SUEZ_CANAL_NET_TONNAGE = "Suez Canal Net Tonnage"
        NONE = "none"
        CUBIC_METRES = "cubic metres"
        SUEZ_CANAL_GROSS_TONNAGE = "Suez Canal Gross Tonnage"

    class VesselsCharacteristics(models.TextChoices):
        """
        :cvar LENGTH_OVERALL: The maximum length of the ship (L.O.A.).
            (http://en.wikipedia.org/wiki/Ship_measurements; 24 July 2010)
        :cvar LENGTH_AT_WATERLINE: The ship's length measured at the
            waterline (L.W.L.).
            (http://en.wikipedia.org/wiki/Ship_measurements; 24 July 2010)
        :cvar BREADTH: The width or beam of the vessel. (Adapted from
            http://en.wikipedia.org/wiki/Ship_measurements; 24 July 2010)
        :cvar DRAUGHT: The depth of water necessary to float a vessel fully
            loaded. (http://en.wikipedia.org/wiki/Ship_measurements; 24 July
            2010)
        :cvar HEIGHT: The height of the highest point of a vessel's
            structure (e.g. radar aerial, funnel, cranes, masthead) above
            her waterline. (UKHO NP100/2009)
        :cvar DISPLACEMENT_TONNAGE: A measurement of the weight of the
            vessel, usually used for warships. (Merchant ships are usually
            measured based on the volume of cargo space; see tonnage).
            Displacement is expressed either in long tons of 2,240 pounds or
            metric tonnes of 1,000 kg. Since the two units are very close in
            size (2,240 pounds = 1,016 kg and 1,000 kg = 2,205 pounds), it
            is common not to distinguish between them. To preserve secrecy,
            nations sometimes misstate a warship's displacement.
            (http://en.wikipedia.org/wiki/Ship_measurements; 24 July 2010)
        :cvar DISPLACEMENT_TONNAGE_LIGHT: The weight of the ship excluding
            cargo, fuel, ballast, stores, passengers, and crew, but with
            water in the boilers to steaming level.
            (http://en.wikipedia.org/wiki/Ship_measurements; 24 July 2010)
        :cvar DISPLACEMENT_TONNAGE_LOADED: The weight of the ship including
            cargo, passengers, fuel, water, stores, dunnage and such other
            items necessary for use on a voyage, which brings the vessel
            down to her load draft.
            (http://en.wikipedia.org/wiki/Ship_measurements; 24 July 2010)
        :cvar DEADWEIGHT_TONNAGE: The difference between displacement, light
            and displacement, loaded. A measure of the ship's total carrying
            capacity. (http://en.wikipedia.org/wiki/Ship_measurements; 24
            July 2010)
        :cvar GROSS_TONNAGE: The entire internal cubic capacity of the ship
            expressed in tons of 100 cubic feet to the ton, except certain
            spaces with are exempted such as: peak and other tanks for water
            ballast, open forecastle bridge and poop, access of hatchways,
            certain light and air spaces, domes of skylights, condenser,
            anchor gear, steering gear, wheel house, galley and cabin for
            passengers. (http://en.wikipedia.org/wiki/Ship_measurements; 24
            July 2010)
        :cvar NET_TONNAGE: Obtained from the gross tonnage by deducting crew
            and navigating spaces and allowances for propulsion
            machinery.(http://en.wikipedia.org/wiki/Ship_measurements; 24
            July 2010)
        :cvar PANAMA_CANAL_UNIVERSAL_MEASUREMENT_SYSTEM_NET_TONNAGE: the
            Panama Canal/Universal Measurement System (PC/UMS) is based on
            net tonnage, modified for Panama Canal purposes. PC/UMS is based
            on a mathematical formula to calculate a vessel's total volume;
            a PC/UMS net ton is equivalent to 100 cubic feet of capacity.
            (Adapted from http://en.wikipedia.org/wiki/Tonnage 4 Oct 2010)
        :cvar SUEZ_CANAL_NET_TONNAGE: the Suez Canal Net Tonnage (SCNT) is
            derived with a number of modifications from the former net
            register tonnage of the Moorsom System and was established by
            the International Commission of Constantinople in its Protocol
            of 18 December 1873. It is still in use, as amended by the Rules
            of Navigation of the Suez Canal Authority, and is registered in
            the Suez Canal Tonnage Certificate. (Adapted from
            http://en.wikipedia.org/wiki/Tonnage 4 Oct 2010)
        :cvar SUEZ_CANAL_GROSS_TONNAGE: Suez Canal Gross Tonnage (SCGT) is
            derived with a number of modifications from the former net
            register tonnage of the Moorsom System and was established by
            the International Commission of Constantinople in its Protocol
            of 18 December 1873. It is still in use, as amended by the Rules
            of Navigation of the Suez Canal Authority, and is registered in
            the Suez Canal Tonnage Certificate.
        """

        LENGTH_OVERALL = "length overall"
        LENGTH_AT_WATERLINE = "length at waterline"
        BREADTH = "breadth"
        DRAUGHT = "draught"
        HEIGHT = "height"
        DISPLACEMENT_TONNAGE = "displacement tonnage"
        DISPLACEMENT_TONNAGE_LIGHT = "displacement tonnage, light"
        DISPLACEMENT_TONNAGE_LOADED = "displacement tonnage, loaded"
        DEADWEIGHT_TONNAGE = "deadweight tonnage"
        GROSS_TONNAGE = "gross tonnage"
        NET_TONNAGE = "net tonnage"
        PANAMA_CANAL_UNIVERSAL_MEASUREMENT_SYSTEM_NET_TONNAGE = (
            "Panama Canal/Universal Measurement System net tonnage"
        )
        SUEZ_CANAL_NET_TONNAGE = "Suez Canal net tonnage"
        SUEZ_CANAL_GROSS_TONNAGE = "Suez Canal gross tonnage"

    applicability = models.ForeignKey(
        Applicability, on_delete=models.CASCADE, related_name="vessels_measurements"
    )
    comparison_operator = models.CharField(
        max_length=255,
        choices=ComparisonOperator.choices,
        blank=True,
        null=True,
    )
    vessels_characteristics = models.CharField(
        max_length=255,
        choices=VesselsCharacteristics.choices,
        blank=True,
        null=True,
    )
    vessels_characteristics_value = models.FloatField()
    vessels_characteristics_unit = models.CharField(
        max_length=255,
        choices=VesselsCharacteristicsUnit.choices,
        blank=True,
        null=True,
    )
