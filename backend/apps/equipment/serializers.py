from rest_framework import serializers
from .models import Equipment,EquipmentAuditLog
class EquipmentSerializer(serializers.ModelSerializer):
 class Meta: model=Equipment; fields='__all__'; read_only_fields=['owner']
class EquipmentAuditLogSerializer(serializers.ModelSerializer):
 class Meta: model=EquipmentAuditLog; fields='__all__'
