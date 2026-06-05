from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet,ArticleAuditLogViewSet
router=DefaultRouter(); router.register('',ArticleViewSet,basename='news'); router.register('audit-logs',ArticleAuditLogViewSet,basename='news-audit')
urlpatterns=router.urls
