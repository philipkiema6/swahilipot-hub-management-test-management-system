from rest_framework import serializers
from .models import ProjectSubmission,ProjectSubmissionAuditLog
class ProjectSubmissionSerializer(serializers.ModelSerializer):
 class Meta: model=ProjectSubmission; fields='__all__'; read_only_fields=['owner']
class ProjectSubmissionAuditLogSerializer(serializers.ModelSerializer):
 class Meta: model=ProjectSubmissionAuditLog; fields='__all__'
