from rest_framework.routers import DefaultRouter
from .views import EquipmentViewSet,EquipmentAuditLogViewSet
router=DefaultRouter(); router.register('',EquipmentViewSet,basename='equipment'); router.register('audit-logs',EquipmentAuditLogViewSet,basename='equipment-audit')
urlpatterns=router.urls
