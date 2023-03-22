from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union
from s123.models.s100_3_0_0.s100_gml.pkg_20170505.s100gmlbase import (
    Curve as S100GmlbaseCurve,
    OrientableCurve as S100GmlbaseOrientableCurve,
    Point as S100GmlbasePoint,
    Polygon as S100GmlbasePolygon,
    S100ArcByCenterPoint,
    S100CircleByCenterPoint,
    Surface as S100GmlbaseSurface,
)
from s123.models.s100_3_0_0.w3c.xml.pkg_2008.pkg_06.xlink import (
    ActuateType,
    ShowType,
    TypeType,
)
from s123.models.s123.pkg_1.pkg_0.pkg_20170831.s123 import (
    Building,
    CoastguardStation,
    DataCoverage,
    FeatureType,
    ForecastAreaAggregate,
    Gmdssarea,
    IndeterminateZone,
    InmarsatOceanRegionArea,
    Landmark,
    MetaFeatureType,
    NavigationalMeteorologicalArea,
    NavtexStationArea,
    QualityOfNonBathymetricData,
    QualityOfTemporalVariationType,
    RadioServiceArea,
    RadioServiceAreaAggregate,
    RadioStation,
    WeatherForecastWarningArea,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractCurveSegmentType:
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
    num_derivative_interior: int = field(
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
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class AbstractRingType:
    pass


@dataclass
class AbstractSurfacePatchType:
    pass


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
    """
    gml:CurveInterpolationType is a list of codes that may be used to identify
    the interpolation mechanisms specified by an application schema.
    """
    LINEAR = "linear"
    GEODESIC = "geodesic"
    CIRCULAR_ARC3_POINTS = "circularArc3Points"
    CIRCULAR_ARC_CENTER_POINT_WITH_RADIUS = "circularArcCenterPointWithRadius"
    CIRCULAR_ARC2_POINT_WITH_BULGE = "circularArc2PointWithBulge"
    ELLIPTICAL = "elliptical"
    CLOTHOID = "clothoid"
    CONIC = "conic"
    POLYNOMIAL_SPLINE = "polynomialSpline"
    CUBIC_SPLINE = "cubicSpline"
    RATIONAL_SPLINE = "rationalSpline"


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
class GmlProfileSchema:
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
    pass


@dataclass
class AssociationRoleType:
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


@dataclass
class EnvelopeType:
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
class FeaturePropertyType:
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
class LengthType(MeasureType):
    """This is a prototypical definition for a specific measure type defined as
    a vacuous extension (i.e. aliases) of gml:MeasureType.

    In this case, the content model supports the description of a length
    (or distance) quantity, with its units. The unit of measure
    referenced by uom shall be suitable for a length, such as metres or
    feet.
    """


@dataclass
class ReferenceType:
    """
    gml:ReferenceType is intended to be used in application schemas directly,
    if a property element shall use a "by-reference only" encoding.
    """
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
    pass


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
class AbstractGeometricAggregateType(AbstractGeometryType):
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
class AbstractCurveType(AbstractGeometricPrimitiveType):
    """gml:AbstractCurveType is an abstraction of a curve to support the
    different levels of complexity.

    The curve may always be viewed as a geometric primitive, i.e. is
    continuous.
    """


@dataclass
class AbstractSurfaceType(AbstractGeometricPrimitiveType):
    """gml:AbstractSurfaceType is an abstraction of a surface to support the
    different levels of complexity.

    A surface is always a continuous region of a plane.
    """


@dataclass
class BoundingShapeType:
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
class PointType(AbstractGeometricPrimitiveType):
    """S-100 XML supports two different ways to specify the direct positon of a
    point.

    1. The "pos" element is of type DirectPositionType.
    """
    pos: Optional[Pos] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )


@dataclass
class CompositeCurveType(AbstractCurveType):
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
class Point(PointType):
    """A Point is defined by a single coordinate tuple.

    The direct position of a point is specified by the pos element which
    is of type DirectPositionType.
    """
    class Meta:
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
class AbstractFeatureType(AbstractGmltype):
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
class CompositeCurve(CompositeCurveType):
    """A gml:CompositeCurve is represented by a sequence of (orientable) curves
    such that each curve in the sequence terminates at the start point of the
    subsequent curve in the list.

    curveMember references or contains inline one curve in the composite
    curve. The curves are contiguous, the collection of curves is
    ordered. Therefore, if provided, the aggregationType attribute shall
    have the value "sequence".
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class OrientableCurve(OrientableCurveType):
    """OrientableCurve consists of a curve and an orientation.

    If the orientation is "+", then the OrientableCurve is identical to
    the baseCurve. If the orientation is "-", then the OrientableCurve
    is related to another AbstractCurve with a parameterization that
    reverses the sense of the curve traversal.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class PointPropertyType:
    """A property that has a point as its value domain may either be an
    appropriate geometry element encapsulated in an element of this type or an
    XLink reference to a remote geometry element (where remote includes
    geometry elements located elsewhere in the same document).

    Either the reference or the contained element shall be given, but
    neither both nor none.
    """
    point: Optional[Point] = field(
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
class PointMember(PointPropertyType):
    """
    This property element either references a Point via the XLink-attributes or
    contains the Point element.
    """
    class Meta:
        name = "pointMember"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class PointProperty(PointPropertyType):
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
class GeodesicStringType(AbstractCurveSegmentType):
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
    point_property: List[PointProperty] = field(
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
    pos: List[Pos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 2,
            "sequential": True,
        }
    )
    point_property: List[PointProperty] = field(
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
    pos: List[Pos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 2,
            "sequential": True,
        }
    )
    point_property: List[PointProperty] = field(
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
    pos: List[Pos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 4,
            "sequential": True,
        }
    )
    point_property: List[PointProperty] = field(
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
class MultiPointType(AbstractGeometricAggregateType):
    point_member: List[PointMember] = field(
        default_factory=list,
        metadata={
            "name": "pointMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )


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
    pass


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
class MultiPoint(MultiPointType):
    """A gml:MultiPoint consists of one or more gml:Points.

    The members of the geometric aggregate may be specified either using
    the "standard" property (gml:pointMember) or the array property
    (gml:pointMembers). It is also valid to use both the "standard" and
    the array properties in the same collection.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


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
class CurveSegmentArrayPropertyType:
    """
    gml:CurveSegmentArrayPropertyType is a container for an array of curve
    segments.
    """
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
class Segments(CurveSegmentArrayPropertyType):
    """This property element contains a list of curve segments.

    The order of the elements is significant and shall be preserved when
    processing the array.
    """
    class Meta:
        name = "segments"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class CurveType(AbstractCurveType):
    segments: Optional[Segments] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )


@dataclass
class Curve(CurveType):
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
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class CurvePropertyType:
    """A property that has a curve as its value domain may either be an
    appropriate geometry element encapsulated in an element of this type or an
    XLink reference to a remote geometry element (where remote includes
    geometry elements located elsewhere in the same document).

    Either the reference or the contained element shall be given, but
    neither both nor none.
    """
    orientable_curve: Optional[S100GmlbaseOrientableCurve] = field(
        default=None,
        metadata={
            "name": "OrientableCurve",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    composite_curve: Optional[CompositeCurve] = field(
        default=None,
        metadata={
            "name": "CompositeCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    opengis_net_gml_3_2_orientable_curve: Optional[OrientableCurve] = field(
        default=None,
        metadata={
            "name": "OrientableCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    curve: Optional[S100GmlbaseCurve] = field(
        default=None,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    opengis_net_gml_3_2_curve: Optional[Curve] = field(
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
class BaseCurve(CurvePropertyType):
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
class CurveMember(CurvePropertyType):
    class Meta:
        name = "curveMember"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class RingType(AbstractRingType):
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
class AbstractRingPropertyType:
    """
    A property with the content model of gml:AbstractRingPropertyType
    encapsulates a ring to represent the surface boundary property of a
    surface.
    """
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
class PolygonType(AbstractSurfaceType):
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
class Polygon(PolygonType):
    """A Polygon is a special surface that is defined by a single surface patch
    (see D.3.6).

    The boundary of this patch is coplanar and the polygon uses planar
    interpolation in its interior. The elements exterior and interior
    describe the surface boundary of the polygon.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


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
class SurfacePatchArrayPropertyType:
    """
    gml:SurfacePatchArrayPropertyType is a container for a sequence of surface
    patches.
    """
    polygon_patch: List[PolygonPatch] = field(
        default_factory=list,
        metadata={
            "name": "PolygonPatch",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
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
class SurfaceType(AbstractSurfaceType):
    patches: Optional[Patches] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        }
    )


@dataclass
class Surface(SurfaceType):
    """A Surface is a 2-dimensional primitive and is composed of one or more
    surface patches as specified in ISO 19107:2003, 6.3.17.1.

    The surface patches are connected to one another. patches
    encapsulates the patches of the surface.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class GeometricPrimitivePropertyType:
    """A property that has a geometric primitive as its value domain may either
    be an appropriate geometry element encapsulated in an element of this type
    or an XLink reference to a remote geometry element (where remote includes
    geometry elements located elsewhere in the same document).

    Either the reference or the contained element shall be given, but
    neither both nor none.
    """
    point: Optional[S100GmlbasePoint] = field(
        default=None,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    surface: Optional[S100GmlbaseSurface] = field(
        default=None,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    opengis_net_gml_3_2_surface: Optional[Surface] = field(
        default=None,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    polygon: Optional[S100GmlbasePolygon] = field(
        default=None,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    opengis_net_gml_3_2_polygon: Optional[Polygon] = field(
        default=None,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    orientable_curve: Optional[S100GmlbaseOrientableCurve] = field(
        default=None,
        metadata={
            "name": "OrientableCurve",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    composite_curve: Optional[CompositeCurve] = field(
        default=None,
        metadata={
            "name": "CompositeCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    opengis_net_gml_3_2_orientable_curve: Optional[OrientableCurve] = field(
        default=None,
        metadata={
            "name": "OrientableCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    curve: Optional[S100GmlbaseCurve] = field(
        default=None,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    opengis_net_gml_3_2_curve: Optional[Curve] = field(
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
    opengis_net_gml_3_2_point: Optional[Point] = field(
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
class SurfacePropertyType:
    """A property that has a surface as its value domain may either be an
    appropriate geometry element encapsulated in an element of this type or an
    XLink reference to a remote geometry element (where remote includes
    geometry elements located elsewhere in the same document).

    Either the reference or the contained element shall be given, but
    neither both nor none.
    """
    surface: Optional[S100GmlbaseSurface] = field(
        default=None,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    opengis_net_gml_3_2_surface: Optional[Surface] = field(
        default=None,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    polygon: Optional[S100GmlbasePolygon] = field(
        default=None,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    opengis_net_gml_3_2_polygon: Optional[Polygon] = field(
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
