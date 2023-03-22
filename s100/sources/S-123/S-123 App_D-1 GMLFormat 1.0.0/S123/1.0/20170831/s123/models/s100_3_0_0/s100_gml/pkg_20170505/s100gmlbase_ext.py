from dataclasses import dataclass, field
from typing import Optional
from s123.models.s100_3_0_0.s100_gml.pkg_20170505.s100gmlbase import (
    CompositeCurveProperty,
    CurveProperty as S100GmlbaseCurveProperty,
    OrientableCurveProperty,
    PointProperty as S100GmlbasePointProperty,
    SurfaceProperty as S100GmlbaseSurfaceProperty,
)

__NAMESPACE__ = "http://www.iho.int/s100gml/1.0+EXT"


@dataclass
class CurveOrSurfacePropertyType:
    curve_property: Optional[S100GmlbaseCurveProperty] = field(
        default=None,
        metadata={
            "name": "curveProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    surface_property: Optional[S100GmlbaseSurfaceProperty] = field(
        default=None,
        metadata={
            "name": "surfaceProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )


@dataclass
class CurvePropertyType:
    """WIP update to spatial property types in profile.

    Spatial quality for an individual should be indicated by either the
    generic information association or the SpatialQuality role-element.
    """
    curve_property: Optional[S100GmlbaseCurveProperty] = field(
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
class PointCurveSurfacePropertyType:
    point_property: Optional[S100GmlbasePointProperty] = field(
        default=None,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    curve_property: Optional[S100GmlbaseCurveProperty] = field(
        default=None,
        metadata={
            "name": "curveProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    surface_property: Optional[S100GmlbaseSurfaceProperty] = field(
        default=None,
        metadata={
            "name": "surfaceProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )


@dataclass
class PointOrSurfacePropertyType:
    point_property: Optional[S100GmlbasePointProperty] = field(
        default=None,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )
    surface_property: Optional[S100GmlbaseSurfaceProperty] = field(
        default=None,
        metadata={
            "name": "surfaceProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )


@dataclass
class PointPropertyType:
    """WIP update to spatial property types in profile.

    Spatial quality for an individual should be indicated by either the
    generic information association or the SpatialQuality role-element.
    """
    point_property: Optional[S100GmlbasePointProperty] = field(
        default=None,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
            "required": True,
        }
    )


@dataclass
class SurfacePropertyType:
    """WIP update to spatial property types in profile.

    Spatial quality for an individual should be indicated by either the
    generic information association or the SpatialQuality role-element.
    """
    surface_property: Optional[S100GmlbaseSurfaceProperty] = field(
        default=None,
        metadata={
            "name": "surfaceProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0",
        }
    )


@dataclass
class CurveOrSurfaceProperty(CurveOrSurfacePropertyType):
    class Meta:
        namespace = "http://www.iho.int/s100gml/1.0+EXT"


@dataclass
class CurveProperty(CurvePropertyType):
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
class PointProperty(PointPropertyType):
    class Meta:
        namespace = "http://www.iho.int/s100gml/1.0+EXT"


@dataclass
class SurfaceProperty(SurfacePropertyType):
    class Meta:
        namespace = "http://www.iho.int/s100gml/1.0+EXT"


@dataclass
class PointOrCurvePropertyType:
    curve_property: Optional[CurveProperty] = field(
        default=None,
        metadata={
            "name": "CurveProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0+EXT",
        }
    )
    surface_property: Optional[SurfaceProperty] = field(
        default=None,
        metadata={
            "name": "SurfaceProperty",
            "type": "Element",
            "namespace": "http://www.iho.int/s100gml/1.0+EXT",
        }
    )


@dataclass
class PointOrCurveProperty(PointOrCurvePropertyType):
    class Meta:
        namespace = "http://www.iho.int/s100gml/1.0+EXT"
