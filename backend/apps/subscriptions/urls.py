from rest_framework.routers import DefaultRouter
from .views import SoftwareSubscriptionViewSet,SoftwareSubscriptionAuditLogViewSet
router=DefaultRouter(); router.register('',SoftwareSubscriptionViewSet,basename='subscriptions'); router.register('audit-logs',SoftwareSubscriptionAuditLogViewSet,basename='subscriptions-audit')
urlpatterns=router.urls
