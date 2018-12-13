# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EmergencyTeamSerializer, EmergencyCallSerializer
from .models import EmergencyTeam, EmergencyCall
from .permissions import EmergencyTeamPermission, EmergencyCallPermission
from rest_framework.response import Response
from rest_framework import status
from user_profile.models import MedicalOfficer, Patient
from random import randint

import json
import uuid

# Create your views here.

class EmergencyTeamViewSet(viewsets.ModelViewSet):
    queryset = EmergencyTeam.objects.all().order_by('-id')
    serializer_class = EmergencyTeamSerializer
    permission_classes = (EmergencyTeamPermission,)


class EmergencyCallViewSet(viewsets.ModelViewSet):
    queryset = EmergencyCall.objects.all().order_by('-id')
    serializer_class = EmergencyCallSerializer
    permission_classes = (EmergencyCallPermission,)

    def retrieve(self, request, *args, **kwargs):
        emergency_call = EmergencyCall.objects.filter(patient__user__id=request.user.id).filter(call_status='onprogress')
        emergency_call_count = emergency_call.count()

        if emergency_call_count < 1:
            doctor = MedicalOfficer.objects.filter(role='doctor').order_by('?').first()
            psychologist = MedicalOfficer.objects.filter(role='psychologist').order_by('?').first()

            doctor_distance = randint(0, 1000)
            psychologist_distance = randint(0, 1000)

            new_emergency_call = EmergencyCall(
                patient = Patient.objects.get(user=request.user),
                call_status = 'onprogress',
                evidence_lat = float(randint(48, 58)),
                evidence_lon = float(randint(48, 58)),
                evidence_place = '',
                emergency_call_code='EC-'+str(uuid.uuid4())[0:8].upper()
            )

            new_emergency_call.save()

            team_member_1 = EmergencyTeam(
                emergency_call_code = new_emergency_call,
                officer = doctor,
                last_lat = float(randint(48, 58)),
                last_lon = float(randint(48, 58)),
                status =  'accept',
                distance_to_patient = doctor_distance
            )

            team_member_1.save()

            team_member_2 = EmergencyTeam(
                emergency_call_code = new_emergency_call,
                officer = psychologist,
                last_lat = float(randint(48, 58)),
                last_lon = float(randint(48, 58)),
                status =  'accept',
                distance_to_patient = psychologist_distance
            )

            team_member_2.save()

            medics = EmergencyTeam.objects.filter(emergency_call_code=emergency_call.first())
            return Response({"message":"ok", "data": EmergencyTeamSerializer(medics, many=True).data},  status.HTTP_200_OK)

        else:

            medics = EmergencyTeam.objects.filter(emergency_call_code=emergency_call.first())
            return Response({"message":"already created", "data": EmergencyTeamSerializer(medics, many=True).data},  status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        """
        1. Find the nearest doctor and psychologist within radius 1000 meters
        2. Check if the doctor and psychologist is not assign to any team (not accept status in emergency team)
        3. Assign the doctor or psychologist to the emergency call with status waiting
        4. emergency call will be on progress if one member of the team accept the call
        """

        print "creating the emergency call and team"