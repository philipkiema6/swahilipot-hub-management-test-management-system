from django.contrib import admin
from .models import CallRecording,CallRecordingAuditLog
admin.site.register([CallRecording,CallRecordingAuditLog])
