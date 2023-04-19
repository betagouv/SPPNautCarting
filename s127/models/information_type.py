from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.contrib.gis.db import models

import s100.models
from s127.models.shared import BooleanChoices, CategoryOfVessel, ChoiceArrayField


class S127Applicability(s100.models.InformationType):
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

    in_ballast = models.BooleanField(
        null=True,
        blank=True,
        help_text="Whether the vessel is in ballast.",
        choices=BooleanChoices.choices,
    )
    # FIXME: check remarks in https://github.com/betagouv/SPPNautS1xyModelisation/blob/main/S127/XSD/S127/1.0.0/20181129/S127.xsd
    # and write corresponding validators
    # Example : If item 7 is used, the nature of dangerous or hazardous cargoes can be amplified with category of dangerous or hazardous cargo.
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
    information = GenericRelation(s100.models.Information)

    def __str__(self):
        # FIXME : check reprensentation
        foo = f"{self.id}"

        if self.category_of_vessel:
            foo = f"{foo} - {self.category_of_vessel}"

        if self.category_of_cargo:
            foo = f"{foo} - {self.category_of_cargo}"

        if self.category_of_dangerous_or_hazardous_cargo:
            foo = f"{foo} - {self.category_of_dangerous_or_hazardous_cargo}"

        return foo

    class Meta:
        verbose_name_plural = "Applicabilities"


class S127PermissionType(models.Model):
    class CategoryOfRelationship(models.TextChoices):
        """
        This attribute expresses the level of insistence for or against an action
        or activity.

        :cvar PROHIBITED: use of facility, waterway or service is forbidden
        :cvar NOT_RECOMMENDED: use of facility, waterway or service is not
            recommended
        :cvar PERMITTED: use of facility, waterway, or service is permitted
            but not required
        :cvar RECOMMENDED: use of facility, waterway, or service is
            recommended
        :cvar REQUIRED: use of facility, waterway, or service is required
        :cvar NOT_REQUIRED: use of facility, waterway, or service is not
            required
        """

        PROHIBITED = "prohibited"
        NOT_RECOMMENDED = "not recommended"
        PERMITTED = "permitted"
        RECOMMENDED = "recommended"
        REQUIRED = "required"
        NOT_REQUIRED = "not required"

    category_of_relationship = models.CharField(
        choices=CategoryOfRelationship.choices, max_length=255
    )

    # ManyToMany
    feature_content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, related_name="+"
    )
    feature_object_id = models.BigIntegerField()
    feature_object = GenericForeignKey("feature_content_type", "feature_object_id")
    applicability = models.ForeignKey(S127Applicability, on_delete=models.CASCADE)


class S127VesselsMeasurements(s100.models.ComplexAttributeType):
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
        S127Applicability, on_delete=models.CASCADE, related_name="vessels_measurements"
    )
    vessels_characteristics = models.CharField(
        max_length=255,
        choices=VesselsCharacteristics.choices,
        blank=True,
        null=True,
    )
    comparison_operator = models.CharField(
        max_length=255,
        choices=ComparisonOperator.choices,
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
