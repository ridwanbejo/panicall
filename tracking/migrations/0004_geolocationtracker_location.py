# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-12-12 10:44
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0003_auto_20181212_0938'),
    ]

    operations = [
        migrations.AddField(
            model_name='geolocationtracker',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(default=django.contrib.gis.geos.point.Point(0.0, 0.0), geography=True, srid=4326),
        ),
    ]
