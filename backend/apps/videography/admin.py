from django.contrib import admin
from .models import ShootRequest,ShootRequestAuditLog
admin.site.register([ShootRequest,ShootRequestAuditLog])
