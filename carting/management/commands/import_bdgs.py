# from django.contrib.gis.gdal.envelope import OGREnvelope
from ctypes import c_void_p

from django.contrib.gis.gdal import DataSource
from django.contrib.gis.gdal.error import GDALException
from django.contrib.gis.gdal.geometries import GEO_CLASSES, OGRGeometry, Polygon
from django.contrib.gis.gdal.geomtype import OGRGeomType
from django.contrib.gis.gdal.libgdal import lgdal
from django.contrib.gis.gdal.prototypes import ds as capi
from django.contrib.gis.gdal.prototypes import geom as geom_api
from django.contrib.gis.gdal.prototypes.generation import geom_output
from django.core.management.base import BaseCommand

from carting.models import BDGS

# from django.contrib.gis.gdal.prototypes import geom as capi


class ExtendedOGRGeometry(OGRGeometry):
    def __init__(self, geom_input, srs=None):
        try:
            super().__init__(geom_input, srs)
        except KeyError:
            if not isinstance(geom_input, self.ptr_type) and self.geom_type.num not in [
                9,
                10,
            ]:
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


EXTENDED_GEO_CLASSES = {**GEO_CLASSES, 9: CompoundCurve, 10: CurvePolygon}


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
    }


# OGR_GT_GetLinear
# OGR_G_ForceToPolygon
force_to_polygon = geom_output(lgdal.OGR_G_ForceToPolygon, [c_void_p])
# clone_geom = geom_output(lgdal.OGR_G_Clone, [c_void_p])
# to_gml = string_output(
#     lgdal.OGR_G_ExportToGML, [c_void_p], str_result=True, decoding="ascii"
# )


class Command(BaseCommand):
    def handle(self, *args, **options):
        BDGS.objects.all().delete()

        flux = DataSource(
            "WFS:https://services.data.shom.fr/INSPIRE/wfs?version=2.0.0",
            # encoding="utf-8",  # iso-8859-1
        )

        # for layer_name in (
        #     "BALISAGE_BDD_WFS:boycar",  # Balisages : Bouées cardinales
        #     # "BALISAGE_BDD_WFS:lights",  # Balisages : Feux
        #     # "BALISAGE_BDD_WFS:lndmrk",  # Balisages : Amers
        #     # "INFORMATIONS_PORTUAIRES_BDD_WFS:hrbare_polygon",  # Ports <-- ce layer est pas fou fou
        #     # "REGLEMENTATION_NAVIGATION_BDD_WFS:achare_polygon",  # zone de mouillage <-- même problème de geomType
        # ):

        for layer in flux:
            count = 0
            errors = []
            print(f"Layer name : {layer.name} with {layer.num_feat} objects")
            if "inspireid" not in layer.fields:
                continue
            for feature in layer:
                raw = {
                    field: fix_encoding(feature.get(field))
                    for field in feature.fields
                    if field not in ("inspireid")
                }

                geom_ptr = capi.get_feat_geom_ref(feature.ptr)
                geom = ExtendedOGRGeometry(geom_api.clone_geom(geom_ptr))
                if geom.geom_type == 10:
                    geom = ExtendedOGRGeometry(
                        force_to_polygon(geom_api.clone_geom(geom_ptr))
                    )
                    geom.srid = 3857
                    geom.transform(4326)

                bdgs_object = BDGS(
                    inspire_id=feature.get("inspireid"),
                    category=layer.name,
                    raw=raw,
                    geometry=geom.json,
                )
                try:
                    bdgs_object.save()
                    count += 1
                except Exception as e:
                    errors.append((raw, e))
            print(f"{count} bdgs objects imported.")

            for raw, error in errors:
                print(f"Error for {raw} | {error}")


def fix_encoding(field):
    if isinstance(field, str):
        try:
            return field.encode("iso-8859-1").decode("utf-8")
        except UnicodeDecodeError:
            return field
    return field
