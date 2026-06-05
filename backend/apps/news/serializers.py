from rest_framework import serializers
from .models import Article,ArticleAuditLog
class ArticleSerializer(serializers.ModelSerializer):
 class Meta: model=Article; fields='__all__'; read_only_fields=['owner']
class ArticleAuditLogSerializer(serializers.ModelSerializer):
 class Meta: model=ArticleAuditLog; fields='__all__'
