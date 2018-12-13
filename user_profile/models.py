# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
SALUTATION_CHOICES = (
    ('mr', 'Mr'),
    ('mrs', 'Mrs'),
    ('miss', 'Miss'),
    ('sir', 'Sir'),
    ('lady', 'Lady')
)

class BaseProfile(models.Model):
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    salutation = models.CharField(max_length=10, choices=SALUTATION_CHOICES)
    code = models.CharField(max_length=15)
    address = models.TextField()
    phone = models.CharField(max_length=25)
    police_certificate_code = models.CharField(max_length=30, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)


class Patient(BaseProfile):
    medical_symptomps = models.TextField()

    def __unicode__(self):
        return self.first_name + ' - ' + self.code

class MedicalOfficer(BaseProfile):
    MEDICAL_OFFICER_CHOICES = (
        ('doctor', 'Doctor'),
        ('psychologist', 'Psychologist'),
        ('physiotherapist', 'Physio Therapist')
    )

    role = models.CharField(max_length=30, choices=MEDICAL_OFFICER_CHOICES)
    skillset = models.TextField()

    def __unicode__(self):
        return self.first_name + ' - ' + self.code + ' - ' + self.role