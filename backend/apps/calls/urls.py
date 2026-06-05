from rest_framework.routers import DefaultRouter
from .views import CallRecordingViewSet,CallRecordingAuditLogViewSet
router=DefaultRouter(); router.register('',CallRecordingViewSet,basename='calls'); router.register('audit-logs',CallRecordingAuditLogViewSet,basename='calls-audit')
urlpatterns=router.urls
