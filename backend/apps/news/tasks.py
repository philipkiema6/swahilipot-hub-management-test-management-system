from background_task import background
@background(schedule=300)
def run_news_checks(): return None
