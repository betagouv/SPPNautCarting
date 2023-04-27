# Generated by Django 4.1.7 on 2023-04-27 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("carting", "0008_remove_applicability_content_type_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="permissiontype",
            name="applicability_content_type",
        ),
        migrations.RemoveField(
            model_name="permissiontype",
            name="applicability_object_id",
        ),
        migrations.AddField(
            model_name="permissiontype",
            name="applicability",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                to="carting.applicability",
            ),
            preserve_default=False,
        ),
    ]
