from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Union
from xsdata.models.datatype import XmlDate, XmlPeriod, XmlTime


class ComplianceLevelValue(Enum):
    VALUE_1 = 1
    VALUE_2 = 2


@dataclass
class GmlProfileSchema2:
    """
    This URI references the profile schema to which a GML application schema
    conforms.
    """
    class Meta:
        name = "gmlProfileSchema"
        namespace = "http://www.iho.int/S-100/profile/s100_gmlProfile"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class S100TruncatedDate2:
    """
    built in date types from W3C XML schema, implementing S-100 truncated date.
    """
    class Meta:
        name = "S100_TruncatedDate"
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    g_day: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "gDay",
            "type": "Element",
            "namespace": "",
        }
    )
    g_month: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "gMonth",
            "type": "Element",
            "namespace": "",
        }
    )
    g_year: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "gYear",
            "type": "Element",
            "namespace": "",
        }
    )
    g_month_day: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "gMonthDay",
            "type": "Element",
            "namespace": "",
        }
    )
    g_year_month: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "gYearMonth",
            "type": "Element",
            "namespace": "",
        }
    )
    date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class ActionOrActivityTypeValue(Enum):
    """
    :cvar NAVIGATING_WITH_A_PILOT: Carrying a qualified pilot as part of
        the vessel navigation team.
    :cvar ENTERING_PORT: navigating a vessel into a port
    :cvar LEAVING_PORT: Navigating a vessel out of a port.
    :cvar BERTHING: Attaching a vessel to a wharf or jetty.
    :cvar SLIPPING: Detaching a vessel from a wharf or jetty.
    :cvar ANCHORING: Attaching a vessel to the seabed by means of an
        anchor and cable.
    :cvar WEIGHING_ANCHOR: Detaching a vessel from the seabed by
        recovering an anchor and cable.
    :cvar TRANSITING: Navigating a vessel along a route or through a
        narrow gap, such as under a bridge or through a lock.
    :cvar OVERTAKING: Navigating a vessel past another traveling broadly
        in the same direction.
    :cvar REPORTING: Providing details such as the name, location or
        intentions of a vessel
    :cvar WORKING_CARGO: Loading or unloading cargo
    :cvar LANDING: Placing crew or passengers on shore.
    :cvar DIVING: Placing a swimmer with an air supply below the sea
        surface.
    :cvar FISHING: Hunting or catching fish.
    :cvar DISCHARGING_OVERBOARD: Releasing anything into the sea; often
        ballast water; or spoil from dredging elsewhere.
    :cvar PASSING: Navigating a vessel past another traveling broadly in
        the opposite direction.
    """
    NAVIGATING_WITH_A_PILOT = "navigating with a pilot"
    ENTERING_PORT = "entering port"
    LEAVING_PORT = "leaving port"
    BERTHING = "berthing"
    SLIPPING = "slipping"
    ANCHORING = "anchoring"
    WEIGHING_ANCHOR = "weighing anchor"
    TRANSITING = "transiting"
    OVERTAKING = "overtaking"
    REPORTING = "reporting"
    WORKING_CARGO = "working cargo"
    LANDING = "landing"
    DIVING = "diving"
    FISHING = "fishing"
    DISCHARGING_OVERBOARD = "discharging overboard"
    PASSING = "passing"


class CardinalDirectionType(Enum):
    """
    Principal and intermediate compass points.

    :cvar N: North
    :cvar NNE: Northnortheast
    :cvar NE: Northeast
    :cvar ENE: Eastnortheast
    :cvar E: East
    :cvar ESE: Eastsoutheast
    :cvar SE: Southeast
    :cvar SSE: Southsoutheast
    :cvar S: South
    :cvar SSW: Southsouthwest
    :cvar SW: Southwest
    :cvar WSW: Westsouthwest
    :cvar W: West
    :cvar WNW: Westnorthwest
    :cvar NW: Northwest
    :cvar NNW: Northnorthwest
    """
    N = "N"
    NNE = "NNE"
    NE = "NE"
    ENE = "ENE"
    E = "E"
    ESE = "ESE"
    SE = "SE"
    SSE = "SSE"
    S = "S"
    SSW = "SSW"
    SW = "SW"
    WSW = "WSW"
    W = "W"
    WNW = "WNW"
    NW = "NW"
    NNW = "NNW"


class CategoryOfAuthorityType(Enum):
    """
    The type of person, government agency or organisation granted powers of
    managing or controlling access to and/or activity in an area.

    :cvar CUSTOMS: The agency or establishment for collecting duties,
        tolls. (Merriam-Websters online Dictionary 23rd February 2006,
        amended).
    :cvar BORDER_CONTROL: The administration to prevent or detect and
        prosecute violations of rules and regulations at international
        boundaries (adapted from Merriam-Websters online Dictionary 23rd
        February 2006).
    :cvar POLICE: The department of government, or civil force, charged
        with maintaining public order. (Adapted from OED)
    :cvar PORT: Person or corporation, owners of, or entrusted with or
        invested with the power of managing a port. May be called a
        Harbour Board, Port Trust, Port Commission, Harbour Commission,
        Marine Department (NP 100 8th Edition 14 Oct 2004)
    :cvar IMMIGRATION: The authority controlling people entering a
        country.
    :cvar HEALTH: The authority with responsibility for checking the
        validity of the health declaration of a vessel and for declaring
        free pratique.
    :cvar COAST_GUARD: Organisation keeping watch on shipping and
        coastal waters according to governmental law; normally the
        authority with reponsibility for search and rescue.
    :cvar AGRICULTURAL: The authority with responsibility for preventing
        infection of the agriculture of a country and for the protection
        of the agricultural interests of a country.
    :cvar MILITARY: A military authority which provides control of
        access to or approval for transit through designated areas or
        airspace.
    :cvar PRIVATE_COMPANY: A private or publicly owned company or
        commercial enterprise which exercises control of facilities, for
        example a callibration area.
    :cvar MARITIME_POLICE: A governmental or military force with
        jurisdiction in territorial waters. Examples could include
        Gendarmerie Maritime, Carabinierie, and Guardia Civil.
    :cvar ENVIRONMENTAL: An authority with responsibility for the
        protection of the environment.
    :cvar FISHERY: An authority with responsibility for the control of
        fisheries.
    :cvar FINANCE: an authority with responsibility for the control and
        movement of money.
    :cvar MARITIME: A national or regional authority charged with
        administration of maritime affairs.
    """
    CUSTOMS = "customs"
    BORDER_CONTROL = "border control"
    POLICE = "police"
    PORT = "port"
    IMMIGRATION = "immigration"
    HEALTH = "health"
    COAST_GUARD = "coast guard"
    AGRICULTURAL = "agricultural"
    MILITARY = "military"
    PRIVATE_COMPANY = "private company"
    MARITIME_POLICE = "maritime police"
    ENVIRONMENTAL = "environmental"
    FISHERY = "fishery"
    FINANCE = "finance"
    MARITIME = "maritime"


class CategoryOfCargoType(Enum):
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


class CategoryOfCommPrefType(Enum):
    """
    :cvar PREFERRED_CALLING: the first choice channel or frequency to be
        used when calling a radio station
    :cvar ALTERNATE_CALLING: a channel or frequency to be used for
        calling a radio station when the preferred channel or frequency
        is busy or is suffering from interference
    :cvar PREFERRED_WORKING: the first choice channel or frequency to be
        used when working with a radio station
    :cvar ALTERNATE_WORKING: a channel or frequency to be used for
        working with a radio station when the preferred working channel
        or frequency is busy or is suffering from interference
    """
    PREFERRED_CALLING = "preferred calling"
    ALTERNATE_CALLING = "alternate calling"
    PREFERRED_WORKING = "preferred working"
    ALTERNATE_WORKING = "alternate working"


class CategoryOfConcentrationOfShippingHazardAreaType(Enum):
    """
    Classification of shipping hazards due to traffic volume or density.

    :cvar CONCENTRATION_OF_MERCHANT_SHIPPING: Concentration of vessels
        whose primary purpose is to engage in commerce, including
        ferries.
    :cvar CONCENTRATION_OF_RECREATIONAL_VESSELS: Concentration of
        powered or sailing vessels principally engaged in recreation,
        leisure, or sporting competition.
    :cvar CONCENTRATION_OF_FISHING_VESSELS: Concentration of vessels
        whose primary purpose is to hunt, trap or process fish. The
        concentration could be on the fishing ground, in transit or in
        the approaches to home bases or fish markets.
    :cvar CONCENTRATION_OF_MILITARY_VESSELS: Concentration of vessels
        principally engaged in military activities. This includes
        activities based on mandate of international organisations (e.g.
        UN). The concentration is in areas others than military exercise
        areas.
    """
    CONCENTRATION_OF_MERCHANT_SHIPPING = "concentration of merchant shipping"
    CONCENTRATION_OF_RECREATIONAL_VESSELS = "concentration of recreational vessels"
    CONCENTRATION_OF_FISHING_VESSELS = "concentration of fishing vessels"
    CONCENTRATION_OF_MILITARY_VESSELS = "concentration of military vessels"


class CategoryOfDangerousOrHazardousCargoType(Enum):
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


class CategoryOfMaritimeBroadcastType(Enum):
    """
    Classification of maritime broadcast based on the nature of information
    conveyed.

    :cvar NAVIGATIONAL_WARNING: message containing urgent information
        relevant to safe navigation broadcast to ships in accordance
        with the provisions of the International Convention for the
        Safety of Life at Sea, 1974, as amended
    :cvar METEOROLOGICAL_WARNING: warning of adverse weather conditions
    :cvar ICE_REPORT: report of the ice situation and restrictions to
        shipping
    :cvar SAR_INFORMATION: broadcast message with information about an
        ongoing SAR operation
    :cvar PIRATE_ATTACK_WARNING: warning of possible attack by pirates
    :cvar METEOROLOGICAL_FORECAST: broadcast message containing
        meteorological forecast
    :cvar PILOT_SERVICE_MESSAGE: broadcast message about pilot service
    :cvar AIS_INFORMATION: broadcast message about AIS information
    :cvar LORAN_MESSAGE: broadcast message about the LORAN service
    :cvar SATNAV_MESSAGE: broadcast message about Satellite Navigation
        service
    :cvar GALE_WARNING: warning of winds of Beaufort force 8 or 9
    :cvar STORM_WARNING: warning of winds of Beaufort force 10 or over
    :cvar TROPICAL_REVOLVING_STORM_WARNING: warning of hurricanes in the
        North Atlantic and eastern North Pacific, typhoons in the
        Western Pacific, cyclones in the Indian Ocean and cyclones of
        similar nature in other regions
    :cvar NAVAREA_WARNING: navigational warning or in-force bulletin
        promulgated as part of a numbered series by a NAVAREA
        coordinator (Maritime Safety Information Manual 2009)
    :cvar COASTAL_WARNING: navigational warning promulgated as part of a
        numbered series by a National coordinator (Maritime Safety
        Information Manual 2009)
    :cvar LOCAL_WARNING: warning which covers inshore waters, often
        within the limits of jurisdiction of a harbour or port authority
        (Maritime Safety Information Manual 2009)
    :cvar LOW_WATER_LEVEL_WARNING_NEGATIVE_TIDAL_SURGE: warning of
        actual or expected low water level
    :cvar ICING_WARNING: warning of accretion of ice on ships
    :cvar TSUNAMI_BROADCAST: broadcasts about tsunamis, including
        watches, advisories, and other types of messages relating to
        tsunamis or potential tsunamis
    """
    NAVIGATIONAL_WARNING = "navigational warning"
    METEOROLOGICAL_WARNING = "meteorological warning"
    ICE_REPORT = "ice report"
    SAR_INFORMATION = "SAR information"
    PIRATE_ATTACK_WARNING = "pirate attack warning"
    METEOROLOGICAL_FORECAST = "meteorological forecast"
    PILOT_SERVICE_MESSAGE = "pilot service message"
    AIS_INFORMATION = "AIS information"
    LORAN_MESSAGE = "LORAN message"
    SATNAV_MESSAGE = "SATNAV message"
    GALE_WARNING = "gale warning"
    STORM_WARNING = "storm warning"
    TROPICAL_REVOLVING_STORM_WARNING = "tropical revolving storm warning"
    NAVAREA_WARNING = "NAVAREA warning"
    COASTAL_WARNING = "coastal warning"
    LOCAL_WARNING = "local warning"
    LOW_WATER_LEVEL_WARNING_NEGATIVE_TIDAL_SURGE = "low water level warning/negative tidal surge"
    ICING_WARNING = "icing warning"
    TSUNAMI_BROADCAST = "tsunami broadcast"


class CategoryOfMilitaryPracticeAreaType(Enum):
    """
    Classification of area by military use.

    :cvar TORPEDO_EXERCISE_AREA: An area within which exercises are
        carried out with torpedoes.
    :cvar SUBMARINE_EXERCISE_AREA: An area within which submarine
        exercises are carried out.
    :cvar FIRING_DANGER_AREA: Areas for bombing and missile exercises.
    :cvar MINE_LAYING_PRACTICE_AREA: An area within which mine-laying
        exercises are carried out.
    :cvar SMALL_ARMS_FIRING_RANGE: An area for shooting pistols, rifles
        and machine guns, etc. at a target.
    """
    TORPEDO_EXERCISE_AREA = "torpedo exercise area"
    SUBMARINE_EXERCISE_AREA = "submarine exercise area"
    FIRING_DANGER_AREA = "firing danger area"
    MINE_LAYING_PRACTICE_AREA = "mine-laying practice area"
    SMALL_ARMS_FIRING_RANGE = "small arms firing range"


class CategoryOfNavigationLineType(Enum):
    """
    Classification of route guidance given to vessels.

    :cvar CLEARING_LINE: A straight line that marks the boundary between
        a safe and a dangerous area or that passes clear of a
        navigational danger.
    :cvar TRANSIT_LINE: A line passing through one or more fixed marks.
    :cvar LEADING_LINE_BEARING_A_RECOMMENDED_TRACK: A line passing
        through one or more clearly defined features, along the path of
        which a vessel can approach safely up to a certain distance off.
    """
    CLEARING_LINE = "clearing line"
    TRANSIT_LINE = "transit line"
    LEADING_LINE_BEARING_A_RECOMMENDED_TRACK = "leading line bearing a recommended track"


class CategoryOfPilotBoardingPlaceType(Enum):
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


class CategoryOfPilotType(Enum):
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


class CategoryOfPreferenceType(Enum):
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


class CategoryOfRadioMethodsType(Enum):
    """
    Categories of radiocommunications based on frequency band and radio traffic
    method.

    :cvar LOW_FREQUENCY_LF_VOICE_TRAFFIC: Frequency in a frequency range
        between 30 and 300 kHz used for voice traffic
    :cvar MEDIUM_FREQUENCY_MF_VOICE_TRAFFIC: Frequency in a frequency
        range between 300 and 3 000kHz used for voice traffic
    :cvar HIGH_FREQUENCY_HF_VOICE_TRAFFIC: Frequency in a frequency
        range between 3 and 30 MHz used for voice traffic
    :cvar VERY_HIGH_FREQUENCY_VHF_VOICE_TRAFFIC: Frequency in a
        frequency range between 30 and 300 MHz used for voice traffic
    :cvar HIGH_FREQUENCY_NARROW_BAND_DIRECT_PRINTING: High Frequency
        Narrow Band Direct Printing
    :cvar NAVTEX: Narrow-band direct-printing telegraphy system for
        transmission of maritime safety information.
    :cvar SAFETY_NET: SafetyNET is an international automatic direct-
        printing satellite-based service for the promulgation of
        navigational and meteorological warnings, meteorological
        forecasts and other urgent safety-related messages - maritime
        safety information (MSI) - to ships.
    :cvar NBDP_TELEGRAPHY_NARROW_BAND_DIRECT_PRINTING_TELEGRAPHY: Narrow
        Band Direct Printing Telegraphy. A communications system
        consisting of teletypewriters connected to a telephonic network
        to send and receive wireless signals.
    :cvar FACSIMILE: A method or device for transmitting documents,
        drawings, photographs, or the like, by means of radio or
        telephone for exact reproduction elsewhere.
    :cvar NAVIP: A Russian system transmitting navigational information,
        send by radio and containing information relevant to coastal
        waters of foreign countries and high seas.
    :cvar LOW_FREQUENCY_LF_DIGITAL_TRAFFIC: Frequency in a frequency
        range between 30 and 300 kHz used for digital traffic
    :cvar MEDIUM_FREQUENCY_MF_DIGITAL_TRAFFIC: Frequency in a frequency
        range between 300 and 3000kHz used for digital traffic
    :cvar HIGH_FREQUENCY_HF_DIGITAL_TRAFFIC: Frequency in a frequency
        range between 3 and 30 MHz used for digital traffic
    :cvar VERY_HIGH_FREQUENCY_VHF_DIGITAL_TRAFFIC: Frequency in a
        frequency range between 30 and 300 MHz used for digital traffic
    :cvar LOW_FREQUENCY_LF_TELEGRAPH_TRAFFIC: Frequency in a frequency
        range between 30 and 300 kHz used for telegraph traffic
    :cvar MEDIUM_FREQUENCY_MF_TELEGRAPH_TRAFFIC: Frequency in a
        frequency range between 300 and 3 000kHz used for telegraph
        traffic
    :cvar HIGH_FREQUENCY_HF_TELEGRAPH_TRAFFIC: Frequency in a frequency
        range between 3 and 30 MHz used for telegraph traffic
    :cvar MEDIUM_FREQUENCY_MF_DIGITAL_SELECTIVE_CALL_TRAFFIC: Frequency
        in a frequency range between 300 and 3000kHz used for Digital
        Selective Call traffic
    :cvar HIGH_FREQUENCY_HF_DIGITAL_SELECTIVE_CALL_TRAFFIC: Frequency in
        a frequency range between 3 and 30 MHz used for Digital
        Selective Call traffic
    :cvar VERY_HIGH_FREQUENCY_VHF_DIGITAL_SELECTIVE_CALL_TRAFFIC:
        Frequency in a frequency range between 30 and 300 MHz used for
        Digital Selective Call traffic
    """
    LOW_FREQUENCY_LF_VOICE_TRAFFIC = "Low Frequency (LF) voice traffic"
    MEDIUM_FREQUENCY_MF_VOICE_TRAFFIC = "Medium Frequency (MF) voice traffic"
    HIGH_FREQUENCY_HF_VOICE_TRAFFIC = "High Frequency (HF) voice traffic"
    VERY_HIGH_FREQUENCY_VHF_VOICE_TRAFFIC = "Very High Frequency (VHF) voice traffic"
    HIGH_FREQUENCY_NARROW_BAND_DIRECT_PRINTING = "High Frequency Narrow Band Direct Printing"
    NAVTEX = "NAVTEX"
    SAFETY_NET = "SafetyNET"
    NBDP_TELEGRAPHY_NARROW_BAND_DIRECT_PRINTING_TELEGRAPHY = "NBDP Telegraphy (Narrow Band Direct Printing Telegraphy)"
    FACSIMILE = "facsimile"
    NAVIP = "NAVIP"
    LOW_FREQUENCY_LF_DIGITAL_TRAFFIC = "Low Frequency (LF) digital traffic"
    MEDIUM_FREQUENCY_MF_DIGITAL_TRAFFIC = "Medium Frequency (MF) digital traffic"
    HIGH_FREQUENCY_HF_DIGITAL_TRAFFIC = "High Frequency (HF) digital traffic"
    VERY_HIGH_FREQUENCY_VHF_DIGITAL_TRAFFIC = "Very High Frequency (VHF) digital traffic"
    LOW_FREQUENCY_LF_TELEGRAPH_TRAFFIC = "Low Frequency (LF) telegraph traffic"
    MEDIUM_FREQUENCY_MF_TELEGRAPH_TRAFFIC = "Medium Frequency (MF) telegraph traffic"
    HIGH_FREQUENCY_HF_TELEGRAPH_TRAFFIC = "High Frequency (HF) telegraph traffic"
    MEDIUM_FREQUENCY_MF_DIGITAL_SELECTIVE_CALL_TRAFFIC = "Medium Frequency (MF) Digital Selective Call traffic"
    HIGH_FREQUENCY_HF_DIGITAL_SELECTIVE_CALL_TRAFFIC = "High Frequency (HF) Digital Selective Call traffic"
    VERY_HIGH_FREQUENCY_VHF_DIGITAL_SELECTIVE_CALL_TRAFFIC = "Very High Frequency (VHF) Digital Selective Call traffic"


class CategoryOfRelationshipType(Enum):
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


class CategoryOfRestrictedAreaType(Enum):
    """
    The official legal status of each kind of restricted area defines the kind
    of restriction(s), e.g., the restriction for a 'game preserve' may be
    'entering prohibited', the restriction for an 'anchoring prohibition area'
    is 'anchoring prohibited'.

    :cvar NATURE_RESERVE: A tract of land or water managed so as to
        preserve it's flora, fauna, physical features, etc.
    :cvar BIRD_SANCTUARY: A place where birds are bred and protected.
    :cvar GAME_RESERVE: A place where wild animals or birds hunted for
        sport or food are kept undisturbed for private use.
    :cvar SEAL_SANCTUARY: A place where seals are protected.
    :cvar HISTORIC_WRECK_AREA: An area around certain wrecks of
        historical importance to protect the wrecks from unauthorized
        interference by diving, salvage or deposition (including
        anchoring).
    :cvar RESEARCH_AREA: an area where marine research takes place.
    :cvar FISH_SANCTUARY: A place where fish are protected.
    :cvar ECOLOGICAL_RESERVE: A tract of land or water managed so as to
        preserve the relation of plants and living creatures to each
        other and to their surroundings.
    :cvar ENVIRONMENTALLY_SENSITIVE_SEA_AREA: A generic term which may
        be used to describe a wide range of areas, considered sensitive
        for a variety of environmental reasons.
    :cvar PARTICULARLY_SENSITIVE_SEA_AREA: An area that needs special
        protection through action by IMO because of its significance for
        regional ecological, socio-economic or scientific reasons and
        because it may be vulnerable to damage by international shipping
        activities.
    :cvar CORAL_SANCTUARY: A place where coral is protected. (TSMAD 29)
    :cvar RECREATION_AREA: An area within which recreational activities
        regularly take place and therefore vessel movement may be
        restricted. (Adapted from S-57 Edition 3.1, Appendix A – Chapter
        2, Page 2.76, November 2000).
    :cvar MILITARY_AREA: An area controlled by the military in which
        restrictions may apply.
    :cvar NAVIGATIONAL_AID_SAFETY_ZONE: An area around a navigational
        aid which vessels are prohibited from entering.
    :cvar MINEFIELD: An area laid and maintained with explosive mines
        for defence or practice purposes.
    :cvar WAITING_AREA: An area reserved for vessels waiting to enter a
        harbour.
    :cvar SWINGING_AREA: An area where vessels turn.
    :cvar DISENGAGEMENT_AREA: An area near a fairway where vessels can
        go to clear the way or make an about turn and possibly return to
        a waiting area when the nautical conditions impose it.
    :cvar PORT_SECURITY_AREA:
    :cvar OFFSHORE_SAFETY_ZONE: The area around an offshore installation
        within which vessels are prohibited from entering without
        permission. Special regulations protect installations within a
        safety zone and vessels of all nationalities are required to
        respect the zone.
    :cvar DEGAUSSING_RANGE: an area, usually about two cables diameter,
        within which ships' magnetic fields may be measured sensing
        instruments and cables are installed on the sea bed in the range
        and there are cables leading from the range to a control
        position ashore.
    """
    NATURE_RESERVE = "nature reserve"
    BIRD_SANCTUARY = "bird sanctuary"
    GAME_RESERVE = "game reserve"
    SEAL_SANCTUARY = "seal sanctuary"
    HISTORIC_WRECK_AREA = "historic wreck area"
    RESEARCH_AREA = "research area"
    FISH_SANCTUARY = "fish sanctuary"
    ECOLOGICAL_RESERVE = "ecological reserve"
    ENVIRONMENTALLY_SENSITIVE_SEA_AREA = "environmentally sensitive sea area"
    PARTICULARLY_SENSITIVE_SEA_AREA = "particularly sensitive sea area"
    CORAL_SANCTUARY = "coral sanctuary"
    RECREATION_AREA = "recreation area"
    MILITARY_AREA = "military area"
    NAVIGATIONAL_AID_SAFETY_ZONE = "navigational aid safety zone"
    MINEFIELD = "minefield"
    WAITING_AREA = "waiting area"
    SWINGING_AREA = "swinging area"
    DISENGAGEMENT_AREA = "disengagement area"
    PORT_SECURITY_AREA = "port security area"
    OFFSHORE_SAFETY_ZONE = "offshore safety zone"
    DEGAUSSING_RANGE = "degaussing range"


class CategoryOfRouteingMeasureType(Enum):
    """
    Classification of routeing measures by type.

    :cvar ARCHIPELAGIC_SEA_LANE: Sea lanes designated by an archipelagic
        State for the passage of ships and aircraft.
    :cvar DEEP_WATER_ROUTE: A route within defined limits which has been
        accurately surveyed for clearance of sea bottom and submerged
        obstacles as indicated on the chart.
    :cvar FAIRWAY_SYSTEM: That part of a river, harbour and so on, where
        the main navigable channel for vessels of larger size lies. It
        is also the usual course followed by vessels entering or leaving
        harbours, called “ship channel”.
    :cvar RECOMMENDED_ROUTE: A navigation line, range system, or a
        recommended track, lane, or route.
    :cvar TRAFFIC_SEPARATION_SCHEME: A scheme which aims to reduce the
        risk of collision in congested and/or converging areas by
        separating traffic moving in opposite, or nearly opposite,
        directions.
    :cvar TWO_WAY_ROUTE: A route within defined limits inside which two
        way traffic is established, aimed at providing safe passage of
        ships through waters where navigation is difficult or dangerous.
    """
    ARCHIPELAGIC_SEA_LANE = "archipelagic sea lane"
    DEEP_WATER_ROUTE = "deep water route"
    FAIRWAY_SYSTEM = "fairway system"
    RECOMMENDED_ROUTE = "recommended route"
    TRAFFIC_SEPARATION_SCHEME = "traffic separation scheme"
    TWO_WAY_ROUTE = "two-way route"


class CategoryOfRxNtypeValue(Enum):
    """
    :cvar NAVIGATION: Pertaining to navigation
    :cvar COMMUNICATION: Pertaining to communications
    :cvar ENVIRONMENTAL_PROTECTION: Pertaining to environmental
        protection
    :cvar WILDLIFE_PROTECTION: Pertaining to wildlife protection
    :cvar SECURITY: Pertaining to security
    :cvar CUSTOMS: Pertaining to customs
    :cvar CARGO_OPERATION: Pertaining to cargo operations
    :cvar REFUGE: Pertaining to a place of safety or refuge
    :cvar NATURAL_RESOURCES_OR_EXPLOITATION: Pertaining to natural
        resources or exploitation
    :cvar PORT: Pertaining to a port
    :cvar FINANCE: Pertaining to finance
    :cvar AGRICULTURE: Pertaining to agriculture
    """
    NAVIGATION = "navigation"
    COMMUNICATION = "communication"
    ENVIRONMENTAL_PROTECTION = "environmental protection"
    WILDLIFE_PROTECTION = "wildlife protection"
    SECURITY = "security"
    CUSTOMS = "customs"
    CARGO_OPERATION = "cargo operation"
    REFUGE = "refuge"
    NATURAL_RESOURCES_OR_EXPLOITATION = "natural resources or exploitation"
    PORT = "port"
    FINANCE = "finance"
    AGRICULTURE = "agriculture"


