from rest_framework import serializers
from .models import EmergencyCall, EmergencyTeam


class EmergencyTeamSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    phone = serializers.SerializerMethodField()
    role = serializers.SerializerMethodField()

    class Meta:
        model = EmergencyTeam
        fields = ('id', 'emergency_call_code', 'officer', 'username', 'last_lat', 'last_lon', 'status', 'distance_to_patient', 'email', 'phone', 'role', 'created_at')
        read_only_fields = ()

    def get_username(self, obj):
        return obj.officer.user.username

    def get_email(self, obj):
        return obj.officer.user.email

    def get_phone(self, obj):
        return obj.officer.phone

    def get_role(self, obj):
        return obj.officer.role

class EmergencyCallSerializer(serializers.ModelSerializer):
    medics = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()

    class Meta:
        model = EmergencyCall
        fields = ('id', 'emergency_call_code', 'patient', 'username', 'evidence_lat', 'evidence_lon', 'evidence_place', 'created_at', 'medics')
        read_only_fields = ()


    def get_medics(self, obj):
        medics = EmergencyTeam.objects.filter(emergency_call_code=obj)

        return EmergencyTeamSerializer(medics, many=True).data

    def get_username(self, obj):
        return obj.patient.user.username