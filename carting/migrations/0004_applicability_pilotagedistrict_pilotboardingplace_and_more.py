# Generated by Django 4.1.7 on 2023-04-26 13:19

import carting.models.s127
import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("carting", "0003_alter_ouvragesection_typology"),
    ]

    operations = [
        migrations.CreateModel(
            name="Applicability",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("object_id", models.BigIntegerField()),
                ("in_ballast", models.BooleanField(blank=True, null=True)),
                (
                    "category_of_cargo",
                    carting.models.s127.ChoiceArrayField(
                        base_field=models.CharField(
                            blank=True,
                            choices=[
                                ("bulk", "Bulk"),
                                ("container", "Container"),
                                ("general", "General"),
                                ("liquid", "Liquid"),
                                ("passenger", "Passenger"),
                                ("livestock", "Livestock"),
                                ("dangerous or hazardous", "Dangerous Or Hazardous"),
                                ("heavy lift", "Heavy Lift"),
                                ("ballast", "Ballast"),
                            ],
                            max_length=255,
                            null=True,
                        ),
                        blank=True,
                        default=list,
                        null=True,
                        size=None,
                    ),
                ),
                (
                    "category_of_dangerous_or_hazardous_cargo",
                    carting.models.s127.ChoiceArrayField(
                        base_field=models.CharField(
                            blank=True,
                            choices=[
                                (
                                    "IMDG Code Class 1 Div. 1.1",
                                    "Imdg Code Class 1 Div 1 1",
                                ),
                                (
                                    "IMDG Code Class 1 Div. 1.2",
                                    "Imdg Code Class 1 Div 1 2",
                                ),
                                (
                                    "IMDG Code Class 1 Div. 1.3",
                                    "Imdg Code Class 1 Div 1 3",
                                ),
                                (
                                    "IMDG Code Class 1 Div. 1.4",
                                    "Imdg Code Class 1 Div 1 4",
                                ),
                                (
                                    "IMDG Code Class 1 Div. 1.5",
                                    "Imdg Code Class 1 Div 1 5",
                                ),
                                (
                                    "IMDG Code Class 1 Div. 1.6",
                                    "Imdg Code Class 1 Div 1 6",
                                ),
                                (
                                    "IMDG Code Class 2 Div. 2.1",
                                    "Imdg Code Class 2 Div 2 1",
                                ),
                                (
                                    "IMDG Code Class 2 Div. 2.2",
                                    "Imdg Code Class 2 Div 2 2",
                                ),
                                (
                                    "IMDG Code Class 2 Div. 2.3",
                                    "Imdg Code Class 2 Div 2 3",
                                ),
                                ("IMDG Code Class 3", "Imdg Code Class 3"),
                                (
                                    "IMDG Code Class 4 Div. 4.1",
                                    "Imdg Code Class 4 Div 4 1",
                                ),
                                (
                                    "IMDG Code Class 4 Div. 4.2",
                                    "Imdg Code Class 4 Div 4 2",
                                ),
                                (
                                    "IMDG Code Class 4 Div. 4.3",
                                    "Imdg Code Class 4 Div 4 3",
                                ),
                                (
                                    "IMDG Code Class 5 Div. 5.1",
                                    "Imdg Code Class 5 Div 5 1",
                                ),
                                (
                                    "IMDG Code Class 5 Div. 5.2",
                                    "Imdg Code Class 5 Div 5 2",
                                ),
                                (
                                    "IMDG Code Class 6 Div. 6.1",
                                    "Imdg Code Class 6 Div 6 1",
                                ),
                                (
                                    "IMDG Code Class 6 Div. 6.2",
                                    "Imdg Code Class 6 Div 6 2",
                                ),
                                ("IMDG Code Class 7", "Imdg Code Class 7"),
                                ("IMDG Code Class 8", "Imdg Code Class 8"),
                                ("IMDG Code Class 9", "Imdg Code Class 9"),
                                (
                                    "Harmful Substances in packaged form",
                                    "Harmful Substances In Packaged Form",
                                ),
                            ],
                            max_length=255,
                            null=True,
                        ),
                        blank=True,
                        default=list,
                        null=True,
                        size=None,
                    ),
                ),
                (
                    "category_of_vessel",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("general cargo vessel", "General Cargo Vessel"),
                            ("container carrier", "Container Carrier"),
                            ("tanker", "Tanker"),
                            ("bulk carrier", "Bulk Carrier"),
                            ("passenger vessel", "Passenger Vessel"),
                            ("roll-on roll-off", "Roll On Roll Off"),
                            ("refrigerated cargo vessel", "Refrigerated Cargo Vessel"),
                            ("fishing vessel", "Fishing Vessel"),
                            ("service", "Service"),
                            ("warship", "Warship"),
                            (
                                "towed or pushed composite unit",
                                "Towed Or Pushed Composite Unit",
                            ),
                            ("tug and tow", "Tug And Tow"),
                            ("light recreational", "Light Recreational"),
                            (
                                "semi-submersible offshore installation",
                                "Semi Submersible Offshore Installation",
                            ),
                            (
                                "jackup exploration or project installation",
                                "Jackup Exploration Or Project Installation",
                            ),
                            ("livestock carrier", "Livestock Carrier"),
                            ("sport fishing", "Sport Fishing"),
                        ],
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "category_of_vessel_registry",
                    models.CharField(
                        blank=True,
                        choices=[("domestic", "Domestic"), ("foreign", "Foreign")],
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "logical_connectives",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("logical conjunction", "Logical Conjunction"),
                            ("logical disjunction", "Logical Disjunction"),
                        ],
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "thickness_of_ice_capability",
                    models.IntegerField(blank=True, null=True),
                ),
                (
                    "vessel_performance",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "content_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contenttypes.contenttype",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PilotageDistrict",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "communication_channel",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(
                            blank=True, max_length=255, null=True
                        ),
                        blank=True,
                        null=True,
                        size=None,
                    ),
                ),
                (
                    "geometry",
                    django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="PilotBoardingPlace",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "call_sign",
                    models.CharField(
                        blank=True,
                        help_text="The designated call-sign of a radio station.",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "category_of_pilot_boarding_place",
                    models.CharField(
                        blank=True,
                        choices=[
                            (
                                "boarding by pilot-cruising vessel",
                                "Boarding By Pilot Cruising Vessel",
                            ),
                            ("boarding by helicopter", "Boarding By Helicopter"),
                            (
                                "pilot comes out from shore",
                                "Pilot Comes Out From Shore",
                            ),
                        ],
                        help_text="The place or general direction to which a vessel is going or directed. Remarks: In addition to a placename of a port, harbour area or terminal, the place could include generalities such as “The north-west”, or “upriver”.",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "category_of_preference",
                    models.CharField(
                        blank=True,
                        choices=[("primary", "Primary"), ("alternate", "Alternate")],
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "category_of_vessel",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("general cargo vessel", "General Cargo Vessel"),
                            ("container carrier", "Container Carrier"),
                            ("tanker", "Tanker"),
                            ("bulk carrier", "Bulk Carrier"),
                            ("passenger vessel", "Passenger Vessel"),
                            ("roll-on roll-off", "Roll On Roll Off"),
                            ("refrigerated cargo vessel", "Refrigerated Cargo Vessel"),
                            ("fishing vessel", "Fishing Vessel"),
                            ("service", "Service"),
                            ("warship", "Warship"),
                            (
                                "towed or pushed composite unit",
                                "Towed Or Pushed Composite Unit",
                            ),
                            ("tug and tow", "Tug And Tow"),
                            ("light recreational", "Light Recreational"),
                            (
                                "semi-submersible offshore installation",
                                "Semi Submersible Offshore Installation",
                            ),
                            (
                                "jackup exploration or project installation",
                                "Jackup Exploration Or Project Installation",
                            ),
                            ("livestock carrier", "Livestock Carrier"),
                            ("sport fishing", "Sport Fishing"),
                        ],
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "communication_channel",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(
                            blank=True, max_length=255, null=True
                        ),
                        blank=True,
                        null=True,
                        size=None,
                    ),
                ),
                (
                    "destination",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "pilot_movement",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("embarkation", "Embarkation"),
                            ("disembarkation", "Disembarkation"),
                            ("pilot change", "Pilot Change"),
                        ],
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "pilot_vessel",
                    models.CharField(
                        blank=True,
                        help_text="Description of the pilot vessel. The pilot vessel is a small vessel used by a pilot to go to or from a vessel employing the pilot's services.",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "status",
                    carting.models.s127.ChoiceArrayField(
                        base_field=models.CharField(
                            blank=True,
                            choices=[
                                ("permanent", "Permanent"),
                                ("occasional", "Occasional"),
                                ("recommended", "Recommended"),
                                ("not in use", "Not In Use"),
                                ("periodic/intermittent", "Periodic Intermittent"),
                                ("reserved", "Reserved"),
                                ("temporary", "Temporary"),
                                ("private", "Private"),
                                ("mandatory", "Mandatory"),
                                ("extinguished", "Extinguished"),
                                ("illuminated", "Illuminated"),
                                ("historic", "Historic"),
                                ("public", "Public"),
                                ("synchronised", "Synchronised"),
                                ("watched", "Watched"),
                                ("un-watched", "Un Watched"),
                                ("existence doubtful", "Existence Doubtful"),
                                ("buoyed", "Buoyed"),
                            ],
                            max_length=255,
                            null=True,
                        ),
                        blank=True,
                        default=list,
                        null=True,
                        size=None,
                    ),
                ),
                (
                    "geometry",
                    django.contrib.gis.db.models.fields.GeometryField(srid=4326),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="VesselsMeasurements",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "comparison_operator",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("greater than", "Greater Than"),
                            ("greater than or equal to", "Greater Than Or Equal To"),
                            ("less than", "Less Than"),
                            ("less than or equal to", "Less Than Or Equal To"),
                            ("equal to", "Equal To"),
                            ("not equal to", "Not Equal To"),
                        ],
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "vessels_characteristics",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("length overall", "Length Overall"),
                            ("length at waterline", "Length At Waterline"),
                            ("breadth", "Breadth"),
                            ("draught", "Draught"),
                            ("height", "Height"),
                            ("displacement tonnage", "Displacement Tonnage"),
                            (
                                "displacement tonnage, light",
                                "Displacement Tonnage Light",
                            ),
                            (
                                "displacement tonnage, loaded",
                                "Displacement Tonnage Loaded",
                            ),
                            ("deadweight tonnage", "Deadweight Tonnage"),
                            ("gross tonnage", "Gross Tonnage"),
                            ("net tonnage", "Net Tonnage"),
                            (
                                "Panama Canal/Universal Measurement System net tonnage",
                                "Panama Canal Universal Measurement System Net Tonnage",
                            ),
                            ("Suez Canal net tonnage", "Suez Canal Net Tonnage"),
                            ("Suez Canal gross tonnage", "Suez Canal Gross Tonnage"),
                        ],
                        max_length=255,
                        null=True,
                    ),
                ),
                ("vessels_characteristics_value", models.FloatField()),
                (
                    "vessels_characteristics_unit",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("metre", "Metre"),
                            ("foot", "Foot"),
                            ("metric ton", "Metric Ton"),
                            ("ton", "Ton"),
                            ("short ton", "Short Ton"),
                            ("gross ton", "Gross Ton"),
                            ("net ton", "Net Ton"),
                            (
                                "Panama Canal/Universal Measurement System net tonnage",
                                "Panama Canal Universal Measurement System Net Tonnage",
                            ),
                            ("Suez Canal Net Tonnage", "Suez Canal Net Tonnage"),
                            ("none", "None"),
                            ("cubic metres", "Cubic Metres"),
                            ("Suez Canal Gross Tonnage", "Suez Canal Gross Tonnage"),
                        ],
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "applicability",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="vessels_measurements",
                        to="carting.applicability",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TextContent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("object_id", models.BigIntegerField()),
                (
                    "category_of_text",
                    models.CharField(
                        choices=[
                            ("abstract or summary", "Abstract Or Summary"),
                            ("extract", "Extract"),
                            ("full text", "Full Text"),
                        ],
                        max_length=255,
                    ),
                ),
                (
                    "content_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contenttypes.contenttype",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PilotService",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "category_of_pilot",
                    carting.models.s127.ChoiceArrayField(
                        base_field=models.CharField(
                            blank=True,
                            choices=[
                                ("pilot", "Pilot"),
                                ("deep sea", "Deep Sea"),
                                ("harbour", "Harbour"),
                                ("bar", "Bar"),
                                ("river", "River"),
                                ("channel", "Channel"),
                                ("lake", "Lake"),
                            ],
                            max_length=255,
                            null=True,
                        ),
                        blank=True,
                        default=list,
                        null=True,
                        size=None,
                    ),
                ),
                (
                    "pilot_qualification",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("government pilot", "Government Pilot"),
                            (
                                "pilot approved by government",
                                "Pilot Approved By Government",
                            ),
                            ("state pilot", "State Pilot"),
                            ("federal pilot", "Federal Pilot"),
                            ("company pilot", "Company Pilot"),
                            ("local pilot", "Local Pilot"),
                            (
                                "citizen with sufficient local knowledge",
                                "Citizen With Sufficient Local Knowledge",
                            ),
                            (
                                "citizen with doubtful local knowledge",
                                "Citizen With Doubtful Local Knowledge",
                            ),
                        ],
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "pilot_request",
                    models.CharField(
                        blank=True,
                        help_text="Description of the pilot request procedure",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "remote_pilot",
                    models.BooleanField(
                        blank=True,
                        help_text="Whether remote pilot services are available. True: remote pilot is available: Pilotage is available remotely from shore or other location remote from the vessel requiring pilotage.False: remote pilot is not available: Remote pilotage is not available.",
                        null=True,
                    ),
                ),
                (
                    "geometry",
                    django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326),
                ),
                (
                    "pilotage_district",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pilot_service",
                        to="carting.pilotagedistrict",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="NoticeTime",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "notice_time_hours",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.FloatField(),
                        help_text="The time duration prior to the time the service is needed, when notice must be provided to the service provider.",
                        size=None,
                    ),
                ),
                (
                    "notice_time_text",
                    models.CharField(
                        blank=True,
                        help_text="Text string qualifying the notice time specified in NTCHRS.This may explain the time specification in NTCHRS (e.g., “3 working days” for a NTCHRS value of “72” where NTCTIM is supposed to be “3 working days”) or consist of other language qualifying the time, e.g., “On departure from last port” or “On passing reporting line XY”)",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "operation",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("largest value", "Largest Value"),
                            ("smallest value", "Smallest Value"),
                        ],
                        help_text="Indicates whether the minimum or maximum value should be used to describe a condition or in application processing",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "pilot_service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="notice_time",
                        to="carting.pilotservice",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Information",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("object_id", models.BigIntegerField()),
                (
                    "language",
                    models.CharField(
                        choices=[("fra", "French"), ("eng", "English")], max_length=3
                    ),
                ),
                ("headline", models.CharField(blank=True, max_length=255)),
                ("text", models.TextField(blank=True)),
                (
                    "content_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contenttypes.contenttype",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FeatureName",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("object_id", models.BigIntegerField()),
                (
                    "language",
                    models.CharField(
                        choices=[("fra", "French"), ("eng", "English")], max_length=3
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="The individual name of a feature.", max_length=255
                    ),
                ),
                ("display_name", models.BooleanField(default=False)),
                (
                    "content_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contenttypes.contenttype",
                    ),
                ),
            ],
        ),
    ]
