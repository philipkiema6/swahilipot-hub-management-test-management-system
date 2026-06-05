from django.contrib import admin
from .models import Article,ArticleAuditLog
admin.site.register([Article,ArticleAuditLog])
