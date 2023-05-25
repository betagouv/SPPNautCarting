from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.contrib.gis.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, RegexValidator
from django.utils.text import Truncator

import s100.models
from carting.fields import ChoiceArrayField
from s127.models.shared import BOOLEAN_CHOICES, CategoryOfVessel


class Applicability(s100.models.InformationType):
    class CategoryOfDangerousOrHazardousCargo(models.TextChoices):
        # fmt: off
        IMDG_CODE_CLASS_1_DIV_1_1 = "IMDG Code Class 1 Div. 1.1", "Explosives, Division 1: substances and articles which have a mass explosion hazard"
        IMDG_CODE_CLASS_1_DIV_1_2 = "IMDG Code Class 1 Div. 1.2", "Explosives, Division 2: substances and articles which have a projection hazard but not a mass explosion hazard"
        IMDG_CODE_CLASS_1_DIV_1_3 = "IMDG Code Class 1 Div. 1.3", "Explosives, Division 3: substances and articles which have a fire hazard and either a minor blast hazard or a minor projection hazard or both, but not a mass explosion hazard"
        IMDG_CODE_CLASS_1_DIV_1_4 = "IMDG Code Class 1 Div. 1.4", "Explosives, Division 4: substances and articles which present no significant hazard"
        IMDG_CODE_CLASS_1_DIV_1_5 = "IMDG Code Class 1 Div. 1.5", "Explosives, Division 5: very insensitive substances which have a mass explosion hazard"
        IMDG_CODE_CLASS_1_DIV_1_6 = "IMDG Code Class 1 Div. 1.6", "Explosives, Division 6: extremely insensitive articles which do not have a mass explosion hazard"
        IMDG_CODE_CLASS_2_DIV_2_1 = "IMDG Code Class 2 Div. 2.1", "Gases, flammable gases"
        IMDG_CODE_CLASS_2_DIV_2_2 = "IMDG Code Class 2 Div. 2.2", "Gases, non-flammable, non-toxic gases"
        IMDG_CODE_CLASS_2_DIV_2_3 = "IMDG Code Class 2 Div. 2.3", "Gases, toxic gases"
        IMDG_CODE_CLASS_3 = "IMDG Code Class 3", "flammable liquids"
        IMDG_CODE_CLASS_4_DIV_4_1 = "IMDG Code Class 4 Div. 4.1", "flammable solids, self-reactive substances and desensitized explosives"
        IMDG_CODE_CLASS_4_DIV_4_2 = "IMDG Code Class 4 Div. 4.2", "substances liable to spontaneous combustion"
        IMDG_CODE_CLASS_4_DIV_4_3 = "IMDG Code Class 4 Div. 4.3", "substances which, in contact with water, emit flammable gases"
        IMDG_CODE_CLASS_5_DIV_5_1 = "IMDG Code Class 5 Div. 5.1", "oxidizing substances"
        IMDG_CODE_CLASS_5_DIV_5_2 = "IMDG Code Class 5 Div. 5.2", "organic peroxides"
        IMDG_CODE_CLASS_6_DIV_6_1 = "IMDG Code Class 6 Div. 6.1", "toxic substances"
        IMDG_CODE_CLASS_6_DIV_6_2 = "IMDG Code Class 6 Div. 6.2", "infectious substances"
        IMDG_CODE_CLASS_7 = "IMDG Code Class 7", "Radioactive material"
        IMDG_CODE_CLASS_8 = "IMDG Code Class 8", "Corrosive substances"
        IMDG_CODE_CLASS_9 = "IMDG Code Class 9", "Miscellaneous dangerous substances and articles"
        HARMFUL_SUBSTANCES_IN_PACKAGED_FORM = "Harmful Substances in packaged form", # Harmful substances are those substances which are identified as marine pollutants in the International Maritime Dangerous Goods Code (IMDG Code). Packaged form is defined as the forms of containment specified for harmful substances in the IMDG Code. (MARPOL (73/78) Annex III)
        # fmt: on

    class CategoryOfCargo(models.TextChoices):
        # fmt: off
        BULK = "bulk" # Normally dry cargo which is transported to and from the vessel on conveyors or grabs
        CONTAINER = "container" # One of a number of standard sized cargo carrying units, secured using standard corner attachments and bars
        GENERAL = "general" # Break bulk cargo normally loaded by crane
        LIQUID = "liquid" # Any cargo loaded by pipeline
        PASSENGER = "passenger" # A fee paying traveller
        LIVESTOCK = "livestock" # Live animals carried in bulk
        DANGEROUS_OR_HAZARDOUS = "dangerous or hazardous" # Dangerous or hazardous cargo as described by the IMO International Maritime Dangerous Goods code
        HEAVY_LIFT = "heavy lift" #
        BALLAST = "ballast" #
        # fmt: on

    class CategoryOfVesselRegistry(models.TextChoices):
        # fmt: off
        DOMESTIC = "domestic" # The vessel is registered or enrolled under the same national flag as the port, harbour, territorial sea, exclusive economic zone, or administrative area in which the object that possesses this attribute applies or is located.
        FOREIGN = "foreign" # The vessel is registered or enrolled under a national flag different from the port, harbour, territorial sea, exclusive economic zone, or other administrative area in which the object that possesses this attribute applies or is located.
        # fmt: on

    class LogicalConnectives(models.TextChoices):
        # fmt: off
        LOGICAL_CONJUNCTION = "logical conjunction", "Logical conjunction (AND)" # all the conditions described by the other attributes of the object, or sub-attributes of the same complex attribute, are true
        LOGICAL_DISJUNCTION = "logical disjunction", "Logical disjunction (OR)" # at least one of the conditions described by the other attributes of the object, or sub-attributes of the same complex attributes, is true
        # fmt: on

    in_ballast = models.BooleanField(
        choices=BOOLEAN_CHOICES,
        null=True,
        blank=True,
        help_text="Whether the vessel is in ballast.",
    )
    category_of_cargo = ChoiceArrayField(
        base_field=models.CharField(
            max_length=255,
            choices=CategoryOfCargo.choices,
        ),
        default=list,
        blank=True,
        help_text="Classification of the different types of cargo that a ship may be carrying",
    )
    category_of_dangerous_or_hazardous_cargo = ChoiceArrayField(
        base_field=models.CharField(
            max_length=255,
            choices=CategoryOfDangerousOrHazardousCargo.choices,
        ),
        default=list,
        blank=True,
        help_text="Classification of dangerous goods or hazardous materials based on the International Maritime Dangerous Goods Code"
        " (<a href='https://www.imo.org/fr/OurWork/Safety/Pages/DangerousGoods-default.aspx' target='_blank'>IMDG Code</a>)",
    )

    category_of_vessel = models.CharField(
        max_length=255,
        choices=CategoryOfVessel.choices,
        blank=True,
        null=True,
        help_text="Classification of vessels by function or use",
    )
    category_of_vessel_registry = models.CharField(
        max_length=255,
        choices=CategoryOfVesselRegistry.choices,
        blank=True,
        null=True,
        help_text="The locality of vessel registration or enrolment relative to the nationality of a port, territorial sea, administrative area, exclusive zone or other location.",
    )

    # https://github.com/betagouv/SPPNautInterface/issues/231
    thickness_of_ice_capability = models.IntegerField(
        null=True,
        blank=True,
        help_text="The thickness of ice that the ship can safely transit",
    )
    vessel_performance = models.TextField(
        blank=True,
        null=True,
        help_text="A description of the required handling characteristics of a vessel including hull design, main and auxilliary machinery, cargo handling equipment, navigation equipment and manoeuvring behaviour.",
    )
    # https://github.com/betagouv/SPPNautInterface/issues/230
    logical_connectives = models.CharField(
        max_length=255,
        choices=LogicalConnectives.choices,
        blank=True,
        null=True,
        # No description in XSD
    )
    information = GenericRelation(s100.models.Information)

    def __str__(self):
        parts = []

        if self.in_ballast is not None:
            parts.append("In ballast" if self.in_ballast else "Not in ballast")

        if self.category_of_cargo:
            parts.append(
                " or ".join(
                    self.CategoryOfCargo(x).label for x in self.category_of_cargo
                )
            )

        if self.category_of_dangerous_or_hazardous_cargo:
            parts.append(
                " or ".join(
                    self.CategoryOfDangerousOrHazardousCargo(x).label
                    for x in self.category_of_dangerous_or_hazardous_cargo
                )
            )

        if self.category_of_vessel:
            parts.append(CategoryOfVessel(self.category_of_vessel).label)

        if self.category_of_vessel_registry:
            parts.append(
                self.CategoryOfVesselRegistry(self.category_of_vessel_registry).label
            )

        if self.thickness_of_ice_capability:
            parts.append(
                f"Thickness of ice capability: {self.thickness_of_ice_capability}"
            )

        if self.vessel_performance:
            parts.append(Truncator(self.vessel_performance).chars(25, truncate="…"))

        logical_connective = " - "
        if self.logical_connectives == self.LogicalConnectives.LOGICAL_CONJUNCTION:
            logical_connective = " AND "
        if self.logical_connectives == self.LogicalConnectives.LOGICAL_DISJUNCTION:
            logical_connective = " OR "

        if self.pk and self.vessels_measurements.all():
            parts.append(
                logical_connective.join(str(x) for x in self.vessels_measurements.all())
            )

        if not parts:
            return super().__str__()
        return ", ".join(parts)

    class Meta:
        verbose_name_plural = "Applicabilities"


