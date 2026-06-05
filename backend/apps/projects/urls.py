from rest_framework.routers import DefaultRouter
from .views import ProjectSubmissionViewSet,ProjectSubmissionAuditLogViewSet
router=DefaultRouter(); router.register('',ProjectSubmissionViewSet,basename='projects'); router.register('audit-logs',ProjectSubmissionAuditLogViewSet,basename='projects-audit')
urlpatterns=router.urls
