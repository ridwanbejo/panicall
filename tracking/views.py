# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from .serializers import GeoLocationTrackerSerializer
from .models import GeoLocationTracker
from .permissions import GeoLocationTrackerPermission


import json

# Create your views here.

class GeoLocationTrackerViewSet(viewsets.ModelViewSet):
    queryset = GeoLocationTracker.objects.all().order_by('-id')
    serializer_class = GeoLocationTrackerSerializer
    permission_classes = (GeoLocationTrackerPermission,)