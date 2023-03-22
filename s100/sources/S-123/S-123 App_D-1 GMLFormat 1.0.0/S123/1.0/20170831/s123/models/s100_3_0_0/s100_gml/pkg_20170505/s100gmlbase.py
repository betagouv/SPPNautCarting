from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Union
from xsdata.models.datatype import XmlDate
from s123.models.s100_3_0_0.s100_gml.pkg_20170505.s100_gml_profile import (
    AbstractCurveSegmentType,
    AbstractFeatureType as S100GmlProfileAbstractFeatureType,
    AbstractGmltype,
    CompositeCurveType as S100GmlProfileCompositeCurveType,
    CurveInterpolationType,
    CurveType as S100GmlProfileCurveType,
    LengthType,
    MultiPointType as S100GmlProfileMultiPointType,
    NilReasonEnumerationValue,
    OrientableCurveType,
    PointType as S100GmlProfilePointType,
    Polygon as S100GmlProfilePolygon,
    PolygonType as S100GmlProfilePolygonType,
    Surface as S100GmlProfileSurface,
    SurfaceType as S100GmlProfileSurfaceType,
    PointProperty as S100GmlProfilePointProperty,
    Pos,
)
from s123.models.s100_3_0_0.w3c.xml.pkg_2008.pkg_06.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)

__NAMESPACE__ = "http://www.iho.int/s100gml/1.0"


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
class AbstractAttributeType(AbstractGmltype):
    """
    Abstract type for attributes.
    """


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
class OrientableCurve(OrientableCurveType):
    """S-100 orientable curve is the same as GML orientable curve.

    Added for consistency.
    """
    class Meta:
        namespace = "http://www.iho.int/s100gml/1.0"


