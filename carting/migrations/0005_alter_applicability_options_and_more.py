# Generated by Django 4.1.7 on 2023-04-26 15:34

import carting.models.s127
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("carting", "0004_applicability_pilotagedistrict_pilotboardingplace_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="applicability",
            options={"verbose_name_plural": "Applicabilities"},
        ),
        migrations.AlterField(
            model_name="applicability",
            name="category_of_cargo",
            field=carting.models.s127.ChoiceArrayField(
                base_field=models.CharField(
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
                ),
                blank=True,
                default=list,
                help_text="Classification of the different types of cargo that a ship may be carrying <br/>If item 7 is used, the nature of dangerous or hazardous cargoes can be amplified with category of dangerous or hazardous cargo.",
                null=True,
                size=None,
            ),
        ),
        migrations.AlterField(
            model_name="applicability",
            name="category_of_dangerous_or_hazardous_cargo",
            field=carting.models.s127.ChoiceArrayField(
                base_field=models.CharField(
                    choices=[
                        ("IMDG Code Class 1 Div. 1.1", "Imdg Code Class 1 Div 1 1"),
                        ("IMDG Code Class 1 Div. 1.2", "Imdg Code Class 1 Div 1 2"),
                        ("IMDG Code Class 1 Div. 1.3", "Imdg Code Class 1 Div 1 3"),
                        ("IMDG Code Class 1 Div. 1.4", "Imdg Code Class 1 Div 1 4"),
                        ("IMDG Code Class 1 Div. 1.5", "Imdg Code Class 1 Div 1 5"),
                        ("IMDG Code Class 1 Div. 1.6", "Imdg Code Class 1 Div 1 6"),
                        ("IMDG Code Class 2 Div. 2.1", "Imdg Code Class 2 Div 2 1"),
                        ("IMDG Code Class 2 Div. 2.2", "Imdg Code Class 2 Div 2 2"),
                        ("IMDG Code Class 2 Div. 2.3", "Imdg Code Class 2 Div 2 3"),
                        ("IMDG Code Class 3", "Imdg Code Class 3"),
                        ("IMDG Code Class 4 Div. 4.1", "Imdg Code Class 4 Div 4 1"),
                        ("IMDG Code Class 4 Div. 4.2", "Imdg Code Class 4 Div 4 2"),
                        ("IMDG Code Class 4 Div. 4.3", "Imdg Code Class 4 Div 4 3"),
                        ("IMDG Code Class 5 Div. 5.1", "Imdg Code Class 5 Div 5 1"),
                        ("IMDG Code Class 5 Div. 5.2", "Imdg Code Class 5 Div 5 2"),
                        ("IMDG Code Class 6 Div. 6.1", "Imdg Code Class 6 Div 6 1"),
                        ("IMDG Code Class 6 Div. 6.2", "Imdg Code Class 6 Div 6 2"),
                        ("IMDG Code Class 7", "Imdg Code Class 7"),
                        ("IMDG Code Class 8", "Imdg Code Class 8"),
                        ("IMDG Code Class 9", "Imdg Code Class 9"),
                        (
                            "Harmful Substances in packaged form",
                            "Harmful Substances In Packaged Form",
                        ),
                    ],
                    max_length=255,
                ),
                blank=True,
                default=list,
                help_text="Classification of dangerous goods or hazardous materials based on the International Maritime Dangerous Goods Code (<a href='https://www.imo.org/fr/OurWork/Safety/Pages/DangerousGoods-default.aspx' target='_blank' rel='noreferrer noopener'>IMDG Code</a>)",
                null=True,
                size=None,
            ),
        ),
        migrations.AlterField(
            model_name="applicability",
            name="in_ballast",
            field=models.BooleanField(
                blank=True, help_text="Whether the vessel is in ballast.", null=True
            ),
        ),
        migrations.AlterField(
            model_name="pilotagedistrict",
            name="communication_channel",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(blank=True, max_length=255, null=True),
                blank=True,
                help_text="ℹ️ Saisissez des valeurs séparées par une virgule pour en définir plusieurs.",
                null=True,
                size=None,
            ),
        ),
        migrations.AlterField(
            model_name="pilotboardingplace",
            name="communication_channel",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=255),
                blank=True,
                null=True,
                size=None,
            ),
        ),
        migrations.AlterField(
            model_name="pilotservice",
            name="category_of_pilot",
            field=carting.models.s127.ChoiceArrayField(
                base_field=models.CharField(
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
                ),
                blank=True,
                default=list,
                null=True,
                size=None,
            ),
        ),
    ]