class PermissionType(s100.models.GenericManyToMany):
    class CategoryOfRelationship(models.TextChoices):
        # fmt: off
        PROHIBITED = "prohibited"  # use of facility, waterway or service is forbidden
        NOT_RECOMMENDED = "not recommended"  # use of facility, waterway or service is not recommended
        PERMITTED = "permitted"  # use of facility, waterway, or service is permitted but not required
        RECOMMENDED = "recommended"  # use of facility, waterway, or service is recommended
        REQUIRED = "required"  # use of facility, waterway, or service is required
        NOT_REQUIRED = "not required"  # use of facility, waterway, or service is not required
        # fmt: on

    category_of_relationship = models.CharField(
        choices=CategoryOfRelationship.choices,
        max_length=255,
        help_text="This attribute expresses the level of insistence for or against an action or activity.",
    )

    # ManyToMany
    feature_content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, related_name="+"
    )
    feature_object_id = models.BigIntegerField()
    feature_object = GenericForeignKey("feature_content_type", "feature_object_id")
    applicability = models.ForeignKey(Applicability, on_delete=models.CASCADE)


class VesselsMeasurements(s100.models.ComplexAttributeType):
    class ComparisonOperator(models.TextChoices):
        """
        Remarks: The definition of COMPOP provides the relation between the value given in the model and the real ship's value.
        """

        # fmt: off
        GREATER_THAN = "greater than", ">"  # The value of the left value is greater than that of the right.(http://en.wikipedia.org/wiki/Logical_connective)
        GREATER_THAN_OR_EQUAL_TO = "greater than or equal to", "≥"  # The value of the left expression is greater than or equal to that of the right. (http://en.wikipedia.org/wiki/Logical_connective)
        LESS_THAN = "less than", "<"  # The value of the left expression is less than that of the right. (http://en.wikipedia.org/wiki/Logical_connective)
        LESS_THAN_OR_EQUAL_TO = "less than or equal to", "≤"  # The value of the left expression is less than or equal to that of the right. (http://en.wikipedia.org/wiki/Logical_connective)
        EQUAL_TO = "equal to", "="  # The two values are equivalent. (adapted http://en.wikipedia.org/wiki/Logical_connective)
        NOT_EQUAL_TO = "not equal to", "≠"  # The two values are not equivalent. (adapted http://en.wikipedia.org/wiki/Logical_connective)
        # fmt: on

    class VesselsCharacteristicsUnit(models.TextChoices):
        # fmt: off
        METRE = "metre" # The metre (or meter) is the base unit of length in the International System of Units (SI). It is defined as the distance travelled by light in vacuum in 1/299,792,458 of a second.
        FOOT = "foot" # A foot (plural: feet) is a non-SI unit of length in a number of different systems including English units, Imperial units, and United States customary units. The most commonly used foot today is the international foot. There are three feet in a yard and 12 inches in a foot.
        METRIC_TON = "metric ton" # The tonne or metric ton (U.S.), often redundantly referred to as a metric tonne, is a unit of mass equal to 1,000 kg (2,205 lb) or approximately the mass of one cubic metre of water at four degrees Celsius. It is sometimes abbreviated as mt in the United States, but this conflicts with other SI symbols. The tonne is not a unit in the International System of Units (SI), but is accepted for use with the SI. In SI units and prefixes, the tonne is a megagram (Mg). The Imperial and US customary units comparable to the tonne are both spelled ton in English, though they differ in mass. Pronunciation of tonne (the word used in the UK) and ton is usually identical, but is not too confusing unless accuracy is important as the tonne and UK long ton differ by only 1.6%.
        TON = "ton" # Long ton (weight ton or imperial ton) is the name for the unit called the "ton" in the avoirdupois or Imperial system of measurements, as used in the United Kingdom and several other Commonwealth countries. It has been mostly replaced by the tonne, and in the United States by the short ton. One long ton is equal to 2,240 pounds (1,016 kg) or 35 cubic feet (0.9911 m3) of salt water with a density of 64 lb/ft³ (1.025 g/ml). It has some limited use in the United States, most commonly in measuring the displacement of ships, and was the unit prescribed for warships by the Washington Naval Treaty—for example battleships were limited to a mass of 35,000 long tons (36,000 t; 39,000 ST).
        SHORT_TON = "short ton" # The short ton is a unit of weight equal to 2,000 pounds (907.18474 kg). In the United States it is often called simply ton without distinguishing it from the metric ton (tonne, 1,000 kilograms) or the long ton (2,240 pounds / 1,016.0469088 kilograms); rather, the other two are specifically noted. There are, however, some U.S. applications for which unspecified tons normally means long tons (for example, Navy ships) or metric tons (world grain production figures). Both the long and short ton are defined as 20 hundredweights, but a hundredweight is 100 pounds (45.359237 kg) in the U.S. system (short or net hundredweight) and 112 pounds (50.80234544 kg) in the Imperial system (long or gross hundredweight).
        GROSS_TON = "gross ton" # Gross tonnage (GT) is a function of the volume of all ship's enclosed spaces (from keel to funnel) measured to the outside of the hull framing. There is a sliding scale factor. So GT is a kind of capacity-derived index that is used to rank a ship for purposes of determining manning, safety and other statutory requirements and is expressed simply as GT, which is a unitless entity, even though its derivation is tied to the cubic meter unit of volumetric capacity. Tonnage measurements are now governed by an IMO Convention (International Convention on Tonnage Measurement of Ships, 1969 (London-Rules)), which applies to all ships built after July 1982. In accordance with the Convention, the correct term to use now is GT, which is a function of the moulded volume of all enclosed spaces of the ship.
        NET_TON = "net ton" # Net tonnage (NT) is based on a calculation of the volume of all cargo spaces of the ship. It indicates a vessel’s earning space and is a function of the moulded volume of all cargo spaces of the ship.
        PANAMA_CANAL_UNIVERSAL_MEASUREMENT_SYSTEM_NET_TONNAGE = "Panama Canal/Universal Measurement System net tonnage" # The Panama Canal/Universal Measurement System (PC/UMS) is based on net tonnage, modified for Panama Canal purposes. PC/UMS is based on a mathematical formula to calculate a vessel's total volume; a PC/UMS net ton is equivalent to 100 cubic feet of capacity.
        SUEZ_CANAL_NET_TONNAGE = "Suez Canal Net Tonnage" # The Suez Canal Net Tonnage (SCNT) is derived with a number of modifications from the former net register tonnage of the Moorsom System and was established by the International Commission of Constantinople in its Protocol of 18 December 1873. It is still in use, as amended by the Rules of Navigation of the Suez Canal Authority, and is registered in the Suez Canal Tonnage Certificate.
        NONE = "none" # Can be used for net and gross tonnages, including Panama Canal/Universal Measurement System net tonnage and The Suez Canal Net Tonnage.
        CUBIC_METRES = "cubic metres" # cubic metres
        SUEZ_CANAL_GROSS_TONNAGE = "Suez Canal Gross Tonnage" # The Suez Canal Gross Tonnage (SCGT) is derived with a number of modifications from the former net register tonnage of the Moorsom System and was established by the International Commission of Constantinople in its Protocol of 18 December 1873. It is still in use, as amended by the Rules of Navigation of the Suez Canal Authority, and is registered in the Suez Canal Tonnage Certificate.
        # fmt: on

    class VesselsCharacteristics(models.TextChoices):
        # fmt: off
        LENGTH_OVERALL = "length overall" # The maximum length of the ship (L.O.A.). (http://en.wikipedia.org/wiki/Ship_measurements; 24 July 2010)
        LENGTH_AT_WATERLINE = "length at waterline" # The ship's length measured at the waterline (L.W.L.). (http://en.wikipedia.org/wiki/Ship_measurements; 24 July 2010)
        BREADTH = "breadth" # The width or beam of the vessel. (Adapted from http://en.wikipedia.org/wiki/Ship_measurements; 24 July 2010)
        DRAUGHT = "draught" # The depth of water necessary to float a vessel fully loaded. (http://en.wikipedia.org/wiki/Ship_measurements; 24 July 2010)
        HEIGHT = "height" # The height of the highest point of a vessel's structure (e.g. radar aerial, funnel, cranes, masthead) above her waterline. (UKHO NP100/2009)
        DISPLACEMENT_TONNAGE = "displacement tonnage" # A measurement of the weight of the vessel, usually used for warships. (Merchant ships are usually measured based on the volume of cargo space; see tonnage). Displacement is expressed either in long tons of 2,240 pounds or metric tonnes of 1,000 kg. Since the two units are very close in size (2,240 pounds = 1,016 kg and 1,000 kg = 2,205 pounds), it is common not to distinguish between them. To preserve secrecy, nations sometimes misstate a warship's displacement. (http://en.wikipedia.org/wiki/Ship_measurements; 24 July 2010)
        DISPLACEMENT_TONNAGE_LIGHT = "displacement tonnage, light" # The weight of the ship excluding cargo, fuel, ballast, stores, passengers, and crew, but with water in the boilers to steaming level. (http://en.wikipedia.org/wiki/Ship_measurements; 24 July 2010)
        DISPLACEMENT_TONNAGE_LOADED = "displacement tonnage, loaded" # The weight of the ship including cargo, passengers, fuel, water, stores, dunnage and such other items necessary for use on a voyage, which brings the vessel down to her load draft. (http://en.wikipedia.org/wiki/Ship_measurements; 24 July 2010)
        DEADWEIGHT_TONNAGE = "deadweight tonnage" # The difference between displacement, light and displacement, loaded. A measure of the ship's total carrying capacity. (http://en.wikipedia.org/wiki/Ship_measurements; 24 July 2010)
        GROSS_TONNAGE = "gross tonnage" # The entire internal cubic capacity of the ship expressed in tons of 100 cubic feet to the ton, except certain spaces with are exempted such as: peak and other tanks for water ballast, open forecastle bridge and poop, access of hatchways, certain light and air spaces, domes of skylights, condenser, anchor gear, steering gear, wheel house, galley and cabin for passengers. (http://en.wikipedia.org/wiki/Ship_measurements; 24 July 2010)
        NET_TONNAGE = "net tonnage" # Obtained from the gross tonnage by deducting crew and navigating spaces and allowances for propulsion machinery.(http://en.wikipedia.org/wiki/Ship_measurements; 24 July 2010)
        PANAMA_CANAL_UNIVERSAL_MEASUREMENT_SYSTEM_NET_TONNAGE = "Panama Canal/Universal Measurement System net tonnage" # the Panama Canal/Universal Measurement System (PC/UMS) is based on net tonnage, modified for Panama Canal purposes. PC/UMS is based on a mathematical formula to calculate a vessel's total volume; a PC/UMS net ton is equivalent to 100 cubic feet of capacity. (Adapted from http://en.wikipedia.org/wiki/Tonnage 4 Oct 2010)
        SUEZ_CANAL_NET_TONNAGE = "Suez Canal net tonnage" # the Suez Canal Net Tonnage (SCNT) is derived with a number of modifications from the former net register tonnage of the Moorsom System and was established by the International Commission of Constantinople in its Protocol of 18 December 1873. It is still in use, as amended by the Rules of Navigation of the Suez Canal Authority, and is registered in the Suez Canal Tonnage Certificate. (Adapted from http://en.wikipedia.org/wiki/Tonnage 4 Oct 2010)
        SUEZ_CANAL_GROSS_TONNAGE = "Suez Canal gross tonnage" # Suez Canal Gross Tonnage (SCGT) is derived with a number of modifications from the former net register tonnage of the Moorsom System and was established by the International Commission of Constantinople in its Protocol of 18 December 1873. It is still in use, as amended by the Rules of Navigation of the Suez Canal Authority, and is registered in the Suez Canal Tonnage Certificate.
        # fmt: on

    applicability = models.ForeignKey(
        Applicability, on_delete=models.CASCADE, related_name="vessels_measurements"
    )
    vessels_characteristics = models.CharField(
        max_length=255, choices=VesselsCharacteristics.choices
    )
    comparison_operator = models.CharField(
        max_length=255, choices=ComparisonOperator.choices
    )

    # https://github.com/betagouv/SPPNautInterface/issues/232
    # https://github.com/betagouv/SPPNautInterface/issues/233
    vessels_characteristics_value = models.DecimalField(
        max_digits=10, decimal_places=3, validators=[MinValueValidator(0)]
    )
    vessels_characteristics_unit = models.CharField(
        max_length=255, choices=VesselsCharacteristicsUnit.choices
    )

    def __str__(self):
        if self.pk:
            # FIXME : pluralize and lower case the unit
            return (
                f"{self.VesselsCharacteristics(self.vessels_characteristics).label} "
                f"{self.ComparisonOperator(self.comparison_operator).label} "
                # .normalize() is required on a decimal value to remove trailing zeros.
                # It prevents variation between the output of the decimal value when the
                # object has been fetched from the database or directly instantiated.
                f"{self.vessels_characteristics_value.normalize()} "
                f"{self.VesselsCharacteristicsUnit(self.vessels_characteristics_unit).label}"
            )
        return super().__str__()


