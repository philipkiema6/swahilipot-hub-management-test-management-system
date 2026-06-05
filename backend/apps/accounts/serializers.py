from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Role,Permission,ActivityLog,UserSession,PasswordResetToken
User=get_user_model()
class PermissionSerializer(serializers.ModelSerializer):
 class Meta: model=Permission; fields='__all__'
class RoleSerializer(serializers.ModelSerializer):
 class Meta: model=Role; fields='__all__'
class UserSerializer(serializers.ModelSerializer):
 class Meta: model=User; exclude=['password','groups','user_permissions']
class UserCreateSerializer(serializers.ModelSerializer):
 password=serializers.CharField(write_only=True)
 class Meta: model=User; fields=['id','email','password','first_name','last_name','role','phone_number','department','job_title','is_active']
 def create(self,v): p=v.pop('password'); return User.objects.create_user(password=p,**v)
class SHMSTokenObtainPairSerializer(TokenObtainPairSerializer):
 username_field=User.EMAIL_FIELD
 def validate(self,attrs):
  data=super().validate(attrs); data['user']=UserSerializer(self.user).data; return data
class ActivityLogSerializer(serializers.ModelSerializer):
 class Meta: model=ActivityLog; fields='__all__'
class UserSessionSerializer(serializers.ModelSerializer):
 class Meta: model=UserSession; fields='__all__'
class PasswordResetTokenSerializer(serializers.ModelSerializer):
 class Meta: model=PasswordResetToken; fields='__all__'
