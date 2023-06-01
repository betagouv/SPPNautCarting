# Generated by Django 4.1.9 on 2023-06-01 13:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("s100", "0001_initial"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="featurename",
            constraint=models.UniqueConstraint(
                fields=("content_type", "name", "language"),
                name="unique_name_per_feature_type_and_language",
            ),
        ),
    ]
