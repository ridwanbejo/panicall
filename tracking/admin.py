# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.forms.widgets import TextInput
from .models import *


# Register your models here.
class GeoLocationTrackerAdmin (admin.ModelAdmin):
    formfield_overrides = {
        models.PointField: {'widget': TextInput},
    }

    list_display = ['user', 'lat', 'lon', 'location', 'device_id', 'device_type', 'created_at']
    list_per_page = 25

admin.site.register(GeoLocationTracker, GeoLocationTrackerAdmin)