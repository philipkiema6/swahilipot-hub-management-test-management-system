from django.contrib.auth import get_user_model
from rest_framework import viewsets,permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Role,Permission,ActivityLog,UserSession
from .permissions import IsAdminRole
from .serializers import *
User=get_user_model()
class SHMSTokenObtainPairView(TokenObtainPairView): serializer_class=SHMSTokenObtainPairSerializer
class UserViewSet(viewsets.ModelViewSet):
 queryset=User.objects.all(); serializer_class=UserSerializer; permission_classes=[IsAdminRole]; search_fields=['email','first_name','last_name']; filterset_fields=['role','is_active']
 def get_serializer_class(self): return UserCreateSerializer if self.action=='create' else UserSerializer
class RoleViewSet(viewsets.ModelViewSet): queryset=Role.objects.all(); serializer_class=RoleSerializer; permission_classes=[IsAdminRole]
class PermissionViewSet(viewsets.ModelViewSet): queryset=Permission.objects.all(); serializer_class=PermissionSerializer; permission_classes=[IsAdminRole]
class ActivityLogViewSet(viewsets.ReadOnlyModelViewSet): queryset=ActivityLog.objects.all(); serializer_class=ActivityLogSerializer; permission_classes=[IsAdminRole]
class UserSessionViewSet(viewsets.ReadOnlyModelViewSet): queryset=UserSession.objects.all(); serializer_class=UserSessionSerializer; permission_classes=[permissions.IsAuthenticated]
