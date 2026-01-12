from celery import Celery

def create_celery_app():
    """
    Minimal Celery application factory.
    This is a placeholder for a real Celery setup.
    """

    app = Celery(
        "demo_app",
        broker="redis://localhost:6379/0",
        backend="redis://localhost:6379/1"
    )

    # Load configuration
    app.conf.update(
        task_routes={
            "tasks.example_task": {"queue": "default"},
            "tasks.scheduled_task": {"queue": "scheduled"},
        },
        beat_schedule={}
    )

    return app

celery_app = create_celery_app()
