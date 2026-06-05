from django.contrib import admin
from .models import SoftwareSubscription,SoftwareSubscriptionAuditLog
admin.site.register([SoftwareSubscription,SoftwareSubscriptionAuditLog])
