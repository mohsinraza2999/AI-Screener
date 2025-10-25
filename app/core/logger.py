import logging
from logging.handlers import RotatingFileHandler
import os

def get_logger(name, log_file='app.log'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # File handler with rotation
    file_handler = RotatingFileHandler(log_file, maxBytes=5_000_000, backupCount=3)
    file_handler.setFormatter(formatter)

    # Add handlers only once
    if not logger.hasHandlers():
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger


#Usage Example in Your Script

logger = get_logger(__name__)
logger.info("Starting CV parsing...")
logger.warning("Missing 'Experience' section in CV")
logger.error("Failed to connect to vector DB")
