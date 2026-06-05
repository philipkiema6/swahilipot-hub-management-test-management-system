from django.db.models import Count
from rest_framework import viewsets,decorators,response
from .models import WifiAccessRequest,WifiAccessRequestAuditLog
from .serializers import WifiAccessRequestSerializer,WifiAccessRequestAuditLogSerializer
from .permissions import CanManageWifiAccessRequest
from .services import export_csv
class WifiAccessRequestViewSet(viewsets.ModelViewSet):
 queryset=WifiAccessRequest.objects.all(); serializer_class=WifiAccessRequestSerializer; permission_classes=[CanManageWifiAccessRequest]; filterset_fields=['status','owner']; search_fields=['title','description']; ordering_fields=['created_at','updated_at','status']
 def perform_create(self,serializer): serializer.save(owner=self.request.user)
 @decorators.action(detail=False,methods=['get'])
 def stats(self,request): return response.Response({'total':self.get_queryset().count(),'by_status':list(self.get_queryset().values('status').annotate(count=Count('id')))})
 @decorators.action(detail=False,methods=['get'],url_path='export-csv')
 def export(self,request): return export_csv(self.filter_queryset(self.get_queryset()))
class WifiAccessRequestAuditLogViewSet(viewsets.ReadOnlyModelViewSet): queryset=WifiAccessRequestAuditLog.objects.all(); serializer_class=WifiAccessRequestAuditLogSerializer; permission_classes=[CanManageWifiAccessRequest]
