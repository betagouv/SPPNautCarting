import copy

from django.contrib.gis.geos import GEOSGeometry
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from lxml import etree

from carting.models import S1xyObject


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "filepath",
            type=str,
            help="filepath to S1xy.xml file",
        )

    def handle(self, *args, **options):
        S1xyObject.objects.all().delete()

        filepath = options.get("filepath")
        tree = etree.parse(filepath)
        root = tree.getroot()
        nsmap = root.nsmap

        object_root = copy.deepcopy(root)
        etree.strip_elements(object_root, "member", "imember")
        many2many = []

        for member in ("member", "imember"):
            for object in root.findall(member):
                sub_member = object[0]
                object_content = copy.deepcopy(object_root)
                object_content.append(object)
                content = etree.tostring(
                    object_content, method="xml", encoding="unicode"
                )
                gml_id = sub_member.get("{" + nsmap["gml"] + "}id")
                typology = sub_member.prefix + ":" + etree.QName(sub_member).localname

                geometry = None
                geom = sub_member.find("geometry")
                if geom is not None:
                    try:
                        geometry = GEOSGeometry.from_gml(
                            etree.tostring(geom[0][0], method="xml", encoding="unicode")
                        )
                    except IndexError:
                        pass

                s1xy_object = S1xyObject(
                    id=gml_id,
                    typology=typology,
                    content=content,
                    geometry=geometry,
                )
                s1xy_object.save()

                # ManyToMany Relationship
                for child in sub_member:
                    child_href = child.get("{" + nsmap["xlink"] + "}href")
                    if child_href is not None:
                        child_href = child_href.replace("#", "")
                        many2many.append({"obj1": gml_id, "obj2": child_href})

        for relation in many2many:
            try:
                obj1 = S1xyObject.objects.get(id=relation["obj1"])
                obj2 = S1xyObject.objects.get(id=relation["obj2"])
                obj1.link_to.add(obj2)
            except ObjectDoesNotExist:
                pass
