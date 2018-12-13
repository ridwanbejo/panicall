from rest_framework import serializers
from .models import GeoLocationTracker


class GeoLocationTrackerSerializer(serializers.ModelSerializer):

    class Meta:
        model = GeoLocationTracker
        fields = ('id', 'user', 'lat', 'lon', 'location', 'device_id', 'device_type', 'created_at')
        read_only_fields = ()
