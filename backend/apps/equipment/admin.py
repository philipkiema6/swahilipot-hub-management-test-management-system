from django.contrib import admin
from .models import Equipment,EquipmentAuditLog
admin.site.register([Equipment,EquipmentAuditLog])
