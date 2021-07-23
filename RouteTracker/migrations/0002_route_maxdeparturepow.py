# Generated by Django 3.1.2 on 2021-07-21 16:51

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RouteTracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='maxDeparturePow',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), null=True, size=None, verbose_name='Max Departure Power Req'),
        ),
    ]
