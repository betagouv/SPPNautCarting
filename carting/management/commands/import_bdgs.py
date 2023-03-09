# from django.contrib.gis.gdal.envelope import OGREnvelope
from ctypes import c_void_p

from django.contrib.gis.gdal import DataSource
from django.contrib.gis.gdal.error import GDALException
from django.contrib.gis.gdal.geometries import GEO_CLASSES, OGRGeometry
from django.contrib.gis.gdal.geomtype import OGRGeomType
from django.contrib.gis.gdal.libgdal import lgdal
from django.contrib.gis.gdal.prototypes import ds as capi
from django.contrib.gis.gdal.prototypes import geom as geom_api
from django.contrib.gis.gdal.prototypes.generation import geom_output
from django.core.management.base import BaseCommand

from carting.models import BDGS

force_to_polygon = geom_output(lgdal.OGR_G_ForceToPolygon, [c_void_p])
force_to_multi_polygon = geom_output(lgdal.OGR_G_ForceToMultiPolygon, [c_void_p])
force_to_line = geom_output(lgdal.OGR_G_ForceToLineString, [c_void_p])
force_to_multi_line = geom_output(lgdal.OGR_G_ForceToMultiLineString, [c_void_p])

gdal_transform = {
    9: force_to_line,
    10: force_to_polygon,
    11: force_to_multi_line,
    12: force_to_multi_polygon,
}


class ExtendedOGRGeometry(OGRGeometry):
    def __init__(self, geom_input, srs=None):
        try:
            super().__init__(geom_input, srs)
        except KeyError:
            if (
                not isinstance(geom_input, self.ptr_type)
                and self.geom_type.num not in gdal_transform.keys()
            ):
                raise

            self.__class__ = EXTENDED_GEO_CLASSES[self.geom_type.num]

    @property
    def geom_type(self):
        "Return the Type for this Geometry."
        return ExtendedOGRGeomType(geom_api.get_geom_type(self.ptr))


class CurvePolygon(ExtendedOGRGeometry):
    pass


class CompoundCurve(ExtendedOGRGeometry):
    pass


class MultiSurface(ExtendedOGRGeometry):
    pass


class MultiCurve(ExtendedOGRGeometry):
    pass


EXTENDED_GEO_CLASSES = {
    **GEO_CLASSES,
    9: CompoundCurve,
    10: CurvePolygon,
    11: MultiCurve,
    12: MultiSurface,
}


class ExtendedOGRGeomType(OGRGeomType):
    # Copy paste of original types dictionnary from GeoDjango implementation
    # https://github.com/django/django/blob/main/django/contrib/gis/gdal/geomtype.py#L9
    # FIXME : remove when issue XYZ merged
    _types = {
        0: "Unknown",
        1: "Point",
        2: "LineString",
        3: "Polygon",
        4: "MultiPoint",
        5: "MultiLineString",
        6: "MultiPolygon",
        7: "GeometryCollection",
        100: "None",
        101: "LinearRing",
        102: "PointZ",
        1 + OGRGeomType.wkb25bit: "Point25D",
        2 + OGRGeomType.wkb25bit: "LineString25D",
        3 + OGRGeomType.wkb25bit: "Polygon25D",
        4 + OGRGeomType.wkb25bit: "MultiPoint25D",
        5 + OGRGeomType.wkb25bit: "MultiLineString25D",
        6 + OGRGeomType.wkb25bit: "MultiPolygon25D",
        7 + OGRGeomType.wkb25bit: "GeometryCollection25D",
        # Extended geometry types
        9: "CompoundCurve",
        10: "CurvePolygon",
        11: "MultiCurve",
        12: "MultiSurface",
    }


