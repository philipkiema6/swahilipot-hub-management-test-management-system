from django.contrib import admin
from .models import FileTransfer,FileTransferAuditLog
admin.site.register([FileTransfer,FileTransferAuditLog])
