"""
logger.py
统一日志模块

整个项目统一调用：
    from logger import get_logger

    logger = get_logger(__name__)
    logger.info("message")
"""

from pathlib import Path
import logging

from config import LOG_DIR


def get_logger(name: str = "SalesOrderAgent") -> logging.Logger:
    """
    创建并返回 Logger

    Args:
        name: Logger名称

    Returns:
        logging.Logger
    """

    LOG_DIR.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger(name)

    # 防止重复添加 Handler
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    file_handler = logging.FileHandler(
        LOG_DIR / "sales_order.log",
        encoding="utf-8",
    )

    console_handler = logging.StreamHandler()

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger