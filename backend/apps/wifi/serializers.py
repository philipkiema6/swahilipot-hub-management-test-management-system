from rest_framework import serializers
from .models import WifiAccessRequest,WifiAccessRequestAuditLog
class WifiAccessRequestSerializer(serializers.ModelSerializer):
 class Meta: model=WifiAccessRequest; fields='__all__'; read_only_fields=['owner']
class WifiAccessRequestAuditLogSerializer(serializers.ModelSerializer):
 class Meta: model=WifiAccessRequestAuditLog; fields='__all__'
