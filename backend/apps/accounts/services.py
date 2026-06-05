from .models import ActivityLog
def log_activity(user,action,module,**kw): return ActivityLog.objects.create(user=user,action=action,module=module,**kw)
