from django.conf import settings
from django.contrib.gis.geos import GEOSGeometry
from django.core.management.base import BaseCommand

from carting.models import OuvrageSection

some_geom = {
    "ALINEA": {
        "4.1.0.07": '{"type": "Polygon", "coordinates": [[[-1.8726666, 48.721], [-1.566, 48.7643333], [-1.3308333, 48.634], [-1.8841666, 48.5983333], [-1.8726666, 48.721]]] }',
        "4.1.0.19": '{"type": "Polygon", "coordinates": [[[-2.0741666, 48.6583333], [-2.0238333, 48.6585], [-2.0265, 48.6356666], [-2.0555, 48.6351666], [-2.0741666, 48.6583333]]] }',
        "4.1.0.25": '{"type": "Polygon", "coordinates": [[[-2.0345, 48.6428333], [-2.0251666, 48.6475], [-2.022, 48.653], [-2.007, 48.6525], [-2.0095, 48.6385], [-2.0205, 48.635], [-2.0341666, 48.6388333], [-2.0345, 48.6428333]]] }',
        "4.1.0.31": '{"type": "Polygon", "coordinates": [[[-3.0715, 48.8291666], [-2.9075, 48.9211666], [-2.2841666, 48.6926666], [-2.7051666, 48.5296666], [-3.0715, 48.8291666]]] }',
        "4.1.0.37": '{"type": "Polygon", "coordinates": [[[-2.942, 49.1426666], [-2.9455, 48.9941666], [-2.6891666, 48.9965], [-2.704, 49.146], [-2.942, 49.1426666]]] }',
        "4.1.0.43": '{"type": "Polygon", "coordinates": [[[-3.1971666, 48.9685], [-3.2023333, 48.7615], [-2.6791666, 48.4775], [-1.6785, 48.5711666], [-1.9685, 48.8626666], [-3.1971666, 48.9685]]] }',
        "4.1.1.1.0.05": '{"type": "Polygon", "coordinates": [[[-2.269, 49.0475], [-1.7331666, 49.0325], [-1.6626666, 48.8441666], [-2.3711666, 48.8705], [-2.269, 49.0475]]] }',
        "4.1.1.1.0.09": '{"type": "Polygon", "coordinates": [[[-2.8745, 49.1288333], [-2.8748333, 49.0726666], [-2.762, 49.0721666], [-2.761, 49.1281666], [-2.8745, 49.1288333]]] }',
        "4.1.1.1.0.13": '{"type": "Polygon", "coordinates": [[[-2.8745, 49.1288333], [-2.8748333, 49.0726666], [-2.762, 49.0721666], [-2.761, 49.1281666], [-2.8745, 49.1288333]]] }',
        "4.1.1.1.0.17": '{"type": "Point", "coordinates": [-2.8141666, 49.105] }',
        "4.1.1.1.0.21": '{"type": "Polygon", "coordinates": [[[-2.8833333, 49.0596666], [-2.8835, 49.0038333], [-2.7643333, 49.0038333], [-2.7653333, 49.0598333], [-2.8833333, 49.0596666]]] }',
        "4.1.1.1.0.25": '{"type": "Point", "coordinates": [-2.8066666, 49.0273333] }',
        "4.1.1.1.0.29": '{"type": "Polygon", "coordinates": [[[-2.9531666, 49.1421666], [-2.956, 48.9815], [-2.6948333, 48.9815], [-2.696, 49.1411666], [-2.9531666, 49.1421666]]] }',
        "4.1.1.1.0.33": '{"type": "Polygon", "coordinates": [[[-3.788, 49.1078333], [-2.2133333, 49.9166666], [-1.255, 49.2286666], [-1.248, 48.5171666], [-3.295, 48.4673333], [-3.788, 49.1078333]]] }',
        "4.1.1.1.0.37": '{"type": "Point", "coordinates": [-1.8936666, 48.7505] }',
        "4.1.1.1.0.41": '{"type": "Point", "coordinates": [-1.9005, 48.7301666] }',
        "4.1.1.1.0.45": '{"type": "Point", "coordinates": [-1.9403333, 48.7281666] }',
        "4.1.1.1.0.49": '{"type": "Point", "coordinates": [-2.0873333, 48.8078333] }',
        "4.1.1.1.0.53": '{"type": "Point", "coordinates": [-2.202, 48.7548333] }',
        "4.1.1.1.0.57": '{"type": "Point", "coordinates": [-2.2478333, 48.7081666] }',
        "4.1.1.1.0.65": '{"type": "Polygon", "coordinates": [[[-2.1963333, 48.6768333], [-2.1965, 48.6693333], [-2.1778333, 48.6695], [-2.1783333, 48.6768333], [-2.1963333, 48.6768333]]] }',
        "4.1.1.1.0.73": '{"type": "Polygon", "coordinates": [[[-3.0436666, 48.9206666], [-3.0443333, 48.8223333], [-2.8488333, 48.8223333], [-2.8498333, 48.9231666], [-3.0436666, 48.9206666]]] }',
        "4.1.1.1.0.77": '{"type": "Polygon", "coordinates": [[[-2.9328333, 48.9135], [-2.9335, 48.885], [-2.8758333, 48.885], [-2.8766666, 48.9133333], [-2.9328333, 48.9135]]] }',
        "4.1.1.1.0.81": '{"type": "Polygon", "coordinates": [[[-2.9611666, 48.8923333], [-2.9616666, 48.8508333], [-2.905, 48.8503333], [-2.905, 48.8921666], [-2.9611666, 48.8923333]]] }',
        "4.1.1.1.0.85": '{"type": "Polygon", "coordinates": [[[-2.9451666, 48.8418333], [-2.867, 48.8418333], [-2.8675, 48.8836666], [-2.9438333, 48.8835], [-2.9451666, 48.8418333]]] }',
        "4.1.1.1.0.89": '{"type": "Polygon", "coordinates": [[[-2.9071666, 48.828], [-2.912, 48.816], [-2.8886666, 48.8146666], [-2.8913333, 48.8275], [-2.9071666, 48.828]]] }',
        "4.1.1.1.0.93": '{"type": "Polygon", "coordinates": [[[-2.908, 48.7765], [-2.9085, 48.7646666], [-2.877, 48.7645], [-2.8778333, 48.7763333], [-2.908, 48.7765]]] }',
        "4.1.1.2.1.0.07": '{"type": "Polygon", "coordinates": [[[-1.5193333, 48.7885], [-1.459, 48.5943333], [-2.4256666, 48.5975], [-2.428, 48.8583333], [-1.5193333, 48.7885]]] }',
        "4.1.1.2.1.0.13": '{"type": "Polygon", "coordinates": [[[-1.917, 48.6916666], [-1.5723333, 48.8545], [-1.294, 48.6535], [-1.8568333, 48.557], [-1.917, 48.6916666]]] }',
        "4.1.1.2.1.0.19": '{"type": "Polygon", "coordinates": [[[-1.9066666, 48.7188333], [-1.9066666, 48.6955], [-1.9638333, 48.6958333], [-1.9626666, 48.7185], [-1.9066666, 48.7188333]]] }',
        "4.1.1.2.1.0.25": '{"type": "Polygon", "coordinates": [[[-1.9563333, 48.7695], [-1.9188333, 48.6385], [-2.1123333, 48.6078333], [-2.2386666, 48.7193333], [-1.9563333, 48.7695]]] }',
        "4.1.1.2.1.0.31": '{"type": "Polygon", "coordinates": [[[-1.9563333, 48.7695], [-1.9188333, 48.6385], [-2.1123333, 48.6078333], [-2.2386666, 48.7193333], [-1.9563333, 48.7695]]] }',
        "4.1.1.2.1.0.43": '{"type": "Point", "coordinates": [-2.0466666, 48.6516666] }',
        "4.1.1.2.1.0.49": '{"type": "Polygon", "coordinates": [[[-1.9563333, 48.7695], [-1.9188333, 48.6385], [-2.1123333, 48.6078333], [-2.2386666, 48.7193333], [-1.9563333, 48.7695]]] }',
        "4.1.1.2.2.0.07": '{"type": "Polygon", "coordinates": [[[-3.0056666, 48.7595], [-2.7193333, 48.5131666], [-2.2951666, 48.6098333], [-2.244, 48.7395], [-2.7778333, 48.8638333], [-3.0056666, 48.7595]]] }',
        "4.1.1.2.2.0.13": '{"type": "Polygon", "coordinates": [[[-2.5413333, 48.8426666], [-2.4488333, 48.6288333], [-2.2976666, 48.6015], [-1.9246666, 48.7881666], [-2.5413333, 48.8426666]]] }',
        "4.1.1.2.2.0.19": '{"type": "Polygon", "coordinates": [[[-2.3946666, 48.7048333], [-2.3938333, 48.6745], [-2.3165, 48.6746666], [-2.3126666, 48.704], [-2.3946666, 48.7048333]]] }',
        "4.1.1.2.2.0.25": '{"type": "Polygon", "coordinates": [[[-2.3206666, 48.6941666], [-2.3171666, 48.6783333], [-2.4086666, 48.6375], [-2.4891666, 48.6536666], [-2.445, 48.6935], [-2.3206666, 48.6941666]]] }',
        "4.1.1.2.2.0.31": '{"type": "Polygon", "coordinates": [[[-2.8398333, 48.6016666], [-2.7895, 48.616], [-2.6988333, 48.5836666], [-2.5936666, 48.5966666], [-2.54, 48.5725], [-2.6325, 48.5223333], [-2.7348333, 48.5293333], [-2.8398333, 48.6016666]]] }',
        "4.1.1.2.2.0.37": '{"type": "Polygon", "coordinates": [[[-2.9243333, 48.7145], [-2.3458333, 48.6973333], [-2.5928333, 48.5126666], [-2.795, 48.512], [-2.9243333, 48.7145]]] }',
        "4.1.1.2.2.0.43": '{"type": "Point", "coordinates": [-2.6218333, 48.6693333] }',
        "4.1.1.2.3.0.13": '{"type": "Polygon", "coordinates": [[[-3.2043333, 49.0005], [-3.2063333, 48.7191666], [-2.699, 48.7138333], [-2.701, 48.9993333], [-3.2043333, 49.0005]]] }',
        "4.1.1.2.3.0.19": '{"type": "Polygon", "coordinates": [[[-3.2043333, 49.0005], [-3.2063333, 48.7191666], [-2.699, 48.7138333], [-2.701, 48.9993333], [-3.2043333, 49.0005]]] }',
        "4.1.1.2.3.0.25": '{"type": "Polygon", "coordinates": [[[-2.9448333, 48.9151666], [-2.9458333, 48.8735], [-2.8665, 48.8733333], [-2.8676666, 48.9155], [-2.9448333, 48.9151666]]] }',
        "4.1.1.2.3.0.31": '{"type": "Polygon", "coordinates": [[[-3.1181666, 48.9248333], [-3.1188333, 48.8958333], [-3.0596666, 48.8961666], [-3.059, 48.9251666], [-3.1181666, 48.9248333]]] }',
        "4.1.5.3.0.19": '{"type": "Polygon", "coordinates": [[[-2.8025, 48.6603333], [-2.7953333, 48.6648333], [-2.783, 48.6666666], [-2.7725, 48.6638333], [-2.7651666, 48.657], [-2.7663333, 48.647], [-2.7786666, 48.6403333], [-2.8005, 48.6416666], [-2.8043333, 48.6516666], [-2.8025, 48.6603333]]] }',
    },
    "TOPONYME": {
        "4.1.1.1.0.81": '{"type": "LineString", "coordinates": [[-2.977, 48.9098333], [-2.9528333, 48.8383333], [-2.9656666, 48.8025]] }',
    },
}


class Command(BaseCommand):
    def handle(self, *args, **options):
        for typology, geoms in some_geom.items():
            in_sections = OuvrageSection.objects.filter(
                ouvrage_name="z99", numero__in=geoms.keys(), typology=typology
            ).order_by("numero")

            for geometry, in_section in zip(geoms.values(), in_sections, strict=True):
                in_section.geometry = GEOSGeometry(geometry)
            updated = OuvrageSection.objects.bulk_update(in_sections, ["geometry"])
            print(f"{updated} {typology} géométrisées")