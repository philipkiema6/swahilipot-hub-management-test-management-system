from django.contrib import admin
from .models import Ticket,TicketAuditLog
admin.site.register([Ticket,TicketAuditLog])
