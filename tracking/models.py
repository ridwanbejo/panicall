# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.contrib.gis.geos import Point


# Create your models here.
class GeoLocationTracker(models.Model):
    DEVICE_TYPE_CHOICES = (
        ('android', 'Android'),
        ('ios', 'iOS')
    )

    user = models.ForeignKey(User)
    lat = models.FloatField()
    lon = models.FloatField()
    device_id = models.CharField(blank=True, max_length=25)
    device_manufacturer = models.CharField(blank=True, max_length=50, null=True)
    device_model = models.CharField(blank=True, max_length=25, null=True)
    device_os = models.CharField(blank=True, max_length=25, null=True)
    device_type = models.CharField(blank=True, max_length=10, choices=DEVICE_TYPE_CHOICES)
    device_battery_level = models.IntegerField(blank=True, null=True)
    device_uptime = models.TimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    location = models.PointField(geography=True, srid=4326, default=Point(0.0, 0.0))

    def save(self, **kwargs):
        self.location = Point(self.lon, self.lat)
        super(GeoLocationTracker, self).save(**kwargs)
