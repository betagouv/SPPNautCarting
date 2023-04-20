# Generated by Django 4.1.7 on 2023-04-20 12:26

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("carting", "0004_organisationcontactarea_pilotagedistrict_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="featurename",
            name="language",
            field=models.CharField(
                blank=True,
                choices=[("FRA", "Fra"), ("ENG", "Eng")],
                help_text="The language is encoded by a character code following ISO 639-3",
                max_length=3,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="information",
            name="language",
            field=models.CharField(
                blank=True,
                choices=[("FRA", "Fra"), ("ENG", "Eng")],
                help_text="The language is encoded by a character code following ISO 639-3",
                max_length=3,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="pilotagedistrict",
            name="communication_channel",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(blank=True, max_length=255, null=True),
                blank=True,
                null=True,
                size=None,
            ),
        ),
        migrations.AlterField(
            model_name="pilotboardingplace",
            name="communication_channel",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(blank=True, max_length=255, null=True),
                blank=True,
                null=True,
                size=None,
            ),
        ),
    ]
