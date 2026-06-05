from rest_framework import serializers
class KpiSerializer(serializers.Serializer): key=serializers.CharField(); label=serializers.CharField(); value=serializers.IntegerField()
