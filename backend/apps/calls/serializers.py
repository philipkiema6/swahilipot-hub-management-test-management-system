from rest_framework import serializers
from .models import CallRecording,CallRecordingAuditLog
class CallRecordingSerializer(serializers.ModelSerializer):
 class Meta: model=CallRecording; fields='__all__'; read_only_fields=['owner']
class CallRecordingAuditLogSerializer(serializers.ModelSerializer):
 class Meta: model=CallRecordingAuditLog; fields='__all__'
