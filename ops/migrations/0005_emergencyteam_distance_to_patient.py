# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-12-13 04:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ops', '0004_auto_20181213_0355'),
    ]

    operations = [
        migrations.AddField(
            model_name='emergencyteam',
            name='distance_to_patient',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
