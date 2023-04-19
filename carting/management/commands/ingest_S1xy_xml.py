from django.core.management.base import BaseCommand

from carting.models import S1xyObject


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "filepath",
            type=str,
            help="filepath to S1xy.xml file",
        )

    def handle(self, *args, **options):
        S1xyObject.objects.inject_from_xml_file(options["filepath"])