class CategoryOfCommPref(models.TextChoices):
    # fmt: off
    PREFERRED_CALLING = "preferred calling" # the first choice channel or frequency to be used when calling a radio station
    ALTERNATE_CALLING = "alternate calling" # a channel or frequency to be used for calling a radio station when the preferred channel or frequency is busy or is suffering from interference
    PREFERRED_WORKING = "preferred working" # the first choice channel or frequency to be used when working with a radio station
    ALTERNATE_WORKING = "alternate working" # a channel or frequency to be used for working with a radio station when the preferred working channel or frequency is busy or is suffering from interference
    # fmt: on


# https://github.com/betagouv/SPPNautInterface/issues/244
class FrequencyPair(s100.models.GenericComplexAttributeType):
    """
    A pair of frequencies for transmitting and receiving radio signals.
    The shore station transmits and receives on the frequencies indicated
    """

    frequency_shore_station_transmits = models.DecimalField(
        max_digits=6,
        decimal_places=1,
        validators=[MinValueValidator(0)],
        help_text="The shore station transmitter frequency expressed in kHz to one decimal place. Units: kHZ, Resolution: 0.1, Format: XXXXXX Examples: 4379.1 kHz becomes 043791; 13162.8 kHz becomes 131628",
    )

    frequency_shore_station_receives = models.DecimalField(
        max_digits=6,
        decimal_places=1,
        validators=[MinValueValidator(0)],
        help_text="The shore station receiver frequency expressed in kHz to one decimal place. Units: kHz, Resolution: 0.1, Format: XXXXXX Examples: 4379.1 kHz becomes 043791; 13162.8 kHz becomes 131628",
    )

    contact_instructions = models.TextField(
        blank=True,
        null=True,
        help_text="Supplemental instructions on how or when to contact the individual, organisation, or service",
    )


