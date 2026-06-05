from rest_framework import serializers
from .models import ShootRequest,ShootRequestAuditLog
class ShootRequestSerializer(serializers.ModelSerializer):
 class Meta: model=ShootRequest; fields='__all__'; read_only_fields=['owner']
class ShootRequestAuditLogSerializer(serializers.ModelSerializer):
 class Meta: model=ShootRequestAuditLog; fields='__all__'