"""
GeometryType enum
https://gdal.org/doxygen/ogr__core_8h.html#a800236a0d460ef66e687b7b65610f12a
 {
  wkbUnknown = 0 , wkbPoint = 1 , wkbLineString = 2 , wkbPolygon = 3 ,
  wkbMultiPoint = 4 , wkbMultiLineString , wkbMultiPolygon = 6 , wkbGeometryCollection = 7 ,
  wkbCircularString = 8 , wkbCompoundCurve = 9 , wkbCurvePolygon = 10 , wkbMultiCurve = 11 ,
  wkbMultiSurface = 12 , wkbCurve , wkbSurface , wkbPolyhedralSurface ,
  wkbTIN = 16 , wkbTriangle = 17 , wkbNone = 100 , wkbLinearRing = 101 ,
  wkbCircularStringZ = 1008 , wkbCompoundCurveZ = 1009 , wkbCurvePolygonZ = 1010 , wkbMultiCurveZ = 1011 ,
  wkbMultiSurfaceZ = 1012 , wkbCurveZ = 1013 , wkbSurfaceZ = 1014 , wkbPolyhedralSurfaceZ = 1015 ,
  wkbTINZ = 1016 , wkbTriangleZ = 1017 , wkbPointM = 2001 , wkbLineStringM = 2002 ,
  wkbPolygonM = 2003 , wkbMultiPointM = 2004 , wkbMultiLineStringM = 2005 , wkbMultiPolygonM = 2006 ,
  wkbGeometryCollectionM = 2007 , wkbCircularStringM = 2008 , wkbCompoundCurveM = 2009 , wkbCurvePolygonM = 2010 ,
  wkbMultiCurveM = 2011 , wkbMultiSurfaceM = 2012 , wkbCurveM = 2013 , wkbSurfaceM = 2014 ,
  wkbPolyhedralSurfaceM = 2015 , wkbTINM = 2016 , wkbTriangleM = 2017 , wkbPointZM = 3001 ,
  wkbLineStringZM = 3002 , wkbPolygonZM = 3003 , wkbMultiPointZM = 3004 , wkbMultiLineStringZM = 3005 ,
  wkbMultiPolygonZM = 3006 , wkbGeometryCollectionZM = 3007 , wkbCircularStringZM = 3008 , wkbCompoundCurveZM = 3009 ,
  wkbCurvePolygonZM = 3010 , wkbMultiCurveZM = 3011 , wkbMultiSurfaceZM = 3012 , wkbCurveZM = 3013 ,
  wkbSurfaceZM = 3014 , wkbPolyhedralSurfaceZM = 3015 , wkbTINZM = 3016 , wkbTriangleZM = 3017 ,
  wkbPoint25D = -2147483647 , wkbLineString25D = -2147483646 , wkbPolygon25D = -2147483645 , wkbMultiPoint25D = -2147483644 ,
  wkbMultiLineString25D = -2147483643 , wkbMultiPolygon25D = -2147483642 , wkbGeometryCollection25D = -2147483641
}

Layers qui posent problème :
    - encodage différent d'un layer à l'autre
    - inspireid avec des espaces -> DST_BDD_WFS:dwrtpt
    - inspireid sous forme d'url -> ESPACES_MARITIMES_BDD_WFS:au_contiguous_zone

Layers avec géométries non supportées par geodjango:
    - Contient des multicurve -> LIMITES_PECHE_BDD_WFS:limite_100milles_peche_outre_mer_wgs84_epsg4326
    - Contient des CompoundCurve -> "DST_BDD_WFS:rdocal_lne",
"""


class Command(BaseCommand):
    def handle(self, *args, **options):
        BDGS.objects.all().delete()

        flux = DataSource(
            "WFS:https://services.data.shom.fr/INSPIRE/wfs?version=2.0.0",
        )

        ignored_layers = []
        errored_layers = []
        print("Start importing WFS layers \n")
        for layer in flux:
            new_objects = []
            if "inspireid" not in layer.fields:
                ignored_layers.append(layer)
                continue
            try:
                for feature in layer:
                    raw = {
                        field: fix_encoding(feature.get(field))
                        for field in feature.fields
                        if field not in ("inspireid")
                    }

                    geom_ptr = capi.get_feat_geom_ref(feature.ptr)
                    geom = ExtendedOGRGeometry(geom_api.clone_geom(geom_ptr))
                    if geom.geom_type.num in gdal_transform.keys():
                        foo = gdal_transform[geom.geom_type.num]
                        geom = ExtendedOGRGeometry(foo(geom_api.clone_geom(geom_ptr)))

                        # FIXME : comprendre pourquoi on a besoin de faire ca
                        geom.srid = 3857
                        geom.transform(4326)

                    # FIXME : ajouter un validateur sur le champ django
                    inspire_id = feature.get("inspireid")
                    if " " in inspire_id:
                        inspire_id = inspire_id.replace(" ", "")
                        raise Exception("Un inspire id contient des espaces")
                    if "http" in inspire_id:
                        inspire_id = inspire_id.split("/")[-1]
                        raise Exception("Un inspire id est sous forme d'url")

                    new_objects.append(
                        BDGS(
                            inspire_id=inspire_id,
                            category=layer.name,
                            raw=raw,
                            geometry=geom.json,
                        )
                    )
                created = BDGS.objects.bulk_create(new_objects)
                print(f"{len(created)} BDGS objects imported from layer {layer.name}.")
            except Exception as e:
                errored_layers.append((layer, e))

        self.stdout.write(
            self.style.SUCCESS(
                f"✨ {len(flux) - len(ignored_layers) - len(errored_layers)} layers were successfully imported"
            )
        )
        for layer in ignored_layers:
            self.stdout.write(
                self.style.WARNING(f"No objects found in the layer {layer.name}")
            )
        for layer, error in errored_layers:
            self.stdout.write(self.style.ERROR(f"Error for {layer.name} | {error}"))


def fix_encoding(field):
    if isinstance(field, str):
        try:
            return field.encode("iso-8859-1").decode("utf-8")
        except UnicodeDecodeError:
            return field
    return field
