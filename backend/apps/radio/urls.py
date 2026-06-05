from rest_framework.routers import DefaultRouter
from .views import RadioShowViewSet,RadioShowAuditLogViewSet
router=DefaultRouter(); router.register('',RadioShowViewSet,basename='radio'); router.register('audit-logs',RadioShowAuditLogViewSet,basename='radio-audit')
urlpatterns=router.urls
