from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Union
from xsdata.models.datatype import XmlDate, XmlPeriod, XmlTime
from s123.models.s100_3_0_0.s100_gml.pkg_20170505.s100_gml_profile import (
    AbstractFeatureMemberType,
    AbstractFeatureType as ProfileAbstractFeatureType,
    NilReasonEnumerationValue,
    ReferenceType,
)
from s123.models.s100_3_0_0.s100_gml.pkg_20170505.s100gmlbase import (
    AbstractFeatureType as S100GmlbaseAbstractFeatureType,
    AbstractInformationType,
    CompositeCurve,
    Curve,
    DataSetIdentificationType,
    DataSetStructureInformationType,
    MultiPoint,
    OrientableCurve,
    Point,
    Polygon,
    Surface,
    CurveProperty,
    PointProperty,
    SurfaceProperty,
)
from s123.models.s100_3_0_0.s100_gml.pkg_20170505.s100gmlbase_ext import SurfacePropertyType
from s123.models.s100_3_0_0.w3c.xml.pkg_2008.pkg_06.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://www.iho.int/S123/gml/1.0"


class Quapostype(Enum):
    """
    Definition required.

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


@dataclass
class S100TruncatedDate:
    """
    built in date types from W3C XML schema, implementing S-100 truncated date.
    """
    class Meta:
        name = "S100_TruncatedDate"

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


class CategoryOfBroadcastCommunicationType(Enum):
    """
    Classification of broadcast or communications based on public availability
    and commercial/non-commercial nature.

    :cvar COMMERCIAL: A service operated with the intention of earning
        money
    :cvar NON_COMMERCIAL: A service without any financial interest
    :cvar PUBLIC: A service available for the general community
    :cvar NON_PUBLIC: A service available for limited and pre-defined
        customers
    """
    COMMERCIAL = "commercial"
    NON_COMMERCIAL = "non-commercial"
    PUBLIC = "public"
    NON_PUBLIC = "non-public"


class CategoryOfCargoType(Enum):
    """Remarks: If item 7 is used, the nature of dangerous or hazardous cargoes can be amplified with category of dangerous or hazardous cargo.

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
    """
    BULK = "bulk"
    CONTAINER = "container"
    GENERAL = "general"
    LIQUID = "liquid"
    PASSENGER = "passenger"
    LIVESTOCK = "livestock"
    DANGEROUS_OR_HAZARDOUS = "dangerous or hazardous"


class CategoryOfCommPrefType(Enum):
    """
    Classification of frequencies, VHF channels, telephone numbers, or other
    means of communication based on preference.

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
    IMDG_CODE_CLASS_6_DIV_6_2 = "IMDG Code Class 6. Div. 6.2"
    IMDG_CODE_CLASS_7 = "IMDG Code Class 7"
    IMDG_CODE_CLASS_8 = "IMDG Code Class 8"
    IMDG_CODE_CLASS_9 = "IMDG Code Class 9"
    HARMFUL_SUBSTANCES_IN_PACKAGED_FORM = "Harmful Substances in packaged form"


class CategoryOfFrcstAndWarningAreaType(Enum):
    """
    Classification of weather forecast and weather warning areas based on
    source of warnings and forecasts.

    :cvar WORLD_METEOROLOGICAL_ORGANIZATION_WMO: The forecast and
        warning area defined by WMO
    :cvar NATIONAL_HIGH_SEAS: The forecast and warning area defined by
        national authorities covering High Seas
    :cvar NATIONAL_OFFSHORE: The forecast and warning area defined by
        national authorities covering offshore waters.
    :cvar NATIONAL_COASTAL: The forecast and warning area defined by
        national authorities covering coastal waters.
    :cvar NATIONAL_INSHORE: The forecast and warning area defined by
        national authorities covering inshore waters.
    :cvar NATIONAL_LOCAL: The forecast and warning area defined by
        national authorities covering local waters.
    :cvar ICE: The ice forecast area defined by international or
        national authorities.
    """
    WORLD_METEOROLOGICAL_ORGANIZATION_WMO = "World Meteorological Organization (WMO)"
    NATIONAL_HIGH_SEAS = "National high seas"
    NATIONAL_OFFSHORE = "National offshore"
    NATIONAL_COASTAL = "National coastal"
    NATIONAL_INSHORE = "National inshore"
    NATIONAL_LOCAL = "National local"
    ICE = "Ice"


class CategoryOfGmdssareaType(Enum):
    """
    Classification of GMDSS areas based on availability of GMDSS services and
    GMDSS equipment requirements.

    :cvar AREA_A1: Within range of VHF coast stations with continuous
        DSC alerting available (about 20 – 30 miles)
    :cvar AREA_A2: Beyond area A1, but within range of MF coastal
        stations with continuous DSC alerting available (about l00
        miles)
    :cvar AREA_A3: Beyond the first two areas, but within coverage of
        geostationary maritime communication satellites (in practice
        this means Inmarsat). This covers the area between roughly 70
        deg N and 70 deg S.
    :cvar AREA_A4: The remaining sea areas. The most important of these
        is the sea around the North Pole (the area around the South Pole
        is mostly land). Geostationary satellites, which are positioned
        above the equator, cannot reach this far.
    """
    AREA_A1 = "Area A1"
    AREA_A2 = "Area A2"
    AREA_A3 = "Area A3"
    AREA_A4 = "Area A4"


class CategoryOfLandmarkType(Enum):
    """Classification of prominent cultural and natural features in the
    landscape.

    S-123 Note: Only landmarks of relevance to radiocommunications are
    encoded in S-123 datasets, e.g., radio masts used for marine
    broadcasts if their location needs to be shown

    :cvar DISH_AERIAL: A parabolic aerial for the receipt and
        transmission of high frequency radio signals. (IHO Dictionary –
        S-32).
    :cvar MAST: A relatively tall structure usually held vertical by guy
        lines. (S-57 Edition 3.1, Appendix A – Chapter 2, Page 2.45,
        November 2000).
    :cvar TOWER: A relatively tall, narrow structure that may either
        stand alone or may form part of another structure. (Defence
        Geospatial Information Working Group; Feature Data Dictionary
        Register, 2010).
    """
    DISH_AERIAL = "dish aerial"
    MAST = "mast"
    TOWER = "tower"


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
    :cvar NBDP_TELEGRAPHY: Narrow Band Direct Printing Telegraphy. A
        communications system consisting of teletypewriters connected to
        a telephonic network to send and receive wireless signals.
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
    NBDP_TELEGRAPHY = "NBDP Telegraphy"
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


class CategoryOfRadioStationType(Enum):
    """
    Classification of radio services offered by a radio station.

    :cvar RADIO_DIRECTION_FINDING_STATION: A radio station intended only
        to determine the direction of other stations by means of
        transmission from the latter.
    :cvar DECCA: The Decca Navigator System is a high-accuracy, short to
        medium range radio navigation aid intended for coastal and
        landfall navigation.
    :cvar LORAN_C: A low frequency electronic position fixing system
        using pulsed transmissions at 100 Khz.
    :cvar DIFFERENTIAL_GNSS: A radiobeacon transmitting DGPS correction
        signals.
    :cvar TORAN: An electronic position fixing system used mainly by
        aircraft.
    :cvar OMEGA: A long-range radio navigational aid which operates
        within the VLF frequency band. The system comprises eight land
        based stations.
    :cvar SYLEDIS: A ranging position fixing system operating at
        420-450MHz over a range of up to 400 Km.
    :cvar CHAIKA: A low frequency electronic position fixing system
        using pulsed transmissions at 100 Khz.
    :cvar FACSIMILE_TRANSMISSION: facsimile transmission (IHO HYDRO
        register, 2010-11-14)
    :cvar RADIO_TELEPHONE_STATION: The equipment needed at one station
        to carry on two way voice communication by radio waves only.
    :cvar AIS_BASE_STATION: Remark: Not defined in GI Registry
        (2017-04-20).
    """
    RADIO_DIRECTION_FINDING_STATION = "radio direction-finding station"
    DECCA = "Decca"
    LORAN_C = "Loran C"
    DIFFERENTIAL_GNSS = "Differential GNSS"
    TORAN = "Toran"
    OMEGA = "Omega"
    SYLEDIS = "Syledis"
    CHAIKA = "Chaika"
    FACSIMILE_TRANSMISSION = "facsimile transmission"
    RADIO_TELEPHONE_STATION = "radio telephone station"
    AIS_BASE_STATION = "AIS base station"


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


