# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *


# Register your models here.
class BranchOfficeAdmin (admin.ModelAdmin):
    list_display = ['name', 'address']
    search_fields = ['name', 'address']
    list_per_page = 25

admin.site.register(BranchOffice, BranchOfficeAdmin)

class BranchOfficeMemberAdmin (admin.ModelAdmin):
    list_display = ['medical_officer', 'office', 'created_at']
    list_per_page = 25

admin.site.register(BranchOfficeMember, BranchOfficeMemberAdmin)


class EmergencyCallAdmin (admin.ModelAdmin):
    list_display = ['emergency_call_code', 'patient', 'call_status', 'evidence_lat', 'evidence_lon', 'evidence_place', 'created_at']
    search_fields = ['emergency_call_code', 'evidence_place']
    list_per_page = 25

admin.site.register(EmergencyCall, EmergencyCallAdmin)

class EmergencyTeamAdmin (admin.ModelAdmin):
    list_display = ['emergency_call_code', 'officer', 'status', 'last_lat', 'last_lon', 'created_at']
    search_fields = ['emergency_call_code',]
    list_per_page = 25

admin.site.register(EmergencyTeam, EmergencyTeamAdmin)
