from rest_framework.routers import DefaultRouter
from .views import FileTransferViewSet,FileTransferAuditLogViewSet
router=DefaultRouter(); router.register('',FileTransferViewSet,basename='filetransfer'); router.register('audit-logs',FileTransferAuditLogViewSet,basename='filetransfer-audit')
urlpatterns=router.urls
