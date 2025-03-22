from datetime import datetime
from app.core.celery_app import celery_app
from app.core.logger import log_task_execution


@celery_app.task
def log_task():
    """Log task execution date and time."""
    task_name = "log_task"
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_task_execution(f"{task_name} - Executed at {now}")
    return f"Task '{task_name}' executed at {now}"
