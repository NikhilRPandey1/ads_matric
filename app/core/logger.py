import logging
import os

LOG_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "logs"))
LOG_FILE = os.path.join(LOG_DIR, "task_log.log")

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logger = logging.getLogger("task_logger")
logger.setLevel(logging.INFO)

if not logger.handlers:
    handler = logging.FileHandler(LOG_FILE)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)


def log_task_execution(task_name: str):
    logger.info(f"Task '{task_name}' executed successfully.")
    logger.handlers[0].flush()
