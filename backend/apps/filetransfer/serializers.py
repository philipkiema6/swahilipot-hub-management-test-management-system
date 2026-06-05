from rest_framework import serializers
from .models import FileTransfer,FileTransferAuditLog
class FileTransferSerializer(serializers.ModelSerializer):
 class Meta: model=FileTransfer; fields='__all__'; read_only_fields=['owner']
class FileTransferAuditLogSerializer(serializers.ModelSerializer):
 class Meta: model=FileTransferAuditLog; fields='__all__'
