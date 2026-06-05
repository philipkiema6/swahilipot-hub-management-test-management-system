import uuid
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.db import models
from django.conf import settings
from django.utils import timezone
class Stamp(models.Model):
 id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False); created_at=models.DateTimeField(default=timezone.now,db_index=True); updated_at=models.DateTimeField(auto_now=True)
 class Meta: abstract=True
class UserManager(BaseUserManager):
 def create_user(self,email,password=None,**kw):
  email=self.normalize_email(email); u=self.model(email=email,username=email,**kw); u.set_password(password); u.save(); return u
 def create_superuser(self,email,password=None,**kw): kw.update(is_staff=True,is_superuser=True); return self.create_user(email,password,**kw)
class Permission(Stamp):
 name=models.CharField(max_length=150); code=models.SlugField(max_length=140,unique=True); module=models.CharField(max_length=80,db_index=True); description=models.TextField(blank=True)
 def __str__(self): return self.code
class Role(Stamp):
 class RoleType(models.TextChoices): ADMIN='admin','Admin'; STAFF='staff','Staff'; ATTACHEE='attachee_intern','Attachee/Intern'; SUPERVISOR='supervisor','Supervisor'
 name=models.CharField(max_length=80,unique=True); role_type=models.CharField(max_length=30,choices=RoleType.choices,unique=True); permissions=models.ManyToManyField(Permission,blank=True); is_active=models.BooleanField(default=True)
 def __str__(self): return self.name
class User(AbstractUser):
 id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False); email=models.EmailField(unique=True,db_index=True); username=models.CharField(max_length=255,unique=True); role=models.ForeignKey(Role,on_delete=models.PROTECT,null=True,blank=True); phone_number=models.CharField(max_length=30,blank=True); department=models.CharField(max_length=120,blank=True); job_title=models.CharField(max_length=120,blank=True); avatar=models.ImageField(upload_to='avatars/',null=True,blank=True); last_activity_at=models.DateTimeField(null=True,blank=True); created_at=models.DateTimeField(default=timezone.now); updated_at=models.DateTimeField(auto_now=True)
 USERNAME_FIELD='email'; REQUIRED_FIELDS=['first_name','last_name']; objects=UserManager()
 @property
 def full_name(self): return self.get_full_name()
 def has_shms_permission(self,code): return self.is_superuser or bool(self.role and self.role.permissions.filter(code=code).exists())
class ActivityLog(Stamp):
 user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,blank=True); action=models.CharField(max_length=40); module=models.CharField(max_length=80); object_id=models.CharField(max_length=120,blank=True); description=models.TextField(blank=True); metadata=models.JSONField(default=dict,blank=True)
class UserSession(Stamp):
 user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE); refresh_token_jti=models.CharField(max_length=255,unique=True); expires_at=models.DateTimeField(); revoked_at=models.DateTimeField(null=True,blank=True)
class PasswordResetToken(Stamp):
 user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE); token_hash=models.CharField(max_length=255,unique=True); expires_at=models.DateTimeField(); used_at=models.DateTimeField(null=True,blank=True)
