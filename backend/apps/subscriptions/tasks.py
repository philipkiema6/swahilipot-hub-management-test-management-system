from background_task import background
@background(schedule=300)
def run_subscriptions_checks(): return None