@dataclass
class S100ArcByCenterPointType(AbstractCurveSegmentType):
    """
    Type for S-100 arc by center point geometry.
    """
    class Meta:
        name = "S100_ArcByCenterPointType"

    pos: Optional[Pos] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    point_property: Optional[S100GmlProfilePointProperty] = field(
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
class FeaturePropertyType(AbstractAttributeType):
    """
    Abstract type for an S-100 feature association.
    """
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
class OrientableCurvePropertyType:
    """
    Orientable Curve property using the S-100 orientable curve element.
    """
    orientable_curve: Optional[OrientableCurve] = field(
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
class FeatureAssociation(FeaturePropertyType):
    class Meta:
        name = "featureAssociation"
        namespace = "http://www.iho.int/s100gml/1.0"


@dataclass
class InformationAssociation(InformationPropertyType):
    class Meta:
        name = "informationAssociation"
        namespace = "http://www.iho.int/s100gml/1.0"


@dataclass
class InvFeatureAssociation(FeaturePropertyType):
    class Meta:
        name = "invFeatureAssociation"
        namespace = "http://www.iho.int/s100gml/1.0"


@dataclass
class InvInformationAssociation(InverseInformationAssociationType):
    class Meta:
        name = "invInformationAssociation"
        namespace = "http://www.iho.int/s100gml/1.0"


@dataclass
class OrientableCurveProperty(OrientableCurvePropertyType):
    class Meta:
        name = "orientableCurveProperty"
        namespace = "http://www.iho.int/s100gml/1.0"


@dataclass
class AbstractFeatureType(S100GmlProfileAbstractFeatureType):
    """Abstract type for an S-100 feature.

    This is the base type from which domain application schemas derive
    definitions for their individual features. It derives from GML
    AbstractFeatureType. It provides for all information types in the
    data product's GML application schema to have feature identifiers
    and properties for feature associations, information associations
    and inverse information associations.
    """
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
class AbstractInformationType(AbstractGmltype):
    """Abstract type for an S-100 information type.

    This is the base type from which domain application schemas derive
    definitions for their individual information types. It provides for
    all information types in the data product's GML application schema
    to have properties for information associations and inverse
    information associations.
    """
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
class CompositeCurveType(S100GmlProfileCompositeCurveType):
    """
    S-100 composite curve type adds an information association to the GML
    spatial type CompositeCurve.
    """
    information_association: List[InformationAssociation] = field(
        default_factory=list,
        metadata={
            "name": "informationAssociation",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )


@dataclass
class CurveType(S100GmlProfileCurveType):
    """
    S-100 curve type adds an information association to the GML spatial type
    Curve.
    """
    information_association: List[InformationAssociation] = field(
        default_factory=list,
        metadata={
            "name": "informationAssociation",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )


@dataclass
class MultiPointType(S100GmlProfileMultiPointType):
    """
    S-100 multipoint type adds an information association to the GML spatial
    type MultiPoint.
    """
    information_association: List[InformationAssociation] = field(
        default_factory=list,
        metadata={
            "name": "informationAssociation",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )


@dataclass
class PointType(S100GmlProfilePointType):
    """
    S-100 point type adds an information association to the GML spatial type
    Point.
    """
    information_association: List[InformationAssociation] = field(
        default_factory=list,
        metadata={
            "name": "informationAssociation",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )


@dataclass
class PolygonType(S100GmlProfilePolygonType):
    """
    S-100 polygon type adds an information association to the GML spatial type
    Polygon.
    """
    information_association: List[InformationAssociation] = field(
        default_factory=list,
        metadata={
            "name": "informationAssociation",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )


@dataclass
class SurfaceType(S100GmlProfileSurfaceType):
    """
    S-100 surface type adds an information association to the GML spatial type
    Surface.
    """
    information_association: List[InformationAssociation] = field(
        default_factory=list,
        metadata={
            "name": "informationAssociation",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )


@dataclass
class CompositeCurve(CompositeCurveType):
    class Meta:
        namespace = "http://www.iho.int/s100gml/1.0"


@dataclass
class Curve(CurveType):
    class Meta:
        namespace = "http://www.iho.int/s100gml/1.0"


@dataclass
class MultiPoint(MultiPointType):
    class Meta:
        namespace = "http://www.iho.int/s100gml/1.0"


@dataclass
class Point(PointType):
    class Meta:
        namespace = "http://www.iho.int/s100gml/1.0"


@dataclass
class Polygon(PolygonType):
    """
    S100 version of polygon type.
    """
    class Meta:
        namespace = "http://www.iho.int/s100gml/1.0"


@dataclass
class Surface(SurfaceType):
    class Meta:
        namespace = "http://www.iho.int/s100gml/1.0"


@dataclass
class CompositeCurvePropertyType:
    """
    Composite Curve property using the S-100 composite curve type.
    """
    composite_curve: Optional[CompositeCurve] = field(
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
class CurvePropertyType:
    """
    Curve property using the S-100 curve type.
    """
    curve: Optional[Curve] = field(
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
class MultiPointPropertyType:
    """
    MultiPoint property using the S-100 multipoint type.
    """
    multi_point: Optional[MultiPoint] = field(
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
class PointPropertyType:
    """
    Point property using the S-100 point type.
    """
    point: Optional[Point] = field(
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
class PolygonPropertyType:
    """
    Polygon property using the S-100 polygon type.
    """
    polygon: Optional[Polygon] = field(
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
class SurfacePropertyType:
    """
    Surface property using the S-100 surface type.
    """
    surface: Optional[Surface] = field(
        default=None,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    opengis_net_gml_3_2_surface: Optional[S100GmlProfileSurface] = field(
        default=None,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    polygon: Optional[Polygon] = field(
        default=None,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    opengis_net_gml_3_2_polygon: Optional[S100GmlProfilePolygon] = field(
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
class CompositeCurveProperty(CompositeCurvePropertyType):
    class Meta:
        name = "compositeCurveProperty"
        namespace = "http://www.iho.int/s100gml/1.0"


@dataclass
class CurveProperty(CurvePropertyType):
    class Meta:
        name = "curveProperty"
        namespace = "http://www.iho.int/s100gml/1.0"


@dataclass
class MultiPointProperty(MultiPointPropertyType):
    class Meta:
        name = "multiPointProperty"
        namespace = "http://www.iho.int/s100gml/1.0"


@dataclass
class PointProperty(PointPropertyType):
    class Meta:
        name = "pointProperty"
        namespace = "http://www.iho.int/s100gml/1.0"


@dataclass
class PolygonProperty(PolygonPropertyType):
    class Meta:
        name = "polygonProperty"
        namespace = "http://www.iho.int/s100gml/1.0"


@dataclass
class SurfaceProperty(SurfacePropertyType):
    class Meta:
        name = "surfaceProperty"
        namespace = "http://www.iho.int/s100gml/1.0"