class CategoryOfTemporalVariationType(Enum):
    """
    An assessment of the likelihood of change within an area since last survey.

    :cvar EXTREME_EVENT: NIPWG: No new hydrographic survey conducted
        after an event (e.g., hurricane, earthquake, volcanic eruption,
        landslide, etc.) which is considered likely to have resulted in
        significant change at the location. In GI Registry: Definition:
        No new hydrographic survey conducted after an event (e.g.
        hurricane, earthquake, volcanic eruption, landslide, etc), which
        is considered likely to have changed the seafloor significantly.
    :cvar LIKELY_TO_CHANGE: NIPWG: Continuous or frequent change (e.g.,
        river siltation, sand waves, seasonal storms, construction,
        etc.) GI Registry: Continuous or frequent change (e.g. river
        siltation, sand waves, seasonal storms, ice bergs, etc).
    :cvar LIKELY_TO_CHANGE_BUT_SIGNIFICANT_SHOALING_NOT_EXPECTED: GI
        Registry: Likely to change but significant shoaling no expected
        [Proposed draft 6/27/2014: Recommended that SNPWG not use this
        enumerate - ref. E.M. email 6/27/2014.]
    :cvar UNLIKELY_TO_CHANGE: NIPWG: Significant change at the location
        is not expected. GI Registry: Significant change to the seafloor
        is not expected.
    :cvar UNASSESSED: Temporal variation not assessed or cannot be
        determined
    """
    EXTREME_EVENT = "extreme event"
    LIKELY_TO_CHANGE = "likely to change"
    LIKELY_TO_CHANGE_BUT_SIGNIFICANT_SHOALING_NOT_EXPECTED = "likely to change but significant shoaling not expected"
    UNLIKELY_TO_CHANGE = "unlikely to change"
    UNASSESSED = "unassessed"


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


