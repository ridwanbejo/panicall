# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *


# Register your models here.
# class BaseProfileAdmin (admin.ModelAdmin):
#     list_display = ['user', 'phone']
#     search_fields = ['user', 'phone']
#     list_per_page = 25

# admin.site.register(BaseProfile, BaseProfileAdmin)

class PatientAdmin (admin.ModelAdmin):
    list_display = ['user', 'medical_symptomps']
    search_fields = ['user', 'medical_symptomps']
    list_per_page = 25

admin.site.register(Patient, PatientAdmin)

class MedicalOfficerAdmin (admin.ModelAdmin):
    list_display = ['user', 'role', 'skillset']
    search_fields = ['user', 'skillset']
    list_per_page = 25

admin.site.register(MedicalOfficer, MedicalOfficerAdmin)