# PDF page 26
class ContactDetails(s100.models.InformationType):
    """
    Information on how to reach a person or organisation by postal, internet,
    telephone, telex and radio systems.
    """

    # https://github.com/betagouv/SPPNautInterface/issues/261
    communication_channel = ArrayField(
        models.CharField(max_length=255),
        default=list,
        blank=True,
        help_text="A channel number assigned to a specific radio frequency, frequencies or frequency band.<br/>"
        "Separate multiple values with a comma.<br/>",
    )
    call_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="The designated call name of a station, e.g. radio station, radar station, pilot. Remarks: This is the name used when calling a radio station by radio i.e. 'Singapore Pilots'.",
    )

    call_sign = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="The designated call-sign of a radio station.",
    )

    # Language is not mandatory in the spec. We think it's because the language can be defined once at the XML root level and then is implied.
    # We make it mandatory because we need to know explicitly.
    language = models.CharField(
        max_length=3,
        choices=s100.models.ISO639_3.choices,
        # No description in XSD
    )

    category_of_comm_pref = models.CharField(
        max_length=255,
        choices=CategoryOfCommPref.choices,
        blank=True,
        null=True,
        # No description in XSD
    )

    frequency_pair = GenericRelation(FrequencyPair)

    contact_instructions = models.TextField(
        blank=True,
        null=True,
        help_text="Supplemental instructions on how or when to contact the individual, organisation, or service",
    )
    mmsi_code = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="The Maritime Mobile Service Identity (MMSI) Code is formed of a series of nine digits which are transmitted over the radio path in order to uniquely identify ship stations, ship earth stations, coast stations, coast earth stations, and group calls. These identities are formed in such a way that the identity or part thereof can be used by telephone and telex subscribers connected to the general telecommunications network principally to call ships automatically.",
        validators=[RegexValidator(regex=r"^\d{9}$")],
    )

    information = GenericRelation(s100.models.Information)

    class Meta:
        verbose_name_plural = "Contact Details"


