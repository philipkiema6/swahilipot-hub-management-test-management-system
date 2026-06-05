from rest_framework import serializers
from .models import Ticket,TicketAuditLog
class TicketSerializer(serializers.ModelSerializer):
 class Meta: model=Ticket; fields='__all__'; read_only_fields=['owner']
class TicketAuditLogSerializer(serializers.ModelSerializer):
 class Meta: model=TicketAuditLog; fields='__all__'
