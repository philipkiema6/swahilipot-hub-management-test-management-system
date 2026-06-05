from rest_framework import serializers
from .models import SoftwareSubscription,SoftwareSubscriptionAuditLog
class SoftwareSubscriptionSerializer(serializers.ModelSerializer):
 class Meta: model=SoftwareSubscription; fields='__all__'; read_only_fields=['owner']
class SoftwareSubscriptionAuditLogSerializer(serializers.ModelSerializer):
 class Meta: model=SoftwareSubscriptionAuditLog; fields='__all__'