# PDF page 39
class SrvContact(s100.models.GenericManyToMany):
    # ManyToMany
    contactable_content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, related_name="+"
    )
    contactable_object_id = models.BigIntegerField()
    contactable_object = GenericForeignKey(
        "contactable_content_type", "contactable_object_id"
    )
    contact_details = models.ForeignKey(ContactDetails, on_delete=models.CASCADE)


class ContactAddress(s100.models.ComplexAttributeType):
    """
    Direction or superscription of a letter, package, etc., specifying the name
    of the place to which it is directed, and optionally a contact person or
    organisation who should receive it.
    """

    contact_details = models.ForeignKey(
        ContactDetails, on_delete=models.CASCADE, related_name="contact_addresses"
    )

    # https://github.com/betagouv/SPPNautInterface/issues/262
    delivery_point = models.TextField(
        blank=True,
        null=True,
        help_text="Details of where post can be delivered such as the apartment, name and/or number of a street, building or PO Box.",
    )

    city_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="The name of a town or city.",
    )

    postal_code = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Known in various countries as a postcode, or ZIP code, the postal code is a series of letters and/or digits that identifies each postal delivery area.",
    )

    administrative_division = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Administrative division is a generic term for an administrative region within a country at a level below that of the sovereign state.",
    )

    country_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="The name of a nation. (Adapted from The American Heritage Dictionaries)",
    )

    class Meta:
        verbose_name_plural = "Contact Addresses"


