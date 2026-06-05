import uuid
from django.conf import settings
from django.db import models
from django.utils import timezone
class ShootRequest(models.Model):
 class Status(models.TextChoices): DRAFT='draft','Draft'; PENDING='pending','Pending'; ACTIVE='active','Active'; APPROVED='approved','Approved'; RESOLVED='resolved','Resolved'; CLOSED='closed','Closed'; ARCHIVED='archived','Archived'
 id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False); owner=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,blank=True,related_name='videography_records'); title=models.CharField(max_length=220); description=models.TextField(blank=True); status=models.CharField(max_length=30,choices=Status.choices,default=Status.ACTIVE,db_index=True); file=models.FileField(upload_to='videography/%Y/%m/',null=True,blank=True); starts_at=models.DateTimeField(null=True,blank=True); ends_at=models.DateTimeField(null=True,blank=True); metadata=models.JSONField(default=dict,blank=True); created_at=models.DateTimeField(default=timezone.now,db_index=True); updated_at=models.DateTimeField(auto_now=True)
 class Meta: ordering=['-created_at']; indexes=[models.Index(fields=['status','created_at'])]
 def __str__(self): return self.title
class ShootRequestAuditLog(models.Model):
 id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False); record=models.ForeignKey(ShootRequest,on_delete=models.CASCADE,related_name='audit_logs'); actor=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,blank=True); action=models.CharField(max_length=60); metadata=models.JSONField(default=dict,blank=True); created_at=models.DateTimeField(default=timezone.now)
