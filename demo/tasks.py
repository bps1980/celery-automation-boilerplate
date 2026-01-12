from celery_app import celery_app
import time

@celery_app.task
def example_task(x, y):
    """
    Simple placeholder task.
    """
    print(f"Running example_task({x}, {y})")
    return x + y

@celery_app.task
def scheduled_task():
    """
    Placeholder scheduled task.
    """
    print("Running scheduled task...")
    time.sleep(1)
    return "done"
