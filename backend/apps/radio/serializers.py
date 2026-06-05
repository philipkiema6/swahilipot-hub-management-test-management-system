from rest_framework import serializers
from .models import RadioShow,RadioShowAuditLog
class RadioShowSerializer(serializers.ModelSerializer):
 class Meta: model=RadioShow; fields='__all__'; read_only_fields=['owner']
class RadioShowAuditLogSerializer(serializers.ModelSerializer):
 class Meta: model=RadioShowAuditLog; fields='__all__'