class CategoryOfScheduleTypeValue(Enum):
    """
    :cvar NORMAL_OPERATION: The service, office, is open, fully manned,
        and operating normally, or the area is accessible as usual.
    :cvar CLOSURE: The service, office, or area is closed.
    :cvar UNMANNED_OPERATION: The service is available but not manned.
    """
    NORMAL_OPERATION = "normal operation"
    CLOSURE = "closure"
    UNMANNED_OPERATION = "unmanned operation"


class CategoryOfShipReportType(Enum):
    """Classification of ship reports based on IMO standard report formats.

    Remarks: Through Resolution A.851(20), the IMO encourages authorities to require standard formats and procedures for ship reporting specified at ID 1 to 7 above but recognises that some authorities require amended formats and these cases are covered by ID 8 "any other report".
    (Appendix to IMO Resolution A.851(20) GENERAL PRINCIPLES FOR SHIP REPORTING SYSTEMS AND SHIP REPORTING REQUIREMENTS, INCLUDING GUIDELINES FOR REPORTING INCIDENTS INVOLVING DANGEROUS GOODS, HARMFUL SUBSTANCES AND/OR MARINE POLLUTANTS.)

    :cvar SAILING_PLAN: before or as near as possible to the time of
        departure from a port within a system or when entering the area
        covered by a system [for instance A, B, J, X etc]
    :cvar POSITION_REPORT: when necessary to ensure effective operation
        of the system
    :cvar DEVIATION_REPORT: when the ship’s position varies
        significantly from the position that would have been predicted
        from previous reports, when changing the reported route, or as
        decided by the master
    :cvar FINAL_REPORT: on arrival at the destination or on leaving the
        area covered by the system
    :cvar DANGEROUS_GOODS_REPORT: when an incident takes place involving
        the loss or likely loss overboard of packaged dangerous goods,
        including those in freight containers, portable tanks, road and
        rail vehicles and shipborne barges, into the sea
    :cvar HARMFUL_SUBSTANCES_REPORT: when an incident takes place
        involving the discharge or probable discharge of oil (Annex I of
        MARPOL 73/78) or noxious liquid substances in bulk (Annex II of
        MARPOL 73/78)
    :cvar MARINE_POLLUTANTS_REPORT: in the case of the loss or likely
        loss overboard of harmful substances in packaged form, including
        those in freight containers, portable tanks, road and rail
        vehicles and shipborne barges identified in the International
        Maritime Goods Code as marine pollutants (Annex III of MARPOL
        73/78).
    :cvar ANY_OTHER_REPORT: any other report should be made in
        accordance with the system procedures as notified in accordance
        with paragraph 9 of the general principles
    """
    SAILING_PLAN = "sailing plan"
    POSITION_REPORT = "position report"
    DEVIATION_REPORT = "deviation report"
    FINAL_REPORT = "final report"
    DANGEROUS_GOODS_REPORT = "dangerous goods report"
    HARMFUL_SUBSTANCES_REPORT = "harmful substances report"
    MARINE_POLLUTANTS_REPORT = "marine pollutants report"
    ANY_OTHER_REPORT = "any other report"


class CategoryOfSignalStationTrafficType(Enum):
    """
    Classification of station based on the traffic service provided.

    :cvar PORT_CONTROL: A signal station for the control of vessels
        within a port.
    :cvar PORT_ENTRY_AND_DEPARTURE: A signal station for the control of
        vessels entering or leaving a port.
    :cvar INTERNATIONAL_PORT_TRAFFIC: A signal station displaying
        International Port Traffic signals.
    :cvar BERTHING: A signal station for the control of vessels when
        berthing.
    :cvar DOCK: A signal station for the control of vessels entering or
        leaving a dock.
    :cvar LOCK: A signal station for the control of vessels entering or
        leaving a lock.
    :cvar FLOOD_BARRAGE: A signal station for the control of vessels
        wishing to pass through a flood control barrage.
    :cvar BRIDGE_PASSAGE: A signal station for the control of vessels
        wishing to pass under a bridge.
    :cvar DREDGING: A signal station indicating when dredging is in
        progress.
    :cvar TRAFFIC_CONTROL_LIGHT: Visual signal lights placed in a
        waterway to indicate to shipping the movements authorised at the
        time at which they are shown.
    :cvar ONCOMING_TRAFFIC_INDICATION: Indicates the oncoming traffic on
        an inland waterway.
    """
    PORT_CONTROL = "port control"
    PORT_ENTRY_AND_DEPARTURE = "port entry and departure"
    INTERNATIONAL_PORT_TRAFFIC = "international port traffic"
    BERTHING = "berthing"
    DOCK = "dock"
    LOCK = "lock"
    FLOOD_BARRAGE = "flood barrage"
    BRIDGE_PASSAGE = "bridge passage"
    DREDGING = "dredging"
    TRAFFIC_CONTROL_LIGHT = "traffic control light"
    ONCOMING_TRAFFIC_INDICATION = "oncoming traffic indication"


class CategoryOfSignalStationWarningType(Enum):
    """
    Classification of station based on the warning service provided.

    :cvar DANGER: A signal or message warning of the presence of a
        danger to navigation.
    :cvar MARITIME_OBSTRUCTION: A signal or message warning of the
        presence of a maritime obstruction.
    :cvar CABLE: A signal or message warning of the presence of a cable.
    :cvar MILITARY_PRACTICE: A signal or message warning of activity in
        a military practice area.
    :cvar DISTRESS: A station that may receive or transmit distress
        signals.
    :cvar WEATHER: A visual signal displayed to indicate a weather
        forecast.
    :cvar STORM: A signal or message conveying information about storm
        conditions.
    :cvar ICE: A signal or message conveying information about ice
        conditions.
    :cvar TIME: An accurate signal marking a specified time or time
        interval. It is used primarily for determining errors of
        timepieces. Such signals are usually sent from an observatory by
        radio or telegraph, but visual signals are used at some ports.
    :cvar TIDE: A signal or message conveying information on tidal
        conditions in the area in question.
    :cvar TIDAL_STREAM: A signal or message conveying information on
        condition of tidal currents in the area in question.
    :cvar TIDE_GAUGE: A device for measuring the height of tide. A
        graduated staff in a sheltered area where visual observations
        can be made; or it may consist of an elaborate recording
        instrument making a continuous graphic record of tide height
        against time. Such an instrument is usually actuated by a float
        in a pipe communicating with the sea through a small hole which
        filters out shorter waves.
    :cvar TIDE_SCALE: A visual scale which directly shows the height of
        the water above chart datum or a local datum.
    :cvar DIVING: A signal or message warning of diving activity.
    :cvar WATER_LEVEL_GAUGE: A device for measuring and conveying
        information about the water level (non-tidal) in the area in
        question.
    :cvar VERTICAL_CLEARANCE_INDICATION: An indication of the vertical
        clearance of a bridge, overhead cable, etc.
    :cvar HIGH_WATER_MARK: An indication of the official high water
        level.
    :cvar DEPTH_INDICATION: An indication of the local depth.
    """
    DANGER = "danger"
    MARITIME_OBSTRUCTION = "maritime obstruction"
    CABLE = "cable"
    MILITARY_PRACTICE = "military practice"
    DISTRESS = "distress"
    WEATHER = "weather"
    STORM = "storm"
    ICE = "ice"
    TIME = "time"
    TIDE = "tide"
    TIDAL_STREAM = "tidal stream"
    TIDE_GAUGE = "tide gauge"
    TIDE_SCALE = "tide scale"
    DIVING = "diving"
    WATER_LEVEL_GAUGE = "water level gauge"
    VERTICAL_CLEARANCE_INDICATION = "vertical clearance indication"
    HIGH_WATER_MARK = "high water mark"
    DEPTH_INDICATION = "depth indication"


class CategoryOfTemporalVariationType(Enum):
    """
    An assessment of the likelihood of change over time.

    :cvar EXTREME_EVENT: Indication of the possible impact of a
        significant event (for example hurricane, earthquake, volcanic
        eruption, landslide, etc), which is considered likely to have
        changed the seafloor or landscape significantly.
    :cvar LIKELY_TO_CHANGE: Continuous or frequent change to non-
        bathymetric features (for example river siltation, glacier
        creep/recession, sand dunes, buoys, marine farms, etc.).
    :cvar UNLIKELY_TO_CHANGE: Significant change to the seafloor is not
        expected.
    """
    EXTREME_EVENT = "Extreme Event"
    LIKELY_TO_CHANGE = "Likely to Change"
    UNLIKELY_TO_CHANGE = "Unlikely to Change"


class CategoryOfTextType(Enum):
    """
    Classification of completeness of textual information in relation to the
    source.

    :cvar ABSTRACT_OR_SUMMARY: A statement summarizing the important
        points of a text.
    :cvar EXTRACT: An excerpt or excerpts from a text.
    :cvar FULL_TEXT: The whole text
    """
    ABSTRACT_OR_SUMMARY = "abstract or summary"
    EXTRACT = "extract"
    FULL_TEXT = "full text"


class CategoryOfTrafficSeparationSchemeType(Enum):
    """
    International classification of traffic separation scheme.

    :cvar IMO_ADOPTED: A defined Traffic Separation Scheme that has been
        adopted as an IMO routeing measure.
    :cvar NOT_IMO_ADOPTED: A defined Traffic Separation Scheme that has
        not been adopted as an IMO routeing measure.
    """
    IMO_ADOPTED = "IMO - adopted"
    NOT_IMO_ADOPTED = "not IMO - adopted"


class CategoryOfVesselRegistryType(Enum):
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


class CategoryOfVesselTrafficServiceType(Enum):
    """
    Classification of vessel traffic services based on the nature of the
    control or services provided.

    :cvar INFORMATION_SERVICE: A service to ensure that essential
        information becomes available in time for on-board navigational
        decision-making
    :cvar TRAFFIC_ORGANISATION_SERVICE: A service to assist on-board
        navigational decision-making and to monitor its effects
    :cvar NAVIGATIONAL_ASSISTANCE_SERVICE: A service to prevent the
        development of dangerous maritime traffic situations and to
        provide for the safe and efficient movement of vessel traffic
        within the VTS area
    """
    INFORMATION_SERVICE = "Information Service"
    TRAFFIC_ORGANISATION_SERVICE = "Traffic Organisation Service"
    NAVIGATIONAL_ASSISTANCE_SERVICE = "Navigational Assistance Service"


class CategoryOfVesselTypeValue(Enum):
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
    JACKUP_EXPLORATION_OR_PROJECT_INSTALLATION = "jackup exploration or project installation"
    LIVESTOCK_CARRIER = "livestock carrier"
    SPORT_FISHING = "sport fishing"


class ComparisonOperatorType(Enum):
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


class ConditionType(Enum):
    """
    The various conditions of buildings and other constructions.

    :cvar VALUE:
    :cvar UNDER_CONSTRUCTION: a structure that is in the process of
        being built.
    :cvar UNDER_RECLAMATION: an area of the sea that is being reclaimed
        as land, usually by the dumping of earth and other material.
    :cvar PLANNED_CONSTRUCTION: an area where a future construction is
        planned.
    """
    VALUE = ""
    UNDER_CONSTRUCTION = "under construction"
    UNDER_RECLAMATION = "under reclamation"
    PLANNED_CONSTRUCTION = "planned construction"


@dataclass
class ContactAddressType:
    """
    Direction or superscription of a letter, package, etc., specifying the name
    of the place to which it is directed, and optionally a contact person or
    organisation who should receive it.

    :ivar delivery_point: Details of where post can be delivered such as
        the apartment, name and/or number of a street, building or PO
        Box.
    :ivar city_name: The name of a town or city.
    :ivar administrative_division: Administrative division is a generic
        term for an administrative region within a country at a level
        below that of the sovereign state.
    :ivar country_name: The name of a nation. (Adapted from The American
        Heritage Dictionaries)
    :ivar postal_code: Known in various countries as a postcode, or ZIP
        code, the postal code is a series of letters and/or digits that
        identifies each postal delivery area.
    """
    class Meta:
        name = "contactAddressType"
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    delivery_point: List[str] = field(
        default_factory=list,
        metadata={
            "name": "deliveryPoint",
            "type": "Element",
            "namespace": "",
        }
    )
    city_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "cityName",
            "type": "Element",
            "namespace": "",
        }
    )
    administrative_division: Optional[str] = field(
        default=None,
        metadata={
            "name": "administrativeDivision",
            "type": "Element",
            "namespace": "",
        }
    )
    country_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "countryName",
            "type": "Element",
            "namespace": "",
        }
    )
    postal_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "postalCode",
            "type": "Element",
            "namespace": "",
        }
    )


class DayOfWeekType(Enum):
    """
    :cvar MONDAY: The second day of the week.
    :cvar TUESDAY: The third day of the week.
    :cvar WEDNESDAY: The fourth day of the week.
    :cvar THURSDAY: The fifth day of the week.
    :cvar FRIDAY: The sixth day of the week.
    :cvar SATURDAY: The seventh day of the week.
    :cvar SUNDAY: The first day of the week.
    """
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"


class DynamicResourceType(Enum):
    """
    Whether a vessel must use a shore-based or other resource to obtain up-to-
    date information.

    :cvar STATIC: The information is static, or a source of up-to-date
        information is unavailable or unknown.
    :cvar MANDATORY_EXTERNAL_DYNAMIC: An external source of up-to-date
        information is available and interaction with it to obtain up-
        to-date information is required.
    :cvar OPTIONAL_EXTERNAL_DYNAMIC: An external source of up-to-date
        information is available but interaction with it to obtain up-
        to-date information is not required.
    :cvar ONBOARD_DYNAMIC: Up-to-date information may be computed using
        only onboard resources.
    """
    STATIC = "static"
    MANDATORY_EXTERNAL_DYNAMIC = "mandatory external dynamic"
    OPTIONAL_EXTERNAL_DYNAMIC = "optional external dynamic"
    ONBOARD_DYNAMIC = "onboard dynamic"


@dataclass
class FeatureNameType:
    """
    The complex attribute provides the name of an entity, defines the national
    language of the name, and provides the option to display the name at
    various system display settings.

    :ivar display_name: A statement expressing if a feature name is to
        be displayed in certain display settings or not. Indication:
        Boolean. A True value is an indication that the name is intended
        to be displayed. Remarks: Where it is allowable to encode
        multiple instances of feature name for a single feature
        instance, only one feature name instance can indicate that the
        name is to be displayed (display name set to True).
    :ivar language: The method of human communication, either spoken or
        written, consisting of the use of words in a structured and
        conventional way Remarks: The language is encoded by a character
        code following ISO 639-3
    :ivar name: The individual name of a feature.
    """
    class Meta:
        name = "featureNameType"
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    display_name: Optional[bool] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"\w{3}",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "nillable": True,
        }
    )


@dataclass
class FrequencyPairType:
    """A pair of frequencies for transmitting and receiving radio signals.

    The shore station transmits and receives on the frequencies
    indicated

    :ivar frequency_shore_station_transmits: The shore station
        transmitter frequency expressed in kHz to one decimal place.
        Units: kHZ, Resolution: 0.1, Format: XXXXXX Examples: 4379.1 kHz
        becomes 043791; 13162.8 kHz becomes 131628
    :ivar frequency_shore_station_receives: The shore station receiver
        frequency expressed in kHz to one decimal place. Units: kHz,
        Resolution: 0.1, Format: XXXXXX Examples: 4379.1 kHz becomes
        043791; 13162.8 kHz becomes 131628
    :ivar contact_instructions:
    """
    class Meta:
        name = "frequencyPairType"
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    frequency_shore_station_transmits: List[int] = field(
        default_factory=list,
        metadata={
            "name": "frequencyShoreStationTransmits",
            "type": "Element",
            "namespace": "",
        }
    )
    frequency_shore_station_receives: List[int] = field(
        default_factory=list,
        metadata={
            "name": "frequencyShoreStationReceives",
            "type": "Element",
            "namespace": "",
        }
    )
    contact_instructions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "contactInstructions",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class HorizontalPositionUncertaintyType:
    """The best estimate of the accuracy of a position.

    The uncertaintyVariableFactor sub-attribute is not used in S-127

    :ivar uncertainty_fixed: The best estimate of the fixed horizontal
        or vertical accuracy component for positions, depths, heights,
        vertical distances and vertical clearances.
    """
    class Meta:
        name = "horizontalPositionUncertaintyType"
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    uncertainty_fixed: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "uncertaintyFixed",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": Decimal("0.0"),
            "fraction_digits": 1,
        }
    )


@dataclass
class InformationType:
    """Textual information about the feature.

    The information may be provided as a string of text or as a file
    name of a single external text file that contains the text.

    :ivar file_locator: The string encodes the location of a fragment of
        text or other information in a support file. Remarks: -
        Application schemas must describe how the associated file is
        identified. The associated file will commonly be named in a file
        reference co-attribute of the same complex attribute.; - Each
        DCEG must specify requirements for the format of the associated
        file and the semantics of file locator. For example, the value
        of file locator may be an HTML ID in an HTML file, line number
        in a text file) or a bookmark in a PDF file.
    :ivar file_reference: The string encodes the file name of a single
        external text file that contains the text. Remarks: The
        attribute file reference is generally used for long text strings
        or those that require formatting, however there is no
        restriction on the type of text (except for lexical level) that
        can be held in files referenced by sub-attribute file reference.
    :ivar headline: Words set at the head of a passage or page to
        introduce or categorize
    :ivar language: ISO 639-3 value
    :ivar text: A non-formatted digital text string. Remarks: The
        attribute should be used, for example, to hold the information
        that is shown on paper charts by short cautionary and
        explanatory notes. Therefore text populated in text must not
        exceed 300 characters. Text may be in English or in a national
        language defined by the attribute language. No formatting of
        text is possible within the sub-attribute text. If formatted
        text, or text strings exceeding 300 characters, is required,
        then the attribute file reference must be used.
    """
    class Meta:
        name = "informationType"
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    file_locator: Optional[str] = field(
        default=None,
        metadata={
            "name": "fileLocator",
            "type": "Element",
            "namespace": "",
        }
    )
    file_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "fileReference",
            "type": "Element",
            "namespace": "",
        }
    )
    headline: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


class IspsLevelType(Enum):
    """
    Classification of ISPS security levels according to the ISPS Code.

    :cvar ISPS_LEVEL_1: The level for which minimum appropriate
        protective security measures shall be maintained at all times.
    :cvar ISPS_LEVEL_2: The level for which appropriate additional
        protective security measures shall be maintained for a period of
        time as a result of heightened risk of a security incident.
    :cvar ISPS_LEVEL_3: The level for which further specific protective
        security measures shall be maintained for a limited period of
        time when a security incident is probable or imminent, although
        it may not be possible to identify the specific target.
    """
    ISPS_LEVEL_1 = "ISPS Level 1"
    ISPS_LEVEL_2 = "ISPS Level 2"
    ISPS_LEVEL_3 = "ISPS Level 3"


class LogicalConnectivesType(Enum):
    """
    :cvar LOGICAL_CONJUNCTION: all the conditions described by the other
        attributes of the object, or sub-attributes of the same complex
        attribute, are true
    :cvar LOGICAL_DISJUNCTION: at least one of the conditions described
        by the other attributes of the object, or sub-attributes of the
        same complex attributes, is true
    """
    LOGICAL_CONJUNCTION = "logical conjunction"
    LOGICAL_DISJUNCTION = "logical disjunction "


class MembershipType(Enum):
    """
    Definition required.

    :cvar INCLUDED: Vessels with these characteristics are included in
        the regulation/restriction/recommendation/nautical information.
    :cvar EXCLUDED: Vessels with these characteristics are excluded from
        the regulation/restriction/recommendation/nautical information.
    """
    INCLUDED = "included"
    EXCLUDED = "excluded"


class OnlineFunctionTypeValue(Enum):
    """
    :cvar DOWNLOAD: Online instructions for transferring data from one
        storage device or system to another.
    :cvar INFORMATION: Online information about the resource.
    :cvar OFFLINE_ACCESS: Online instructions for requesting the
        resource from the provider.
    :cvar ORDER: Online order process for obtaining the resource.
    :cvar SEARCH: Online search interface for seeking out information
        about the resource.
    :cvar COMPLETE_METADATA: Complete metadata provided.
    :cvar BROWSE_GRAPHIC: Browse graphic provided.
    :cvar UPLOAD: Online resource upload capability provided.
    :cvar EMAIL_SERVICE: Online email service provided.
    :cvar BROWSING: Online browsing provided.
    :cvar FILE_ACCESS: Online file access provided.
    """
    DOWNLOAD = "download"
    INFORMATION = "information"
    OFFLINE_ACCESS = "offline access"
    ORDER = "order"
    SEARCH = "search"
    COMPLETE_METADATA = "complete metadata"
    BROWSE_GRAPHIC = "browse graphic"
    UPLOAD = "upload"
    EMAIL_SERVICE = "email service"
    BROWSING = "browsing"
    FILE_ACCESS = "file access"


class OperationType(Enum):
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


@dataclass
class OrientationType:
    class Meta:
        name = "orientationType"
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    orientation_uncertainty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "orientationUncertainty",
            "type": "Element",
            "namespace": "",
        }
    )
    orientation_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "orientationValue",
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": Decimal("0.0"),
            "max_inclusive": Decimal("360.0"),
            "fraction_digits": 1,
        }
    )


class PilotMovementType(Enum):
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


class PilotQualificationType(Enum):
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


class QualityOfHorizontalMeasurementType(Enum):
    """
    The degree of reliability attributed to a position.

    :cvar SURVEYED: The position(s) was(were) determined by the
        operation of making measurements for determining the relative
        position of points on, above, or beneath the earth's surface.
        Survey implies a regular, controlled, survey of any date.
    :cvar UNSURVEYED: Survey data does not exist or is very poor
    :cvar INADEQUATELY_SURVEYED: Position data is of very poor quality
    :cvar APPROXIMATE: A position that is considered to be less than
        third-order accuracy, but is generally considered to be within
        30.5 meters of its correct geographic location. Also, may apply
        to a feature whose position does not remain fixed.
    :cvar POSITION_DOUBTFUL: A feature whose position has been reported
        but which is considered to be doubtful
    :cvar UNRELIABLE: A feature's position obtained from questionable or
        unreliable data.
    :cvar REPORTED_NOT_SURVEYED: A feature whose position has been
        reported and its position confirmed by some means other than a
        formal survey such as an independent report of the same feature.
    :cvar REPORTED_NOT_CONFIRMED: A feature whose position has been
        reported and its position has not been confirmed.
    :cvar ESTIMATED: The most probable position of a feature determined
        from incomplete data or data of questionable accuracy.
    :cvar PRECISELY_KNOWN: A position that is of a known value, such as
        the position of an anchor berth or other defined feature.
    :cvar CALCULATED: A position that is computed from data.
    """
    SURVEYED = "surveyed"
    UNSURVEYED = "unsurveyed"
    INADEQUATELY_SURVEYED = "inadequately surveyed"
    APPROXIMATE = "approximate"
    POSITION_DOUBTFUL = "position doubtful"
    UNRELIABLE = "unreliable"
    REPORTED_NOT_SURVEYED = "reported (not surveyed)"
    REPORTED_NOT_CONFIRMED = "reported (not confirmed"
    ESTIMATED = "estimated"
    PRECISELY_KNOWN = "precisely known"
    CALCULATED = "calculated"


