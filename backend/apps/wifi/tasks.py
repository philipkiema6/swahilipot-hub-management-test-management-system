from background_task import background
@background(schedule=300)
def run_wifi_checks(): return None
