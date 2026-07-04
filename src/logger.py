"""
logger.py
Logging module for SalesOrderAgent
"""

from __future__ import annotations

import logging
from logging.handlers import RotatingFileHandler

from app_config import LOG_DIR, SETTINGS


LOG_FILE = LOG_DIR / "SalesOrderAgent.log"


def get_logger(name: str = "SalesOrderAgent") -> logging.Logger:
    """
    Create and return a singleton logger.
    """

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    level_name = SETTINGS.get("log_level", "INFO").upper()
    level = getattr(logging, level_name, logging.INFO)

    logger.setLevel(level)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # File Handler
    file_handler = RotatingFileHandler(
        filename=LOG_FILE,
        maxBytes=5 * 1024 * 1024,
        backupCount=5,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger.propagate = False

    return logger


logger = get_logger()