class RestrictionType(Enum):
    """
    The official legal statute of each kind of restricted area.

    :cvar ANCHORING_PROHIBITED: An area within which anchoring is not
        permitted.
    :cvar ANCHORING_RESTRICTED: a specified area designated by
        appropriate authority, within which anchoring is restricted in
        accordance with certain specified conditions.
    :cvar FISHING_PROHIBITED: An area within which fishing is not
        permitted.
    :cvar FISHING_RESTRICTED: a specified area designated by appropriate
        authority, within which fishing is restricted in accordance with
        certain specified conditions.
    :cvar TRAWLING_PROHIBITED: An area within which trawling is not
        permitted.
    :cvar TRAWLING_RESTRICTED: a specified area designated by
        appropriate authority, within which trawling is restricted in
        accordance with certain specified conditions.
    :cvar ENTRY_PROHIBITED: An area within which navigation and/or
        anchoring is prohibited.
    :cvar ENTRY_RESTRICTED: a specified area designated by appropriate
        authority, within which navigation is restricted in accordance
        with certain specified conditions.
    :cvar DREDGING_PROHIBITED: An area within which dredging is not
        permitted.
    :cvar DREDGING_RESTRICTED: a specified area designated by
        appropriate authority, within which dredging is restricted in
        accordance with certain specified conditions.
    :cvar DIVING_PROHIBITED: An area within which diving is not
        permitted.
    :cvar DIVING_RESTRICTED: a specified area designated by appropriate
        authority, within which diving is restricted in accordance with
        certain specified conditions.
    :cvar NO_WAKE: Mariners must adjust the speed of their vessels to
        reduce the wave or wash which may cause erosion or disturb
        moored vessels.
    :cvar AREA_TO_BE_AVOIDED: An IMO declared routeing measure
        comprising an area within defined limits in which either
        navigation is particularly hazardous or it is exceptionally
        important to avoid casualties and which should be avoided by all
        ships, or certain classes of ships.
    :cvar CONSTRUCTION_PROHIBITED: The erection of permanent or
        temporary fixed structures or artificial islands is prohibited.
    :cvar DISCHARGING_PROHIBITED: An area in which discharging or
        dumping is prohibited.
    :cvar DISCHARGING_RESTRICTED: A specified area designated by
        appropriate authority, within which discharging or dumping is
        restricted in accordance with certain specified conditions.
    :cvar INDUSTRIAL_OR_MINERAL_EXPLORATION_DEVELOPMENT_PROHIBITED: An
        area in which industrial or mineral exploration and development
        are prohibited.
    :cvar INDUSTRIAL_OR_MINERAL_EXPLORATION_DEVELOPMENT_RESTRICTED: A
        specified area designated by appropriate authority, within which
        industrial or mineral exploration and development is restricted
        in accordance with certain specified conditions.
    :cvar DRILLING_PROHIBITED: An area in which excavating a hole on the
        seabed with a drill is prohibited.
    :cvar DRILLING_RESTRICTED: A specified area designated by
        appropriate authority, within which excavating a hole on the
        seabed with a drill is restricted in accordance with certain
        specified conditions.
    :cvar REMOVAL_OF_HISTORICAL_ARTIFACTS_PROHIBITED: An area in which
        the removal of historical artifacts is prohibited.
    :cvar CARGO_TRANSHIPMENT_LIGHTERING_PROHIBITED: An area in which
        cargo transhipment (lightering) is prohibited.
    :cvar DRAGGING_PROHIBITED: An area in which the dragging or anything
        along the seabed, e.g., bottom trawling, is prohibited.
    :cvar STOPPING_PROHIBITED: An area in which a vessel is prohibited
        from stopping.
    :cvar LANDING_PROHIBITED: An area in which landing is prohibited.
    :cvar SPEED_RESTRICTED: An area in which speed is restricted.
    :cvar OVERTAKING_PROHIBITED: a specified area designated by
        appropriate authority, within which overtaking is generally
        prohibited
    :cvar OVERTAKING_OF_CONVOYS_BY_CONVOYS_PROHIBITED: a specified area
        designated by appropriate authority, within which overtaking
        between convoys prohibited
    :cvar PASSING_OR_OVERTAKING_PROHIBITED: a specified area designated
        by appropriate authority, within which passing or overtaking is
        generally prohibited
    :cvar BERTHING_PROHIBITED: a specified area designated by
        appropriate authority, within which vessels, assemblies of
        floating material or floating establishments may not berth.
    :cvar BERTHING_RESTRICTED: a specified area designated by
        appropriate authority, within which berthing is restricted
    :cvar MAKING_FAST_PROHIBITED: a specified area designated by
        appropriate authority, within which vessels, assemblies of
        floating material or floating establishments may not make fast
        to the bank.
    :cvar MAKING_FAST_RESTRICTED: a specified area designated by
        appropriate authority, within which making fast to the bank is
        restricted
    :cvar TURNING_PROHIBITED: a specified area designated by appropriate
        authority, within which all turning is generally prohibited
    :cvar RESTRICTED_FAIRWAY_DEPTH: an area within which the fairway
        depth is restricted.
    :cvar RESTRICTED_FAIRWAY_WIDTH: an area within which the fairway
        width is restricted.
    :cvar USE_OF_SPUDS_PROHIBITED: The use of anchoring spuds
        (telescopic piles) is prohibited
    :cvar SWIMMING_PROHIBITED: An area in which swimming is prohibited.
    """
    ANCHORING_PROHIBITED = "anchoring prohibited"
    ANCHORING_RESTRICTED = "anchoring restricted"
    FISHING_PROHIBITED = "fishing prohibited"
    FISHING_RESTRICTED = "fishing restricted"
    TRAWLING_PROHIBITED = "trawling prohibited"
    TRAWLING_RESTRICTED = "trawling restricted"
    ENTRY_PROHIBITED = "entry prohibited"
    ENTRY_RESTRICTED = "entry restricted"
    DREDGING_PROHIBITED = "dredging prohibited"
    DREDGING_RESTRICTED = "dredging restricted"
    DIVING_PROHIBITED = "diving prohibited"
    DIVING_RESTRICTED = "diving restricted"
    NO_WAKE = "no wake"
    AREA_TO_BE_AVOIDED = "area to be avoided"
    CONSTRUCTION_PROHIBITED = "construction prohibited"
    DISCHARGING_PROHIBITED = "discharging prohibited"
    DISCHARGING_RESTRICTED = "discharging restricted"
    INDUSTRIAL_OR_MINERAL_EXPLORATION_DEVELOPMENT_PROHIBITED = "industrial or mineral exploration/development prohibited"
    INDUSTRIAL_OR_MINERAL_EXPLORATION_DEVELOPMENT_RESTRICTED = "industrial or mineral exploration/development restricted"
    DRILLING_PROHIBITED = "drilling prohibited"
    DRILLING_RESTRICTED = "drilling restricted"
    REMOVAL_OF_HISTORICAL_ARTIFACTS_PROHIBITED = "removal of historical artifacts prohibited"
    CARGO_TRANSHIPMENT_LIGHTERING_PROHIBITED = "cargo transhipment (lightering) prohibited"
    DRAGGING_PROHIBITED = "dragging prohibited"
    STOPPING_PROHIBITED = "stopping prohibited"
    LANDING_PROHIBITED = "landing prohibited"
    SPEED_RESTRICTED = "speed restricted"
    OVERTAKING_PROHIBITED = "overtaking prohibited"
    OVERTAKING_OF_CONVOYS_BY_CONVOYS_PROHIBITED = "overtaking of convoys by convoys prohibited"
    PASSING_OR_OVERTAKING_PROHIBITED = "passing or overtaking prohibited"
    BERTHING_PROHIBITED = "berthing prohibited"
    BERTHING_RESTRICTED = "berthing restricted"
    MAKING_FAST_PROHIBITED = "making fast prohibited"
    MAKING_FAST_RESTRICTED = "making fast restricted"
    TURNING_PROHIBITED = "turning prohibited"
    RESTRICTED_FAIRWAY_DEPTH = "restricted fairway depth"
    RESTRICTED_FAIRWAY_WIDTH = "restricted fairway width"
    USE_OF_SPUDS_PROHIBITED = "use of spuds prohibited"
    SWIMMING_PROHIBITED = "swimming prohibited"


class SourceTypeType(Enum):
    """
    :cvar LAW_OR_REGULATION: treaty, convention, or international
        agreement; law or regulation issued by a national or other
        authority
    :cvar OFFICIAL_PUBLICATION: publication not having the force of law,
        issued by an international organisation or a national or local
        administration
    :cvar MARINER_REPORT_CONFIRMED: Reported by mariner(s) and confirmed
        by another source
    :cvar MARINER_REPORT_NOT_CONFIRMED: reported by mariner(s) but not
        confirmed
    :cvar INDUSTRY_PUBLICATIONS_AND_REPORTS: shipping and other industry
        publication, including graphics, charts and web sites
    :cvar REMOTELY_SENSED_IMAGES: information obtained from satellite
        images
    :cvar PHOTOGRAPHS: information obtained from photographs
    :cvar PRODUCTS_ISSUED_BY_HO_SERVICES: information obtained from
        products issued by Hydropgrahic Offices
    :cvar NEWS_MEDIA: information obtained from news media
    :cvar TRAFFIC_DATA: information obtained from the analysis of
        traffic data
    """
    LAW_OR_REGULATION = "law or regulation"
    OFFICIAL_PUBLICATION = "official publication"
    MARINER_REPORT_CONFIRMED = "mariner report, confirmed"
    MARINER_REPORT_NOT_CONFIRMED = "mariner report, not confirmed"
    INDUSTRY_PUBLICATIONS_AND_REPORTS = "industry publications and reports"
    REMOTELY_SENSED_IMAGES = "remotely sensed images"
    PHOTOGRAPHS = "photographs"
    PRODUCTS_ISSUED_BY_HO_SERVICES = "products issued by HO services"
    NEWS_MEDIA = "news media"
    TRAFFIC_DATA = "traffic data"


class StatusType(Enum):
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


class TelecommunicationServiceTypeValue(Enum):
    """
    :cvar VOICE: The transfer or exchange of information by using sounds
        that are being made by mouth and throat when speaking
    :cvar FACSIMILE: a system of transmitting and reproducing graphic
        matter (as printing or still pictures) by means of signals sent
        over telephone lines
    :cvar SMS: Short Message Service, a form of text messaging
        communication on phones and mobile phones
    :cvar DATA: facts or information used usually to calculate, analyze,
        or plan something
    :cvar STREAMED_DATA: Streamed data is data that that is constantly
        received by and presented to an end-user while being delivered
        by a provider.
    :cvar TELEX: a system of communication in which messages are sent
        over long distances by using a telephone system and are printed
        by using a special machine (called a teletypewriter)
    :cvar TELEGRAPH: an apparatus, system, or process for communication
        at a distance by electric transmission over wire
    :cvar EMAIL: Messages and other data exchanged between individuals
        using computers in a network.
    """
    VOICE = "voice"
    FACSIMILE = "facsimile"
    SMS = "sms"
    DATA = "data"
    STREAMED_DATA = "streamedData"
    TELEX = "telex"
    TELEGRAPH = "telegraph"
    EMAIL = "email"


class TextJustificationType(Enum):
    """
    The anchor point of a text string.

    :cvar LEFT: The anchor point is at the start of the text string.
    :cvar CENTRED: The anchor point is at the centre of the text string.
    :cvar RIGHT: The anchor point is at the end of the text string.
    """
    LEFT = "left"
    CENTRED = "centred"
    RIGHT = "right"


class TextTypeType(Enum):
    """
    The attribute from which a text string is derived.

    :cvar FEATURE_NAME: Definition required
    """
    FEATURE_NAME = "Feature name"


class TrafficFlowType(Enum):
    """
    Direction of vessels passing a reference point.

    :cvar INBOUND: Traffic flow in a general direction toward a port or
        similar destination.
    :cvar OUTBOUND: Traffic flow in a general direction away from a port
        or similar point of origin.
    :cvar ONE_WAY: Traffic flow in one general direction only.
    :cvar TWO_WAY: Traffic flow in two generally opposite directions.
    """
    INBOUND = "inbound"
    OUTBOUND = "outbound"
    ONE_WAY = "one-way"
    TWO_WAY = "two-way"


class VesselsCharacteristicsType(Enum):
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
    PANAMA_CANAL_UNIVERSAL_MEASUREMENT_SYSTEM_NET_TONNAGE = "Panama Canal/Universal Measurement System net tonnage"
    SUEZ_CANAL_NET_TONNAGE = "Suez Canal net tonnage"
    SUEZ_CANAL_GROSS_TONNAGE = "Suez Canal gross tonnage"


class VesselsCharacteristicsUnitType(Enum):
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
    PANAMA_CANAL_UNIVERSAL_MEASUREMENT_SYSTEM_NET_TONNAGE = "Panama Canal/Universal Measurement System net tonnage"
    SUEZ_CANAL_NET_TONNAGE = "Suez Canal Net Tonnage"
    NONE = "none"
    CUBIC_METRES = "cubic metres"
    SUEZ_CANAL_GROSS_TONNAGE = "Suez Canal Gross Tonnage"


class WaterLevelTrendType(Enum):
    """
    The tendency of water level to change in a particular direction.

    :cvar DECREASING: Becoming smaller in magnitude.
    :cvar INCREASING: Becoming larger in magnitude.
    :cvar STEADY: Constant.
    """
    DECREASING = "decreasing"
    INCREASING = "increasing"
    STEADY = "steady"


@dataclass
class S100TruncatedDate1:
    """
    built in date types from W3C XML schema, implementing S-100 truncated date.
    """
    class Meta:
        name = "S100_TruncatedDate"
        target_namespace = "http://www.iho.int/s100gml/1.0+EXT"

    g_day: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "gDay",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0+EXT",
        }
    )
    g_month: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "gMonth",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0+EXT",
        }
    )
    g_year: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "gYear",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0+EXT",
        }
    )
    g_month_day: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "gMonthDay",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0+EXT",
        }
    )
    g_year_month: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "gYearMonth",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0+EXT",
        }
    )
    date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0+EXT",
        }
    )