class Radiocommunications(s100.models.ComplexAttributeType):
    """
    Detailed radiocommunications description with channels, frequencies,
    preferences and time schedules.
    """

    class CategoryOfMaritimeBroadcast(models.TextChoices):
        # fmt: off
        NAVIGATIONAL_WARNING = "navigational warning" # message containing urgent information relevant to safe navigation broadcast to ships in accordance with the provisions of the International Convention for the Safety of Life at Sea, 1974, as amended
        METEOROLOGICAL_WARNING = "meteorological warning" # warning of adverse weather conditions
        ICE_REPORT = "ice report" # report of the ice situation and restrictions to shipping
        SAR_INFORMATION = "SAR information" # broadcast message with information about an ongoing SAR operation
        PIRATE_ATTACK_WARNING = "pirate attack warning" # warning of possible attack by pirates
        METEOROLOGICAL_FORECAST = "meteorological forecast" # broadcast message containing meteorological forecast
        PILOT_SERVICE_MESSAGE = "pilot service message" # broadcast message about pilot service
        AIS_INFORMATION = "AIS information" # broadcast message about AIS information
        LORAN_MESSAGE = "LORAN message" # broadcast message about the LORAN service
        SATNAV_MESSAGE = "SATNAV message" # broadcast message about Satellite Navigation service
        GALE_WARNING = "gale warning" # warning of winds of Beaufort force 8 or 9
        STORM_WARNING = "storm warning" # warning of winds of Beaufort force 10 or over
        TROPICAL_REVOLVING_STORM_WARNING = "tropical revolving storm warning" # warning of hurricanes in the North Atlantic and eastern North Pacific, typhoons in the Western Pacific, cyclones in the Indian Ocean and cyclones of similar nature in other regions
        NAVAREA_WARNING = "NAVAREA warning" # navigational warning or in-force bulletin promulgated as part of a numbered series by a NAVAREA coordinator (Maritime Safety Information Manual 2009)
        COASTAL_WARNING = "coastal warning" # navigational warning promulgated as part of a numbered series by a National coordinator (Maritime Safety Information Manual 2009)
        LOCAL_WARNING = "local warning" # warning which covers inshore waters, often within the limits of jurisdiction of a harbour or port authority (Maritime Safety Information Manual 2009)
        LOW_WATER_LEVEL_WARNING_NEGATIVE_TIDAL_SURGE = "low water level warning/negative tidal surge" # warning of actual or expected low water level
        ICING_WARNING = "icing warning" # warning of accretion of ice on ships
        TSUNAMI_BROADCAST = "tsunami broadcast" # broadcasts about tsunamis, including watches, advisories, and other types of messages relating to tsunamis or potential tsunamis
        # fmt: on

    class CategoryOfRadioMethods(models.TextChoices):
        # fmt: off
        LOW_FREQUENCY_LF_VOICE_TRAFFIC = "Low Frequency (LF) voice traffic" # Frequency in a frequency range between 30 and 300 kHz used for voice traffic
        MEDIUM_FREQUENCY_MF_VOICE_TRAFFIC = "Medium Frequency (MF) voice traffic" # Frequency in a frequency range between 300 and 3 000kHz used for voice traffic
        HIGH_FREQUENCY_HF_VOICE_TRAFFIC = "High Frequency (HF) voice traffic" # Frequency in a frequency range between 3 and 30 MHz used for voice traffic
        VERY_HIGH_FREQUENCY_VHF_VOICE_TRAFFIC = "Very High Frequency (VHF) voice traffic" # Frequency in a frequency range between 30 and 300 MHz used for voice traffic
        HIGH_FREQUENCY_NARROW_BAND_DIRECT_PRINTING = "High Frequency Narrow Band Direct Printing" # High Frequency Narrow Band Direct Printing
        NAVTEX = "NAVTEX" # Narrow-band direct-printing telegraphy system for transmission of maritime safety information.
        SAFETY_NET = "SafetyNET" # SafetyNET is an international automatic direct- printing satellite-based service for the promulgation of navigational and meteorological warnings, meteorological forecasts and other urgent safety-related messages - maritime safety information (MSI) - to ships.
        NBDP_TELEGRAPHY_NARROW_BAND_DIRECT_PRINTING_TELEGRAPHY = "NBDP Telegraphy (Narrow Band Direct Printing Telegraphy)" # Narrow Band Direct Printing Telegraphy. A communications system consisting of teletypewriters connected to a telephonic network to send and receive wireless signals.
        FACSIMILE = "facsimile" # A method or device for transmitting documents, drawings, photographs, or the like, by means of radio or telephone for exact reproduction elsewhere.
        NAVIP = "NAVIP" # A Russian system transmitting navigational information, send by radio and containing information relevant to coastal waters of foreign countries and high seas.
        LOW_FREQUENCY_LF_DIGITAL_TRAFFIC = "Low Frequency (LF) digital traffic" # Frequency in a frequency range between 30 and 300 kHz used for digital traffic
        MEDIUM_FREQUENCY_MF_DIGITAL_TRAFFIC = "Medium Frequency (MF) digital traffic" # Frequency in a frequency range between 300 and 3000kHz used for digital traffic
        HIGH_FREQUENCY_HF_DIGITAL_TRAFFIC = "High Frequency (HF) digital traffic" # Frequency in a frequency range between 3 and 30 MHz used for digital traffic
        VERY_HIGH_FREQUENCY_VHF_DIGITAL_TRAFFIC = "Very High Frequency (VHF) digital traffic" # Frequency in a frequency range between 30 and 300 MHz used for digital traffic
        LOW_FREQUENCY_LF_TELEGRAPH_TRAFFIC = "Low Frequency (LF) telegraph traffic" # Frequency in a frequency range between 30 and 300 kHz used for telegraph traffic
        MEDIUM_FREQUENCY_MF_TELEGRAPH_TRAFFIC = "Medium Frequency (MF) telegraph traffic" # Frequency in a frequency range between 300 and 3 000kHz used for telegraph traffic
        HIGH_FREQUENCY_HF_TELEGRAPH_TRAFFIC = "High Frequency (HF) telegraph traffic" # Frequency in a frequency range between 3 and 30 MHz used for telegraph traffic
        MEDIUM_FREQUENCY_MF_DIGITAL_SELECTIVE_CALL_TRAFFIC = "Medium Frequency (MF) Digital Selective Call traffic" # Frequency in a frequency range between 300 and 3000kHz used for Digital Selective Call traffic
        HIGH_FREQUENCY_HF_DIGITAL_SELECTIVE_CALL_TRAFFIC = "High Frequency (HF) Digital Selective Call traffic" # Frequency in a frequency range between 3 and 30 MHz used for Digital Selective Call traffic
        VERY_HIGH_FREQUENCY_VHF_DIGITAL_SELECTIVE_CALL_TRAFFIC = "Very High Frequency (VHF) Digital Selective Call traffic" # Frequency in a frequency range between 30 and 300 MHz used for Digital Selective Call traffic
        # fmt: on

    contact_details = models.ForeignKey(
        ContactDetails, on_delete=models.CASCADE, related_name="radiocommunications"
    )

    category_of_comm_pref = models.CharField(
        max_length=255,
        choices=CategoryOfCommPref.choices,
        blank=True,
        null=True,
        # No description in XSD
    )

    category_of_maritime_broadcast = ChoiceArrayField(
        base_field=models.CharField(
            max_length=255,
            choices=CategoryOfMaritimeBroadcast.choices,
        ),
        default=list,
        blank=True,
        help_text="Classification of maritime broadcast based on the nature of information conveyed.",
    )

    category_of_radio_methods = ChoiceArrayField(
        base_field=models.CharField(
            max_length=255,
            choices=CategoryOfRadioMethods.choices,
        ),
        default=list,
        blank=True,
        help_text="Categories of radiocommunications based on frequency band and radio traffic method.",
    )

    communication_channel = ArrayField(
        models.CharField(max_length=255),
        default=list,
        blank=True,
        help_text="A channel number assigned to a specific radio frequency, frequencies or frequency band.<br/>"
        "ℹ️ Write comma separated values to define multiple.",
    )

    contact_instructions = models.TextField(
        blank=True,
        null=True,
        help_text="Supplemental instructions on how or when to contact the individual, organisation, or service",
    )

    # Complex attribute used by multiple classes
    frequency_pair = GenericRelation(FrequencyPair)

    # https://github.com/betagouv/SPPNautInterface/issues/240
    signal_frequency = ArrayField(
        models.IntegerField(),
        default=list,
        blank=True,
        # No description in XSD
    )

    # https://github.com/betagouv/SPPNautInterface/issues/241
    transmission_content = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Content of transmission. Remarks: Not to be used if CATMAB is populated",
    )


