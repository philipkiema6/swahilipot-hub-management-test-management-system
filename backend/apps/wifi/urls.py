from rest_framework.routers import DefaultRouter
from .views import WifiAccessRequestViewSet,WifiAccessRequestAuditLogViewSet
router=DefaultRouter(); router.register('',WifiAccessRequestViewSet,basename='wifi'); router.register('audit-logs',WifiAccessRequestAuditLogViewSet,basename='wifi-audit')
urlpatterns=router.urls
