from rest_framework.routers import DefaultRouter
from .views import ShootRequestViewSet,ShootRequestAuditLogViewSet
router=DefaultRouter(); router.register('',ShootRequestViewSet,basename='videography'); router.register('audit-logs',ShootRequestAuditLogViewSet,basename='videography-audit')
urlpatterns=router.urls