@dataclass
class ContactAddressType:
    """Direction or superscription of a letter, package, etc., specifying the
    name of the place to which it is directed, and optionally a contact person
    or organisation who should receive it.

    (Oxford English Dictionary, 2nd Ed., adapted).

    :ivar delivery_point: Details of where post can be delivered such as
        the apartment, name and/or number of a street, building or PO
        Box.
    :ivar city_name: The name of a town or city.
    :ivar administrative_division: Administrative division is a generic
        term for an administrative region within a country at a level
        below that of the sovereign state.
    :ivar country: The name of a nation. (Adapted from The American
        Heritage Dictionaries)
    :ivar postal_code: Known in various countries as a postcode, or ZIP
        code, the postal code is a series of letters and/or digits that
        identifies each postal delivery area.
    """
    class Meta:
        name = "contactAddressType"

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
    country: Optional[str] = field(
        default=None,
        metadata={
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


class DataAssessmentType(Enum):
    """
    The categorisation of the assessment level of bathymetric data for an area.

    :cvar ASSESSED: The quality of the bathymetric data has been
        assessed.
    :cvar OCEANIC: The quality of oceanic bathymetric data has been
        assessed or is not required.
    :cvar UNASSESSED: The quality of the bathymetric data has yet to be
        assessed.
    """
    ASSESSED = "assessed"
    OCEANIC = "oceanic"
    UNASSESSED = "unassessed"


class DayOfWeekType(Enum):
    """
    :cvar MONDAY: monday - the day of the week before Tuesday and
        following Sunday
    :cvar TUESDAY: the day of the week before Wednesday and following
        Monday
    :cvar WEDNESDAY: wednesday - the day of the week before Thursday and
        following Tuesday
    :cvar THURSDAY: thursday - the day of the week before Friday and
        following Wednesday
    :cvar FRIDAY: friday - the day of the week before Saturday and
        following Thursday
    :cvar SATURDAY: saturday - the day of the week before Sunday and
        following Friday (together with Sunday forming part of the
        weekend)
    :cvar SUNDAY: sunday - the day of the week before Monday and
        following Saturday (together with Saturday forms part of the
        weekend)
    """
    MONDAY = "monday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"
    THURSDAY = "thursday"
    FRIDAY = "friday"
    SATURDAY = "saturday"
    SUNDAY = "sunday"


@dataclass
class FacsimileDrumSpeedType:
    """
    The drum speed and index of co-operation of a facsimile machine.

    :ivar drum_speed: The drum speed in revolutions per minute. The drum
        speed should be encoded using three digits for the speed
        including a leading zero if necessary. Resolution: 1
    :ivar index_of_cooperation: A factor governing the image resolution
        of radiofax transmissions. The Index of Cooperation must be
        known to decode the transmission. The Index of Co-operation is
        generally 576, although 288 with alternate line scanning is
        sometimes used.
    """
    class Meta:
        name = "facsimileDrumSpeedType"

    drum_speed: Optional[int] = field(
        default=None,
        metadata={
            "name": "drumSpeed",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    index_of_cooperation: Optional[int] = field(
        default=None,
        metadata={
            "name": "indexOfCooperation",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


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
    """
    class Meta:
        name = "frequencyPairType"

    frequency_shore_station_transmits: Optional[int] = field(
        default=None,
        metadata={
            "name": "frequencyShoreStationTransmits",
            "type": "Element",
            "namespace": "",
        }
    )
    frequency_shore_station_receives: Optional[int] = field(
        default=None,
        metadata={
            "name": "frequencyShoreStationReceives",
            "type": "Element",
            "namespace": "",
        }
    )


class FunctionType(Enum):
    """
    A specific role that describes a feature.

    :cvar COMMUNICATION: Transmitting and/or receiving electronic
        communication signals. (Defence Geospatial Information Working
        Group; Feature Data Dictionary Register, 2010).
    :cvar RADIO: Transmitting and/or receiving radio-frequency
        electromagnetic waves as a means of communication. (Defence
        Geospatial Information Working Group; Feature Data Dictionary
        Register, 2010).
    :cvar MICROWAVE: Broadcasting and receiving signals using
        microwaves. (S-57 Edition 3.1, Appendix A – Chapter 2, Page
        2.133, November 2000).
    :cvar CONTROL: Used to control the flow of traffic within a
        specified range of an installation. (Defence Geospatial
        Information Working Group; Feature Data Dictionary Register,
        2010).
    :cvar SEA_RESCUE_CONTROL: A unit responsible for promoting efficient
        organization of search and rescue services and for coordinating
        the conduct of search and rescue operations within a search and
        rescue region. (Defence Geospatial Information Working Group;
        Feature Data Dictionary Register, 2010).
    """
    COMMUNICATION = "communication"
    RADIO = "radio"
    MICROWAVE = "microwave"
    CONTROL = "control"
    SEA_RESCUE_CONTROL = "sea rescue control"


@dataclass
class HorizontalPositionalUncertainty:
    """
    Definition required.

    :ivar uncertainty_fixed: Definition required
    :ivar uncertainty_variable: Definition required
    """
    class Meta:
        name = "horizontalPositionalUncertainty"

    uncertainty_fixed: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "uncertaintyFixed",
            "type": "Element",
            "namespace": "",
            "nillable": True,
        }
    )
    uncertainty_variable: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "uncertaintyVariable",
            "type": "Element",
            "namespace": "",
        }
    )


class InformationConfidenceType(Enum):
    """
    The likelihood that a vessel will experience the phenomenon described by a
    feature, or that the service described by the feature will be available.

    :cvar VIRTUALLY_CERTAIN: Virtually certain to be experienced by (or
        available to) an individual vessel; will be experienced by
        nearly all vessels.  (FAA, adapted.)
    :cvar HIGH_LIKELIHOOD: Frequently experienced by (or available to)
        an individual vessel; experienced by a majority of vessels.
        (FAA, adapted.)
    :cvar MEDIUM_LIKELIHOOD: Occasionally experienced by (or available
        to) an individual vessel; experienced by (or available to) about
        half of all vessels. (FAA, adapted.)
    :cvar LOW_LIKELIHOOD: Unlikely, but sometimes (rarely) experienced
        by (or available to) an individual vessel; experienced by (or
        available to) a minority of vessels). (FAA, adapted.)
    """
    VIRTUALLY_CERTAIN = "virtuallyCertain"
    HIGH_LIKELIHOOD = "highLikelihood"
    MEDIUM_LIKELIHOOD = "mediumLikelihood"
    LOW_LIKELIHOOD = "lowLikelihood"


@dataclass
class InformationType:
    """Provides textual information that cannot be provided using other
    allowable attributes for the feature, in a defined language. The
    information may be provided as a string in sub-attribute text, or by
    encoding the file name of a single external text file that contains the
    text in sub-attribute file reference.

    Remarks: - The sub-attribute text should be used, for example, to hold the information that is shown on paper charts by cautionary and explanatory notes. No formatting of text is possible within the sub-attribute text. If formatted text is required then an associated text file referenced by the sub-attribute file reference must be used; - The sub-attribute file reference is generally used for long text strings or those that require formatting, however there is no restriction on the type of text (except for lexical level) that can be held in files referenced by sub-attribute file reference.

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
    :cvar DOWNLOAD: online instructions for transferring data from one
        storage device or system to another. (ISO 19115:2014)
    :cvar INFORMATION: online information about the resource (ISO
        19115:2014)
    :cvar OFFLINE_ACCESS: online instructions for requesting the
        resource from the provider (ISO 19115:2014)
    :cvar ORDER: online order process for obtaining the resource (ISO
        19115:2014).
    :cvar SEARCH: online search interface for seeking out information
        about the resource (ISO 19115:2014).
    :cvar COMPLETE_METADATA: complete metadata provided (ISO
        19115:2014).
    :cvar BROWSE_GRAPHIC: browse graphic provided (ISO 19115:2014).
    :cvar UPLOAD: online resource upload capability provided (ISO
        19115:2014).
    :cvar EMAIL_SERVICE: online email service provided (ISO 19115:2014)
    :cvar BROWSING: online browsing provided (ISO 19115:2014)
    :cvar FILE_ACCESS: online file access provided (ISO 19115:2014).
    """
    DOWNLOAD = "download"
    INFORMATION = "information"
    OFFLINE_ACCESS = "offlineAccess"
    ORDER = "order"
    SEARCH = "search"
    COMPLETE_METADATA = "completeMetadata"
    BROWSE_GRAPHIC = "browseGraphic"
    UPLOAD = "upload"
    EMAIL_SERVICE = "emailService"
    BROWSING = "browsing"
    FILE_ACCESS = "fileAccess"


@dataclass
class OrientationType:
    class Meta:
        name = "orientationType"

    orientation_uncertainty: Optional[str] = field(
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
            "nillable": True,
        }
    )


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
    """The attribute from which a text string is derived.

    (S-122/123) Remark: S-122/123 do not include light features and
    therefore listed value '2: light characteristic' is omitted from the
    S-122 application schema.

    :cvar FEATURE_NAME: Definition required
    """
    FEATURE_NAME = "feature name"


class TimeReferenceType(Enum):
    """
    :cvar UTC: Coordinated Universal Time
    :cvar LT: Local time
    """
    UTC = "UTC"
    LT = "LT"


class TransmissionRegularityType(Enum):
    """
    :cvar CONTINUOUS: transmission is made continuously
    :cvar REGULAR: transmission is made regularly according to a
        schedule
    :cvar ON_RECEIPT: transmission is made when warning or information
        is received from another authority
    :cvar AS_REQUIRED: transmission is made under specified conditions
        or when needed
    :cvar ON_REQUEST: transmission is made when requested by a user
    """
    CONTINUOUS = "continuous"
    REGULAR = "regular"
    ON_RECEIPT = "on receipt"
    AS_REQUIRED = "as required"
    ON_REQUEST = "on request"


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
        her waterline.(UKHO NP100/2009)
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


@dataclass
class CurveOrSurface:
    curve_property: Optional[CurveProperty] = field(
        default=None,
        metadata={
            "name": "curveProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    surface_property: Optional[SurfaceProperty] = field(
        default=None,
        metadata={
            "name": "surfaceProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )


@dataclass
class GmCurve:
    class Meta:
        name = "GM_Curve"

    curve_property: Optional[CurveProperty] = field(
        default=None,
        metadata={
            "name": "curveProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )


@dataclass
class GmPoint:
    class Meta:
        name = "GM_Point"

    point_property: Optional[PointProperty] = field(
        default=None,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )


@dataclass
class GmSurface:
    class Meta:
        name = "GM_Surface"

    surface_property: Optional[SurfaceProperty] = field(
        default=None,
        metadata={
            "name": "surfaceProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )


@dataclass
class MetaFeatureType(S100GmlbaseAbstractFeatureType):
    """
    Generalized feature type which carry all the common attributes.
    """
    class Meta:
        namespace = "http://www.iho.int/S123/gml/1.0"


@dataclass
class PointCurveSurface:
    point_property: Optional[PointProperty] = field(
        default=None,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    curve_property: Optional[CurveProperty] = field(
        default=None,
        metadata={
            "name": "curveProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    surface_property: Optional[SurfaceProperty] = field(
        default=None,
        metadata={
            "name": "surfaceProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )


@dataclass
class PointOrCurve:
    curve_property: Optional[CurveProperty] = field(
        default=None,
        metadata={
            "name": "curveProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    surface_property: Optional[SurfaceProperty] = field(
        default=None,
        metadata={
            "name": "surfaceProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )


@dataclass
class PointOrSurface:
    point_property: Optional[PointProperty] = field(
        default=None,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    surface_property: Optional[SurfaceProperty] = field(
        default=None,
        metadata={
            "name": "surfaceProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )


@dataclass
class BearingInformationType:
    """A bearing is the direction one object is from another object.

    At least one of the sub-attributes must be present.
    """
    class Meta:
        name = "bearingInformationType"

    cardinal_direction: Optional[CardinalDirectionType] = field(
        default=None,
        metadata={
            "name": "cardinalDirection",
            "type": "Element",
            "namespace": "",
        }
    )
    distance: Optional[str] = field(
        default=None,
        metadata={
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

    :ivar date_start: The start date or time of the interval.
    :ivar date_end: The end date or time of the interval.
    """
    class Meta:
        name = "fixedDateRangeType"

    date_start: Optional[S100TruncatedDate] = field(
        default=None,
        metadata={
            "name": "dateStart",
            "type": "Element",
            "namespace": "",
        }
    )
    date_end: Optional[S100TruncatedDate] = field(
        default=None,
        metadata={
            "name": "dateEnd",
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
    :ivar online_description: detailed text description of what the
        online resource is/does (ISO 19115)
    :ivar online_function: code for function performed by the online
        resource (ISO 19115)
    :ivar protocol_request: Request used to access the resource.
        Structure and content depend on the protocol and standard used
        by the online resource, such as Web Feature Service standard.
        (ISO 19115, adapted)
    """
    class Meta:
        name = "onlineResourceType"

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
    online_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "onlineDescription",
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

    date_start: Optional[S100TruncatedDate] = field(
        default=None,
        metadata={
            "name": "dateStart",
            "type": "Element",
            "namespace": "",
            "nillable": True,
        }
    )
    date_end: Optional[S100TruncatedDate] = field(
        default=None,
        metadata={
            "name": "dateEnd",
            "type": "Element",
            "namespace": "",
            "nillable": True,
        }
    )


@dataclass
class RadioStationCommunicationDescriptionType:
    """Description of the type and content of a communication or broadcast from
    a radio station.

    Remark: This complex attribute is not intended for detailed descriptions of a station's radio services. For detailed descriptions of radio service, use the attributes of the  associated RadioServiceArea feature.

    :ivar category_of_maritime_broadcast:
    :ivar communication_channel: A channel number assigned to a specific
        radio frequency, frequencies or frequency band. Remarks: The
        attribute “communication channel” encodes the various VHF-
        Channels used for communication.
    :ivar signal_frequency: The frequency of a signal. TBD: Upper bound
        on multiplcity is a divergence from April 2017 model.
    :ivar transmission_content: Content of transmission. Remark: Other
        than MSI. Not to be used if CATMAB is populated.
    """
    class Meta:
        name = "radioStationCommunicationDescriptionType"

    category_of_maritime_broadcast: List[CategoryOfMaritimeBroadcastType] = field(
        default_factory=list,
        metadata={
            "name": "categoryOfMaritimeBroadcast",
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
    :ivar country:
    :ivar feature_name:
    :ivar reported_date:
    :ivar source: The publication, document, or reference work from
        which information comes or is acquired.
    :ivar source_type: Type of source
    """
    class Meta:
        name = "sourceIndicationType"

    category_of_authority: Optional[CategoryOfAuthorityType] = field(
        default=None,
        metadata={
            "name": "categoryOfAuthority",
            "type": "Element",
            "namespace": "",
        }
    )
    country: Optional[str] = field(
        default=None,
        metadata={
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
    reported_date: Optional[S100TruncatedDate] = field(
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

    date_start: Optional[S100TruncatedDate] = field(
        default=None,
        metadata={
            "name": "dateStart",
            "type": "Element",
            "namespace": "",
            "nillable": True,
        }
    )
    date_end: Optional[S100TruncatedDate] = field(
        default=None,
        metadata={
            "name": "dateEnd",
            "type": "Element",
            "namespace": "",
            "nillable": True,
        }
    )


@dataclass
class TimeOfObservationType:
    """The time in the day when a weather or ice observation is made, expressed
    in UTC or local time.

    The time of observation normally amplifies the time of transmission
    of radio-facsimile weather maps or ice charts.

    :ivar observation_time: The time on each day when observations are
        made
    :ivar time_reference:
    """
    class Meta:
        name = "timeOfObservationType"

    observation_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "observationTime",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    time_reference: Optional[TimeReferenceType] = field(
        default=None,
        metadata={
            "name": "timeReference",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class TimesOfTransmissionType:
    """
    One or more times in the day when the radio station starts a routine
    transmission, normally expressed in UTC or local time.

    :ivar minute_past_even_hours: The minute past even hours when a
        routine transmission starts.
    :ivar minute_past_every_hour: The minute past every hour when a
        routine transmission starts
    :ivar minute_past_odd_hours: The minute past odd hours when a
        routine transmission starts.
    :ivar time_reference:
    :ivar transmission_time: The time in the day when scheduled
        transmissions start.
    """
    class Meta:
        name = "timesOfTransmissionType"

    minute_past_even_hours: Optional[int] = field(
        default=None,
        metadata={
            "name": "minutePastEvenHours",
            "type": "Element",
            "namespace": "",
        }
    )
    minute_past_every_hour: Optional[int] = field(
        default=None,
        metadata={
            "name": "minutePastEveryHour",
            "type": "Element",
            "namespace": "",
        }
    )
    minute_past_odd_hours: Optional[int] = field(
        default=None,
        metadata={
            "name": "minutePastOddHours",
            "type": "Element",
            "namespace": "",
        }
    )
    time_reference: Optional[TimeReferenceType] = field(
        default=None,
        metadata={
            "name": "timeReference",
            "type": "Element",
            "namespace": "",
        }
    )
    transmission_time: List[XmlTime] = field(
        default_factory=list,
        metadata={
            "name": "transmissionTime",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class TmIntervalsByDoW:
    """Time intervals by days of the week.
    Remarks:
    The sub-attribute dayOfWeekIsRanges indicates whether an instance of this attribute encodes a range of days or discrete days. The days or day-range(s) are encoded in sub-attribute dayOfWeek. Multiple ranges are allowed but mixing range with discrete days(s) is not allowed (encode another instance of this attribute instead).
    An indeterminate range may be indicated with a null value at the appropriate position in the sequence.
    Examples:
    - To code the range “Monday through Friday” use the sequence: dayOfWeek=1, dayOfWeek=5 and set dayOfWeekIsRanges=TRUE.
    - To encode the days Monday, Wednesday, Friday, use the sequence dayOfWeek=1, dayOfWeek=3, dayOfWeek=5 and set dayOfWeekIsRanges=FALSE.
    - The sequence dayOfWeek=1, dayOfWeek=3, dayOfWeek=5  to indicate Mon-Wed and Thursday is not allowed. Encode the Mon-Wed and Thursday schedules in different instances of this complex attribute.
    Product specifications may need to allow this attribute to be repeated in order to allow encoding of schedules which vary for different days of the week.

    :ivar day_of_week: Encodes either range(s) of days or discrete days.
    :ivar day_of_week_is_ranges: Indicates whether the values in
        dayOfWeek indicate a range of days (true) or discrete days
        (false).
    :ivar time_reference: Indicates whether the time co-attributes are
        encoded in UTC or local time (LT).
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
        name = "tmIntervalsByDoW"

    day_of_week: List[DayOfWeekType] = field(
        default_factory=list,
        metadata={
            "name": "dayOfWeek",
            "type": "Element",
            "namespace": "",
            "max_occurs": 7,
        }
    )
    day_of_week_is_ranges: Optional[bool] = field(
        default=None,
        metadata={
            "name": "dayOfWeekIsRanges",
            "type": "Element",
            "namespace": "",
            "nillable": True,
        }
    )
    time_reference: Optional[TimeReferenceType] = field(
        default=None,
        metadata={
            "name": "timeReference",
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
class VesselsMeasurementsType:
    class Meta:
        name = "vesselsMeasurementsType"

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
class DataCoverageType(MetaFeatureType):
    """
    A geographical area that describes the coverage and extent of spatial
    types.

    :ivar maximum_display_scale: The largest intended viewing scale for
        the data. Not nillable(?)
    :ivar minimum_display_scale: The smallest intended viewing scale for
        the data. Not nillable(?)
    :ivar geometry:
    """
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
    geometry: Optional[SurfacePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class DataQualityType(MetaFeatureType):
    """
    Abstract feature type for data quality meta-features.

    :ivar information: Use of attribute information is discouraged for
        nautical publications data quality meta-features.
    """
    information: List[InformationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class InformationTypeType(AbstractInformationType):
    """
    Generalized information type which carry all the common attributes.
    """
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
    provides_information: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "providesInformation",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class TextPlacement:
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
    :ivar identifies: Association to feature for which the text is
        placed
    :ivar geometry:
    """
    class Meta:
        namespace = "http://www.iho.int/S123/gml/1.0"

    flip_bearing: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "flipBearing",
            "type": "Element",
            "namespace": "",
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
    :ivar category_of_radio_methods:
    :ivar category_of_maritime_broadcast:
    :ivar communication_channel:
    :ivar contact_instructions: supplemental instructions on how or when
        to contact the individual, organisation, or service
    :ivar facsimile_drum_speed:
    :ivar frequency_pair:
    :ivar selective_call_number: When stations of the maritime mobile
        service (direct printing telegraphy) use selective calling
        devices, their Selective Call numbers (SELCAL) are formed of
        four digits (coast stations). (Adapted: Radio Regulations (ITU))
    :ivar signal_frequency: TBD: Upper bound on multiplcity is a
        divergence from April 2017 model.
    :ivar time_of_observation:
    :ivar times_of_transmission:
    :ivar transmission_content: Content of transmission. Remarks: Not to
        be used if CATMAB is populated
    :ivar tm_intervals_by_do_w:
    :ivar transmission_regularity: Classification of regularity or
        conditions for transmission
    """
    class Meta:
        name = "radiocommunicationsType"

    category_of_comm_pref: Optional[CategoryOfCommPrefType] = field(
        default=None,
        metadata={
            "name": "categoryOfCommPref",
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
    category_of_maritime_broadcast: List[CategoryOfMaritimeBroadcastType] = field(
        default_factory=list,
        metadata={
            "name": "categoryOfMaritimeBroadcast",
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
    facsimile_drum_speed: Optional[FacsimileDrumSpeedType] = field(
        default=None,
        metadata={
            "name": "facsimileDrumSpeed",
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
    selective_call_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "selectiveCallNumber",
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
    time_of_observation: Optional[TimeOfObservationType] = field(
        default=None,
        metadata={
            "name": "timeOfObservation",
            "type": "Element",
            "namespace": "",
        }
    )
    times_of_transmission: Optional[TimesOfTransmissionType] = field(
        default=None,
        metadata={
            "name": "timesOfTransmission",
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
    tm_intervals_by_do_w: List[TmIntervalsByDoW] = field(
        default_factory=list,
        metadata={
            "name": "tmIntervalsByDoW",
            "type": "Element",
            "namespace": "",
        }
    )
    transmission_regularity: List[TransmissionRegularityType] = field(
        default_factory=list,
        metadata={
            "name": "transmissionRegularity",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class ScheduleByDoWtype:
    """
    Describes the nature and timings of a daily schedule by days of the week.

    :ivar category_of_schedule: Describes the type of schedule, e.g.,
        opening, closure, etc.
    :ivar tm_intervals_by_do_w:
    """
    class Meta:
        name = "scheduleByDoWType"

    category_of_schedule: Optional[Union[str, CategoryOfScheduleTypeValue]] = field(
        default=None,
        metadata={
            "name": "categoryOfSchedule",
            "type": "Element",
            "namespace": "",
            "pattern": r"other: [a-zA-Z0-9]+( [a-zA-Z0-9]+)*",
        }
    )
    tm_intervals_by_do_w: List[TmIntervalsByDoW] = field(
        default_factory=list,
        metadata={
            "name": "tmIntervalsByDoW",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class TextContentType:
    """Remarks: - Exactly one of sub-attributes onlineResource or information must be completed in one instance of textContent.
    - Product specifications may restrict the use or content  of onlineResource for security. For example, a product specification may forbid populating onlineResource.
    - Product specification authors must consider whether applications using the data product may be prevented from accessing off-system resources by security policies."""
    class Meta:
        name = "textContentType"

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
class AbstractRxntype(InformationTypeType):
    """An abstract superclass for information types that encode rules,
    recommendations, and general information in text or graphic form.

    Remarks: Subtypes of AbstractRxN carry the same attributes, but differ in the nature of information they encode. There are currently four such subtypes: Regulations, Restrictions, Recommendations, and NauticalInformation.
    """
    class Meta:
        name = "AbstractRXNType"

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

    :ivar ballast: True: Vessel is predominantly empty of cargo and
        stabilised with the use of ballast water False: Vessel is
        carrying cargo and is not ballasted.
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
    """
    ballast: Optional[bool] = field(
        default=None,
        metadata={
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


@dataclass
class AuthorityType(InformationTypeType):
    """A person or organisation having political or administrative power and
    control.

    (Oxford Dictionary of English)
    """
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
    the_information: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "theInformation",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class DataCoverage(DataCoverageType):
    class Meta:
        namespace = "http://www.iho.int/S123/gml/1.0"


@dataclass
class FeatureType(S100GmlbaseAbstractFeatureType):
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
        namespace = "http://www.iho.int/S123/gml/1.0"

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
        namespace = "http://www.iho.int/S123/gml/1.0"

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

    :ivar fixed_date: The date when a festival or national holiday
        recurs on the same day each year in the Gregorian calendar.
    :ivar variable_date: A day which is not fixed in the Gregorian
        calendar. Examples: The fourth Thursday in November; new moon
        day of Kartika (Diwali); Easter Sunday.
    :ivar information:
    :ivar the_service_hours_nsdy: optional
    """
    fixed_date: List[S100TruncatedDate] = field(
        default_factory=list,
        metadata={
            "name": "fixedDate",
            "type": "Element",
            "namespace": "",
        }
    )
    variable_date: List[str] = field(
        default_factory=list,
        metadata={
            "name": "variableDate",
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
        namespace = "http://www.iho.int/S123/gml/1.0"

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
class QualityOfTemporalVariationType(DataQualityType):
    """
    Abstract type for meta-feature which can describe temporal variation.

    :ivar category_of_temporal_variation:
    :ivar data_assessment: The categorisation of the assessment level of
        bathymetric data for an area.
    """
    class Meta:
        namespace = "http://www.iho.int/S123/gml/1.0"

    category_of_temporal_variation: Optional[CategoryOfTemporalVariationType] = field(
        default=None,
        metadata={
            "name": "categoryOfTemporalVariation",
            "type": "Element",
            "namespace": "",
            "nillable": True,
        }
    )
    data_assessment: Optional[DataAssessmentType] = field(
        default=None,
        metadata={
            "name": "dataAssessment",
            "type": "Element",
            "namespace": "",
            "nillable": True,
        }
    )


@dataclass
class ServiceHoursType(InformationTypeType):
    """
    The time when a service is available and known exceptions.

    :ivar schedule_by_do_w:
    :ivar information:
    :ivar the_authority_srv_hrs: optional
    :ivar partial_working_day:
    """
    schedule_by_do_w: List[ScheduleByDoWtype] = field(
        default_factory=list,
        metadata={
            "name": "scheduleByDoW",
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
class SpatialQuality(InformationTypeType):
    class Meta:
        namespace = "http://www.iho.int/S123/gml/1.0"

    category_of_temporal_variation: Optional[CategoryOfTemporalVariationType] = field(
        default=None,
        metadata={
            "name": "categoryOfTemporalVariation",
            "type": "Element",
            "namespace": "",
        }
    )
    horizontal_positional_uncertainty: Optional[HorizontalPositionalUncertainty] = field(
        default=None,
        metadata={
            "name": "horizontalPositionalUncertainty",
            "type": "Element",
            "namespace": "",
        }
    )
    quality_of_horizontal_measurement: Optional[Quapostype] = field(
        default=None,
        metadata={
            "name": "qualityOfHorizontalMeasurement",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class TelecommunicationsType:
    """
    A means or channel of communication at a distance by electrical,
    electronic, or electromagnetic means such as telegraphy, telephony, or
    broadcasting.

    :ivar telecommunication_identifier: Identifier used for contact by
        means of a telecommunications service, such as a telephone
        number
    :ivar telcom_carrier: The name of provider or type of carrier for  a
        telecommunications service
    :ivar contact_instructions: instructions on how and when to contact
        an individual or organisation
    :ivar telecommunication_service: Type of telecommunications service
    :ivar category_of_comm_pref:
    :ivar schedule_by_do_w:
    """
    class Meta:
        name = "telecommunicationsType"

    telecommunication_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "telecommunicationIdentifier",
            "type": "Element",
            "namespace": "",
            "nillable": True,
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
    contact_instructions: Optional[str] = field(
        default=None,
        metadata={
            "name": "contactInstructions",
            "type": "Element",
            "namespace": "",
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
    category_of_comm_pref: Optional[CategoryOfCommPrefType] = field(
        default=None,
        metadata={
            "name": "categoryOfCommPref",
            "type": "Element",
            "namespace": "",
        }
    )
    schedule_by_do_w: Optional[ScheduleByDoWtype] = field(
        default=None,
        metadata={
            "name": "scheduleByDoW",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class Applicability(ApplicabilityType):
    class Meta:
        namespace = "http://www.iho.int/S123/gml/1.0"


@dataclass
class Authority(AuthorityType):
    class Meta:
        namespace = "http://www.iho.int/S123/gml/1.0"


@dataclass
class BuildingType(FeatureType):
    """A free-standing self-supporting construction that is roofed, usually
    walled, and is intended for human occupancy (for example: a place of work
    or recreation) and/or habitation.

    S-123 Note: Only features relevant to radio communications are
    encoded e.g., radio towers or radio masts. If the feature can be
    encoded as a radio station at the same location, a coincident
    Landmark must not be encoded.
    """
    function: List[FunctionType] = field(
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
    geometry: Optional[PointOrSurface] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class CoastguardStationType(FeatureType):
    """A station at which a visual/radio/radar marine watch is kept either
    continuously or at certain times only.

    S-123 Note: Only those instances concerned to radio communications
    are encoded in S-123 datasets.

    :ivar communication_channel:
    :ivar is_mrcc: In S-123 datasets, only MRCC or MRSC coastguard
        stations are encoded, so the value of this attribute should be
        TRUE for all instances in an S-123 dataset.
    :ivar status: 1: permanent;4: not in use;5:
        periodic/intermittent;16: watched;17: un-watched
    :ivar control_authority: The controlling organization or authority
        for a geographically located service
    :ivar the_contact_details:
    :ivar the_service_hours:
    :ivar geometry:
    """
    communication_channel: List[str] = field(
        default_factory=list,
        metadata={
            "name": "communicationChannel",
            "type": "Element",
            "namespace": "",
        }
    )
    is_mrcc: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isMRCC",
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
    control_authority: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthority",
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
    the_service_hours: Optional[ReferenceType] = field(
        default=None,
        metadata={
            "name": "theServiceHours",
            "type": "Element",
            "namespace": "",
        }
    )
    geometry: Optional[PointOrSurface] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class ContactDetailsType(InformationTypeType):
    """
    Information on how to reach a person or organisation by postal, internet,
    telephone, telex and radio systems.

    :ivar call_name: The designated call name of a station, e.g. radio
        station, radar station, pilot. This is the name used when
        calling a radio station by radio i.e. "Singapore Pilots".
    :ivar call_sign: The designated call-sign of a radio station.
    :ivar communication_channel:
    :ivar contact_address:
    :ivar frequency_pair:
    :ivar contact_instructions: supplemental instructions on how or when
        to contact the individual, organisation, or service
    :ivar information:
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
        categoryOfChannelOrFrequencyPreference - categoryOfRadioMethods
        - tmIntervalsByDoW
    :ivar the_authority: Implements reverse association from
        ContactDetails to Authority from the April 2017 model. To be
        added to feature catalogue.
    """
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
    frequency_pair: List[FrequencyPairType] = field(
        default_factory=list,
        metadata={
            "name": "frequencyPair",
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
    information: List[InformationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    m_msicode: Optional[int] = field(
        default=None,
        metadata={
            "name": "mMSICode",
            "type": "Element",
            "namespace": "",
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
class FuzzyAreaAggregateType(FeatureType):
    """
    Aggregation of a geographic feature describing a service or phenomenon with
    zones of different confidence about the availability of the service,
    occurrence of the phenomenon, or applicability of the information described
    by the geographic feature.

    :ivar consists_of: A pointer to the aggregate in a whole-part
        relationship. Used for both the IndeterminateZone and core
        feature associations (same role name used for both)
    """
    consists_of: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "consistsOf",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class GmdssareaType(FeatureType):
    """An area defined for a global communications service based upon automated
    systems, both satellite based and terrestrial, to provide distress alerting
    and promulgation of maritime safety information for mariners.

    (Adapted IHO Dictionary, S-32, 5th Edition, 2048)

    :ivar category_of_gmdssarea:
    :ivar control_authority: The controlling organization or authority
        for a geographically located service
    :ivar service_provider: TBD: Addition to April 2017 model
    :ivar geometry:
    """
    class Meta:
        name = "GMDSSAreaType"

    category_of_gmdssarea: Optional[CategoryOfGmdssareaType] = field(
        default=None,
        metadata={
            "name": "categoryOfGMDSSArea",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    control_authority: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthority",
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
            "min_occurs": 1,
        }
    )


@dataclass
class IndeterminateZoneType(FeatureType):
    """A region in which the perception of a phenomenon or the availability of
    a service is known only to a specified level of confidence.

    Remark: IndeterminateZone features associated to the same fuzzy area aggregate must not overlap.

    :ivar information_confidence:
    :ivar component_of:
    :ivar geometry: Fuzzy region spatial attribute
    """
    information_confidence: Optional[InformationConfidenceType] = field(
        default=None,
        metadata={
            "name": "informationConfidence",
            "type": "Element",
            "namespace": "",
            "required": True,
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
    geometry: Optional[GmSurface] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class InmarsatOceanRegionAreaType(FeatureType):
    """
    The ocean region of the earth’s surface, within which a station can obtain
    line-of-sight communication, with an Inmarsat satellite.

    :ivar control_authority: The controlling organization or authority
        for a geographically located service
    :ivar geometry:
    """
    control_authority: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthority",
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
class LandmarkType(FeatureType):
    """Any prominent object on land which can be used in determining a location
    or a direction.

    (IHO Dictionary – S-32). S-123 Note: Only features relevant to radio
    communications are encoded e.g., radio towers or radio masts. If the
    feature can be encoded as a radio station at the same location, a
    coincident Landmark must not be encoded.
    """
    category_of_landmark: List[CategoryOfLandmarkType] = field(
        default_factory=list,
        metadata={
            "name": "categoryOfLandmark",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "nillable": True,
        }
    )
    function: List[FunctionType] = field(
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
    geometry: Optional[PointOrSurface] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class NauticalInformationType(AbstractRxntype):
    """Nautical information about a related area or facility.

    Constraint: If Regulations.textContent is populated, there cannot be textualDescription or information attributes directly bound to the Regulations.. A similar constraint applies to the information types Recommendations, Restrictions, and NauticalInformation.

    :ivar information_provided_for: This tag is overloaded, but the
        relationship cannot be to a feature type because
        info-&gt;feature links are not allowed by the 3.0.0 feature
        catalogue
    """
    information_provided_for: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "informationProvidedFor",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class NavigationalMeteorologicalAreaType(FeatureType):
    """The geographic areas in which various governments are responsible for
    navigation and weather warnings.

    Remarks: The roman number of NAV/METAREA is to be coded by using the feature name attribute. NAVTEX transmitting station identification characters are allocated within the same areas.

    :ivar service_provider: The area served by a service provider.
    :ivar control_authority: The controlling organization or authority
        for a geographically located service
    :ivar geometry:
    """
    service_provider: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "serviceProvider",
            "type": "Element",
            "namespace": "",
        }
    )
    control_authority: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthority",
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
class NavtexStationAreaType(FeatureType):
    """
    The geographic areas in which radio stations are responsible for broadcast
    navigation and weather warnings.

    :ivar tx_ident_char: The NAVTEX transmitter identification character
        is a single unique letter, which is allocated to each
        transmitter. It is used to identify the broadcasts, which are to
        be accepted by the receiver, those which are to be rejected, and
        the time slot for the transmission. Remarks: The transmitter
        identification character should be indicated by a single
        character (A-Z)
    :ivar status:
    :ivar service_provider: TBD: Addition to April 2017 model
    :ivar control_authority: The controlling organization or authority
        for a geographically located service
    :ivar geometry:
    """
    tx_ident_char: Optional[str] = field(
        default=None,
        metadata={
            "name": "txIdentChar",
            "type": "Element",
            "namespace": "",
            "required": True,
            "pattern": r"[A-Z]",
        }
    )
    status: Optional[StatusType] = field(
        default=None,
        metadata={
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
    control_authority: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthority",
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
class NonStandardWorkingDay(NonStandardWorkingDayType):
    class Meta:
        namespace = "http://www.iho.int/S123/gml/1.0"


@dataclass
class QualityOfNonBathymetricDataType(QualityOfTemporalVariationType):
    """An area within which a uniform assessment of the quality of the non-
    bathymetric data exists.

    (Adapted from S-57 Edition 3.1, Appendix A – Chapter 1, Page 1.208,
    November 2000).

    :ivar horizontal_distance_uncertainty: The best estimate of the
        horizontal accuracy of horizontal clearances and distances.
    :ivar horizontal_positional_uncertainty: The best estimate of the
        accuracy of a position.
    :ivar direction_uncertainty: The best estimate of the accuracy of a
        bearing
    :ivar source_indication:
    :ivar survey_date_range:
    :ivar geometry:
    """
    horizontal_distance_uncertainty: List[str] = field(
        default_factory=list,
        metadata={
            "name": "horizontalDistanceUncertainty",
            "type": "Element",
            "namespace": "",
        }
    )
    horizontal_positional_uncertainty: Optional[HorizontalPositionalUncertainty] = field(
        default=None,
        metadata={
            "name": "horizontalPositionalUncertainty",
            "type": "Element",
            "namespace": "",
        }
    )
    direction_uncertainty: Optional[str] = field(
        default=None,
        metadata={
            "name": "directionUncertainty",
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
    survey_date_range: Optional[SurveyDateRangeType] = field(
        default=None,
        metadata={
            "name": "surveyDateRange",
            "type": "Element",
            "namespace": "",
        }
    )
    geometry: List[SurfacePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class RadioServiceAreaType(FeatureType):
    """The area where a radio service can be obtained and the characteristics
    of the radio transmission.

    Remarks: The objects RDOSTA; RADSTA are used to encode the point of transmission of the signal.

    :ivar call_sign:
    :ivar category_of_broadcast_communication:
    :ivar language_information: A description of the languages,
        alphabets and scripts in use.
    :ivar radiocommunications:
    :ivar status:
    :ivar time_reference:
    :ivar transmission_power: The maximum power the radio service uses
        (or is authorized to use) for radio transmission. Remark: The
        calculation of the power depends on the type of signal. The
        value encoded must be the actual transmission power, if this is
        known to be different from the authorized transmission power.
        Unit: watt; Resolution: 0.1; Reference: 47 CFR 80.215 (19 April
        2017), adapted.
    :ivar tx_ident_char: The NAVTEX transmitter identification character
        is a single unique letter, which is allocated to each
        transmitter. It is used to identify the broadcasts, which are to
        be accepted by the receiver, those which are to be rejected, and
        the time slot for the transmission. Remarks: The transmitter
        identification character should be indicated by a single
        character (A-Z)
    :ivar tx_traffic_list: Describes whether a station transmits traffic
        lists. Remarks: - True: The radio station transmits traffic
        lists. - False: The radio station does not transmit traffic
        lists.
    :ivar the_service_hours:
    :ivar service_provider:
    :ivar the_contact_details: A pointer to a Contact Details object
    :ivar control_authority: The controlling organization or authority
        for a geographically located service
    :ivar component_of:
    :ivar geometry: TBD. Point geometry is a divergence from the April
        2017 model but service areas are not provided for some services
        in the data sample (the station location is given) and point
        geometries are used in the NIPWG mapping for these services.
    """
    call_sign: Optional[str] = field(
        default=None,
        metadata={
            "name": "callSign",
            "type": "Element",
            "namespace": "",
        }
    )
    category_of_broadcast_communication: Optional[CategoryOfBroadcastCommunicationType] = field(
        default=None,
        metadata={
            "name": "categoryOfBroadcastCommunication",
            "type": "Element",
            "namespace": "",
            "nillable": True,
        }
    )
    language_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "languageInformation",
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
    status: Optional[StatusType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    time_reference: Optional[TimeReferenceType] = field(
        default=None,
        metadata={
            "name": "timeReference",
            "type": "Element",
            "namespace": "",
        }
    )
    transmission_power: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "transmissionPower",
            "type": "Element",
            "namespace": "",
            "min_inclusive": Decimal("0.0"),
            "fraction_digits": 1,
        }
    )
    tx_ident_char: Optional[str] = field(
        default=None,
        metadata={
            "name": "txIdentChar",
            "type": "Element",
            "namespace": "",
            "pattern": r"[A-Z]",
        }
    )
    tx_traffic_list: Optional[bool] = field(
        default=None,
        metadata={
            "name": "txTrafficList",
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
    service_provider: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "serviceProvider",
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
    control_authority: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthority",
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
    geometry: List[PointOrSurface] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class RadioStationType(FeatureType):
    """A place equipped to transmit radio waves.

    Remarks: Such a station may be either stationary or mobile, and may also be provided with a radio receiver. In British terminology, also called 'w/t station'. The transmission of a radio station may serve to provide mariners with a line of position (IHO Chart Specifications, M-4). The object 'radio station' is used to encode the point of transmission of the signal.
    S-123 remarks: (1) The area in which the radio service can be obtained is described by an RDOSVC object. (2) The S-123 definition differs from the 2016 S-101 definition by omitting the optional attribute communicationChannel (bound to the NPUBs domain complex attribute radioStationCommunicationDescription instead). The NPUBs domain feature also binds attribute orientation to RadioStation.

    :ivar call_sign:
    :ivar category_of_radio_station:
    :ivar estimated_range_of_transmission: The estimated range of a non-
        optical electromagnetic transmission.
    :ivar orientation:
    :ivar radiocommunications:
    :ivar status:
    :ivar the_service_hours:
    :ivar service_area: The area served by a service provider.
    :ivar the_contact_details: A pointer to a Contact Details object
    :ivar control_authority: The controlling organization or authority
        for a geographically located service
    :ivar geometry:
    """
    call_sign: Optional[str] = field(
        default=None,
        metadata={
            "name": "callSign",
            "type": "Element",
            "namespace": "",
        }
    )
    category_of_radio_station: Optional[CategoryOfRadioStationType] = field(
        default=None,
        metadata={
            "name": "categoryOfRadioStation",
            "type": "Element",
            "namespace": "",
        }
    )
    estimated_range_of_transmission: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "estimatedRangeOfTransmission",
            "type": "Element",
            "namespace": "",
            "min_inclusive": Decimal("0.0"),
        }
    )
    orientation: Optional[OrientationType] = field(
        default=None,
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
    status: Optional[StatusType] = field(
        default=None,
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
    service_area: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "serviceArea",
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
    control_authority: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthority",
            "type": "Element",
            "namespace": "",
        }
    )
    geometry: Optional[GmPoint] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class RecommendationsType(AbstractRxntype):
    """Recommendations for a related area or facility.

    Constraint: If Regulations.textContent is populated, there cannot be textualDescription or information attributes directly bound to the Regulations.. A similar constraint applies to the information types Recommendations, Restrictions, and NauticalInformation.
    """


@dataclass
class RegulationsType(AbstractRxntype):
    """Regulations for a related area or facility.

    Constraint: If Regulations.textContent is populated, there cannot be textualDescription or information attributes directly bound to the Regulations.. A similar constraint applies to the information types Recommendations, Restrictions, and NauticalInformation.
    """


@dataclass
class RestrictionsType(AbstractRxntype):
    """Restrictions for a related area or facility.

    Constraint: If Regulations.textContent is populated, there cannot be textualDescription or information attributes directly bound to the Regulations.. A similar constraint applies to the information types Recommendations, Restrictions, and NauticalInformation.
    """


@dataclass
class ServiceHours(ServiceHoursType):
    class Meta:
        namespace = "http://www.iho.int/S123/gml/1.0"


@dataclass
class SpatialQualityPoints(SpatialQuality):
    """
    Definition required.
    """
    class Meta:
        namespace = "http://www.iho.int/S123/gml/1.0"


@dataclass
class WeatherForecastWarningAreaType(FeatureType):
    """
    An area for which weather forecasts and warnings are provided for specified
    periods.

    :ivar category_of_frcst_and_warning_area:
    :ivar nationality:
    :ivar status:
    :ivar service_provider: TBD: Addition to April 2017 model
    :ivar control_authority: The controlling organization or authority
        for a geographically located service
    :ivar component_of:
    :ivar geometry:
    """
    category_of_frcst_and_warning_area: Optional[CategoryOfFrcstAndWarningAreaType] = field(
        default=None,
        metadata={
            "name": "categoryOfFrcstAndWarningArea",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    nationality: Optional[str] = field(
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
    service_provider: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "serviceProvider",
            "type": "Element",
            "namespace": "",
        }
    )
    control_authority: List[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "controlAuthority",
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
    geometry: List[GmSurface] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class Building(BuildingType):
    class Meta:
        namespace = "http://www.iho.int/S123/gml/1.0"


@dataclass
class CoastguardStation(CoastguardStationType):
    class Meta:
        namespace = "http://www.iho.int/S123/gml/1.0"


@dataclass
class ContactDetails(ContactDetailsType):
    class Meta:
        namespace = "http://www.iho.int/S123/gml/1.0"


@dataclass
class ForecastAreaAggregateType(FuzzyAreaAggregateType):
    """Aggregation of areas where forecasts and warnings broadcasted for a
    Weather forecast and warning area may be available with differing levels of
    reliability.

    consistsOf removed  from this type because duplicating the element
    of the same name in supertype FuzzyAreaAggregate violates XML schema
    rules
    """


@dataclass
class Gmdssarea(GmdssareaType):
    class Meta:
        name = "GMDSSArea"
        namespace = "http://www.iho.int/S123/gml/1.0"


@dataclass
class IndeterminateZone(IndeterminateZoneType):
    class Meta:
        namespace = "http://www.iho.int/S123/gml/1.0"


@dataclass
class InmarsatOceanRegionArea(InmarsatOceanRegionAreaType):
    class Meta:
        namespace = "http://www.iho.int/S123/gml/1.0"


@dataclass
class Landmark(LandmarkType):
    class Meta:
        namespace = "http://www.iho.int/S123/gml/1.0"


@dataclass
class NauticalInformation(NauticalInformationType):
    class Meta:
        namespace = "http://www.iho.int/S123/gml/1.0"


@dataclass
class NavigationalMeteorologicalArea(NavigationalMeteorologicalAreaType):
    class Meta:
        namespace = "http://www.iho.int/S123/gml/1.0"


@dataclass
class NavtexStationArea(NavtexStationAreaType):
    class Meta:
        namespace = "http://www.iho.int/S123/gml/1.0"


@dataclass
class QualityOfNonBathymetricData(QualityOfNonBathymetricDataType):
    class Meta:
        namespace = "http://www.iho.int/S123/gml/1.0"


@dataclass
class RadioServiceArea(RadioServiceAreaType):
    class Meta:
        namespace = "http://www.iho.int/S123/gml/1.0"


@dataclass
class RadioServiceAreaAggregateType(FuzzyAreaAggregateType):
    """
    Aggregation of areas where radio services from a single radio service are
    available to different levels of reliability consistsOf removed  from this
    type because duplicating the element of the same name in supertype
    FuzzyAreaAggregate violates XML schema rules.
    """


@dataclass
class RadioStation(RadioStationType):
    class Meta:
        namespace = "http://www.iho.int/S123/gml/1.0"


@dataclass
class Recommendations(RecommendationsType):
    class Meta:
        namespace = "http://www.iho.int/S123/gml/1.0"


@dataclass
class Regulations(RegulationsType):
    class Meta:
        namespace = "http://www.iho.int/S123/gml/1.0"


@dataclass
class Restrictions(RestrictionsType):
    class Meta:
        namespace = "http://www.iho.int/S123/gml/1.0"


@dataclass
class WeatherForecastWarningArea(WeatherForecastWarningAreaType):
    class Meta:
        namespace = "http://www.iho.int/S123/gml/1.0"


@dataclass
class ForecastAreaAggregate(ForecastAreaAggregateType):
    class Meta:
        namespace = "http://www.iho.int/S123/gml/1.0"


@dataclass
class ImemberType(AbstractFeatureMemberType):
    """
    dataset member S-100 infotmation types.
    """
    class Meta:
        name = "IMemberType"

    contact_details: Optional[ContactDetails] = field(
        default=None,
        metadata={
            "name": "ContactDetails",
            "type": "Element",
            "namespace": "http://www.iho.int/S123/gml/1.0",
        }
    )
    service_hours: Optional[ServiceHours] = field(
        default=None,
        metadata={
            "name": "ServiceHours",
            "type": "Element",
            "namespace": "http://www.iho.int/S123/gml/1.0",
        }
    )
    restrictions: Optional[Restrictions] = field(
        default=None,
        metadata={
            "name": "Restrictions",
            "type": "Element",
            "namespace": "http://www.iho.int/S123/gml/1.0",
        }
    )
    regulations: Optional[Regulations] = field(
        default=None,
        metadata={
            "name": "Regulations",
            "type": "Element",
            "namespace": "http://www.iho.int/S123/gml/1.0",
        }
    )
    recommendations: Optional[Recommendations] = field(
        default=None,
        metadata={
            "name": "Recommendations",
            "type": "Element",
            "namespace": "http://www.iho.int/S123/gml/1.0",
        }
    )
    non_standard_working_day: Optional[NonStandardWorkingDay] = field(
        default=None,
        metadata={
            "name": "NonStandardWorkingDay",
            "type": "Element",
            "namespace": "http://www.iho.int/S123/gml/1.0",
        }
    )
    nautical_information: Optional[NauticalInformation] = field(
        default=None,
        metadata={
            "name": "NauticalInformation",
            "type": "Element",
            "namespace": "http://www.iho.int/S123/gml/1.0",
        }
    )
    authority: Optional[Authority] = field(
        default=None,
        metadata={
            "name": "Authority",
            "type": "Element",
            "namespace": "http://www.iho.int/S123/gml/1.0",
        }
    )
    applicability: Optional[Applicability] = field(
        default=None,
        metadata={
            "name": "Applicability",
            "type": "Element",
            "namespace": "http://www.iho.int/S123/gml/1.0",
        }
    )
    inclusion_type: Optional[InclusionType] = field(
        default=None,
        metadata={
            "name": "InclusionType",
            "type": "Element",
            "namespace": "http://www.iho.int/S123/gml/1.0",
        }
    )
    permission_type: Optional[PermissionType] = field(
        default=None,
        metadata={
            "name": "PermissionType",
            "type": "Element",
            "namespace": "http://www.iho.int/S123/gml/1.0",
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
class RadioServiceAreaAggregate(RadioServiceAreaAggregateType):
    class Meta:
        namespace = "http://www.iho.int/S123/gml/1.0"


@dataclass
class MemberType(AbstractFeatureMemberType):
    """
    dataset member.
    """
    quality_of_non_bathymetric_data: Optional[QualityOfNonBathymetricData] = field(
        default=None,
        metadata={
            "name": "QualityOfNonBathymetricData",
            "type": "Element",
            "namespace": "http://www.iho.int/S123/gml/1.0",
        }
    )
    data_coverage: Optional[DataCoverage] = field(
        default=None,
        metadata={
            "name": "DataCoverage",
            "type": "Element",
            "namespace": "http://www.iho.int/S123/gml/1.0",
        }
    )
    quality_of_temporal_variation_type: Optional[QualityOfTemporalVariationType] = field(
        default=None,
        metadata={
            "name": "QualityOfTemporalVariationType",
            "type": "Element",
            "namespace": "http://www.iho.int/S123/gml/1.0",
        }
    )
    meta_feature_type: Optional[MetaFeatureType] = field(
        default=None,
        metadata={
            "name": "MetaFeatureType",
            "type": "Element",
            "namespace": "http://www.iho.int/S123/gml/1.0",
        }
    )
    radio_service_area_aggregate: Optional[RadioServiceAreaAggregate] = field(
        default=None,
        metadata={
            "name": "RadioServiceAreaAggregate",
            "type": "Element",
            "namespace": "http://www.iho.int/S123/gml/1.0",
        }
    )
    indeterminate_zone: Optional[IndeterminateZone] = field(
        default=None,
        metadata={
            "name": "IndeterminateZone",
            "type": "Element",
            "namespace": "http://www.iho.int/S123/gml/1.0",
        }
    )
    forecast_area_aggregate: Optional[ForecastAreaAggregate] = field(
        default=None,
        metadata={
            "name": "ForecastAreaAggregate",
            "type": "Element",
            "namespace": "http://www.iho.int/S123/gml/1.0",
        }
    )
    weather_forecast_warning_area: Optional[WeatherForecastWarningArea] = field(
        default=None,
        metadata={
            "name": "WeatherForecastWarningArea",
            "type": "Element",
            "namespace": "http://www.iho.int/S123/gml/1.0",
        }
    )
    radio_station: Optional[RadioStation] = field(
        default=None,
        metadata={
            "name": "RadioStation",
            "type": "Element",
            "namespace": "http://www.iho.int/S123/gml/1.0",
        }
    )
    radio_service_area: Optional[RadioServiceArea] = field(
        default=None,
        metadata={
            "name": "RadioServiceArea",
            "type": "Element",
            "namespace": "http://www.iho.int/S123/gml/1.0",
        }
    )
    navtex_station_area: Optional[NavtexStationArea] = field(
        default=None,
        metadata={
            "name": "NavtexStationArea",
            "type": "Element",
            "namespace": "http://www.iho.int/S123/gml/1.0",
        }
    )
    navigational_meteorological_area: Optional[NavigationalMeteorologicalArea] = field(
        default=None,
        metadata={
            "name": "NavigationalMeteorologicalArea",
            "type": "Element",
            "namespace": "http://www.iho.int/S123/gml/1.0",
        }
    )
    landmark: Optional[Landmark] = field(
        default=None,
        metadata={
            "name": "Landmark",
            "type": "Element",
            "namespace": "http://www.iho.int/S123/gml/1.0",
        }
    )
    inmarsat_ocean_region_area: Optional[InmarsatOceanRegionArea] = field(
        default=None,
        metadata={
            "name": "InmarsatOceanRegionArea",
            "type": "Element",
            "namespace": "http://www.iho.int/S123/gml/1.0",
        }
    )
    gmdssarea: Optional[Gmdssarea] = field(
        default=None,
        metadata={
            "name": "GMDSSArea",
            "type": "Element",
            "namespace": "http://www.iho.int/S123/gml/1.0",
        }
    )
    coastguard_station: Optional[CoastguardStation] = field(
        default=None,
        metadata={
            "name": "CoastguardStation",
            "type": "Element",
            "namespace": "http://www.iho.int/S123/gml/1.0",
        }
    )
    building: Optional[Building] = field(
        default=None,
        metadata={
            "name": "Building",
            "type": "Element",
            "namespace": "http://www.iho.int/S123/gml/1.0",
        }
    )
    feature_type: Optional[FeatureType] = field(
        default=None,
        metadata={
            "name": "FeatureType",
            "type": "Element",
            "namespace": "http://www.iho.int/S123/gml/1.0",
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
class DatasetType(ProfileAbstractFeatureType):
    """
    Dataset element for MPA dataset as "GML document".

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
    point: List[Point] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    multi_point: List[MultiPoint] = field(
        default_factory=list,
        metadata={
            "name": "MultiPoint",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    curve: List[Curve] = field(
        default_factory=list,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    composite_curve: List[CompositeCurve] = field(
        default_factory=list,
        metadata={
            "name": "CompositeCurve",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    orientable_curve: List[OrientableCurve] = field(
        default_factory=list,
        metadata={
            "name": "OrientableCurve",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    surface: List[Surface] = field(
        default_factory=list,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    polygon: List[Polygon] = field(
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
        namespace = "http://www.iho.int/S123/gml/1.0"
