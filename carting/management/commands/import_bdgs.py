from ctypes import POINTER, c_char_p, c_double, c_int, c_long, c_void_p

from django.contrib.gis.gdal import DataSource

# from django.contrib.gis.gdal.envelope import OGREnvelope
# from django.contrib.gis.gdal.error import GDALException
# from django.contrib.gis.gdal.libgdal import lgdal
# from django.contrib.gis.gdal.prototypes.generation import (
#     bool_output,
#     const_string_output,
#     double_output,
#     geom_output,
#     int64_output,
#     int_output,
#     srs_output,
#     void_output,
#     voidptr_output,
# )
from django.core.management.base import BaseCommand

from carting.models import BDGS


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

        # for layer in flux:
        for layer_name in [
            # "INFORMATIONS_PORTUAIRES_BDD_WFS:hrbare_polygon",
            "BALISAGE_BDD_WFS:lndmrk",
        ]:
            layer = flux[layer_name]
            print(f"Layer name : {layer.name} with {layer.num_feat} objects")
            if "inspireid" not in layer.fields:
                continue
            # try:
            for feature in layer:
                # geom_type = int_output(lgdal.OGR_FD_GetGeomType, [c_void_p])
                # geom_readable = geom_output(lgdal.OGR_F_GetGeometryRef, [c_void_p])
                # dump_readable = const_string_output(
                #     lgdal.OGR_F_DumpReadableAsString, [c_void_p]
                # )
                # print(dump_readable(feature.ptr))

                raw = {
                    field: fix_encoding(feature.get(field))
                    for field in feature.fields
                    if field not in ("inspireid")
                }

                bdgs_object = BDGS(
                    inspire_id=feature.get("inspireid"),
                    category=layer.name,
                    raw=raw,
                    geometry=feature.geom.json,
                )
                bdgs_object.save()
            # except GDALException:  # Invalid OGR Integer Type: 10
            #     pass


def fix_encoding(field):
    if isinstance(field, str):
        return field.encode("iso-8859-1").decode("utf-8")
    return field
