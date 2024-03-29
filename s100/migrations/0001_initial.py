# Generated by Django 4.1.7 on 2023-05-09 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
    ]

    operations = [
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
            options={
                "abstract": False,
            },
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
            options={
                "abstract": False,
            },
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
                (
                    "display_name",
                    models.BooleanField(
                        default=False,
                        help_text="A statement expressing if a feature name is to be displayed in certain display settings or not.",
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
        migrations.AddConstraint(
            model_name="featurename",
            constraint=models.UniqueConstraint(
                condition=models.Q(("display_name", True)),
                fields=("content_type", "object_id", "display_name"),
                name="unique_display_name",
            ),
        ),
    ]
