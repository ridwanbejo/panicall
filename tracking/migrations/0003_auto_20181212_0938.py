# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-12-12 09:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0002_auto_20181212_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geolocationtracker',
            name='device_battery_level',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]