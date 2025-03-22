from celery import Celery
from app.core.config import settings

# Load environment variables
CELERY_BROKER_URL = settings.CELERY_RESULT_BACKEND
CELERY_BACKEND_URL = settings.CELERY_RESULT_BACKEND

# Create Celery instance
celery_app = Celery(
    "app",
    broker=CELERY_BROKER_URL,
    backend=CELERY_BACKEND_URL,
    include=["app.task.logging_task"],
)

# Celery configuration
celery_app.conf.update(
    timezone="UTC",
    enable_utc=True,
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
)


celery_app.conf.beat_schedule = {
    "log-task-every-6-hours": {
        "task": "app.task.logging_task.log_task",
        "schedule": 1,
    },
}
