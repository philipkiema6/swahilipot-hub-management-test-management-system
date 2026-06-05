from django.contrib import admin
from .models import ProjectSubmission,ProjectSubmissionAuditLog
admin.site.register([ProjectSubmission,ProjectSubmissionAuditLog])
