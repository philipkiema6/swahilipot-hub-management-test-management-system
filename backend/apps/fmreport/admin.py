from django.contrib import admin
from .models import FMStatusReport,FMStatusReportAuditLog
admin.site.register([FMStatusReport,FMStatusReportAuditLog])
