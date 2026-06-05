from background_task import background
@background(schedule=300)
def expire_old_sessions(): return None
