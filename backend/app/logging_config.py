import logging
import os
from datetime import datetime
from typing import Optional

# Get release info from environment or file
RELEASE_ID = os.getenv("RELEASE_ID", "dev")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")


class ReleaseContextFilter(logging.Filter):
    """Add release context to all log records"""

    def filter(self, record):
        record.release_id = RELEASE_ID
        record.environment = ENVIRONMENT
        record.timestamp = datetime.utcnow().isoformat()
        return True


def setup_logging():
    """Configure logging with release context"""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] [%(environment)s] [%(release_id)s] %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Add release context filter to root logger
    root_logger = logging.getLogger()
    root_logger.addFilter(ReleaseContextFilter())

    return root_logger


def log_user_action(
    action: str, user_id: int, details: Optional[dict] = None, logger=None
):
    """Log user actions with context"""
    if logger is None:
        logger = logging.getLogger(__name__)

    log_data = {
        "action": action,
        "user_id": user_id,
        "release_id": RELEASE_ID,
        "environment": ENVIRONMENT,
        "timestamp": datetime.utcnow().isoformat(),
    }

    if details:
        log_data.update(details)

    logger.info(f"User action: {action}", extra=log_data)


# Initialize logging
logger = setup_logging()
