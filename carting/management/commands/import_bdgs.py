from django.contrib.gis.gdal import DataSource
from django.contrib.gis.gdal.error import GDALException
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        flux = DataSource(
            "WFS:https://services.data.shom.fr/INSPIRE/wfs?version=2.0.0",
            # encoding="utf-8",  # iso-8859-1
        )
        print(f"Layers count in WFS : {flux.layer_count}")

        # layer = wfs["BALISAGE_BDD_WFS:boycar"]
        for layer_name in (
            "BALISAGE_BDD_WFS:boycar",  # Balisages : Bouées cardinales
            # "BALISAGE_BDD_WFS:lights",  # Balisages : Feux
            # "BALISAGE_BDD_WFS:lndmrk",  # Balisages : Amers
            # "INFORMATIONS_PORTUAIRES_BDD_WFS:hrbare_polygon",  # Ports <-- ce layer est pas fou fou
            # "REGLEMENTATION_NAVIGATION_BDD_WFS:achare_polygon",  # zone de mouillage <-- même problème de geomType
        ):
            layer = flux[layer_name]
            print("##########")
            print(f"Layer name : {layer.name}")
            print(f"Layer length : {layer.num_feat}")
            # FIXME : django.contrib.gis.gdal.error.GDALException: Invalid OGR Integer Type: 10
            # print(f"Layer geom type : {layer.geom_type.name}")
            print(f"Layer fields name : {layer.fields}")
            print(f"Layer extent : {layer.extent.tuple}")

            for feature in layer:
                # FIXME : encodage des textes / print(feature.get("objnam").encode("iso-8859-1").decode("utf-8"))
                feature_str = ""
                for field in layer.fields:
                    if field == "objnam" and feature.get(field):
                        feature_str += (
                            str(feature.get(field).encode("iso-8859-1").decode("utf-8"))
                            + " "
                        )
                    else:
                        feature_str += str(feature.get(field)) + " "
                try:
                    feature_str += feature.geom.json
                except GDALException:
                    pass
                print(feature_str)
            print(f"Layer fields name : {layer.fields}")
