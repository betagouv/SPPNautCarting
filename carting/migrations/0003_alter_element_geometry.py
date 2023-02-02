# Generated by Django 4.1.4 on 2023-02-02 09:49

import carting.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("carting", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="element",
            name="geometry",
            field=carting.models.OSMGeometryField(
                blank=True, default=None, null=True, srid=4326
            ),
        ),
    ]
