# Generated by Django 4.1.9 on 2023-06-08 13:03

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("s127", "0006_radiocommunications"),
    ]

    operations = [
        migrations.DeleteModel(
            name="FullPilotageDistrictProxy",
        ),
        migrations.DeleteModel(
            name="SimplePilotageDistrictProxy",
        ),
    ]
