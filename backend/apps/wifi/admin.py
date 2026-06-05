from django.contrib import admin
from .models import WifiAccessRequest,WifiAccessRequestAuditLog
admin.site.register([WifiAccessRequest,WifiAccessRequestAuditLog])
