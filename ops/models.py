# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from user_profile. models import * 

# Create your models here.
class BranchOffice(models.Model):
    name = models.CharField(max_length=20)
    address = models.TextField(blank=True, null=True)


class BranchOfficeMember(models.Model):
    medical_officer = models.ForeignKey(MedicalOfficer)
    office = models.ForeignKey(BranchOffice)    
    created_at = models.DateTimeField(auto_now_add=True)


class EmergencyCall(models.Model):
    """
        - It should be success when at least 1 person willing to help the patient
        - on progress indicate that the emergency call still seeking the volunteer
        - done indicate when user resolve the call
        - fail indicate when no one volunteer are coming to the patient or the call is halted by the patient itself
    """

    CALL_STATUS_CHOICES = (
        ('onprogress', 'On Progress'),
        ('success', 'Success'),
        ('done', 'Done'),
        ('fail', 'Fail')
    )

    emergency_call_code = models.CharField(max_length=15)
    patient = models.ForeignKey(Patient)
    call_status = models.CharField(max_length=10, choices=CALL_STATUS_CHOICES)
    evidence_lat = models.FloatField()
    evidence_lon = models.FloatField()
    evidence_place = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.emergency_call_code + ' - ' + self.patient.code


class EmergencyTeam(models.Model):
    """
        - Emergency Call should has minimum 1 person who can help the patient
        - Ideally it should assign 2 person. 1 doctor and 1 psychologist
        - When someone cancel the call, check the remain team, if its only 1 person, EmergencyCall should be fail.
    """
    TEAM_CALL_STATUS_CHOICES = (
        ('accept', 'Accept'),
        ('waiting', 'Waiting'),
        ('cancel', 'Cancel')
    )
    emergency_call_code = models.ForeignKey(EmergencyCall)
    officer = models.ForeignKey(MedicalOfficer)
    last_lat = models.FloatField()
    last_lon = models.FloatField()
    distance_to_patient = models.FloatField()
    status =  models.CharField(max_length=10, choices=TEAM_CALL_STATUS_CHOICES, default='waiting')
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.emergency_call_code.emergency_call_code + ' - ' + self.officer.code
