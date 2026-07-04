from config import ensure_directories
from logger import get_logger

ensure_directories()

logger = get_logger()

logger.info("SalesOrderAgent Started")