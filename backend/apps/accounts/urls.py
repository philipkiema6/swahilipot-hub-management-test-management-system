from rest_framework.routers import DefaultRouter
from .views import *
router=DefaultRouter(); router.register('users',UserViewSet); router.register('roles',RoleViewSet); router.register('permissions',PermissionViewSet); router.register('activity-logs',ActivityLogViewSet); router.register('sessions',UserSessionViewSet)
urlpatterns=router.urls