@dataclass
class DataSetStructureInformationType:
    """
    Data Set Structure information.

    :ivar dataset_coord_origin_x: Shift used to adjust X coordinate
        before encoding
    :ivar dataset_coord_origin_y: Shift used to adjust Y coordinate
        before encoding
    :ivar dataset_coord_origin_z: Shift used to adjust Z coordinate
        before encoding
    :ivar coord_mult_factor_x: Floating point to integer multiplication
        factor for X coordinate or longitude
    :ivar coord_mult_factor_y: Floating point to integer multiplication
        factor for Y coordinate or latitude
    :ivar coord_mult_factor_z: Floating point to integer multiplication
        factor for Z coordinate or depths or height
    :ivar n_info_rec: Number of information records in the data set
    :ivar n_point_rec: Number of point records in the data set
    :ivar n_multi_point_rec: Number of multipoint records in the data
        set
    :ivar n_curve_rec: Number of curve records in the data set
    :ivar n_composite_curve_rec: Number of composite curve records in
        the data set
    :ivar n_surface_rec: Number of surface records in the data set
    :ivar n_feature_rec: Number of feature records in the data set
    """
    class Meta:
        target_namespace = "http://www.iho.int/s100gml/1.0"

    dataset_coord_origin_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "datasetCoordOriginX",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    dataset_coord_origin_y: Optional[float] = field(
        default=None,
        metadata={
            "name": "datasetCoordOriginY",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    dataset_coord_origin_z: Optional[float] = field(
        default=None,
        metadata={
            "name": "datasetCoordOriginZ",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    coord_mult_factor_x: Optional[int] = field(
        default=None,
        metadata={
            "name": "coordMultFactorX",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    coord_mult_factor_y: Optional[int] = field(
        default=None,
        metadata={
            "name": "coordMultFactorY",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    coord_mult_factor_z: Optional[int] = field(
        default=None,
        metadata={
            "name": "coordMultFactorZ",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    n_info_rec: Optional[int] = field(
        default=None,
        metadata={
            "name": "nInfoRec",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    n_point_rec: Optional[int] = field(
        default=None,
        metadata={
            "name": "nPointRec",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    n_multi_point_rec: Optional[int] = field(
        default=None,
        metadata={
            "name": "nMultiPointRec",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    n_curve_rec: Optional[int] = field(
        default=None,
        metadata={
            "name": "nCurveRec",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    n_composite_curve_rec: Optional[int] = field(
        default=None,
        metadata={
            "name": "nCompositeCurveRec",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    n_surface_rec: Optional[int] = field(
        default=None,
        metadata={
            "name": "nSurfaceRec",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    n_feature_rec: Optional[int] = field(
        default=None,
        metadata={
            "name": "nFeatureRec",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )


@dataclass
class FeatureObjectIdentifier:
    """
    Complex type for feature object identifier combines agency, FIDN, FIDS.
    """
    class Meta:
        target_namespace = "http://www.iho.int/s100gml/1.0"

    agency: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
            "required": True,
            "pattern": r"[a-zA-z0-9][a-zA-z0-9]",
        }
    )
    feature_identification_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "featureIdentificationNumber",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
            "required": True,
            "max_inclusive": 4294967294,
        }
    )
    feature_identification_subdivision: Optional[int] = field(
        default=None,
        metadata={
            "name": "featureIdentificationSubdivision",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
            "required": True,
            "max_inclusive": 65534,
        }
    )


class Iso6391(Enum):
    """
    Utility type for subset of ISO 639-1 alpha-2 language codes.

    :cvar EN: English
    """
    EN = "en"


class MdTopicCategoryCode(Enum):
    """Topic categories in S-100 Edition 1.0.0 and gmxCodelists.xml from OGC ISO 19139 XML schemas - see MD_TopicCategoryCode.
    Alternatives to this enumeration: (1) Add the ISO 19139 schemas to this profile and use the codelist MD_TopicCategoryCode instead.
    (2) Ise numeric codes for literals instead of labels, e.g., "1" instead of "farming".

    :cvar FARMING: rearing of animals and/or cultivation of plants.
        Examples: agriculture, irrigation, aquaculture, plantations,
        herding, pests and diseases affecting crops and livestock
    :cvar BIOTA: flora and/or fauna in natural environment. Examples:
        wildlife, vegetation, biological sciences, ecology, wilderness,
        sealife, wetlands, habitat
    :cvar BOUNDARIES: legal land descriptions. Examples: political and
        administrative boundaries
    :cvar CLIMATOLOGY_METEOROLOGY_ATMOSPHERE: processes and phenomena of
        the atmosphere. Examples: cloud cover, weather, climate,
        atmospheric conditions, climate change, precipitation
    :cvar ECONOMY: economic activities, conditions and employment.
        Examples: production, labour, revenue, commerce, industry,
        tourism and ecotourism, forestry, fisheries, commercial or
        subsistence hunting, exploration and exploitation of resources
        such as minerals, oil and gas
    :cvar ELEVATION: height above or below sea level. Examples:
        altitude, bathymetry, digital elevation models, slope, derived
        products
    :cvar ENVIRONMENT: environmental resources, protection and
        conservation. Examples: environmental pollution, waste storage
        and treatment, environmental impact assessment, monitoring
        environmental risk, nature reserves, landscape
    :cvar GEOSCIENTIFIC_INFORMATION: information pertaining to earth
        sciences. Examples: geophysical features and processes, geology,
        minerals, sciences dealing with the composition, structure and
        origin of the earth s rocks, risks of earthquakes, volcanic
        activity, landslides, gravity information, soils, permafrost,
        hydrogeology, erosion
    :cvar HEALTH: health, health services, human ecology, and safety.
        Examples: disease and illness, factors affecting health,
        hygiene, substance abuse, mental and physical health, health
        services
    :cvar IMAGERY_BASE_MAPS_EARTH_COVER: base maps. Examples: land
        cover, topographic maps, imagery, unclassified images,
        annotations
    :cvar INTELLIGENCE_MILITARY: military bases, structures, activities.
        Examples: barracks, training grounds, military transportation,
        information collection
    :cvar INLAND_WATERS: inland water features, drainage systems and
        their characteristics. Examples: rivers and glaciers, salt
        lakes, water utilization plans, dams, currents, floods, water
        quality, hydrographic charts
    :cvar LOCATION: positional information and services. Examples:
        addresses, geodetic networks, control points, postal zones and
        services, place names
    :cvar OCEANS: features and characteristics of salt water bodies
        (excluding inland waters). Examples: tides, tidal waves, coastal
        information, reefs
    :cvar PLANNING_CADASTRE: information used for appropriate actions
        for future use of the land. Examples: land use maps, zoning
        maps, cadastral surveys, land ownership
    :cvar SOCIETY: characteristics of society and cultures. Examples:
        settlements, anthropology, archaeology, education, traditional
        beliefs, manners and customs, demographic data, recreational
        areas and activities, social impact assessments, crime and
        justice, census information
    :cvar STRUCTURE: man-made construction. Examples: buildings,
        museums, churches, factories, housing, monuments, shops, towers
    :cvar TRANSPORTATION: means and aids for conveying persons and/or
        goods. Examples: roads, airports/airstrips, shipping routes,
        tunnels, nautical charts, vehicle or vessel location,
        aeronautical charts, railways
    :cvar UTILITIES_COMMUNICATION: energy, water and waste systems and
        communications infrastructure and services. Examples:
        hydroelectricity, geothermal, solar and nuclear sources of
        energy, water purification and distribution, sewage collection
        and disposal, electricity and gas distribution, data
        communication, telecommunication, radio, communication networks
    """
    FARMING = "farming"
    BIOTA = "biota"
    BOUNDARIES = "boundaries"
    CLIMATOLOGY_METEOROLOGY_ATMOSPHERE = "climatologyMeteorologyAtmosphere"
    ECONOMY = "economy"
    ELEVATION = "elevation"
    ENVIRONMENT = "environment"
    GEOSCIENTIFIC_INFORMATION = "geoscientificInformation"
    HEALTH = "health"
    IMAGERY_BASE_MAPS_EARTH_COVER = "imageryBaseMapsEarthCover"
    INTELLIGENCE_MILITARY = "intelligenceMilitary"
    INLAND_WATERS = "inlandWaters"
    LOCATION = "location"
    OCEANS = "oceans"
    PLANNING_CADASTRE = "planningCadastre"
    SOCIETY = "society"
    STRUCTURE = "structure"
    TRANSPORTATION = "transportation"
    UTILITIES_COMMUNICATION = "utilitiesCommunication"


class S100CircleByCenterPointTypeAngularDistance(Enum):
    VALUE_360_0 = Decimal("360.0")
    VALUE_360_0_1 = Decimal("-360.0")


@dataclass
class S100GmKnotType:
    """
    S-100 Knot is the GML 3.2.1 definition of Knot with the erroneous "weight"
    element removed.
    """
    class Meta:
        name = "S100_GM_KnotType"
        target_namespace = "http://www.iho.int/s100gml/1.0"

    value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
            "required": True,
        }
    )
    multiplicity: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
            "required": True,
        }
    )


class S100GmKnotTypeType(Enum):
    """This enumeration type specifies values for the knots' type (see ISO
    19107:2003, 6.4.25).

    The S-100 3.1 type extends it with "nonUniform" in keeping with the
    2017 draft of 19107

    :cvar UNIFORM: knots are equally spaced, all multiplicity 1
    :cvar QUASI_UNIFORM: the interior knots are uniform, but the first
        and last have multiplicity one larger than the degree of the
        spline
    :cvar PIECEWISE_BEZIER: the underlying spline is formally a Bézier
        spline, but knot multiplicity is always the degree of the spline
        except at the ends where the knot degree is (p+1). Such a spline
        is a pure Bézier spline between its distinct knots
    :cvar NON_UNIFORM: knots have varying spacing and multiplicity
    """
    UNIFORM = "uniform"
    QUASI_UNIFORM = "quasiUniform"
    PIECEWISE_BEZIER = "piecewiseBezier"
    NON_UNIFORM = "nonUniform"


@dataclass
class AbstractCurveSegmentType:
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    num_derivatives_at_start: int = field(
        default=0,
        metadata={
            "name": "numDerivativesAtStart",
            "type": "Attribute",
        }
    )
    num_derivatives_at_end: int = field(
        default=0,
        metadata={
            "name": "numDerivativesAtEnd",
            "type": "Attribute",
        }
    )
    num_derivative_interior_attribute: int = field(
        default=0,
        metadata={
            "name": "numDerivativeInterior",
            "type": "Attribute",
        }
    )


@dataclass
class AbstractFeatureMemberType:
    """To create a collection of GML features, a property type shall be derived
    by extension from gml:AbstractFeatureMemberType.

    By default, this abstract property type does not imply any ownership
    of the features in the collection. The owns attribute of
    gml:OwnershipAttributeGroup may be used on a property element
    instance to assert ownership of a feature in the collection. A
    collection shall not own a feature already owned by another object.
    """
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class AbstractGmltype:
    class Meta:
        name = "AbstractGMLType"
        target_namespace = "http://www.opengis.net/gml/3.2"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )


@dataclass
class AbstractMemberType:
    """To create a collection of GML Objects that are not all features, a
    property type shall be derived by extension from gml:AbstractMemberType.

    This abstract property type is intended to be used only in object
    types where software shall be able to identify that an instance of
    such an object type is to be interpreted as a collection of objects.
    By default, this abstract property type does not imply any ownership
    of the objects in the collection. The owns attribute of
    gml:OwnershipAttributeGroup may be used on a property element
    instance to assert ownership of an object in the collection. A
    collection shall not own an object already owned by another object.
    """
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class AbstractMetadataPropertyType:
    """To associate metadata described by any XML Schema with a GML object, a
    property element shall be defined whose content model is derived by
    extension from gml:AbstractMetadataPropertyType.

    The value of such a property shall be metadata. The content model of
    such a property type, i.e. the metadata application schema shall be
    specified by the GML Application Schema. By default, this abstract
    property type does not imply any ownership of the metadata. The owns
    attribute of gml:OwnershipAttributeGroup may be used on a metadata
    property element instance to assert ownership of the metadata. If
    metadata following the conceptual model of ISO 19115 is to be
    encoded in a GML document, the corresponding Implementation
    Specification specified in ISO/TS 19139 shall be used to encode the
    metadata information.
    """
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class AbstractRingType:
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractSurfacePatchType:
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"


class AggregationType(Enum):
    SET = "set"
    BAG = "bag"
    SEQUENCE = "sequence"
    ARRAY = "array"
    RECORD = "record"
    TABLE = "table"


@dataclass
class CodeType:
    """gml:CodeType is a generalized type to be used for a term, keyword or
    name.

    It adds a XML attribute codeSpace to a term, where the value of the
    codeSpace attribute (if present) shall indicate a dictionary,
    thesaurus, classification scheme, authority, or pattern for the
    term.
    """
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    code_space: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSpace",
            "type": "Attribute",
        }
    )


class CurveInterpolationType(Enum):
    """gml:CurveInterpolationType is a list of codes that may be used to
    identify the interpolation mechanisms specified by an applicationschema.

    S-100 3.1 note: The list has been extended by adding the S-100 3.1
    interpolations, given that the new draft of ISO 19107 explicitly
    says "As a codelist, there is no intention of limiting the potential
    values ofCurveInterpolation."

    :cvar NONE:
    :cvar LINEAR:
    :cvar GEODESIC:
    :cvar CIRCULAR_ARC3_POINTS:
    :cvar LOXODROMIC: Note that the new draft of 19107 now includes
        "rhumb".
    :cvar ELLIPTICAL:
    :cvar CONIC:
    :cvar CIRCULAR_ARC_CENTER_POINT_WITH_RADIUS:
    :cvar POLYNOMIAL_SPLINE:
    :cvar BEZIER_SPLINE:
    :cvar B_SPLINE:
    :cvar CUBIC_SPLINE:
    :cvar RATIONAL_SPLINE:
    :cvar BLENDED_PARABOLIC:
    """
    NONE = "none"
    LINEAR = "linear"
    GEODESIC = "geodesic"
    CIRCULAR_ARC3_POINTS = "circularArc3Points"
    LOXODROMIC = "loxodromic"
    ELLIPTICAL = "elliptical"
    CONIC = "conic"
    CIRCULAR_ARC_CENTER_POINT_WITH_RADIUS = "circularArcCenterPointWithRadius"
    POLYNOMIAL_SPLINE = "polynomialSpline"
    BEZIER_SPLINE = "bezierSpline"
    B_SPLINE = "bSpline"
    CUBIC_SPLINE = "cubicSpline"
    RATIONAL_SPLINE = "rationalSpline"
    BLENDED_PARABOLIC = "blendedParabolic"


@dataclass
class DirectPositionListType:
    """posList instances (and other instances with the content model specified
    by DirectPositionListType) hold the coordinates for a sequence of direct
    positions within the same coordinate reference system (CRS).

    if no srsName attribute is given, the CRS shall be specified as part
    of the larger context this geometry element is part of, typically a
    geometric object like a point, curve, etc. The optional attribute
    count specifies the number of direct positions in the list. If the
    attribute count is present then the attribute srsDimension shall be
    present, too. The number of entries in the list is equal to the
    product of the dimensionality of the coordinate reference system
    (i.e. it is a derived value of the coordinate reference system
    definition) and the number of direct positions.
    """
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    value: List[float] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
    srs_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Attribute",
        }
    )
    srs_dimension: Optional[int] = field(
        default=None,
        metadata={
            "name": "srsDimension",
            "type": "Attribute",
        }
    )
    count: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DirectPositionType:
    """Direct position instances hold the coordinates for a position within
    some coordinate reference system (CRS).

    Since direct positions, as data types, will often be included in
    larger objects (such as geometry elements) that have references to
    CRS, the srsName attribute will in general be missing, if this
    particular direct position is included in a larger element with such
    a reference to a CRS. In this case, the CRS is implicitly assumed to
    take on the value of the containing object's CRS. if no srsName
    attribute is given, the CRS shall be specified as part of the larger
    context this geometry element is part of, typically a geometric
    object like a point, curve, etc.
    """
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    value: List[float] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
    srs_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Attribute",
        }
    )
    srs_dimension: Optional[int] = field(
        default=None,
        metadata={
            "name": "srsDimension",
            "type": "Attribute",
        }
    )


@dataclass
class InlinePropertyType:
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class MeasureType:
    """gml:MeasureType supports recording an amount encoded as a value of XML
    Schema double, together with a units of measure indicated by an attribute
    uom, short for "units Of measure".

    The value of the uom attribute identifies a reference system for the
    amount, usually a ratio or interval scale.
    """
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[^: /n/r/t]+",
        }
    )


class NilReasonEnumerationValue(Enum):
    INAPPLICABLE = "inapplicable"
    MISSING = "missing"
    TEMPLATE = "template"
    UNKNOWN = "unknown"
    WITHHELD = "withheld"


class SignType(Enum):
    """
    gml:SignType is a convenience type with values "+" (plus) and "-" (minus).
    """
    VALUE = "-"
    VALUE_1 = "+"


class SurfaceInterpolationType(Enum):
    """
    gml:SurfaceInterpolationType is a list of codes that may be used to
    identify the interpolation mechanisms specified by an application schema.
    """
    NONE = "none"
    PLANAR = "planar"
    SPHERICAL = "spherical"
    ELLIPTICAL = "elliptical"
    CONIC = "conic"
    TIN = "tin"
    PARAMETRIC_CURVE = "parametricCurve"
    POLYNOMIAL_SPLINE = "polynomialSpline"
    RATIONAL_SPLINE = "rationalSpline"
    TRIANGULATED_SPLINE = "triangulatedSpline"


@dataclass
class AssociationName:
    class Meta:
        name = "associationName"
        namespace = "http://www.opengis.net/gml/3.2"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class DefaultCodeSpace:
    class Meta:
        name = "defaultCodeSpace"
        namespace = "http://www.opengis.net/gml/3.2"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class GmlProfileSchema1:
    class Meta:
        name = "gmlProfileSchema"
        namespace = "http://www.opengis.net/gml/3.2"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class ReversePropertyName:
    """If the value of an object property is another object and that object
    contains also a property for the association between the two objects, then
    this name of the reverse property may be encoded in a
    gml:reversePropertyName element in an appinfo annotation of the property
    element to document the constraint between the two properties.

    The value of the element shall contain the qualified name of the
    property element.
    """
    class Meta:
        name = "reversePropertyName"
        namespace = "http://www.opengis.net/gml/3.2"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class TargetElement:
    class Meta:
        name = "targetElement"
        namespace = "http://www.opengis.net/gml/3.2"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


class ActuateType(Enum):
    ON_LOAD = "onLoad"
    ON_REQUEST = "onRequest"
    OTHER = "other"
    NONE = "none"


class ShowType(Enum):
    NEW = "new"
    REPLACE = "replace"
    EMBED = "embed"
    OTHER = "other"
    NONE = "none"


class TypeType(Enum):
    SIMPLE = "simple"
    EXTENDED = "extended"
    TITLE = "title"
    RESOURCE = "resource"
    LOCATOR = "locator"
    ARC = "arc"


class LangValue(Enum):
    VALUE = ""


@dataclass
class ComplianceLevel:
    """
    Level 1 = Level 2 =
    """
    class Meta:
        name = "complianceLevel"
        namespace = "http://www.iho.int/S-100/profile/s100_gmlProfile"

    value: Optional[ComplianceLevelValue] = field(
        default=None
    )


@dataclass
class BearingInformationType:
    """A bearing is the direction one object is from another object.

    At least one of the sub-attributes must be present.

    :ivar cardinal_direction:
    :ivar distance: A numeric measure of the spatial separation between
        two locations.
    :ivar information:
    :ivar orientation:
    :ivar sector_bearing:
    """
    class Meta:
        name = "bearingInformationType"
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    cardinal_direction: Optional[CardinalDirectionType] = field(
        default=None,
        metadata={
            "name": "cardinalDirection",
            "type": "Element",
            "namespace": "",
        }
    )
    distance: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": Decimal("0.0"),
        }
    )
    information: List[InformationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    orientation: Optional[OrientationType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    sector_bearing: List[Decimal] = field(
        default_factory=list,
        metadata={
            "name": "sectorBearing",
            "type": "Element",
            "namespace": "",
            "max_occurs": 2,
        }
    )


@dataclass
class FixedDateRangeType:
    """Describes a single fixed period, as the date range between its sub-
    attributes.

    Remarks: Sub-attributes date end and date start must have the calendar year encoded using 4 digits for the calendar year (CCYY). Month (MM) and day (DD) are optional.
    (This definition merges the planned S-100 temporal model with the current S-101 DCEG definition of fixed date range.)

    :ivar date_start: The start date or time of the interval.
    :ivar date_end: The end date or time of the interval.
    """
    class Meta:
        name = "fixedDateRangeType"
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    date_start: Optional[S100TruncatedDate2] = field(
        default=None,
        metadata={
            "name": "dateStart",
            "type": "Element",
            "namespace": "",
        }
    )
    date_end: Optional[S100TruncatedDate2] = field(
        default=None,
        metadata={
            "name": "dateEnd",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class NoticeTimeType:
    """
    :ivar notice_time_hours: The time duration prior to the time the
        service is needed, when notice must be provided to the service
        provider.
    :ivar notice_time_text: Text string qualifying the notice time
        specified in NTCHRS. This may explain the time specification in
        NTCHRS (e.g., “3 working days” for a NTCHRS value of “72” where
        NTCTIM is supposed to be "3 working days") or consist of other
        language qualifying the time, e.g., “On departure from last
        port” or “On passing reporting line XY”).
    :ivar operation:
    """
    class Meta:
        name = "noticeTimeType"
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    notice_time_hours: List[Decimal] = field(
        default_factory=list,
        metadata={
            "name": "noticeTimeHours",
            "type": "Element",
            "namespace": "",
        }
    )
    notice_time_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "noticeTimeText",
            "type": "Element",
            "namespace": "",
        }
    )
    operation: Optional[OperationType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class OnlineResourceType:
    """
    Information about online sources from which a resource or data can be
    obtained (ISO 19115, adapted).

    :ivar linkage: location (address) for on-line access using a URL/URI
        address or similar addressing scheme. (Adapted from ISO
        19115:2014.)
    :ivar protocol: connection protocol to be used. Example: ftp, http
        get KVP, http POST, etc. (ISO 19115)
    :ivar application_profile: name of an application profile that can
        be used with the online resource (ISO 19115)
    :ivar name_of_resource: name of the online resource (ISO 19115,
        adapted)
    :ivar online_resource_description: detailed text description of what
        the online resource is/does (ISO 19115)
    :ivar online_function: code for function performed by the online
        resource (ISO 19115)
    :ivar protocol_request: Request used to access the resource.
        Structure and content depend on the protocol and standard used
        by the online resource, such as Web Feature Service standard.
        (ISO 19115, adapted)
    """
    class Meta:
        name = "onlineResourceType"
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    linkage: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "nillable": True,
        }
    )
    protocol: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    application_profile: Optional[str] = field(
        default=None,
        metadata={
            "name": "applicationProfile",
            "type": "Element",
            "namespace": "",
        }
    )
    name_of_resource: Optional[str] = field(
        default=None,
        metadata={
            "name": "nameOfResource",
            "type": "Element",
            "namespace": "",
        }
    )
    online_resource_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "onlineResourceDescription",
            "type": "Element",
            "namespace": "",
        }
    )
    online_function: Optional[Union[str, OnlineFunctionTypeValue]] = field(
        default=None,
        metadata={
            "name": "onlineFunction",
            "type": "Element",
            "namespace": "",
            "pattern": r"other: [a-zA-Z0-9]+( [a-zA-Z0-9]+)*",
        }
    )
    protocol_request: Optional[str] = field(
        default=None,
        metadata={
            "name": "protocolRequest",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class PeriodicDateRangeType:
    """
    This complex attribute describes the active period for a seasonal feature
    or information type.

    :ivar date_start: The start date or time of the interval.
    :ivar date_end: The end date or time of the interval.
    """
    class Meta:
        name = "periodicDateRangeType"
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    date_start: Optional[S100TruncatedDate2] = field(
        default=None,
        metadata={
            "name": "dateStart",
            "type": "Element",
            "namespace": "",
            "nillable": True,
        }
    )
    date_end: Optional[S100TruncatedDate2] = field(
        default=None,
        metadata={
            "name": "dateEnd",
            "type": "Element",
            "namespace": "",
            "nillable": True,
        }
    )


@dataclass
class RxnCodeType:
    """A summary of the impact of the most common types of regulation,
    restriction, recommendation and nautical information on a vessel.

    Remark: This attribute converts the subject, topic, and effects of regulations, etc., from plain text or natural language into a set of categories.

    :ivar category_of_rx_n:
    :ivar action_or_activity:
    :ivar headline: Words set at the head of a passage or page to
        introduce or categorize
    """
    class Meta:
        name = "rxnCodeType"
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    category_of_rx_n: Optional[Union[str, CategoryOfRxNtypeValue]] = field(
        default=None,
        metadata={
            "name": "categoryOfRxN",
            "type": "Element",
            "namespace": "",
            "pattern": r"other: [a-zA-Z0-9]+( [a-zA-Z0-9]+)*",
        }
    )
    action_or_activity: Optional[Union[str, ActionOrActivityTypeValue]] = field(
        default=None,
        metadata={
            "name": "actionOrActivity",
            "type": "Element",
            "namespace": "",
            "pattern": r"other: [a-zA-Z0-9]+( [a-zA-Z0-9]+)*",
        }
    )
    headline: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class SourceIndicationType:
    """
    Content of featureName is source authority name.

    :ivar category_of_authority:
    :ivar country_name:
    :ivar feature_name:
    :ivar reported_date:
    :ivar source: The publication, document, or reference work from
        which information comes or is acquired.
    :ivar source_type: Type of source
    """
    class Meta:
        name = "sourceIndicationType"
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    category_of_authority: Optional[CategoryOfAuthorityType] = field(
        default=None,
        metadata={
            "name": "categoryOfAuthority",
            "type": "Element",
            "namespace": "",
        }
    )
    country_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "countryName",
            "type": "Element",
            "namespace": "",
        }
    )
    feature_name: List[FeatureNameType] = field(
        default_factory=list,
        metadata={
            "name": "featureName",
            "type": "Element",
            "namespace": "",
        }
    )
    reported_date: Optional[S100TruncatedDate2] = field(
        default=None,
        metadata={
            "name": "reportedDate",
            "type": "Element",
            "namespace": "",
        }
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    source_type: Optional[SourceTypeType] = field(
        default=None,
        metadata={
            "name": "sourceType",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class SurveyDateRangeType:
    """
    The complex attribute describes the period of the hydrographic survey, as
    the time between its sub-attributes.

    :ivar date_start: The start date or time of the interval.
    :ivar date_end: The end date or time of the interval.
    """
    class Meta:
        name = "surveyDateRangeType"
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    date_start: Optional[S100TruncatedDate2] = field(
        default=None,
        metadata={
            "name": "dateStart",
            "type": "Element",
            "namespace": "",
        }
    )
    date_end: Optional[S100TruncatedDate2] = field(
        default=None,
        metadata={
            "name": "dateEnd",
            "type": "Element",
            "namespace": "",
            "nillable": True,
        }
    )


@dataclass
class TimeIntervalsByDayOfWeekType:
    """Time intervals by days of the week.
    The sub-attribute dayOfWeekIsRanges indicates whether an instance of this attribute encodes a range of days or discrete days. The days or day-range(s) are encoded in sub-attribute dayOfWeek. Multiple ranges are allowed but mixing range with discrete days(s) is not allowed (encode another instance of this attribute instead).
    An indeterminate range may be indicated with a null value at the appropriate position in the sequence.
    Examples:
    - To code the range “Monday through Friday” use the sequence: dayOfWeek=1, dayOfWeek=5 and set dayOfWeekIsRanges=TRUE.
    - To encode the days Monday, Wednesday, Friday, use the sequence dayOfWeek=1, dayOfWeek=3, dayOfWeek=5 and set dayOfWeekIsRanges=FALSE.
    - The sequence dayOfWeek=1, dayOfWeek=3, dayOfWeek=5  to indicate Mon-Wed and Thursday is not allowed. Encode the Mon-Wed and Thursday schedules in different instances of this complex attribute.
    Product specifications may need to allow this attribute to be repeated in order to allow encoding of schedules which vary for different days of the week.

    :ivar day_of_week: Encodes either range(s) of days or discrete days.
    :ivar day_of_week_is_range: Indicates whether the values in
        dayOfWeek indicate a range of days (true) or discrete days
        (false).
    :ivar time_of_day_start: Starting time of day, possibly for a period
        within the day. Distinction: Time start (TIMSTA) (S-101) which
        has a format YYYYMMDDThhmmss (mandatory) in the baseline S-101
        DCEG as of October 2015.
    :ivar time_of_day_end: Ending time of day, possibly for a period
        within the day. Distinction: Time end (TIMEND) (S-101) which has
        a format YYYYMMDDThhmmss (mandatory) in the baseline S-101 DCEG
        as of October 2015.
    """
    class Meta:
        name = "timeIntervalsByDayOfWeekType"
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    day_of_week: List[DayOfWeekType] = field(
        default_factory=list,
        metadata={
            "name": "dayOfWeek",
            "type": "Element",
            "namespace": "",
            "max_occurs": 7,
        }
    )
    day_of_week_is_range: Optional[bool] = field(
        default=None,
        metadata={
            "name": "dayOfWeekIsRange",
            "type": "Element",
            "namespace": "",
            "nillable": True,
        }
    )
    time_of_day_start: List[XmlTime] = field(
        default_factory=list,
        metadata={
            "name": "timeOfDayStart",
            "type": "Element",
            "namespace": "",
        }
    )
    time_of_day_end: List[XmlTime] = field(
        default_factory=list,
        metadata={
            "name": "timeOfDayEnd",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class UnderkeelAllowanceType:
    """
    A fixed figure, or a figure derived by calculation, which is added to
    draught in order to maintain the minimum underkeel clearance taking into
    account the vessel's static and dynamic characteristics, sea state and
    weather forecast, the reliability of the chart and variance from predicted
    height of tide or water level.

    :ivar underkeel_allowance_fixed: A fixed allowance given by an
        authority, which is added to draught in order to maintain a
        minimum underkeel clearance.
    :ivar underkeel_allowance_variable_beam_based: A percentage value,
        given by an authority, which is applied to ship's beam in order
        to calculate underkeel allowance.
    :ivar underkeel_allowance_variable_draught_based: A percentage
        value, given by an authority, which is applied to ship's draught
        in order to calculate underkeel allowance.
    :ivar operation: OPERAT is intended to be used in conjunction with
        other attributes (or sub-attributes of a complex attribute) to
        indicate how their values must be combined in order to describe
        a condition.
    """
    class Meta:
        name = "underkeelAllowanceType"
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    underkeel_allowance_fixed: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "underkeelAllowanceFixed",
            "type": "Element",
            "namespace": "",
            "min_inclusive": Decimal("0.0"),
            "fraction_digits": 1,
        }
    )
    underkeel_allowance_variable_beam_based: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "underkeelAllowanceVariableBeamBased",
            "type": "Element",
            "namespace": "",
            "min_inclusive": Decimal("0.0"),
            "fraction_digits": 1,
        }
    )
    underkeel_allowance_variable_draught_based: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "underkeelAllowanceVariableDraughtBased",
            "type": "Element",
            "namespace": "",
            "min_inclusive": Decimal("0.0"),
            "fraction_digits": 1,
        }
    )
    operation: Optional[OperationType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class VesselsMeasurementsType:
    class Meta:
        name = "vesselsMeasurementsType"
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    comparison_operator: Optional[ComparisonOperatorType] = field(
        default=None,
        metadata={
            "name": "comparisonOperator",
            "type": "Element",
            "namespace": "",
            "nillable": True,
        }
    )
    vessels_characteristics: Optional[VesselsCharacteristicsType] = field(
        default=None,
        metadata={
            "name": "vesselsCharacteristics",
            "type": "Element",
            "namespace": "",
            "nillable": True,
        }
    )
    vessels_characteristics_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "vesselsCharacteristicsValue",
            "type": "Element",
            "namespace": "",
            "nillable": True,
        }
    )
    vessels_characteristics_unit: Optional[VesselsCharacteristicsUnitType] = field(
        default=None,
        metadata={
            "name": "vesselsCharacteristicsUnit",
            "type": "Element",
            "namespace": "",
            "nillable": True,
        }
    )


@dataclass
class AbstractAttributeType(AbstractGmltype):
    """
    Abstract type for attributes.
    """
    class Meta:
        target_namespace = "http://www.iho.int/s100gml/1.0"


@dataclass
class DataSetIdentificationType:
    """S-100 Data Set Identification.

    The fields correspond to S-100 10a-5.1.2.1 fields. Attributes
    encodingSpecification and encodingSpecificationEdition are actually
    redundant here because in an XML schema the encoding specification
    and encoding specification edition are usually implicit in the
    namespace URI.

    :ivar encoding_specification: Encoding specification that defines
        the encoding.
    :ivar encoding_specification_edition: Edition of the encoding
        specification
    :ivar product_identifier: Unique identifier of the data product as
        specified in the product specification
    :ivar product_edition: Edition of the product specification
    :ivar application_profile: Identifier that specifies a profile
        within the data product
    :ivar dataset_file_identifier: The file identifier of the dataset
    :ivar dataset_title: The title of the dataset
    :ivar dataset_reference_date: The reference date of the dataset
    :ivar dataset_language: The (primary) language used in this dataset
    :ivar dataset_abstract: The abstract of the dataset
    :ivar dataset_topic_category: A set of topic categories
    """
    class Meta:
        target_namespace = "http://www.iho.int/s100gml/1.0"

    encoding_specification: str = field(
        init=False,
        default="S-100 Part 10b",
        metadata={
            "name": "encodingSpecification",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
            "required": True,
        }
    )
    encoding_specification_edition: str = field(
        init=False,
        default="1.0",
        metadata={
            "name": "encodingSpecificationEdition",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
            "required": True,
        }
    )
    product_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "productIdentifier",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
            "required": True,
        }
    )
    product_edition: Optional[str] = field(
        default=None,
        metadata={
            "name": "productEdition",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
            "required": True,
        }
    )
    application_profile: Optional[str] = field(
        default=None,
        metadata={
            "name": "applicationProfile",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
            "required": True,
        }
    )
    dataset_file_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "datasetFileIdentifier",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
            "required": True,
        }
    )
    dataset_title: Optional[str] = field(
        default=None,
        metadata={
            "name": "datasetTitle",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
            "required": True,
        }
    )
    dataset_reference_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "datasetReferenceDate",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
            "required": True,
        }
    )
    dataset_language: Iso6391 = field(
        default=Iso6391.EN,
        metadata={
            "name": "datasetLanguage",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
            "required": True,
        }
    )
    dataset_abstract: Optional[str] = field(
        default=None,
        metadata={
            "name": "datasetAbstract",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    dataset_topic_category: List[MdTopicCategoryCode] = field(
        default_factory=list,
        metadata={
            "name": "datasetTopicCategory",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
            "min_occurs": 1,
        }
    )


@dataclass
class KnotPropertyType:
    """gml:KnotPropertyType encapsulates a knot to use it in a geometric type.

    The S100 version is needed so as to use the updated definition of
    knots

    :ivar knot: A knot is a breakpoint on a piecewise spline curve.
        value is the value of the parameter at the knot of the spline
        (see ISO 19107:2003, 6.4.24.2). multiplicity is the multiplicity
        of this knot used in the definition of the spline (with the same
        weight). weight is the value of the averaging weight used for
        this knot of the spline.
    """
    class Meta:
        target_namespace = "http://www.iho.int/s100gml/1.0"

    knot: Optional[S100GmKnotType] = field(
        default=None,
        metadata={
            "name": "Knot",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
            "required": True,
        }
    )


@dataclass
class AbstractGeometryType(AbstractGmltype):
    """All geometry elements are derived directly or indirectly from this
    abstract supertype. A geometry element may have an identifying attribute
    (gml:id), one or more names (elements identifier and name) and a
    description (elements description and descriptionReference) . It may be
    associated with a spatial reference system (attribute group
    gml:SRSReferenceGroup). The following rules shall.

    be adhered to: - Every geometry type shall derive from this abstract type. - Every
    geometry element (i.e. an element of a geometry type) shall be directly or
    indirectly in the substitution group of AbstractGeometry.
    """
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    srs_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Attribute",
        }
    )
    srs_dimension: Optional[int] = field(
        default=None,
        metadata={
            "name": "srsDimension",
            "type": "Attribute",
        }
    )


@dataclass
class AngleType(MeasureType):
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class AssociationRoleType:
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:/w{2,}",
        }
    )


@dataclass
class Boolean:
    class Meta:
        nillable = True
        namespace = "http://www.opengis.net/gml/3.2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "nillable": True,
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:/w{2,}",
        }
    )


@dataclass
class CodeWithAuthorityType(CodeType):
    """
    gml:CodeWithAuthorityType requires that the codeSpace attribute is provided
    in an instance.
    """
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class EnvelopeType:
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    lower_corner: Optional[DirectPositionType] = field(
        default=None,
        metadata={
            "name": "lowerCorner",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    upper_corner: Optional[DirectPositionType] = field(
        default=None,
        metadata={
            "name": "upperCorner",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    srs_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Attribute",
        }
    )
    srs_dimension: Optional[int] = field(
        default=None,
        metadata={
            "name": "srsDimension",
            "type": "Attribute",
        }
    )


@dataclass
class LengthType(MeasureType):
    """This is a prototypical definition for a specific measure type defined as
    a vacuous extension (i.e. aliases) of gml:MeasureType.

    In this case, the content model supports the description of a length
    (or distance) quantity, with its units. The unit of measure
    referenced by uom shall be suitable for a length, such as metres or
    feet.
    """
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class ReferenceType:
    """
    gml:ReferenceType is intended to be used in application schemas directly,
    if a property element shall use a "by-reference only" encoding.
    """
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:/w{2,}",
        }
    )


@dataclass
class VolumeType(MeasureType):
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Measure(MeasureType):
    """
    The value of a physical quantity, together with its unit.
    """
    class Meta:
        name = "measure"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Pos(DirectPositionType):
    class Meta:
        name = "pos"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class PosList(DirectPositionListType):
    class Meta:
        name = "posList"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class ArcType:
    """
    :ivar type:
    :ivar arcrole:
    :ivar title:
    :ivar show:
    :ivar actuate:
    :ivar from_value:
    :ivar to: from and to have default behavior when values are missing
    """
    class Meta:
        name = "arcType"
        target_namespace = "http://www.w3.org/1999/xlink"

    type: TypeType = field(
        init=False,
        default=TypeType.ARC,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "required": True,
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    from_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "from",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    to: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )


@dataclass
class Extended:
    """Intended for use as the type of user-declared elements to make them
    extended links.

    Note that the elements referenced in the content model are all
    abstract. The intention is that by simply declaring elements with
    these as their substitutionGroup, all the right things will happen.
    """
    class Meta:
        name = "extended"
        target_namespace = "http://www.w3.org/1999/xlink"

    type: TypeType = field(
        init=False,
        default=TypeType.EXTENDED,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "required": True,
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )


@dataclass
class LocatorType:
    """
    :ivar type:
    :ivar href:
    :ivar role:
    :ivar title:
    :ivar label: label is not required, but locators have no particular
        XLink function if they are not labeled.
    """
    class Meta:
        name = "locatorType"
        target_namespace = "http://www.w3.org/1999/xlink"

    type: TypeType = field(
        init=False,
        default=TypeType.LOCATOR,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "required": True,
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "required": True,
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    label: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )


@dataclass
class ResourceType:
    class Meta:
        name = "resourceType"
        target_namespace = "http://www.w3.org/1999/xlink"

    type: TypeType = field(
        init=False,
        default=TypeType.RESOURCE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "required": True,
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    label: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


@dataclass
class Simple:
    """
    Intended for use as the type of user-declared elements to make them simple
    links.
    """
    class Meta:
        name = "simple"
        target_namespace = "http://www.w3.org/1999/xlink"

    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


@dataclass
class TitleEltType:
    """
    :ivar type:
    :ivar lang: xml:lang is not required, but provides much of the
        motivation for title elements in addition to attributes, and so
        is provided here for convenience.
    :ivar content:
    """
    class Meta:
        name = "titleEltType"
        target_namespace = "http://www.w3.org/1999/xlink"

    type: TypeType = field(
        init=False,
        default=TypeType.TITLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "required": True,
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


@dataclass
class GraphicType:
    """
    :ivar pictorial_representation:
    :ivar picture_caption: Short description of the purpose of the
        image.
    :ivar source_date:
    :ivar picture_information: A set of information to provide credits
        to picture creator, copyright owner etc.
    :ivar bearing_information:
    """
    class Meta:
        name = "graphicType"
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    pictorial_representation: List[str] = field(
        default_factory=list,
        metadata={
            "name": "pictorialRepresentation",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "nillable": True,
        }
    )
    picture_caption: Optional[str] = field(
        default=None,
        metadata={
            "name": "pictureCaption",
            "type": "Element",
            "namespace": "",
        }
    )
    source_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "sourceDate",
            "type": "Element",
            "namespace": "",
        }
    )
    picture_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "pictureInformation",
            "type": "Element",
            "namespace": "",
        }
    )
    bearing_information: Optional[BearingInformationType] = field(
        default=None,
        metadata={
            "name": "bearingInformation",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class RadiocommunicationsType:
    """
    Detailed radiocommunications description with channels, frequencies,
    preferences and time schedules.

    :ivar category_of_comm_pref:
    :ivar category_of_maritime_broadcast:
    :ivar category_of_radio_methods:
    :ivar communication_channel:
    :ivar contact_instructions: supplemental instructions on how or when
        to contact the individual, organisation, or service
    :ivar frequency_pair:
    :ivar signal_frequency:
    :ivar transmission_content: Content of transmission. Remarks: Not to
        be used if CATMAB is populated
    :ivar time_intervals_by_day_of_week:
    """
    class Meta:
        name = "radiocommunicationsType"
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    category_of_comm_pref: Optional[CategoryOfCommPrefType] = field(
        default=None,
        metadata={
            "name": "categoryOfCommPref",
            "type": "Element",
            "namespace": "",
        }
    )
    category_of_maritime_broadcast: List[CategoryOfMaritimeBroadcastType] = field(
        default_factory=list,
        metadata={
            "name": "categoryOfMaritimeBroadcast",
            "type": "Element",
            "namespace": "",
        }
    )
    category_of_radio_methods: List[CategoryOfRadioMethodsType] = field(
        default_factory=list,
        metadata={
            "name": "categoryOfRadioMethods",
            "type": "Element",
            "namespace": "",
        }
    )
    communication_channel: List[str] = field(
        default_factory=list,
        metadata={
            "name": "communicationChannel",
            "type": "Element",
            "namespace": "",
        }
    )
    contact_instructions: Optional[str] = field(
        default=None,
        metadata={
            "name": "contactInstructions",
            "type": "Element",
            "namespace": "",
        }
    )
    frequency_pair: List[FrequencyPairType] = field(
        default_factory=list,
        metadata={
            "name": "frequencyPair",
            "type": "Element",
            "namespace": "",
        }
    )
    signal_frequency: List[int] = field(
        default_factory=list,
        metadata={
            "name": "signalFrequency",
            "type": "Element",
            "namespace": "",
        }
    )
    transmission_content: Optional[str] = field(
        default=None,
        metadata={
            "name": "transmissionContent",
            "type": "Element",
            "namespace": "",
        }
    )
    time_intervals_by_day_of_week: List[TimeIntervalsByDayOfWeekType] = field(
        default_factory=list,
        metadata={
            "name": "timeIntervalsByDayOfWeek",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class ScheduleByDayOfWeekType:
    """
    Describes the nature and timings of a daily schedule by days of the week.

    :ivar category_of_schedule: Describes the type of schedule, e.g.,
        opening, closure, etc.
    :ivar time_intervals_by_day_of_week:
    """
    class Meta:
        name = "scheduleByDayOfWeekType"
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    category_of_schedule: Optional[Union[str, CategoryOfScheduleTypeValue]] = field(
        default=None,
        metadata={
            "name": "categoryOfSchedule",
            "type": "Element",
            "namespace": "",
            "pattern": r"other: [a-zA-Z0-9]+( [a-zA-Z0-9]+)*",
        }
    )
    time_intervals_by_day_of_week: List[TimeIntervalsByDayOfWeekType] = field(
        default_factory=list,
        metadata={
            "name": "timeIntervalsByDayOfWeek",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class TextContentType:
    """Remarks:
    - Exactly one of sub-attributes onlineResource or information must be completed in one instance of textContent.
    - Product specifications may restrict the use or content  of onlineResource for security. For example, a product specification may forbid populating onlineResource.
    - Product specification authors must consider whether applications using the data product may be prevented from accessing off-system resources by security policies."""
    class Meta:
        name = "textContentType"
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    category_of_text: Optional[CategoryOfTextType] = field(
        default=None,
        metadata={
            "name": "categoryOfText",
            "type": "Element",
            "namespace": "",
        }
    )
    information: List[InformationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    online_resource: Optional[OnlineResourceType] = field(
        default=None,
        metadata={
            "name": "onlineResource",
            "type": "Element",
            "namespace": "",
        }
    )
    source_indication: Optional[SourceIndicationType] = field(
        default=None,
        metadata={
            "name": "sourceIndication",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class FeaturePropertyType2(AbstractAttributeType):
    """
    Abstract type for an S-100 feature association.
    """
    class Meta:
        name = "FeaturePropertyType"
        target_namespace = "http://www.iho.int/s100gml/1.0"

    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:/w{2,}",
        }
    )


@dataclass
class InformationPropertyType(AbstractAttributeType):
    """
    Abstract type for an S-100 information associations.
    """
    class Meta:
        target_namespace = "http://www.iho.int/s100gml/1.0"

    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:/w{2,}",
        }
    )


@dataclass
class InverseInformationAssociationType(AbstractAttributeType):
    """
    Abstract type for the inverse association to an information association.
    """
    class Meta:
        target_namespace = "http://www.iho.int/s100gml/1.0"

    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:/w{2,}",
        }
    )


@dataclass
class AbstractGeometricAggregateType(AbstractGeometryType):
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    aggregation_type: Optional[AggregationType] = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        }
    )


@dataclass
class AbstractGeometricPrimitiveType(AbstractGeometryType):
    """gml:AbstractGeometricPrimitiveType is the abstract root type of the
    geometric primitives.

    A geometric primitive is a geometric object that is not decomposed
    further into other primitives in the system. All primitives are
    oriented in the direction implied by the sequence of their
    coordinate tuples.
    """
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Envelope(EnvelopeType):
    """Envelope defines an extent using a pair of positions defining opposite
    corners in arbitrary dimensions.

    The first direct position is the "lower corner" (a coordinate
    position consisting of all the minimal ordinates for each dimension
    for all points within the envelope), the second one the "upper
    corner" (a coordinate position consisting of all the maximal
    ordinates for each dimension for all points within the envelope).
    The use of the properties "coordinates" and "pos" has been
    deprecated. The explicitly named properties "lowerCorner" and
    "upperCorner" shall be used instead.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Angle(AngleType):
    """
    The gml:angle property element is used to record the value of an angle
    quantity as a single number, with its units.
    """
    class Meta:
        name = "angle"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class TelecommunicationsType:
    """
    A means or channel of communicating at a distance by electrical or
    electromagnetic means such as telegraphy, telephony, or broadcasting.

    :ivar category_of_comm_pref:
    :ivar contact_instructions: instructions on how and when to contact
        an individual or organisation
    :ivar telcom_carrier: The name of provider or type of carrier for  a
        telecommunications service
    :ivar telecommunication_identifier: Identifier used for contact by
        means of a telecommunications service, such as a telephone
        number
    :ivar telecommunication_service: Type of telecommunications service
    :ivar schedule_by_day_of_week:
    """
    class Meta:
        name = "telecommunicationsType"
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    category_of_comm_pref: Optional[CategoryOfCommPrefType] = field(
        default=None,
        metadata={
            "name": "categoryOfCommPref",
            "type": "Element",
            "namespace": "",
        }
    )
    contact_instructions: Optional[str] = field(
        default=None,
        metadata={
            "name": "contactInstructions",
            "type": "Element",
            "namespace": "",
        }
    )
    telcom_carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "telcomCarrier",
            "type": "Element",
            "namespace": "",
        }
    )
    telecommunication_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "telecommunicationIdentifier",
            "type": "Element",
            "namespace": "",
            "nillable": True,
        }
    )
    telecommunication_service: List[Union[str, TelecommunicationServiceTypeValue]] = field(
        default_factory=list,
        metadata={
            "name": "telecommunicationService",
            "type": "Element",
            "namespace": "",
            "pattern": r"other: [a-zA-Z0-9]+( [a-zA-Z0-9]+)*",
        }
    )
    schedule_by_day_of_week: Optional[ScheduleByDayOfWeekType] = field(
        default=None,
        metadata={
            "name": "scheduleByDayOfWeek",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class FeatureAssociation(FeaturePropertyType2):
    class Meta:
        name = "featureAssociation"
        namespace = "http://www.iho.int/s100gml/1.0"


@dataclass
class InformationAssociation(InformationPropertyType):
    class Meta:
        name = "informationAssociation"
        namespace = "http://www.iho.int/s100gml/1.0"


@dataclass
class InvFeatureAssociation(FeaturePropertyType2):
    class Meta:
        name = "invFeatureAssociation"
        namespace = "http://www.iho.int/s100gml/1.0"


@dataclass
class InvInformationAssociation(InverseInformationAssociationType):
    class Meta:
        name = "invInformationAssociation"
        namespace = "http://www.iho.int/s100gml/1.0"


@dataclass
class AbstractCurveType(AbstractGeometricPrimitiveType):
    """gml:AbstractCurveType is an abstraction of a curve to support the
    different levels of complexity.

    The curve may always be viewed as a geometric primitive, i.e. is
    continuous.
    """
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractSurfaceType(AbstractGeometricPrimitiveType):
    """gml:AbstractSurfaceType is an abstraction of a surface to support the
    different levels of complexity.

    A surface is always a continuous region of a plane.
    """
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class BoundingShapeType:
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    envelope: Optional[Envelope] = field(
        default=None,
        metadata={
            "name": "Envelope",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:/w{2,}",
        }
    )


@dataclass
class PointType1(AbstractGeometricPrimitiveType):
    """S-100 XML supports two different ways to specify the direct positon of a
    point.

    1. The "pos" element is of type DirectPositionType.
    """
    class Meta:
        name = "PointType"
        target_namespace = "http://www.opengis.net/gml/3.2"

    pos: Optional[Pos] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )


@dataclass
class AbstractInformationType(AbstractGmltype):
    """Abstract type for an S-100 information type.

    This is the base type from which domain application schemas derive
    definitions for their individual information types. It provides for
    all information types in the data product's GML application schema
    to have properties for information associations and inverse
    information associations.
    """
    class Meta:
        target_namespace = "http://www.iho.int/s100gml/1.0"

    information_association: List[InformationAssociation] = field(
        default_factory=list,
        metadata={
            "name": "informationAssociation",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    inv_information_association: List[InvInformationAssociation] = field(
        default_factory=list,
        metadata={
            "name": "invInformationAssociation",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )


@dataclass
class PointType2(PointType1):
    """
    S-100 point type adds an information association to the GML spatial type
    Point.
    """
    class Meta:
        name = "PointType"
        target_namespace = "http://www.iho.int/s100gml/1.0"

    information_association: List[InformationAssociation] = field(
        default_factory=list,
        metadata={
            "name": "informationAssociation",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )


@dataclass
class CompositeCurveType1(AbstractCurveType):
    class Meta:
        name = "CompositeCurveType"
        target_namespace = "http://www.opengis.net/gml/3.2"

    curve_member: List["CurveMember"] = field(
        default_factory=list,
        metadata={
            "name": "curveMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 1,
        }
    )
    aggregation_type: Optional[AggregationType] = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        }
    )


@dataclass
class OrientableCurveType(AbstractCurveType):
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    base_curve: Optional["BaseCurve"] = field(
        default=None,
        metadata={
            "name": "baseCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )
    orientation: SignType = field(
        default=SignType.VALUE,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Point1(PointType1):
    """A Point is defined by a single coordinate tuple.

    The direct position of a point is specified by the pos element which
    is of type DirectPositionType.
    """
    class Meta:
        name = "Point"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class BoundedBy(BoundingShapeType):
    """
    This property describes the minimum bounding box or rectangle that encloses
    the entire feature.
    """
    class Meta:
        name = "boundedBy"
        nillable = True
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class InformationTypeType(AbstractInformationType):
    """
    Generalized information type which carry all the common attributes.
    """
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    fixed_date_range: Optional[FixedDateRangeType] = field(
        default=None,
        metadata={
            "name": "fixedDateRange",
            "type": "Element",
            "namespace": "",
        }
    )
    periodic_date_range: List[PeriodicDateRangeType] = field(
        default_factory=list,
        metadata={
            "name": "periodicDateRange",
            "type": "Element",
            "namespace": "",
        }
    )
    feature_name: List[FeatureNameType] = field(
        default_factory=list,
        metadata={
            "name": "featureName",
            "type": "Element",
            "namespace": "",
        }
    )
    source_indication: List[SourceIndicationType] = field(
        default_factory=list,
        metadata={
            "name": "sourceIndication",
            "type": "Element",
            "namespace": "",
        }
    )
    provides_information: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "providesInformation",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class CompositeCurveType2(CompositeCurveType1):
    """
    S-100 composite curve type adds an information association to the GML
    spatial type CompositeCurve.
    """
    class Meta:
        name = "CompositeCurveType"
        target_namespace = "http://www.iho.int/s100gml/1.0"

    information_association: List[InformationAssociation] = field(
        default_factory=list,
        metadata={
            "name": "informationAssociation",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )


@dataclass
class OrientableCurve2(OrientableCurveType):
    """S-100 orientable curve is the same as GML orientable curve.

    Added for consistency.
    """
    class Meta:
        name = "OrientableCurve"
        namespace = "http://www.iho.int/s100gml/1.0"


@dataclass
class Point2(PointType2):
    class Meta:
        name = "Point"
        namespace = "http://www.iho.int/s100gml/1.0"


@dataclass
class AbstractFeatureType1(AbstractGmltype):
    """The basic feature model is given by the gml:AbstractFeatureType.

    The content model for gml:AbstractFeatureType adds two specific
    properties suitable for geographic features to the content model
    defined in gml:AbstractGMLType. The value of the gml:boundedBy
    property describes an envelope that encloses the entire feature
    instance, and is primarily useful for supporting rapid searching for
    features that occur in a particular location. The value of the
    gml:location property describes the extent, position or relative
    location of the feature.
    """
    class Meta:
        name = "AbstractFeatureType"
        target_namespace = "http://www.opengis.net/gml/3.2"

    bounded_by: Optional[BoundedBy] = field(
        default=None,
        metadata={
            "name": "boundedBy",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "nillable": True,
        }
    )


@dataclass
class CompositeCurve1(CompositeCurveType1):
    """A gml:CompositeCurve is represented by a sequence of (orientable) curves
    such that each curve in the sequence terminates at the start point of the
    subsequent curve in the list.

    curveMember references or contains inline one curve in the composite
    curve. The curves are contiguous, the collection of curves is
    ordered. Therefore, if provided, the aggregationType attribute shall
    have the value "sequence".
    """
    class Meta:
        name = "CompositeCurve"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class OrientableCurve1(OrientableCurveType):
    """OrientableCurve consists of a curve and an orientation.

    If the orientation is "+", then the OrientableCurve is identical to
    the baseCurve. If the orientation is "-", then the OrientableCurve
    is related to another AbstractCurve with a parameterization that
    reverses the sense of the curve traversal.
    """
    class Meta:
        name = "OrientableCurve"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class PointPropertyType1:
    """A property that has a point as its value domain may either be an
    appropriate geometry element encapsulated in an element of this type or an
    XLink reference to a remote geometry element (where remote includes
    geometry elements located elsewhere in the same document).

    Either the reference or the contained element shall be given, but
    neither both nor none.
    """
    class Meta:
        name = "PointPropertyType"
        target_namespace = "http://www.opengis.net/gml/3.2"

    point: Optional[Point1] = field(
        default=None,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:/w{2,}",
        }
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class AbstractRxNtype(InformationTypeType):
    """An abstract superclass for information types that encode rules,
    recommendations, and general information in text or graphic form.

    Remarks: Subtypes of AbstractRxN carry the same attributes, but differ in the nature of information they encode. There are currently four such subtypes: Regulations, Restrictions, Recommendations, and NauticalInformation.
    """
    class Meta:
        name = "AbstractRxNType"
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    category_of_authority: Optional[CategoryOfAuthorityType] = field(
        default=None,
        metadata={
            "name": "categoryOfAuthority",
            "type": "Element",
            "namespace": "",
        }
    )
    text_content: List[TextContentType] = field(
        default_factory=list,
        metadata={
            "name": "textContent",
            "type": "Element",
            "namespace": "",
        }
    )
    graphic: List[GraphicType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    rxn_code: List[RxnCodeType] = field(
        default_factory=list,
        metadata={
            "name": "rxnCode",
            "type": "Element",
            "namespace": "",
        }
    )
    is_applicable_to: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "isApplicableTo",
            "type": "Element",
            "namespace": "",
        }
    )
    the_organisation: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "theOrganisation",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class ApplicabilityType(InformationTypeType):
    """
    Describes the relationship between vessel characteristics and: (i) the
    applicability of an associated information object or feature to the vessel;
    or, (ii) the use of a facility, place, or service by the vessel; or, (iii)
    passage of the vessel through an area.

    :ivar in_ballast: Whether the vessel is in ballast.
    :ivar category_of_cargo:
    :ivar category_of_dangerous_or_hazardous_cargo:
    :ivar category_of_vessel: Codelist - open enumeration - S-100 Ed.
        2.0.0.
    :ivar category_of_vessel_registry:
    :ivar logical_connectives:
    :ivar thickness_of_ice_capability: The thickness of ice that the
        ship can safely transit
    :ivar information:
    :ivar vessel_performance: A description of the required handling
        characteristics of a vessel including hull design, main and
        auxilliary machinery, cargo handling equipment, navigation
        equipment and manoeuvring behaviour.
    :ivar vessels_measurements:
    :ivar vsl_location: Association to the Association class
        PermissionType
    :ivar the_applicable_rx_n: To InclusionType
    :ivar the_ship_report:
    """
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    in_ballast: Optional[bool] = field(
        default=None,
        metadata={
            "name": "inBallast",
            "type": "Element",
            "namespace": "",
        }
    )
    category_of_cargo: List[CategoryOfCargoType] = field(
        default_factory=list,
        metadata={
            "name": "categoryOfCargo",
            "type": "Element",
            "namespace": "",
        }
    )
    category_of_dangerous_or_hazardous_cargo: List[CategoryOfDangerousOrHazardousCargoType] = field(
        default_factory=list,
        metadata={
            "name": "categoryOfDangerousOrHazardousCargo",
            "type": "Element",
            "namespace": "",
        }
    )
    category_of_vessel: Optional[Union[str, CategoryOfVesselTypeValue]] = field(
        default=None,
        metadata={
            "name": "categoryOfVessel",
            "type": "Element",
            "namespace": "",
            "pattern": r"other: [a-zA-Z0-9]+( [a-zA-Z0-9]+)*",
        }
    )
    category_of_vessel_registry: Optional[CategoryOfVesselRegistryType] = field(
        default=None,
        metadata={
            "name": "categoryOfVesselRegistry",
            "type": "Element",
            "namespace": "",
        }
    )
    logical_connectives: Optional[LogicalConnectivesType] = field(
        default=None,
        metadata={
            "name": "logicalConnectives",
            "type": "Element",
            "namespace": "",
        }
    )
    thickness_of_ice_capability: Optional[int] = field(
        default=None,
        metadata={
            "name": "thicknessOfIceCapability",
            "type": "Element",
            "namespace": "",
        }
    )
    information: List[InformationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    vessel_performance: Optional[str] = field(
        default=None,
        metadata={
            "name": "vesselPerformance",
            "type": "Element",
            "namespace": "",
        }
    )
    vessels_measurements: List[VesselsMeasurementsType] = field(
        default_factory=list,
        metadata={
            "name": "vesselsMeasurements",
            "type": "Element",
            "namespace": "",
        }
    )
    vsl_location: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "vslLocation",
            "type": "Element",
            "namespace": "",
        }
    )
    the_applicable_rx_n: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "theApplicableRxN",
            "type": "Element",
            "namespace": "",
        }
    )
    the_ship_report: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "theShipReport",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class AuthorityType(InformationTypeType):
    """A person or organisation having political or administrative power and
    control.

    (Oxford Dictionary of English)
    """
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    category_of_authority: Optional[CategoryOfAuthorityType] = field(
        default=None,
        metadata={
            "name": "categoryOfAuthority",
            "type": "Element",
            "namespace": "",
            "nillable": True,
        }
    )
    text_content: Optional[TextContentType] = field(
        default=None,
        metadata={
            "name": "textContent",
            "type": "Element",
            "namespace": "",
        }
    )
    the_contact_details: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "theContactDetails",
            "type": "Element",
            "namespace": "",
        }
    )
    the_service_hours: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "theServiceHours",
            "type": "Element",
            "namespace": "",
        }
    )
    the_ship_report: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "theShipReport",
            "type": "Element",
            "namespace": "",
        }
    )
    the_information: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "theInformation",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class ContactDetailsType(InformationTypeType):
    """
    Information on how to reach a person or organisation by postal, internet,
    telephone, telex and radio systems.

    :ivar call_name: The designated call name of a station, e.g. radio
        station, radar station, pilot. Remarks: This is the name used
        when calling a radio station by radio i.e. "Singapore Pilots".
    :ivar call_sign: The designated call-sign of a radio station.
    :ivar category_of_comm_pref:
    :ivar communication_channel: A channel number assigned to a specific
        radio frequency, frequencies or frequency band.
    :ivar contact_address:
    :ivar contact_instructions: supplemental instructions on how or when
        to contact the individual, organisation, or service
    :ivar frequency_pair:
    :ivar information:
    :ivar language:
    :ivar m_msicode: The Maritime Mobile Service Identity (MMSI) Code is
        formed of a series of nine digits which are transmitted over the
        radio path in order to uniquely identify ship stations, ship
        earth stations, coast stations, coast earth stations, and group
        calls. These identities are formed in such a way that the
        identity or part thereof can be used by telephone and telex
        subscribers connected to the general telecommunications network
        principally to call ships automatically.
    :ivar online_resource: Information about online sources from which a
        resource or data can be obtained (ISO 19115, adapted)
    :ivar telecommunications: information for contact by means of a
        telecommunications service. Distinctions: emailAddress,
        internetAddress, callName, callSign, COMCHA
    :ivar radiocommunications: When bound to ContactDetails, only the
        listed sub-attributes may be used: - communicationChannel -
        contactinstructions - frequencypair -
        categoryOfChannelOrFrequencyPreference -
        timeIntervalsByDayOfWeek
    :ivar the_authority:
    """
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    call_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "callName",
            "type": "Element",
            "namespace": "",
        }
    )
    call_sign: Optional[str] = field(
        default=None,
        metadata={
            "name": "callSign",
            "type": "Element",
            "namespace": "",
        }
    )
    category_of_comm_pref: Optional[CategoryOfCommPrefType] = field(
        default=None,
        metadata={
            "name": "categoryOfCommPref",
            "type": "Element",
            "namespace": "",
        }
    )
    communication_channel: List[str] = field(
        default_factory=list,
        metadata={
            "name": "communicationChannel",
            "type": "Element",
            "namespace": "",
        }
    )
    contact_address: List[ContactAddressType] = field(
        default_factory=list,
        metadata={
            "name": "contactAddress",
            "type": "Element",
            "namespace": "",
        }
    )
    contact_instructions: Optional[str] = field(
        default=None,
        metadata={
            "name": "contactInstructions",
            "type": "Element",
            "namespace": "",
        }
    )
    frequency_pair: List[FrequencyPairType] = field(
        default_factory=list,
        metadata={
            "name": "frequencyPair",
            "type": "Element",
            "namespace": "",
        }
    )
    information: List[InformationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"\w{3}",
        }
    )
    m_msicode: Optional[str] = field(
        default=None,
        metadata={
            "name": "mMSICode",
            "type": "Element",
            "namespace": "",
            "length": 9,
            "pattern": r"\d{9}",
        }
    )
    online_resource: List[OnlineResourceType] = field(
        default_factory=list,
        metadata={
            "name": "onlineResource",
            "type": "Element",
            "namespace": "",
        }
    )
    telecommunications: List[TelecommunicationsType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    radiocommunications: List[RadiocommunicationsType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    the_authority: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "theAuthority",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class InclusionType(InformationTypeType):
    """
    Association class specifying the relationship between the subset of vessels
    described by an APPLIC data object and a regulation (restriction,
    recommendation, or nautical information).

    :ivar membership: indicates whether a vessel is included or excluded
        from the regulation/restriction/recommendation/nautical
        information
    :ivar the_applicable_rx_n:
    :ivar is_applicable_to:
    """
    class Meta:
        namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    membership: Optional[MembershipType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "nillable": True,
        }
    )
    the_applicable_rx_n: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "theApplicableRxN",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    is_applicable_to: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "isApplicableTo",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class NonStandardWorkingDayType(InformationTypeType):
    """Days when many services are not available.

    Often days of festivity or recreation when normal working hours are
    limited, esp. a national or religious festival, etc.

    :ivar date_fixed: The date when a festival or national holiday
        recurs on the same day each year in the Gregorian calendar.
    :ivar date_variable: A day which is not fixed in the Gregorian
        calendar. Examples: The fourth Thursday in November; new moon
        day of Kartika (Diwali); Easter Sunday.
    :ivar information:
    :ivar the_service_hours_nsdy: optional
    """
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    date_fixed: List[S100TruncatedDate2] = field(
        default_factory=list,
        metadata={
            "name": "dateFixed",
            "type": "Element",
            "namespace": "",
        }
    )
    date_variable: List[str] = field(
        default_factory=list,
        metadata={
            "name": "dateVariable",
            "type": "Element",
            "namespace": "",
        }
    )
    information: List[InformationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    the_service_hours_nsdy: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "theServiceHours_nsdy",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class PermissionType(InformationTypeType):
    """
    Association class for associations describing whether the subsets of
    vessels determined by the ship characteristics specified in APPLIC may (or
    must, etc.) transit,  enter, or use  a feature.

    :ivar category_of_relationship: This attribute expresses the level
        of insistence for or against an action or activity by a vessel
        of the subset described by the APPLIC object at one end in
        relation to the feature at the other end of the association.
    :ivar permission: Reference Applicability
    """
    class Meta:
        namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    category_of_relationship: Optional[CategoryOfRelationshipType] = field(
        default=None,
        metadata={
            "name": "categoryOfRelationship",
            "type": "Element",
            "namespace": "",
            "nillable": True,
        }
    )
    permission: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class ServiceHoursType(InformationTypeType):
    """
    The time when a service is available and known exceptions.

    :ivar schedule_by_day_of_week:
    :ivar information:
    :ivar the_authority_srv_hrs: optional
    :ivar partial_working_day:
    """
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    schedule_by_day_of_week: List[ScheduleByDayOfWeekType] = field(
        default_factory=list,
        metadata={
            "name": "scheduleByDayOfWeek",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "nillable": True,
        }
    )
    information: List[InformationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    the_authority_srv_hrs: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "theAuthority_srvHrs",
            "type": "Element",
            "namespace": "",
        }
    )
    partial_working_day: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "partialWorkingDay",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class ShipReportType(InformationTypeType):
    """
    This describes how a ship should report to a maritime authority, including
    when to report, what to report and whether the format conforms to the IMO
    standard.

    :ivar category_of_ship_report:
    :ivar imo_format_for_reporting: Whether a report must be in an IMO
        standard format
    :ivar report_to:
    :ivar notice_time:
    :ivar text_content:
    :ivar must_be_filed_by:
    """
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    category_of_ship_report: List[CategoryOfShipReportType] = field(
        default_factory=list,
        metadata={
            "name": "categoryOfShipReport",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "nillable": True,
        }
    )
    imo_format_for_reporting: Optional[bool] = field(
        default=None,
        metadata={
            "name": "imoFormatForReporting",
            "type": "Element",
            "namespace": "",
            "nillable": True,
        }
    )
    report_to: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "reportTo",
            "type": "Element",
            "namespace": "",
            "nillable": True,
        }
    )
    notice_time: List[NoticeTimeType] = field(
        default_factory=list,
        metadata={
            "name": "noticeTime",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "nillable": True,
        }
    )
    text_content: Optional[TextContentType] = field(
        default=None,
        metadata={
            "name": "textContent",
            "type": "Element",
            "namespace": "",
        }
    )
    must_be_filed_by: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "mustBeFiledBy",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class SpatialQuality(InformationTypeType):
    """
    :ivar category_of_temporal_variation:
    :ivar horizontal_position_uncertainty: The best estimate of the
        accuracy of a position.
    :ivar quality_of_horizontal_measurement:
    """
    class Meta:
        namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    category_of_temporal_variation: Optional[CategoryOfTemporalVariationType] = field(
        default=None,
        metadata={
            "name": "categoryOfTemporalVariation",
            "type": "Element",
            "namespace": "",
        }
    )
    horizontal_position_uncertainty: Optional[HorizontalPositionUncertaintyType] = field(
        default=None,
        metadata={
            "name": "horizontalPositionUncertainty",
            "type": "Element",
            "namespace": "",
        }
    )
    quality_of_horizontal_measurement: Optional[QualityOfHorizontalMeasurementType] = field(
        default=None,
        metadata={
            "name": "qualityOfHorizontalMeasurement",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class AbstractFeatureType2(AbstractFeatureType1):
    """Abstract type for an S-100 feature.

    This is the base type from which domain application schemas derive
    definitions for their individual features. It derives from GML
    AbstractFeatureType. It provides for all information types in the
    data product's GML application schema to have feature identifiers
    and properties for feature associations, information associations
    and inverse information associations.
    """
    class Meta:
        name = "AbstractFeatureType"
        target_namespace = "http://www.iho.int/s100gml/1.0"

    feature_object_identifier: Optional[FeatureObjectIdentifier] = field(
        default=None,
        metadata={
            "name": "featureObjectIdentifier",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    information_association: List[InformationAssociation] = field(
        default_factory=list,
        metadata={
            "name": "informationAssociation",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    feature_association: List[FeatureAssociation] = field(
        default_factory=list,
        metadata={
            "name": "featureAssociation",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    inv_feature_association: List[InvFeatureAssociation] = field(
        default_factory=list,
        metadata={
            "name": "invFeatureAssociation",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )


@dataclass
class CompositeCurve2(CompositeCurveType2):
    class Meta:
        name = "CompositeCurve"
        namespace = "http://www.iho.int/s100gml/1.0"


@dataclass
class OrientableCurvePropertyType:
    """
    Orientable Curve property using the S-100 orientable curve element.
    """
    class Meta:
        target_namespace = "http://www.iho.int/s100gml/1.0"

    orientable_curve: Optional[OrientableCurve2] = field(
        default=None,
        metadata={
            "name": "OrientableCurve",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:/w{2,}",
        }
    )


@dataclass
class PointPropertyType2:
    """
    Point property using the S-100 point type.
    """
    class Meta:
        name = "PointPropertyType"
        target_namespace = "http://www.iho.int/s100gml/1.0"

    point: Optional[Point2] = field(
        default=None,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:/w{2,}",
        }
    )


@dataclass
class PointMember(PointPropertyType1):
    """
    This property element either references a Point via the XLink-attributes or
    contains the Point element.
    """
    class Meta:
        name = "pointMember"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class PointProperty2(PointPropertyType1):
    """This property element either references a point via the XLink-attributes
    or contains the point element.

    pointProperty is the predefined property which may be used by GML
    Application Schemas whenever a GML feature has a property with a
    value that is substitutable for Point.
    """
    class Meta:
        name = "pointProperty"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Applicability(ApplicabilityType):
    class Meta:
        namespace = "http://www.iho.int/S127/gml/cs0/1.0"


@dataclass
class Authority(AuthorityType):
    class Meta:
        namespace = "http://www.iho.int/S127/gml/cs0/1.0"


@dataclass
class ContactDetails(ContactDetailsType):
    class Meta:
        namespace = "http://www.iho.int/S127/gml/cs0/1.0"


@dataclass
class FeatureType(AbstractFeatureType2):
    """
    Generalized feature type which carry all the common attributes.

    :ivar fixed_date_range:
    :ivar periodic_date_range:
    :ivar feature_name:
    :ivar source_indication:
    :ivar text_content:
    :ivar permission:
    :ivar provides_information:
    :ivar the_rx_n:
    :ivar positions: A pointer to a specific cartographically positioned
        location for text.
    """
    class Meta:
        namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    fixed_date_range: Optional[FixedDateRangeType] = field(
        default=None,
        metadata={
            "name": "fixedDateRange",
            "type": "Element",
            "namespace": "",
        }
    )
    periodic_date_range: List[PeriodicDateRangeType] = field(
        default_factory=list,
        metadata={
            "name": "periodicDateRange",
            "type": "Element",
            "namespace": "",
        }
    )
    feature_name: List[FeatureNameType] = field(
        default_factory=list,
        metadata={
            "name": "featureName",
            "type": "Element",
            "namespace": "",
        }
    )
    source_indication: Optional[SourceIndicationType] = field(
        default=None,
        metadata={
            "name": "sourceIndication",
            "type": "Element",
            "namespace": "",
        }
    )
    text_content: List[TextContentType] = field(
        default_factory=list,
        metadata={
            "name": "textContent",
            "type": "Element",
            "namespace": "",
        }
    )
    permission: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    provides_information: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "providesInformation",
            "type": "Element",
            "namespace": "",
        }
    )
    the_rx_n: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "theRxN",
            "type": "Element",
            "namespace": "",
        }
    )
    positions: Optional[ReferenceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class GenericFeatureType(AbstractFeatureType2):
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    local_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##local",
        }
    )


@dataclass
class MetaFeatureType(AbstractFeatureType2):
    """
    Generalized feature type which carry all the common attributes.
    """
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"


@dataclass
class NauticalInformationType(AbstractRxNtype):
    """Nautical information about a related area or facility.

    Constraint: If Regulations.textContent is populated, there cannot be textualDescription or information attributes directly bound to the Regulations.. A similar constraint applies to the information types Recommendations, Restrictions, and NauticalInformation.

    :ivar information_provided_for: This tag is overloaded, but the
        relationship cannot be to a feature type because
        info-&gt;feature links are not allowed by the 3.0.0 feature
        catalogue
    """
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    information_provided_for: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "informationProvidedFor",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class NonStandardWorkingDay(NonStandardWorkingDayType):
    class Meta:
        namespace = "http://www.iho.int/S127/gml/cs0/1.0"


@dataclass
class RecommendationsType(AbstractRxNtype):
    """Recommendations for a related area or facility.

    Constraint: If Regulations.textContent is populated, there cannot be textualDescription or information attributes directly bound to the Regulations.. A similar constraint applies to the information types Recommendations, Restrictions, and NauticalInformation.
    """
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"


@dataclass
class RegulationsType(AbstractRxNtype):
    """Regulations for a related area or facility.

    Constraint: If Regulations.textContent is populated, there cannot be textualDescription or information attributes directly bound to the Regulations.. A similar constraint applies to the information types Recommendations, Restrictions, and NauticalInformation.
    """
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"


@dataclass
class RestrictionsType(AbstractRxNtype):
    """Restrictions for a related area or facility.

    Constraint: If Regulations.textContent is populated, there cannot be textualDescription or information attributes directly bound to the Regulations.. A similar constraint applies to the information types Recommendations, Restrictions, and NauticalInformation.
    """
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"


@dataclass
class ServiceHours(ServiceHoursType):
    class Meta:
        namespace = "http://www.iho.int/S127/gml/cs0/1.0"


@dataclass
class ShipReport(ShipReportType):
    class Meta:
        namespace = "http://www.iho.int/S127/gml/cs0/1.0"


@dataclass
class SpatialQualityPoints(SpatialQuality):
    """
    Definition required.
    """
    class Meta:
        namespace = "http://www.iho.int/S127/gml/cs0/1.0"


@dataclass
class CompositeCurvePropertyType:
    """
    Composite Curve property using the S-100 composite curve type.
    """
    class Meta:
        target_namespace = "http://www.iho.int/s100gml/1.0"

    composite_curve: Optional[CompositeCurve2] = field(
        default=None,
        metadata={
            "name": "CompositeCurve",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:/w{2,}",
        }
    )


@dataclass
class S100ArcByCenterPointType(AbstractCurveSegmentType):
    """
    Type for S-100 arc by center point geometry.
    """
    class Meta:
        name = "S100_ArcByCenterPointType"
        target_namespace = "http://www.iho.int/s100gml/1.0"

    pos: Optional[Pos] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    point_property: Optional[PointProperty2] = field(
        default=None,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    radius: Optional[LengthType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
            "required": True,
        }
    )
    start_angle: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "startAngle",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
            "min_inclusive": Decimal("0.0"),
            "max_inclusive": Decimal("360.0"),
            "fraction_digits": 1,
        }
    )
    angular_distance: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "angularDistance",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
            "min_inclusive": Decimal("-360.0"),
            "max_inclusive": Decimal("360.0"),
            "fraction_digits": 1,
        }
    )
    interpolation: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.CIRCULAR_ARC_CENTER_POINT_WITH_RADIUS,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class S100GmCurveType(AbstractCurveSegmentType):
    """
    <xs:documentation xmlns:xs="http://www.w3.org/2001/XMLSchema">Type for
    curve segments with other interpolations</xs:documentation>
    """
    class Meta:
        name = "S100_GM_CurveType"
        target_namespace = "http://www.iho.int/s100gml/1.0"

    pos: List[Pos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequential": True,
        }
    )
    point_property: List[PointProperty2] = field(
        default_factory=list,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequential": True,
        }
    )
    pos_list: Optional[PosList] = field(
        default=None,
        metadata={
            "name": "posList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    interpolation: Optional[CurveInterpolationType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class S100GmSplineCurveType(AbstractCurveSegmentType):
    """
    <xs:documentation xmlns:xs="http://www.w3.org/2001/XMLSchema">Type for
    general splines including b-splines</xs:documentation>
    """
    class Meta:
        name = "S100_GM_SplineCurveType"
        target_namespace = "http://www.iho.int/s100gml/1.0"

    pos: List[Pos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequential": True,
        }
    )
    point_property: List[PointProperty2] = field(
        default_factory=list,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequential": True,
        }
    )
    pos_list: Optional[PosList] = field(
        default=None,
        metadata={
            "name": "posList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    degree: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
            "required": True,
        }
    )
    knot: List[KnotPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    knot_spec: Optional[S100GmKnotTypeType] = field(
        default=None,
        metadata={
            "name": "knotSpec",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    is_rational: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "isRational",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
            "required": True,
            "pattern": r"other:/w{2,}",
        }
    )
    interpolation: Optional[CurveInterpolationType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class VectorType:
    """
    Defintion of the Vector datatype used in splines.

    :ivar origin:
    :ivar dimension:
    :ivar offset: The number of values must be the same as "dimension"
        value
    """
    class Meta:
        target_namespace = "http://www.iho.int/s100gml/1.0"

    origin: Optional["VectorType.Origin"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
            "required": True,
        }
    )
    dimension: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
            "required": True,
        }
    )
    offset: List[float] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
            "required": True,
            "tokens": True,
        }
    )

    @dataclass
    class Origin:
        pos: Optional[Pos] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.opengis.net/gml/3.2",
            }
        )
        point_property: Optional[PointProperty2] = field(
            default=None,
            metadata={
                "name": "pointProperty",
                "type": "Element",
                "namespace": "http://www.opengis.net/gml/3.2",
            }
        )


@dataclass
class OrientableCurveProperty(OrientableCurvePropertyType):
    class Meta:
        name = "orientableCurveProperty"
        namespace = "http://www.iho.int/s100gml/1.0"


@dataclass
class PointProperty3(PointPropertyType2):
    class Meta:
        name = "pointProperty"
        namespace = "http://www.iho.int/s100gml/1.0"


@dataclass
class GeodesicStringType(AbstractCurveSegmentType):
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    pos_list: Optional[PosList] = field(
        default=None,
        metadata={
            "name": "posList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    pos: List[Pos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    point_property: List[PointProperty2] = field(
        default_factory=list,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    interpolation: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.GEODESIC,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class LineStringSegmentType(AbstractCurveSegmentType):
    """GML supports two different ways to specify the control points of a line
    string.

    1. A sequence of "pos" (DirectPositionType) or "pointProperty"
    (PointPropertyType) elements. "pos" elements are control points that are only part
    of this curve, "pointProperty" elements contain a point that may be referenced from
    other geometry elements or reference another point defined outside of this curve
    (reuse of existing points). 2. The "posList" element allows for a compact way to
    specifiy the coordinates of the control points, if all control points are in the
    same coordinate reference systems and belong to this curve only. The number of
    direct positions in the list must be at least two.
    """
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    pos: List[Pos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 2,
            "sequential": True,
        }
    )
    point_property: List[PointProperty2] = field(
        default_factory=list,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 2,
            "sequential": True,
        }
    )
    pos_list: Optional[PosList] = field(
        default=None,
        metadata={
            "name": "posList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    interpolation: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.LINEAR,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class LineStringType(AbstractCurveType):
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    pos: List[Pos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 2,
            "sequential": True,
        }
    )
    point_property: List[PointProperty2] = field(
        default_factory=list,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 2,
            "sequential": True,
        }
    )
    pos_list: Optional[PosList] = field(
        default=None,
        metadata={
            "name": "posList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class LinearRingType(AbstractRingType):
    """S-100 XML supports two different ways to specify the control points of a
    linear ring.

    1. A sequence of "pos" (DirectPositionType) or "pointProperty"
    (PointPropertyType) elements. "pos" elements are control points that are only part
    of this ring, "pointProperty" elements contain a point that may be referenced from
    other geometry elements or reference another point defined outside of this ring
    (reuse of existing points). 2. The "posList" element allows for a compact way to
    specifiy the coordinates of the control points, if all control points are in the
    same coordinate reference systems and belong to this ring only. The number of direct
    positions in the list must be at least four.
    """
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    pos: List[Pos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 4,
            "sequential": True,
        }
    )
    point_property: List[PointProperty2] = field(
        default_factory=list,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 4,
            "sequential": True,
        }
    )
    pos_list: Optional[PosList] = field(
        default=None,
        metadata={
            "name": "posList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class MultiPointType1(AbstractGeometricAggregateType):
    class Meta:
        name = "MultiPointType"
        target_namespace = "http://www.opengis.net/gml/3.2"

    point_member: List[PointMember] = field(
        default_factory=list,
        metadata={
            "name": "pointMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class DataQualityType(MetaFeatureType):
    """
    Abstract feature type for data quality meta-features.

    :ivar information: Use of attribute information is discouraged for
        nautical publications data quality meta-features.
    """
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    information: List[InformationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class GmPoint:
    class Meta:
        name = "GM_Point"
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    point_property: Optional[PointProperty3] = field(
        default=None,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )


@dataclass
class NauticalInformation(NauticalInformationType):
    class Meta:
        namespace = "http://www.iho.int/S127/gml/cs0/1.0"


@dataclass
class OrganisationContactAreaType(FeatureType):
    """A feature often associated with contact information for an organization
    that exercises a management role or offers a service in the location.

    Remark: It is not a requirement that every instance of the feature be associated with a management, reporting, or service organization.

    :ivar the_contact_details: A pointer to a Contact Details object
    """
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    the_contact_details: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "theContactDetails",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class Recommendations(RecommendationsType):
    class Meta:
        namespace = "http://www.iho.int/S127/gml/cs0/1.0"


@dataclass
class Regulations(RegulationsType):
    class Meta:
        namespace = "http://www.iho.int/S127/gml/cs0/1.0"


@dataclass
class Restrictions(RestrictionsType):
    class Meta:
        namespace = "http://www.iho.int/S127/gml/cs0/1.0"


@dataclass
class PointPropertyType3:
    """WIP update to spatial property types in profile.

    Spatial quality for an individual should be indicated by either the
    generic information association or the SpatialQuality role-element.
    """
    class Meta:
        name = "PointPropertyType"
        target_namespace = "http://www.iho.int/s100gml/1.0+EXT"

    point_property: Optional[PointProperty3] = field(
        default=None,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
            "required": True,
        }
    )


@dataclass
class MultiPointType2(MultiPointType1):
    """
    S-100 multipoint type adds an information association to the GML spatial
    type MultiPoint.
    """
    class Meta:
        name = "MultiPointType"
        target_namespace = "http://www.iho.int/s100gml/1.0"

    information_association: List[InformationAssociation] = field(
        default_factory=list,
        metadata={
            "name": "informationAssociation",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )


@dataclass
class S100ArcByCenterPoint(S100ArcByCenterPointType):
    """This variant of the arc requires that the points on the arc shall be
    computed instead of storing the coordinates directly.

    The single control point is the center point of the arc. The other
    parameters are the radius, the bearing at start, and the angle from
    the start to the end relative to the center of the arc. This
    representation can be used only in 2D. The element radius specifies
    the radius of the arc. The element startAngle specifies the bearing
    of the arc at the start. The element angularDistance specifies the
    difference in bearing from the start to the end. The sign of
    angularDistance specifies the direction of the arc, positive values
    mean the direction is clockwise from start to end looking down from
    a point vertically above the center of the arc. Drawing starts at a
    bearing of 0.0 from the ray pointing due north from the center. If
    the center is at a pole the reference direction follows the prime
    meridian starting from the pole. The interpolation is fixed as
    "circularArcCenterPointWithRadius". Since this type always describes
    a single arc, the GML attribute "numArc" is not used.
    """
    class Meta:
        name = "S100_ArcByCenterPoint"
        namespace = "http://www.iho.int/s100gml/1.0"


@dataclass
class S100CircleByCenterPointType(S100ArcByCenterPointType):
    class Meta:
        name = "S100_CircleByCenterPointType"
        target_namespace = "http://www.iho.int/s100gml/1.0"

    start_angle: Decimal = field(
        default=Decimal("0.0"),
        metadata={
            "name": "startAngle",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
            "required": True,
            "min_inclusive": Decimal("0.0"),
            "max_inclusive": Decimal("360.0"),
            "fraction_digits": 1,
        }
    )
    angular_distance: S100CircleByCenterPointTypeAngularDistance = field(
        default=S100CircleByCenterPointTypeAngularDistance.VALUE_360_0,
        metadata={
            "name": "angularDistance",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
            "required": True,
        }
    )


@dataclass
class S100GmCurve(S100GmCurveType):
    """
    <xs:documentation xmlns:xs="http://www.w3.org/2001/XMLSchema">Curve
    segments with other interpolations</xs:documentation>
    """
    class Meta:
        name = "S100_GM_Curve"
        namespace = "http://www.iho.int/s100gml/1.0"


@dataclass
class S100GmPolynomialSplineType(S100GmSplineCurveType):
    """
    <xs:documentation xmlns:xs="http://www.w3.org/2001/XMLSchema">Type for
    polynomial splines</xs:documentation>
    """
    class Meta:
        name = "S100_GM_PolynomialSplineType"
        target_namespace = "http://www.iho.int/s100gml/1.0"

    derivative_at_start: List[VectorType] = field(
        default_factory=list,
        metadata={
            "name": "derivativeAtStart",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    derivative_at_end: List[VectorType] = field(
        default_factory=list,
        metadata={
            "name": "derivativeAtEnd",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    num_derivative_interior: Optional[int] = field(
        default=None,
        metadata={
            "name": "numDerivativeInterior",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
            "required": True,
        }
    )


@dataclass
class S100GmSplineCurve(S100GmSplineCurveType):
    class Meta:
        name = "S100_GM_SplineCurve"
        namespace = "http://www.iho.int/s100gml/1.0"


@dataclass
class CompositeCurveProperty(CompositeCurvePropertyType):
    class Meta:
        name = "compositeCurveProperty"
        namespace = "http://www.iho.int/s100gml/1.0"


@dataclass
class GeodesicString(GeodesicStringType):
    """A sequence of geodesic segments.

    The number of control points shall be at least two. interpolation is
    fixed as "geodesic". The content model follows the general pattern
    for the encoding of curve segments.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class GeodesicType(GeodesicStringType):
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class LineString(LineStringType):
    """A LineString is a special curve that consists of a single segment with
    linear interpolation.

    It is defined by two or more coordinate tuples, with linear
    interpolation between them. The number of direct positions in the
    list shall be at least two.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class LineStringSegment(LineStringSegmentType):
    """A LineStringSegment is a curve segment that is defined by two or more
    control points including the start and end point, with linear interpolation
    between them.

    The content model follows the general pattern for the encoding of
    curve segments.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class LinearRing(LinearRingType):
    """A LinearRing is defined by four or more coordinate tuples, with linear
    interpolation between them; the first and last coordinates shall be
    coincident.

    The number of direct positions in the list shall be at least four.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiPoint1(MultiPointType1):
    """A gml:MultiPoint consists of one or more gml:Points.

    The members of the geometric aggregate may be specified either using
    the "standard" property (gml:pointMember) or the array property
    (gml:pointMembers). It is also valid to use both the "standard" and
    the array properties in the same collection.
    """
    class Meta:
        name = "MultiPoint"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class ImemberType(AbstractFeatureMemberType):
    """
    dataset member S-100 infotmation types.
    """
    class Meta:
        name = "IMemberType"
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    contact_details: Optional[ContactDetails] = field(
        default=None,
        metadata={
            "name": "ContactDetails",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    ship_report: Optional[ShipReport] = field(
        default=None,
        metadata={
            "name": "ShipReport",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    service_hours: Optional[ServiceHours] = field(
        default=None,
        metadata={
            "name": "ServiceHours",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    restrictions: Optional[Restrictions] = field(
        default=None,
        metadata={
            "name": "Restrictions",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    regulations: Optional[Regulations] = field(
        default=None,
        metadata={
            "name": "Regulations",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    recommendations: Optional[Recommendations] = field(
        default=None,
        metadata={
            "name": "Recommendations",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    non_standard_working_day: Optional[NonStandardWorkingDay] = field(
        default=None,
        metadata={
            "name": "NonStandardWorkingDay",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    nautical_information: Optional[NauticalInformation] = field(
        default=None,
        metadata={
            "name": "NauticalInformation",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    authority: Optional[Authority] = field(
        default=None,
        metadata={
            "name": "Authority",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    applicability: Optional[Applicability] = field(
        default=None,
        metadata={
            "name": "Applicability",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    inclusion_type: Optional[InclusionType] = field(
        default=None,
        metadata={
            "name": "InclusionType",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    permission_type: Optional[PermissionType] = field(
        default=None,
        metadata={
            "name": "PermissionType",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:/w{2,}",
        }
    )


@dataclass
class QualityOfTemporalVariationType(DataQualityType):
    """
    Abstract type for meta-feature which can describe temporal variation.
    """
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    category_of_temporal_variation: Optional[CategoryOfTemporalVariationType] = field(
        default=None,
        metadata={
            "name": "categoryOfTemporalVariation",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class SupervisedAreaType(OrganisationContactAreaType):
    """
    A location which may be supervised by a responsible or controlling
    authority.
    """
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    control_authority: Optional[ReferenceType] = field(
        default=None,
        metadata={
            "name": "controlAuthority",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class TextPlacementType:
    """The Text Placement feature is used in association with the FeatureName
    attribute or a light description to optimise text positioning in ECDIS.

    Remarks: - The Text Placement feature is used by the ECDIS to position the associated text, which has been populated using an attribute(s) for the related feature. This attribute is identified by populating the attribute text type. Alternatively, the text to be displayed may be encoded using the attribute text.
    - Only one of the attributes text or text type are allowable for each instance of Text Placement.
    - Text Placement should only be associated with features of type point, and used in areas where it is important that text clear navigationally relevant areas, e.g. shipping channels and dredged areas.

    :ivar flip_bearing: The bearing at which text is re-located to the
        opposite side of a feature when screen display is oriented away
        from true north.
    :ivar scale_minimum:
    :ivar text_justification: The anchor point of a text string.
    :ivar text: A non-formatted digital text string. Remarks: The
        attribute should be used, for example, to hold the information
        that is shown on paper charts by short cautionary and
        explanatory notes. Therefore text populated in text must not
        exceed 300 characters. Text may be in English or in a national
        language defined by the attribute language. No formatting of
        text is possible within the sub-attribute text. If formatted
        text, or text strings exceeding 300 characters, is required,
        then the attribute file reference must be used.
    :ivar text_type:
    :ivar identifies:
    :ivar geometry:
    """
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    flip_bearing: Optional[int] = field(
        default=None,
        metadata={
            "name": "flipBearing",
            "type": "Element",
            "namespace": "",
            "min_inclusive": 0,
            "max_inclusive": 360,
        }
    )
    scale_minimum: Optional[int] = field(
        default=None,
        metadata={
            "name": "scaleMinimum",
            "type": "Element",
            "namespace": "",
        }
    )
    text_justification: Optional[TextJustificationType] = field(
        default=None,
        metadata={
            "name": "textJustification",
            "type": "Element",
            "namespace": "",
            "nillable": True,
        }
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    text_type: Optional[TextTypeType] = field(
        default=None,
        metadata={
            "name": "textType",
            "type": "Element",
            "namespace": "",
        }
    )
    identifies: Optional[ReferenceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    geometry: List[GmPoint] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class PointProperty1(PointPropertyType3):
    class Meta:
        name = "PointProperty"
        namespace = "http://www.iho.int/s100gml/1.0+EXT"


@dataclass
class MultiPoint2(MultiPointType2):
    class Meta:
        name = "MultiPoint"
        namespace = "http://www.iho.int/s100gml/1.0"


@dataclass
class S100CircleByCenterPoint(S100CircleByCenterPointType):
    """An S100_CircleByCenterPoint is an S100_ArcByCenterPoint with angular
    distance +/- 360.0 degrees to form a full circle.

    Angular distance is assumed to be +360.0 degrees if it is missing.
    The interpolation is fixed as "circularArcCenterPointWithRadius".
    This representation can be used only in 2D.
    """
    class Meta:
        name = "S100_CircleByCenterPoint"
        namespace = "http://www.iho.int/s100gml/1.0"


@dataclass
class S100GmPolynomialSpline(S100GmPolynomialSplineType):
    class Meta:
        name = "S100_GM_PolynomialSpline"
        namespace = "http://www.iho.int/s100gml/1.0"


@dataclass
class Geodesic(GeodesicType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class LinearRingPropertyType:
    """
    A property with the content model of gml:LinearRingPropertyType
    encapsulates a linear ring to represent a component of a surface boundary.
    """
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    linear_ring: Optional[LinearRing] = field(
        default=None,
        metadata={
            "name": "LinearRing",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )


@dataclass
class ReportableServiceAreaType(SupervisedAreaType):
    """
    A service area that generally has requirements for submission of
    information, including communications not strictly considered "reporting.".
    """
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    rept_for_traffic_serv: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "reptForTrafficServ",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class TextPlacement(TextPlacementType):
    class Meta:
        namespace = "http://www.iho.int/S127/gml/cs0/1.0"


@dataclass
class MultiPointPropertyType:
    """
    MultiPoint property using the S-100 multipoint type.
    """
    class Meta:
        target_namespace = "http://www.iho.int/s100gml/1.0"

    multi_point: Optional[MultiPoint2] = field(
        default=None,
        metadata={
            "name": "MultiPoint",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:/w{2,}",
        }
    )


@dataclass
class CurveSegmentArrayPropertyType:
    """
    gml:CurveSegmentArrayPropertyType is a container for an array of curve
    segments.
    """
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    s100_gm_curve: List[S100GmCurve] = field(
        default_factory=list,
        metadata={
            "name": "S100_GM_Curve",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
            "sequential": True,
        }
    )
    s100_gm_polynomial_spline: List[S100GmPolynomialSpline] = field(
        default_factory=list,
        metadata={
            "name": "S100_GM_PolynomialSpline",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
            "sequential": True,
        }
    )
    s100_gm_spline_curve: List[S100GmSplineCurve] = field(
        default_factory=list,
        metadata={
            "name": "S100_GM_SplineCurve",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
            "sequential": True,
        }
    )
    s100_circle_by_center_point: List[S100CircleByCenterPoint] = field(
        default_factory=list,
        metadata={
            "name": "S100_CircleByCenterPoint",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
            "sequential": True,
        }
    )
    s100_arc_by_center_point: List[S100ArcByCenterPoint] = field(
        default_factory=list,
        metadata={
            "name": "S100_ArcByCenterPoint",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
            "sequential": True,
        }
    )
    geodesic: List[Geodesic] = field(
        default_factory=list,
        metadata={
            "name": "Geodesic",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequential": True,
        }
    )
    geodesic_string: List[GeodesicString] = field(
        default_factory=list,
        metadata={
            "name": "GeodesicString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequential": True,
        }
    )
    line_string_segment: List[LineStringSegment] = field(
        default_factory=list,
        metadata={
            "name": "LineStringSegment",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequential": True,
        }
    )


@dataclass
class MultiPointProperty(MultiPointPropertyType):
    class Meta:
        name = "multiPointProperty"
        namespace = "http://www.iho.int/s100gml/1.0"


@dataclass
class Segments(CurveSegmentArrayPropertyType):
    """This property element contains a list of curve segments.

    The order of the elements is significant and shall be preserved when
    processing the array.
    """
    class Meta:
        name = "segments"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class CurveType1(AbstractCurveType):
    class Meta:
        name = "CurveType"
        target_namespace = "http://www.opengis.net/gml/3.2"

    segments: Optional[Segments] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )


@dataclass
class CurveType2(CurveType1):
    """
    S-100 curve type adds an information association to the GML spatial type
    Curve.
    """
    class Meta:
        name = "CurveType"
        target_namespace = "http://www.iho.int/s100gml/1.0"

    information_association: List[InformationAssociation] = field(
        default_factory=list,
        metadata={
            "name": "informationAssociation",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )


@dataclass
class Curve1(CurveType1):
    """A curve is a 1-dimensional primitive.

    Curves are continuous, connected, and have a measurable length in
    terms of the coordinate system. A curve is composed of one or more
    curve segments. Each curve segment within a curve may be defined
    using a different interpolation method. The curve segments are
    connected to one another, with the end point of each segment except
    the last being the start point of the next segment in the segment
    list. The orientation of the curve is positive. The element segments
    encapsulates the segments of the curve.
    """
    class Meta:
        name = "Curve"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Curve2(CurveType2):
    class Meta:
        name = "Curve"
        namespace = "http://www.iho.int/s100gml/1.0"


@dataclass
class CurvePropertyType2:
    """
    Curve property using the S-100 curve type.
    """
    class Meta:
        name = "CurvePropertyType"
        target_namespace = "http://www.iho.int/s100gml/1.0"

    curve: Optional[Curve2] = field(
        default=None,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:/w{2,}",
        }
    )


@dataclass
class CurvePropertyType1:
    """A property that has a curve as its value domain may either be an
    appropriate geometry element encapsulated in an element of this type or an
    XLink reference to a remote geometry element (where remote includes
    geometry elements located elsewhere in the same document).

    Either the reference or the contained element shall be given, but
    neither both nor none.
    """
    class Meta:
        name = "CurvePropertyType"
        target_namespace = "http://www.opengis.net/gml/3.2"

    orientable_curve: Optional[OrientableCurve2] = field(
        default=None,
        metadata={
            "name": "OrientableCurve",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    composite_curve: Optional[CompositeCurve1] = field(
        default=None,
        metadata={
            "name": "CompositeCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    opengis_net_gml_3_2_orientable_curve: Optional[OrientableCurve1] = field(
        default=None,
        metadata={
            "name": "OrientableCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    curve: Optional[Curve2] = field(
        default=None,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    opengis_net_gml_3_2_curve: Optional[Curve1] = field(
        default=None,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    line_string: Optional[LineString] = field(
        default=None,
        metadata={
            "name": "LineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:/w{2,}",
        }
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class CurveProperty2(CurvePropertyType2):
    class Meta:
        name = "curveProperty"
        namespace = "http://www.iho.int/s100gml/1.0"


@dataclass
class BaseCurve(CurvePropertyType1):
    """The property baseCurve references or contains the base curve, i.e. it
    either references the base curve via the XLink-attributes or contains the
    curve element.

    A curve element is any element which is substitutable for
    AbstractCurve. The base curve has positive orientation.
    """
    class Meta:
        name = "baseCurve"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class CurveMember(CurvePropertyType1):
    class Meta:
        name = "curveMember"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class GmCurve:
    class Meta:
        name = "GM_Curve"
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    curve_property: Optional[CurveProperty2] = field(
        default=None,
        metadata={
            "name": "curveProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )


@dataclass
class PointOrCurve:
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    curve_property: Optional[CurveProperty2] = field(
        default=None,
        metadata={
            "name": "curveProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    point_property: Optional[PointProperty3] = field(
        default=None,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )


@dataclass
class CurvePropertyType3:
    """WIP update to spatial property types in profile.

    Spatial quality for an individual should be indicated by either the
    generic information association or the SpatialQuality role-element.
    """
    class Meta:
        name = "CurvePropertyType"
        target_namespace = "http://www.iho.int/s100gml/1.0+EXT"

    curve_property: Optional[CurveProperty2] = field(
        default=None,
        metadata={
            "name": "curveProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    composite_curve_property: Optional[CompositeCurveProperty] = field(
        default=None,
        metadata={
            "name": "compositeCurveProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    orientable_curve_property: Optional[OrientableCurveProperty] = field(
        default=None,
        metadata={
            "name": "orientableCurveProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )


@dataclass
class RingType(AbstractRingType):
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    curve_member: List[CurveMember] = field(
        default_factory=list,
        metadata={
            "name": "curveMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 1,
        }
    )
    aggregation_type: Optional[AggregationType] = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        }
    )


@dataclass
class RadioCallingInPointType(FeatureType):
    """A designated position at which vessels are required to report to a
    Traffic Control Centre.

    Also called reporting point or radio reporting point. S-127 Remarks:
    category of cargo and vessel attributes added as on NIPWG Wiki.

    :ivar call_sign: The designated call-sign of a radio station.
    :ivar category_of_cargo:
    :ivar category_of_vessel: Codelist - open enumeration - S-100 Ed.
        2.0.0.
    :ivar communication_channel:
    :ivar status:
    :ivar traffic_flow:
    :ivar orientation_value:
    :ivar component_of: NIPWG did not discuss whether the same calling-
        in point feature could be associated to separate Ship reporting,
        Traffic control service, and LPS Area features. Tentatively,
        encode coincident calling point features for each.
    :ivar geometry:
    """
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    call_sign: Optional[str] = field(
        default=None,
        metadata={
            "name": "callSign",
            "type": "Element",
            "namespace": "",
        }
    )
    category_of_cargo: List[CategoryOfCargoType] = field(
        default_factory=list,
        metadata={
            "name": "categoryOfCargo",
            "type": "Element",
            "namespace": "",
        }
    )
    category_of_vessel: List[Union[str, CategoryOfVesselTypeValue]] = field(
        default_factory=list,
        metadata={
            "name": "categoryOfVessel",
            "type": "Element",
            "namespace": "",
            "pattern": r"other: [a-zA-Z0-9]+( [a-zA-Z0-9]+)*",
        }
    )
    communication_channel: List[str] = field(
        default_factory=list,
        metadata={
            "name": "communicationChannel",
            "type": "Element",
            "namespace": "",
        }
    )
    status: List[StatusType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    traffic_flow: Optional[TrafficFlowType] = field(
        default=None,
        metadata={
            "name": "trafficFlow",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    orientation_value: List[Decimal] = field(
        default_factory=list,
        metadata={
            "name": "orientationValue",
            "type": "Element",
            "namespace": "",
            "max_occurs": 2,
            "min_inclusive": Decimal("0.0"),
            "max_inclusive": Decimal("360.0"),
            "fraction_digits": 1,
        }
    )
    component_of: Optional[ReferenceType] = field(
        default=None,
        metadata={
            "name": "componentOf",
            "type": "Element",
            "namespace": "",
        }
    )
    geometry: List[PointOrCurve] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class CurveProperty1(CurvePropertyType3):
    class Meta:
        name = "CurveProperty"
        namespace = "http://www.iho.int/s100gml/1.0+EXT"


@dataclass
class Ring(RingType):
    """A ring is used to represent a single connected component of a surface
    boundary as specified in ISO 19107:2003, 6.3.6.

    Every gml:curveMember references or contains one curve, i.e. any
    element which is substitutable for gml:AbstractCurve. In the context
    of a ring, the curves describe the boundary of the surface. The
    sequence of curves shall be contiguous and connected in a cycle. If
    provided, the aggregationType attribute shall have the value
    "sequence".
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class RadioCallingInPoint(RadioCallingInPointType):
    class Meta:
        namespace = "http://www.iho.int/S127/gml/cs0/1.0"


@dataclass
class AbstractRingPropertyType:
    """
    A property with the content model of gml:AbstractRingPropertyType
    encapsulates a ring to represent the surface boundary property of a
    surface.
    """
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    ring: Optional[Ring] = field(
        default=None,
        metadata={
            "name": "Ring",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    linear_ring: Optional[LinearRing] = field(
        default=None,
        metadata={
            "name": "LinearRing",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class Exterior(AbstractRingPropertyType):
    """A boundary of a surface consists of a number of rings.

    In the normal 2D case, one of these rings is distinguished as being
    the exterior boundary. In a general manifold this is not always
    possible, in which case all boundaries shall be listed as interior
    boundaries, and the exterior will be empty.
    """
    class Meta:
        name = "exterior"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Interior(AbstractRingPropertyType):
    """A boundary of a surface consists of a number of rings.

    The "interior" rings separate the surface / surface patch from the
    area enclosed by the rings.
    """
    class Meta:
        name = "interior"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class PolygonPatchType(AbstractSurfacePatchType):
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    exterior: Optional[Exterior] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    interior: List[Interior] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    interpolation: SurfaceInterpolationType = field(
        init=False,
        default=SurfaceInterpolationType.PLANAR,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class PolygonType1(AbstractSurfaceType):
    class Meta:
        name = "PolygonType"
        target_namespace = "http://www.opengis.net/gml/3.2"

    exterior: Optional[Exterior] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    interior: List[Interior] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class PolygonType2(PolygonType1):
    """
    S-100 polygon type adds an information association to the GML spatial type
    Polygon.
    """
    class Meta:
        name = "PolygonType"
        target_namespace = "http://www.iho.int/s100gml/1.0"

    information_association: List[InformationAssociation] = field(
        default_factory=list,
        metadata={
            "name": "informationAssociation",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )


@dataclass
class PolygonPatch(PolygonPatchType):
    """A gml:PolygonPatch is a surface patch that is defined by a set of
    boundary curves and an underlying surface to which these curves adhere.

    The curves shall be coplanar and the polygon uses planar
    interpolation in its interior. interpolation is fixed to "planar",
    i.e. an interpolation shall return points on a single plane. The
    boundary of the patch shall be contained within that plane.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Polygon1(PolygonType1):
    """A Polygon is a special surface that is defined by a single surface patch
    (see D.3.6).

    The boundary of this patch is coplanar and the polygon uses planar
    interpolation in its interior. The elements exterior and interior
    describe the surface boundary of the polygon.
    """
    class Meta:
        name = "Polygon"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Polygon2(PolygonType2):
    """
    S100 version of polygon type.
    """
    class Meta:
        name = "Polygon"
        namespace = "http://www.iho.int/s100gml/1.0"


@dataclass
class SurfacePatchArrayPropertyType:
    """
    gml:SurfacePatchArrayPropertyType is a container for a sequence of surface
    patches.
    """
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    polygon_patch: List[PolygonPatch] = field(
        default_factory=list,
        metadata={
            "name": "PolygonPatch",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


@dataclass
class PolygonPropertyType:
    """
    Polygon property using the S-100 polygon type.
    """
    class Meta:
        target_namespace = "http://www.iho.int/s100gml/1.0"

    polygon: Optional[Polygon2] = field(
        default=None,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:/w{2,}",
        }
    )


@dataclass
class Patches(SurfacePatchArrayPropertyType):
    """The patches property element contains the sequence of surface patches.

    The order of the elements is significant and shall be preserved when
    processing the array.
    """
    class Meta:
        name = "patches"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class PolygonProperty(PolygonPropertyType):
    class Meta:
        name = "polygonProperty"
        namespace = "http://www.iho.int/s100gml/1.0"


@dataclass
class SurfaceType1(AbstractSurfaceType):
    class Meta:
        name = "SurfaceType"
        target_namespace = "http://www.opengis.net/gml/3.2"

    patches: Optional[Patches] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )


@dataclass
class SurfaceType2(SurfaceType1):
    """
    S-100 surface type adds an information association to the GML spatial type
    Surface.
    """
    class Meta:
        name = "SurfaceType"
        target_namespace = "http://www.iho.int/s100gml/1.0"

    information_association: List[InformationAssociation] = field(
        default_factory=list,
        metadata={
            "name": "informationAssociation",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )


@dataclass
class Surface1(SurfaceType1):
    """A Surface is a 2-dimensional primitive and is composed of one or more
    surface patches as specified in ISO 19107:2003, 6.3.17.1.

    The surface patches are connected to one another. patches
    encapsulates the patches of the surface.
    """
    class Meta:
        name = "Surface"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Surface2(SurfaceType2):
    class Meta:
        name = "Surface"
        namespace = "http://www.iho.int/s100gml/1.0"


@dataclass
class SurfacePropertyType2:
    """
    Surface property using the S-100 surface type.
    """
    class Meta:
        name = "SurfacePropertyType"
        target_namespace = "http://www.iho.int/s100gml/1.0"

    surface: Optional[Surface2] = field(
        default=None,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    opengis_net_gml_3_2_surface: Optional[Surface1] = field(
        default=None,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    polygon: Optional[Polygon2] = field(
        default=None,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    opengis_net_gml_3_2_polygon: Optional[Polygon1] = field(
        default=None,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:/w{2,}",
        }
    )


@dataclass
class GeometricPrimitivePropertyType:
    """A property that has a geometric primitive as its value domain may either
    be an appropriate geometry element encapsulated in an element of this type
    or an XLink reference to a remote geometry element (where remote includes
    geometry elements located elsewhere in the same document).

    Either the reference or the contained element shall be given, but
    neither both nor none.
    """
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    point: Optional[Point2] = field(
        default=None,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    surface: Optional[Surface2] = field(
        default=None,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    opengis_net_gml_3_2_surface: Optional[Surface1] = field(
        default=None,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    polygon: Optional[Polygon2] = field(
        default=None,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    opengis_net_gml_3_2_polygon: Optional[Polygon1] = field(
        default=None,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    orientable_curve: Optional[OrientableCurve2] = field(
        default=None,
        metadata={
            "name": "OrientableCurve",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    composite_curve: Optional[CompositeCurve1] = field(
        default=None,
        metadata={
            "name": "CompositeCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    opengis_net_gml_3_2_orientable_curve: Optional[OrientableCurve1] = field(
        default=None,
        metadata={
            "name": "OrientableCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    curve: Optional[Curve2] = field(
        default=None,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    opengis_net_gml_3_2_curve: Optional[Curve1] = field(
        default=None,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    line_string: Optional[LineString] = field(
        default=None,
        metadata={
            "name": "LineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    opengis_net_gml_3_2_point: Optional[Point1] = field(
        default=None,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:/w{2,}",
        }
    )


@dataclass
class SurfacePropertyType1:
    """A property that has a surface as its value domain may either be an
    appropriate geometry element encapsulated in an element of this type or an
    XLink reference to a remote geometry element (where remote includes
    geometry elements located elsewhere in the same document).

    Either the reference or the contained element shall be given, but
    neither both nor none.
    """
    class Meta:
        name = "SurfacePropertyType"
        target_namespace = "http://www.opengis.net/gml/3.2"

    surface: Optional[Surface2] = field(
        default=None,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    opengis_net_gml_3_2_surface: Optional[Surface1] = field(
        default=None,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    polygon: Optional[Polygon2] = field(
        default=None,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    opengis_net_gml_3_2_polygon: Optional[Polygon1] = field(
        default=None,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:/w{2,}",
        }
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class SurfaceProperty2(SurfacePropertyType2):
    class Meta:
        name = "surfaceProperty"
        namespace = "http://www.iho.int/s100gml/1.0"


@dataclass
class CurveOrSurface:
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    curve_property: Optional[CurveProperty2] = field(
        default=None,
        metadata={
            "name": "curveProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    surface_property: Optional[SurfaceProperty2] = field(
        default=None,
        metadata={
            "name": "surfaceProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )


@dataclass
class GmSurface:
    class Meta:
        name = "GM_Surface"
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    surface_property: Optional[SurfaceProperty2] = field(
        default=None,
        metadata={
            "name": "surfaceProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )


@dataclass
class PointCurveSurface:
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    point_property: Optional[PointProperty3] = field(
        default=None,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    curve_property: Optional[CurveProperty2] = field(
        default=None,
        metadata={
            "name": "curveProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    surface_property: Optional[SurfaceProperty2] = field(
        default=None,
        metadata={
            "name": "surfaceProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )


@dataclass
class PointOrSurface:
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    point_property: Optional[PointProperty3] = field(
        default=None,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    surface_property: Optional[SurfaceProperty2] = field(
        default=None,
        metadata={
            "name": "surfaceProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )


@dataclass
class CurveOrSurfacePropertyType:
    class Meta:
        target_namespace = "http://www.iho.int/s100gml/1.0+EXT"

    curve_property: Optional[CurveProperty2] = field(
        default=None,
        metadata={
            "name": "curveProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    surface_property: Optional[SurfaceProperty2] = field(
        default=None,
        metadata={
            "name": "surfaceProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )


@dataclass
class PointCurveSurfacePropertyType:
    class Meta:
        target_namespace = "http://www.iho.int/s100gml/1.0+EXT"

    point_property: Optional[PointProperty3] = field(
        default=None,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    curve_property: Optional[CurveProperty2] = field(
        default=None,
        metadata={
            "name": "curveProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    surface_property: Optional[SurfaceProperty2] = field(
        default=None,
        metadata={
            "name": "surfaceProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )


@dataclass
class PointOrSurfacePropertyType:
    class Meta:
        target_namespace = "http://www.iho.int/s100gml/1.0+EXT"

    point_property: Optional[PointProperty3] = field(
        default=None,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    surface_property: Optional[SurfaceProperty2] = field(
        default=None,
        metadata={
            "name": "surfaceProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )


@dataclass
class SurfacePropertyType3:
    """WIP update to spatial property types in profile.

    Spatial quality for an individual should be indicated by either the
    generic information association or the SpatialQuality role-element.
    """
    class Meta:
        name = "SurfacePropertyType"
        target_namespace = "http://www.iho.int/s100gml/1.0+EXT"

    surface_property: Optional[SurfaceProperty2] = field(
        default=None,
        metadata={
            "name": "surfaceProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )


@dataclass
class CautionAreaType(FeatureType):
    """
    Generally, an area where the mariner has to be made aware of circumstances
    influencing the safety of navigation.
    """
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    condition: Optional[ConditionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    status: Optional[StatusType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    geometry: List[PointOrSurface] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class ConcentrationOfShippingHazardAreaType(FeatureType):
    """An area where hazards, caused by concentrations of shipping, may occur.

    Hazards are risks to shipping, which stem from sources other than
    shoal water or obstructions.
    """
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    category_of_concentration_of_shipping_hazard_area: List[CategoryOfConcentrationOfShippingHazardAreaType] = field(
        default_factory=list,
        metadata={
            "name": "categoryOfConcentrationOfShippingHazardArea",
            "type": "Element",
            "namespace": "",
        }
    )
    status: List[StatusType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    geometry: List[GmSurface] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class DataCoverageType(MetaFeatureType):
    """
    A geographical area that describes the coverage and extent of spatial
    objects.

    :ivar maximum_display_scale: The largest intended viewing scale for
        the data. Not nillable(?)
    :ivar minimum_display_scale: The smallest intended viewing scale for
        the data. Not nillable(?)
    :ivar geometry:
    """
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    maximum_display_scale: Optional[int] = field(
        default=None,
        metadata={
            "name": "maximumDisplayScale",
            "type": "Element",
            "namespace": "",
            "nillable": True,
        }
    )
    minimum_display_scale: Optional[int] = field(
        default=None,
        metadata={
            "name": "minimumDisplayScale",
            "type": "Element",
            "namespace": "",
            "nillable": True,
        }
    )
    geometry: Optional[SurfacePropertyType3] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class IspsCodeSecurityLevelType(OrganisationContactAreaType):
    """The area to which an International Ship and Port Facility Security
    (ISPS) level applies.

    The ISPS Code is a comprehensive set of measures to enhance the
    security of ships and port facilities, developed in response to the
    perceived threats to ships and port facilities in the wake of the
    9/11 attacks in the United States.
    """
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    isps_level: Optional[IspsLevelType] = field(
        default=None,
        metadata={
            "name": "ispsLevel",
            "type": "Element",
            "namespace": "",
            "nillable": True,
        }
    )
    geometry: List[CurveOrSurface] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class LocalPortServiceAreaType(ReportableServiceAreaType):
    """A service established to provide port information without interaction
    between the customer and the service provider.

    This information could be inter alia berthing information,
    availability of port services, shipping schedules, meteorological
    and hydrological data.

    :ivar service_access_procedure: A description of the procedure to
        access the marine service.
    :ivar requirements_for_maintenance_of_listening_watch: Description
        of continuous listening watch requirements.
    :ivar consists_of: A pointer to a part in a whole-part relationship
    :ivar geometry:
    """
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    service_access_procedure: Optional[str] = field(
        default=None,
        metadata={
            "name": "serviceAccessProcedure",
            "type": "Element",
            "namespace": "",
        }
    )
    requirements_for_maintenance_of_listening_watch: Optional[str] = field(
        default=None,
        metadata={
            "name": "requirementsForMaintenanceOfListeningWatch",
            "type": "Element",
            "namespace": "",
            "nillable": True,
        }
    )
    consists_of: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "consistsOf",
            "type": "Element",
            "namespace": "",
        }
    )
    geometry: List[GmSurface] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class MilitaryPracticeAreaType(SupervisedAreaType):
    """An area within which naval, military, or aerial exercises are carried
    out.

    Also called an exercise area.

    :ivar category_of_military_practice_area:
    :ivar nationality:
    :ivar restriction:
    :ivar status:
    :ivar the_service_hours: Service hours for an authority or service
        provider
    :ivar geometry:
    """
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    category_of_military_practice_area: List[CategoryOfMilitaryPracticeAreaType] = field(
        default_factory=list,
        metadata={
            "name": "categoryOfMilitaryPracticeArea",
            "type": "Element",
            "namespace": "",
        }
    )
    nationality: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    restriction: List[RestrictionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    status: List[StatusType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    the_service_hours: Optional[ReferenceType] = field(
        default=None,
        metadata={
            "name": "theServiceHours",
            "type": "Element",
            "namespace": "",
        }
    )
    geometry: List[PointOrSurface] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class PilotBoardingPlaceType(OrganisationContactAreaType):
    """
    A location offshore where a pilot may board a vessel in preparation to
    piloting it through local waters.

    :ivar call_sign: The designated call-sign of a radio station.
    :ivar category_of_pilot_boarding_place:
    :ivar category_of_preference:
    :ivar category_of_vessel: Codelist - open enumeration - S-100 Ed.
        2.0.0.
    :ivar communication_channel:
    :ivar destination: The place or general direction to which a vessel
        is going or directed. Remarks: In addition to a placename of a
        port, harbour area or terminal, the place could include
        generalities such as “The north-west”, or “upriver”.
    :ivar pilot_movement:
    :ivar pilot_vessel: Description of the pilot vessel. The pilot
        vessel is a small vessel used by a pilot to go to or from a
        vessel employing the pilot's services.
    :ivar status:
    :ivar component_of:
    :ivar service_provider:
    :ivar geometry:
    """
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    call_sign: Optional[str] = field(
        default=None,
        metadata={
            "name": "callSign",
            "type": "Element",
            "namespace": "",
        }
    )
    category_of_pilot_boarding_place: Optional[CategoryOfPilotBoardingPlaceType] = field(
        default=None,
        metadata={
            "name": "categoryOfPilotBoardingPlace",
            "type": "Element",
            "namespace": "",
        }
    )
    category_of_preference: Optional[CategoryOfPreferenceType] = field(
        default=None,
        metadata={
            "name": "categoryOfPreference",
            "type": "Element",
            "namespace": "",
        }
    )
    category_of_vessel: Optional[Union[str, CategoryOfVesselTypeValue]] = field(
        default=None,
        metadata={
            "name": "categoryOfVessel",
            "type": "Element",
            "namespace": "",
            "pattern": r"other: [a-zA-Z0-9]+( [a-zA-Z0-9]+)*",
        }
    )
    communication_channel: List[str] = field(
        default_factory=list,
        metadata={
            "name": "communicationChannel",
            "type": "Element",
            "namespace": "",
        }
    )
    destination: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    pilot_movement: Optional[PilotMovementType] = field(
        default=None,
        metadata={
            "name": "pilotMovement",
            "type": "Element",
            "namespace": "",
        }
    )
    pilot_vessel: Optional[str] = field(
        default=None,
        metadata={
            "name": "pilotVessel",
            "type": "Element",
            "namespace": "",
        }
    )
    status: List[StatusType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    component_of: Optional[ReferenceType] = field(
        default=None,
        metadata={
            "name": "componentOf",
            "type": "Element",
            "namespace": "",
        }
    )
    service_provider: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "serviceProvider",
            "type": "Element",
            "namespace": "",
        }
    )
    geometry: List[PointOrSurface] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class PilotServiceType(ReportableServiceAreaType):
    """
    The service provided by a person who directs the movements of a vessel
    through pilot waters, usually a person who has demonstrated extensive
    knowledge of channels, aids to navigation, dangers to navigation, etc., in
    a particular area and is licensed for that area.

    :ivar category_of_pilot:
    :ivar pilot_qualification:
    :ivar pilot_request: Description of the pilot request procedure.
    :ivar remote_pilot: Definition: Whether remote pilot services are
        available. True: remote pilot is available: Pilotage is
        available remotely from shore or other location remote from the
        vessel requiring pilotage. False: remote pilot is not available:
        Remote pilotage is not available.
    :ivar notice_time:
    :ivar service_area: The area served by a service provider. This
        represents both the association to PilotageDistrict and the
        association to PilotBoardingPlace, so it has to be unbounded.
    :ivar the_service_hours: Service hours for an authority or service
        provider
    :ivar geometry:
    """
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    category_of_pilot: List[CategoryOfPilotType] = field(
        default_factory=list,
        metadata={
            "name": "categoryOfPilot",
            "type": "Element",
            "namespace": "",
        }
    )
    pilot_qualification: Optional[PilotQualificationType] = field(
        default=None,
        metadata={
            "name": "pilotQualification",
            "type": "Element",
            "namespace": "",
        }
    )
    pilot_request: Optional[str] = field(
        default=None,
        metadata={
            "name": "pilotRequest",
            "type": "Element",
            "namespace": "",
        }
    )
    remote_pilot: Optional[bool] = field(
        default=None,
        metadata={
            "name": "remotePilot",
            "type": "Element",
            "namespace": "",
            "nillable": True,
        }
    )
    notice_time: Optional[NoticeTimeType] = field(
        default=None,
        metadata={
            "name": "noticeTime",
            "type": "Element",
            "namespace": "",
        }
    )
    service_area: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "serviceArea",
            "type": "Element",
            "namespace": "",
        }
    )
    the_service_hours: Optional[ReferenceType] = field(
        default=None,
        metadata={
            "name": "theServiceHours",
            "type": "Element",
            "namespace": "",
        }
    )
    geometry: List[GmSurface] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class PilotageDistrictType(FeatureType):
    """An area within which a pilotage direction exists.

    Such directions are regulated by a competent harbour authority which
    dictates circumstances under which they apply.
    """
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    communication_channel: List[str] = field(
        default_factory=list,
        metadata={
            "name": "communicationChannel",
            "type": "Element",
            "namespace": "",
        }
    )
    consists_of: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "consistsOf",
            "type": "Element",
            "namespace": "",
        }
    )
    service_provider: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "serviceProvider",
            "type": "Element",
            "namespace": "",
        }
    )
    geometry: List[GmSurface] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class PiracyRiskAreaType(ReportableServiceAreaType):
    """
    An area where there is a raised risk of piracy or armed robbery.
    """
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    restriction: List[RestrictionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "nillable": True,
        }
    )
    status_type: List[StatusType] = field(
        default_factory=list,
        metadata={
            "name": "statusType",
            "type": "Element",
            "namespace": "",
        }
    )
    geometry: List[GmSurface] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class PlaceOfRefugeType(ReportableServiceAreaType):
    """A place where a ship in need of assistance can take action to enable it
    to stabilize its condition and reduce the hazards to navigation, and to
    protect human life and the environment.

    (Reference: IMO Res. A.949(23))
    """
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    status: List[StatusType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    communication_channel: List[str] = field(
        default_factory=list,
        metadata={
            "name": "communicationChannel",
            "type": "Element",
            "namespace": "",
        }
    )
    geometry: List[PointOrSurface] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class QualityOfNonBathymetricDataType(QualityOfTemporalVariationType):
    """An area within which a uniform assessment of the quality of the non-
    bathymetric data exists.

    (Adapted from S-57 Edition 3.1, Appendix A – Chapter 1, Page 1.208,
    November 2000).

    :ivar horizontal_distance_uncertainty: The best estimate of the
        horizontal accuracy of horizontal clearances and distances.
    :ivar horizontal_position_uncertainty: The best estimate of the
        accuracy of a position. The expected input is the maximum of the
        two-dimensional error. The error is assumed to be positive and
        negative. The plus/minus character shall not be encoded.
    :ivar orientation_uncertainty: The best estimate of the accuracy of
        a bearing
    :ivar source_indication:
    :ivar survey_date_range:
    :ivar geometry:
    """
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    horizontal_distance_uncertainty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "horizontalDistanceUncertainty",
            "type": "Element",
            "namespace": "",
            "min_inclusive": Decimal("0.0"),
        }
    )
    horizontal_position_uncertainty: Optional[HorizontalPositionUncertaintyType] = field(
        default=None,
        metadata={
            "name": "horizontalPositionUncertainty",
            "type": "Element",
            "namespace": "",
        }
    )
    orientation_uncertainty: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "orientationUncertainty",
            "type": "Element",
            "namespace": "",
            "min_inclusive": Decimal("0.0"),
        }
    )
    source_indication: Optional[SourceIndicationType] = field(
        default=None,
        metadata={
            "name": "sourceIndication",
            "type": "Element",
            "namespace": "",
        }
    )
    survey_date_range: Optional[SurveyDateRangeType] = field(
        default=None,
        metadata={
            "name": "surveyDateRange",
            "type": "Element",
            "namespace": "",
        }
    )
    geometry: List[SurfacePropertyType3] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class RadarRangeType(FeatureType):
    """Indicates the coverage of a sea area by a radar surveillance station.

    Inside this area a vessel may request shore-based radar assistance,
    particularly in poor visibility.
    """
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    communication_channel: List[str] = field(
        default_factory=list,
        metadata={
            "name": "communicationChannel",
            "type": "Element",
            "namespace": "",
        }
    )
    status: List[StatusType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    geometry: List[GmSurface] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class RestrictedAreaNavigationalType(SupervisedAreaType):
    """A specified area of land or water designated by an appropriate authority
    within which access or navigation is restricted in accordance with certain
    specified conditions.

    A navigational restricted area is an area where the restrictions
    have a direct impact on the navigation of a vessel in the area.
    """
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    category_of_restricted_area: List[CategoryOfRestrictedAreaType] = field(
        default_factory=list,
        metadata={
            "name": "categoryOfRestrictedArea",
            "type": "Element",
            "namespace": "",
        }
    )
    restriction: List[RestrictionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "nillable": True,
        }
    )
    status: List[StatusType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    geometry: List[GmSurface] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class RestrictedAreaRegulatoryType(SupervisedAreaType):
    """A specified area of land or water designated by an appropriate authority
    within which access or navigation is restricted in accordance with certain
    specified conditions.

    A regulatory restricted area is an area where the restrictions have
    no direct impact on the navigation of a vessel in the area, but
    impact on the activities that can take place within the area.
    """
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    category_of_restricted_area: List[CategoryOfRestrictedAreaType] = field(
        default_factory=list,
        metadata={
            "name": "categoryOfRestrictedArea",
            "type": "Element",
            "namespace": "",
        }
    )
    restriction: List[RestrictionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "nillable": True,
        }
    )
    status: List[StatusType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    geometry: List[GmSurface] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class RouteingMeasureType(FeatureType):
    """An area or line designating the limits or central line of a routeing
    measure (or part of a routeing measure).

    Routeing measures include traffic separation schemes, deep-water
    routes,  two-way routes, archipelagic sea lanes, and fairway
    systems.
    """
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    category_of_routeing_measure: Optional[CategoryOfRouteingMeasureType] = field(
        default=None,
        metadata={
            "name": "categoryOfRouteingMeasure",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    category_of_traffic_separation_scheme: Optional[CategoryOfTrafficSeparationSchemeType] = field(
        default=None,
        metadata={
            "name": "categoryOfTrafficSeparationScheme",
            "type": "Element",
            "namespace": "",
        }
    )
    category_of_navigation_line: Optional[CategoryOfNavigationLineType] = field(
        default=None,
        metadata={
            "name": "categoryOfNavigationLine",
            "type": "Element",
            "namespace": "",
        }
    )
    geometry: List[CurveOrSurface] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class ShipReportingServiceAreaType(ReportableServiceAreaType):
    """
    A service established by a relevant authority consisting of one or more
    reporting points or lines at which ships are required to report their
    identity, course, speed and other data to the monitoring authority.

    :ivar service_access_procedure: A description of the procedure to
        access the marine service.
    :ivar requirements_for_maintenance_of_listening_watch: Description
        of continuous listening watch requirements.
    :ivar consists_of: A pointer to the aggregate in a whole-part
        relationship.
    :ivar geometry:
    """
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    service_access_procedure: Optional[str] = field(
        default=None,
        metadata={
            "name": "serviceAccessProcedure",
            "type": "Element",
            "namespace": "",
        }
    )
    requirements_for_maintenance_of_listening_watch: Optional[str] = field(
        default=None,
        metadata={
            "name": "requirementsForMaintenanceOfListeningWatch",
            "type": "Element",
            "namespace": "",
            "nillable": True,
        }
    )
    consists_of: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "consistsOf",
            "type": "Element",
            "namespace": "",
        }
    )
    geometry: List[GmSurface] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class SignalStationTrafficType(OrganisationContactAreaType):
    """
    A traffic signal station is a place on shore from which signals are made to
    regulate the movement of traffic.
    """
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    category_of_signal_station_traffic: List[CategoryOfSignalStationTrafficType] = field(
        default_factory=list,
        metadata={
            "name": "categoryOfSignalStationTraffic",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "nillable": True,
        }
    )
    communication_channel: List[str] = field(
        default_factory=list,
        metadata={
            "name": "communicationChannel",
            "type": "Element",
            "namespace": "",
        }
    )
    status: List[StatusType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    geometry: List[PointOrSurface] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class SignalStationWarningType(FeatureType):
    """
    A warning signal station is a place on shore from which warning signals are
    made to ships at sea.
    """
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    category_of_signal_station_warning: List[CategoryOfSignalStationWarningType] = field(
        default_factory=list,
        metadata={
            "name": "categoryOfSignalStationWarning",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "nillable": True,
        }
    )
    communication_channel: List[str] = field(
        default_factory=list,
        metadata={
            "name": "communicationChannel",
            "type": "Element",
            "namespace": "",
        }
    )
    status: List[StatusType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    geometry: List[PointOrSurface] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class UnderkeelClearanceAllowanceAreaType(FeatureType):
    """
    An area for which an authority has stated underkeel allowance requirements.
    """
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    underkeel_allowance: Optional[UnderkeelAllowanceType] = field(
        default=None,
        metadata={
            "name": "underkeelAllowance",
            "type": "Element",
            "namespace": "",
        }
    )
    water_level_trend: Optional[WaterLevelTrendType] = field(
        default=None,
        metadata={
            "name": "waterLevelTrend",
            "type": "Element",
            "namespace": "",
        }
    )
    geometry: List[GmSurface] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class UnderkeelClearanceManagementAreaType(ReportableServiceAreaType):
    """
    An area for which an authority permits use of dynamic underkeel clearance
    information or provides dynamic information related to underkeel
    clearances.
    """
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    dynamic_resource: Optional[DynamicResourceType] = field(
        default=None,
        metadata={
            "name": "dynamicResource",
            "type": "Element",
            "namespace": "",
            "nillable": True,
        }
    )
    geometry: List[GmSurface] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class VesselTrafficServiceAreaType(ReportableServiceAreaType):
    """The area of any service implemented by a relevant authority primarily
    designed to improve safety and efficiency of traffic flow and the
    protection of the environment.

    It may range from simple information messages, to extensive
    organisation of the traffic involving national or regional schemes.

    :ivar category_of_vessel_traffic_service:
    :ivar service_access_procedure: A description of the procedure to
        access the marine service.
    :ivar requirements_for_maintenance_of_listening_watch: Description
        of continuous listening watch requirements.
    :ivar consists_of: A pointer to the aggregate in a whole-part
        relationship.
    :ivar geometry:
    """
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    category_of_vessel_traffic_service: List[CategoryOfVesselTrafficServiceType] = field(
        default_factory=list,
        metadata={
            "name": "categoryOfVesselTrafficService",
            "type": "Element",
            "namespace": "",
            "nillable": True,
        }
    )
    service_access_procedure: Optional[str] = field(
        default=None,
        metadata={
            "name": "serviceAccessProcedure",
            "type": "Element",
            "namespace": "",
        }
    )
    requirements_for_maintenance_of_listening_watch: Optional[str] = field(
        default=None,
        metadata={
            "name": "requirementsForMaintenanceOfListeningWatch",
            "type": "Element",
            "namespace": "",
            "nillable": True,
        }
    )
    consists_of: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "consistsOf",
            "type": "Element",
            "namespace": "",
        }
    )
    geometry: List[GmSurface] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class WaterwayAreaType(SupervisedAreaType):
    """
    An area in which uniform general information of the waterway exists.

    :ivar siltation_rate: A description of the rate at which the depth
        in an area decreases.
    :ivar status:
    :ivar dynamic_resource: Whether dynamic water level information is
        available. Remarks: If the value of this attribute is TRUE, the
        source of dynamic water level information, if known, should be
        encoded in the textContent attribute.
    :ivar geometry:
    """
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    siltation_rate: Optional[str] = field(
        default=None,
        metadata={
            "name": "siltationRate",
            "type": "Element",
            "namespace": "",
        }
    )
    status: List[StatusType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    dynamic_resource: Optional[DynamicResourceType] = field(
        default=None,
        metadata={
            "name": "dynamicResource",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    geometry: List[GmSurface] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class CurveOrSurfaceProperty(CurveOrSurfacePropertyType):
    class Meta:
        namespace = "http://www.iho.int/s100gml/1.0+EXT"


@dataclass
class PointCurveSurfaceProperty(PointCurveSurfacePropertyType):
    class Meta:
        namespace = "http://www.iho.int/s100gml/1.0+EXT"


@dataclass
class PointOrSurfaceProperty(PointOrSurfacePropertyType):
    class Meta:
        namespace = "http://www.iho.int/s100gml/1.0+EXT"


@dataclass
class SurfaceProperty1(SurfacePropertyType3):
    class Meta:
        name = "SurfaceProperty"
        namespace = "http://www.iho.int/s100gml/1.0+EXT"


@dataclass
class CautionArea(CautionAreaType):
    class Meta:
        namespace = "http://www.iho.int/S127/gml/cs0/1.0"


@dataclass
class ConcentrationOfShippingHazardArea(ConcentrationOfShippingHazardAreaType):
    class Meta:
        namespace = "http://www.iho.int/S127/gml/cs0/1.0"


@dataclass
class DataCoverage(DataCoverageType):
    class Meta:
        namespace = "http://www.iho.int/S127/gml/cs0/1.0"


@dataclass
class IspsCodeSecurityLevel(IspsCodeSecurityLevelType):
    class Meta:
        namespace = "http://www.iho.int/S127/gml/cs0/1.0"


@dataclass
class LocalPortServiceArea(LocalPortServiceAreaType):
    class Meta:
        namespace = "http://www.iho.int/S127/gml/cs0/1.0"


@dataclass
class MilitaryPracticeArea(MilitaryPracticeAreaType):
    class Meta:
        namespace = "http://www.iho.int/S127/gml/cs0/1.0"


@dataclass
class PilotBoardingPlace(PilotBoardingPlaceType):
    class Meta:
        namespace = "http://www.iho.int/S127/gml/cs0/1.0"


@dataclass
class PilotService(PilotServiceType):
    class Meta:
        namespace = "http://www.iho.int/S127/gml/cs0/1.0"


@dataclass
class PilotageDistrict(PilotageDistrictType):
    class Meta:
        namespace = "http://www.iho.int/S127/gml/cs0/1.0"


@dataclass
class PiracyRiskArea(PiracyRiskAreaType):
    class Meta:
        namespace = "http://www.iho.int/S127/gml/cs0/1.0"


@dataclass
class PlaceOfRefuge(PlaceOfRefugeType):
    class Meta:
        namespace = "http://www.iho.int/S127/gml/cs0/1.0"


@dataclass
class QualityOfNonBathymetricData(QualityOfNonBathymetricDataType):
    class Meta:
        namespace = "http://www.iho.int/S127/gml/cs0/1.0"


@dataclass
class RadarRange(RadarRangeType):
    class Meta:
        namespace = "http://www.iho.int/S127/gml/cs0/1.0"


@dataclass
class RestrictedAreaNavigational(RestrictedAreaNavigationalType):
    class Meta:
        namespace = "http://www.iho.int/S127/gml/cs0/1.0"


@dataclass
class RestrictedAreaRegulatory(RestrictedAreaRegulatoryType):
    class Meta:
        namespace = "http://www.iho.int/S127/gml/cs0/1.0"


@dataclass
class RouteingMeasure(RouteingMeasureType):
    class Meta:
        namespace = "http://www.iho.int/S127/gml/cs0/1.0"


@dataclass
class ShipReportingServiceArea(ShipReportingServiceAreaType):
    class Meta:
        namespace = "http://www.iho.int/S127/gml/cs0/1.0"


@dataclass
class SignalStationTraffic(SignalStationTrafficType):
    class Meta:
        namespace = "http://www.iho.int/S127/gml/cs0/1.0"


@dataclass
class SignalStationWarning(SignalStationWarningType):
    class Meta:
        namespace = "http://www.iho.int/S127/gml/cs0/1.0"


@dataclass
class UnderkeelClearanceAllowanceArea(UnderkeelClearanceAllowanceAreaType):
    class Meta:
        namespace = "http://www.iho.int/S127/gml/cs0/1.0"


@dataclass
class UnderkeelClearanceManagementArea(UnderkeelClearanceManagementAreaType):
    class Meta:
        namespace = "http://www.iho.int/S127/gml/cs0/1.0"


@dataclass
class VesselTrafficServiceArea(VesselTrafficServiceAreaType):
    class Meta:
        namespace = "http://www.iho.int/S127/gml/cs0/1.0"


@dataclass
class WaterwayArea(WaterwayAreaType):
    class Meta:
        namespace = "http://www.iho.int/S127/gml/cs0/1.0"


@dataclass
class PointOrCurvePropertyType:
    class Meta:
        target_namespace = "http://www.iho.int/s100gml/1.0+EXT"

    curve_property: Optional[CurveProperty1] = field(
        default=None,
        metadata={
            "name": "CurveProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0+EXT",
        }
    )
    surface_property: Optional[SurfaceProperty1] = field(
        default=None,
        metadata={
            "name": "SurfaceProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0+EXT",
        }
    )


@dataclass
class MemberType(AbstractFeatureMemberType):
    """
    dataset member.
    """
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    restricted_area_regulatory: Optional[RestrictedAreaRegulatory] = field(
        default=None,
        metadata={
            "name": "RestrictedAreaRegulatory",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    restricted_area_navigational: Optional[RestrictedAreaNavigational] = field(
        default=None,
        metadata={
            "name": "RestrictedAreaNavigational",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    waterway_area: Optional[WaterwayArea] = field(
        default=None,
        metadata={
            "name": "WaterwayArea",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    vessel_traffic_service_area: Optional[VesselTrafficServiceArea] = field(
        default=None,
        metadata={
            "name": "VesselTrafficServiceArea",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    signal_station_warning: Optional[SignalStationWarning] = field(
        default=None,
        metadata={
            "name": "SignalStationWarning",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    signal_station_traffic: Optional[SignalStationTraffic] = field(
        default=None,
        metadata={
            "name": "SignalStationTraffic",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    ship_reporting_service_area: Optional[ShipReportingServiceArea] = field(
        default=None,
        metadata={
            "name": "ShipReportingServiceArea",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    routeing_measure: Optional[RouteingMeasure] = field(
        default=None,
        metadata={
            "name": "RouteingMeasure",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    radio_calling_in_point: Optional[RadioCallingInPoint] = field(
        default=None,
        metadata={
            "name": "RadioCallingInPoint",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    radar_range: Optional[RadarRange] = field(
        default=None,
        metadata={
            "name": "RadarRange",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    place_of_refuge: Optional[PlaceOfRefuge] = field(
        default=None,
        metadata={
            "name": "PlaceOfRefuge",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    piracy_risk_area: Optional[PiracyRiskArea] = field(
        default=None,
        metadata={
            "name": "PiracyRiskArea",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    pilot_service: Optional[PilotService] = field(
        default=None,
        metadata={
            "name": "PilotService",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    pilot_boarding_place: Optional[PilotBoardingPlace] = field(
        default=None,
        metadata={
            "name": "PilotBoardingPlace",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    pilotage_district: Optional[PilotageDistrict] = field(
        default=None,
        metadata={
            "name": "PilotageDistrict",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    military_practice_area: Optional[MilitaryPracticeArea] = field(
        default=None,
        metadata={
            "name": "MilitaryPracticeArea",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    local_port_service_area: Optional[LocalPortServiceArea] = field(
        default=None,
        metadata={
            "name": "LocalPortServiceArea",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    isps_code_security_level: Optional[IspsCodeSecurityLevel] = field(
        default=None,
        metadata={
            "name": "IspsCodeSecurityLevel",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    concentration_of_shipping_hazard_area: Optional[ConcentrationOfShippingHazardArea] = field(
        default=None,
        metadata={
            "name": "ConcentrationOfShippingHazardArea",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    caution_area: Optional[CautionArea] = field(
        default=None,
        metadata={
            "name": "CautionArea",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    underkeel_clearance_management_area: Optional[UnderkeelClearanceManagementArea] = field(
        default=None,
        metadata={
            "name": "UnderkeelClearanceManagementArea",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    underkeel_clearance_allowance_area: Optional[UnderkeelClearanceAllowanceArea] = field(
        default=None,
        metadata={
            "name": "UnderkeelClearanceAllowanceArea",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    feature_type: Optional[FeatureType] = field(
        default=None,
        metadata={
            "name": "FeatureType",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    quality_of_non_bathymetric_data: Optional[QualityOfNonBathymetricData] = field(
        default=None,
        metadata={
            "name": "QualityOfNonBathymetricData",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    data_coverage: Optional[DataCoverage] = field(
        default=None,
        metadata={
            "name": "DataCoverage",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:/w{2,}",
        }
    )


@dataclass
class PointOrCurveProperty(PointOrCurvePropertyType):
    class Meta:
        namespace = "http://www.iho.int/s100gml/1.0+EXT"


@dataclass
class FeaturePropertyType1:
    class Meta:
        name = "FeaturePropertyType"
        target_namespace = "http://www.opengis.net/gml/3.2"

    restricted_area_regulatory: Optional[RestrictedAreaRegulatory] = field(
        default=None,
        metadata={
            "name": "RestrictedAreaRegulatory",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    restricted_area_navigational: Optional[RestrictedAreaNavigational] = field(
        default=None,
        metadata={
            "name": "RestrictedAreaNavigational",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    waterway_area: Optional[WaterwayArea] = field(
        default=None,
        metadata={
            "name": "WaterwayArea",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    vessel_traffic_service_area: Optional[VesselTrafficServiceArea] = field(
        default=None,
        metadata={
            "name": "VesselTrafficServiceArea",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    signal_station_warning: Optional[SignalStationWarning] = field(
        default=None,
        metadata={
            "name": "SignalStationWarning",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    signal_station_traffic: Optional[SignalStationTraffic] = field(
        default=None,
        metadata={
            "name": "SignalStationTraffic",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    ship_reporting_service_area: Optional[ShipReportingServiceArea] = field(
        default=None,
        metadata={
            "name": "ShipReportingServiceArea",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    routeing_measure: Optional[RouteingMeasure] = field(
        default=None,
        metadata={
            "name": "RouteingMeasure",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    radio_calling_in_point: Optional[RadioCallingInPoint] = field(
        default=None,
        metadata={
            "name": "RadioCallingInPoint",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    radar_range: Optional[RadarRange] = field(
        default=None,
        metadata={
            "name": "RadarRange",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    place_of_refuge: Optional[PlaceOfRefuge] = field(
        default=None,
        metadata={
            "name": "PlaceOfRefuge",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    piracy_risk_area: Optional[PiracyRiskArea] = field(
        default=None,
        metadata={
            "name": "PiracyRiskArea",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    pilot_service: Optional[PilotService] = field(
        default=None,
        metadata={
            "name": "PilotService",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    pilot_boarding_place: Optional[PilotBoardingPlace] = field(
        default=None,
        metadata={
            "name": "PilotBoardingPlace",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    pilotage_district: Optional[PilotageDistrict] = field(
        default=None,
        metadata={
            "name": "PilotageDistrict",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    military_practice_area: Optional[MilitaryPracticeArea] = field(
        default=None,
        metadata={
            "name": "MilitaryPracticeArea",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    local_port_service_area: Optional[LocalPortServiceArea] = field(
        default=None,
        metadata={
            "name": "LocalPortServiceArea",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    isps_code_security_level: Optional[IspsCodeSecurityLevel] = field(
        default=None,
        metadata={
            "name": "IspsCodeSecurityLevel",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    concentration_of_shipping_hazard_area: Optional[ConcentrationOfShippingHazardArea] = field(
        default=None,
        metadata={
            "name": "ConcentrationOfShippingHazardArea",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    caution_area: Optional[CautionArea] = field(
        default=None,
        metadata={
            "name": "CautionArea",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    underkeel_clearance_management_area: Optional[UnderkeelClearanceManagementArea] = field(
        default=None,
        metadata={
            "name": "UnderkeelClearanceManagementArea",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    underkeel_clearance_allowance_area: Optional[UnderkeelClearanceAllowanceArea] = field(
        default=None,
        metadata={
            "name": "UnderkeelClearanceAllowanceArea",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    feature_type: Optional[FeatureType] = field(
        default=None,
        metadata={
            "name": "FeatureType",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    quality_of_non_bathymetric_data: Optional[QualityOfNonBathymetricData] = field(
        default=None,
        metadata={
            "name": "QualityOfNonBathymetricData",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    data_coverage: Optional[DataCoverage] = field(
        default=None,
        metadata={
            "name": "DataCoverage",
            "type": "Element",
            "namespace": "http://www.iho.int/S127/gml/cs0/1.0",
        }
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    type: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:/w{2,}",
        }
    )


@dataclass
class DatasetType(AbstractFeatureType1):
    """
    Dataset element for dataset as "GML document".

    :ivar dataset_identification_information: Dataset identification
        information
    :ivar dataset_structure_information: Dataset structure information
    :ivar point:
    :ivar multi_point:
    :ivar curve:
    :ivar composite_curve:
    :ivar orientable_curve:
    :ivar surface:
    :ivar polygon:
    :ivar imember: intended for S100 information types. Extension of GML
        practice, not addressed by ISO 19136.
    :ivar member: intended for technical GML 3.2 requirement for making
        the dataset a "GML document" and clause 21.3 of the OGC GML
        standard
    """
    class Meta:
        target_namespace = "http://www.iho.int/S127/gml/cs0/1.0"

    dataset_identification_information: Optional[DataSetIdentificationType] = field(
        default=None,
        metadata={
            "name": "DatasetIdentificationInformation",
            "type": "Element",
            "namespace": "",
        }
    )
    dataset_structure_information: Optional[DataSetStructureInformationType] = field(
        default=None,
        metadata={
            "name": "DatasetStructureInformation",
            "type": "Element",
            "namespace": "",
        }
    )
    point: List[Point2] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    multi_point: List[MultiPoint2] = field(
        default_factory=list,
        metadata={
            "name": "MultiPoint",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    curve: List[Curve2] = field(
        default_factory=list,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    composite_curve: List[CompositeCurve2] = field(
        default_factory=list,
        metadata={
            "name": "CompositeCurve",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    orientable_curve: List[OrientableCurve2] = field(
        default_factory=list,
        metadata={
            "name": "OrientableCurve",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    surface: List[Surface2] = field(
        default_factory=list,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    polygon: List[Polygon2] = field(
        default_factory=list,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    imember: List[ImemberType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )
    member: List[MemberType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequential": True,
        }
    )


@dataclass
class Dataset(DatasetType):
    class Meta:
        namespace = "http://www.iho.int/S127/gml/cs0/1.0"