class Telecommunications(s100.models.ComplexAttributeType):
    """
    A means or channel of communicating at a distance by electrical or
    electromagnetic means such as telegraphy, telephony, or broadcasting.
    """

    class TelecommunicationService(s100.models.CodeList):
        # fmt: off
        VOICE = "voice" # The transfer or exchange of information by using sounds that are being made by mouth and throat when speaking
        FACSIMILE = "facsimile" # a system of transmitting and reproducing graphic matter (as printing or still pictures) by means of signals sent over telephone lines
        SMS = "sms" # Short Message Service, a form of text messaging communication on phones and mobile phones
        DATA = "data" # facts or information used usually to calculate, analyze, or plan something
        STREAMED_DATA = "streamedData" # Streamed data is data that that is constantly received by and presented to an end-user while being delivered by a provider.
        TELEX = "telex" # a system of communication in which messages are sent over long distances by using a telephone system and are printed by using a special machine (called a teletypewriter)
        TELEGRAPH = "telegraph" # an apparatus, system, or process for communication at a distance by electric transmission over wire
        EMAIL = "email" # Messages and other data exchanged between individuals using computers in a network.
        # fmt: on

    telecommunication_service = ChoiceArrayField(
        base_field=models.CharField(
            max_length=255,
            choices=TelecommunicationService.choices,
        ),
        default=list,
        blank=True,
        help_text="Type of telecommunications service",
    )

    telecommunication_identifier = models.CharField(
        max_length=255,
        help_text="Identifier used for contact by means of a telecommunications service, such as a telephone number",
    )

    contact_details = models.ForeignKey(
        ContactDetails, on_delete=models.CASCADE, related_name="telecommunications"
    )

    category_of_comm_pref = models.CharField(
        max_length=255,
        choices=CategoryOfCommPref.choices,
        blank=True,
        null=True,
        # No description in XSD
    )

    contact_instructions = models.TextField(
        blank=True,
        null=True,
        help_text="Instructions on how and when to contact an individual or organisation",
    )

    telcom_carrier = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="The name of provider or type of carrier for a telecommunications service",
    )

    class Meta:
        verbose_name_plural = "Telecommunications"
