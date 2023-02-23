# Generated by Django 4.1.5 on 2023-02-22 14:06

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("carting", "0001_postgis_extension"),
    ]

    operations = [
        migrations.CreateModel(
            name="OuvrageSection",
            fields=[
                ("bpn_id", models.UUIDField(primary_key=True, serialize=False)),
                ("numero", models.CharField(max_length=20)),
                ("content", models.TextField(blank=True)),
                (
                    "typology",
                    models.CharField(
                        choices=[
                            ("OUVRAGE", "ouvrage"),
                            ("CHAPTER", "chapitre"),
                            ("SUBCHAPTER", "sChapitre"),
                            ("PARAGRAPH", "para"),
                            ("SUBPARAGRAPH", "sPara"),
                            ("SUBSUBPARAGRAPH", "ssPara"),
                            ("ALINEA", "alinea"),
                            ("TABLE", "tableau"),
                            ("ILLUSTRATION", "illustration"),
                            ("TOPONYME", "texte/principal"),
                            ("REFERENCE", "texte/reference"),
                        ],
                        max_length=25,
                    ),
                ),
                ("ouvrage_name", models.CharField(max_length=10)),
                (
                    "geometry",
                    django.contrib.gis.db.models.fields.GeometryField(
                        blank=True, default=None, null=True, srid=4326
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="children",
                        to="carting.ouvragesection",
                        verbose_name="parent",
                    ),
                ),
            ],
            options={
                "ordering": ("numero",),
            },
        ),
    ]
