# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-12-12 11:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ops', '0002_auto_20181212_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='emergencyteam',
            name='status',
            field=models.CharField(choices=[('accept', 'Accept'), ('waiting', 'Waiting'), ('cancel', 'Cancel')], default='waiting', max_length=10),
        ),
    ]
