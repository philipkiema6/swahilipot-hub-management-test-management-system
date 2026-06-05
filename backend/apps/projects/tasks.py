from background_task import background
@background(schedule=300)
def run_projects_checks(): return None
