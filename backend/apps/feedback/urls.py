from rest_framework.routers import DefaultRouter
from .views import TicketViewSet,TicketAuditLogViewSet
router=DefaultRouter(); router.register('',TicketViewSet,basename='feedback'); router.register('audit-logs',TicketAuditLogViewSet,basename='feedback-audit')
urlpatterns=router.urls
