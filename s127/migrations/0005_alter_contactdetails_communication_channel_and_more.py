# Generated by Django 4.1.9 on 2023-05-25 07:28

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("s127", "0004_fullpilotserviceproxy_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contactdetails",
            name="communication_channel",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=255),
                blank=True,
                default=list,
                help_text="A channel number assigned to a specific radio frequency, frequencies or frequency band.<br/>Separate multiple values with a comma.<br/>",
                size=None,
            ),
        ),
        migrations.AlterField(
            model_name="noticetime",
            name="notice_time_hours",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.DurationField(),
                blank=True,
                default=list,
                help_text="Format : hh:mm:ss <br/>Separate multiple values with a comma.<br/>The time duration prior to the time the service is needed, when notice must be provided to the service provider.<br/>",
                size=None,
            ),
        ),
        migrations.AlterField(
            model_name="pilotboardingplace",
            name="communication_channel",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=255),
                blank=True,
                default=list,
                help_text="A channel number assigned to a specific radio frequency, frequencies or frequency band.<br/>Separate multiple values with a comma.<br/>",
                size=None,
            ),
        ),
    ]
