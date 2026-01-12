from celery_app import celery_app

# Example periodic schedule
celery_app.conf.beat_schedule = {
    "run-scheduled-task-every-30-seconds": {
        "task": "tasks.scheduled_task",
        "schedule": 30.0,
    }
}

if __name__ == "__main__":
    print("Beat schedule loaded (demo).")
