# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-12-12 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ops', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branchoffice',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
