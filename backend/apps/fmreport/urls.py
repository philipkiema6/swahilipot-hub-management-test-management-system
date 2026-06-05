from rest_framework.routers import DefaultRouter
from .views import FMStatusReportViewSet,FMStatusReportAuditLogViewSet
router=DefaultRouter(); router.register('',FMStatusReportViewSet,basename='fmreport'); router.register('audit-logs',FMStatusReportAuditLogViewSet,basename='fmreport-audit')
urlpatterns=router.urls
