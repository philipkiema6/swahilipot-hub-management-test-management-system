from rest_framework import serializers
from .models import FMStatusReport,FMStatusReportAuditLog
class FMStatusReportSerializer(serializers.ModelSerializer):
 class Meta: model=FMStatusReport; fields='__all__'; read_only_fields=['owner']
class FMStatusReportAuditLogSerializer(serializers.ModelSerializer):
 class Meta: model=FMStatusReportAuditLog; fields='__all__'
