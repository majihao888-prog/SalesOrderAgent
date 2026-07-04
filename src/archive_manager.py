"""
archive_manager.py
Move processed PDF files.
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from shutil import move

from app_config import ARCHIVE_DIR, FAILED_DIR
from logger import logger


class ArchiveManager:
    """
    Archive processed PDF files.
    """

    @staticmethod
    def archive(pdf_file: Path) -> Path:
        """
        Move successful PDF to archive/YYYYMMDD/.
        """

        today = datetime.now().strftime("%Y%m%d")

        target_dir = ARCHIVE_DIR / today
        target_dir.mkdir(parents=True, exist_ok=True)

        target_file = target_dir / pdf_file.name

        move(str(pdf_file), str(target_file))

        logger.info(
            "Archived: %s -> %s",
            pdf_file.name,
            target_file,
        )

        return target_file

    @staticmethod
    def failed(
        pdf_file: Path,
        reason: str = "",
    ) -> Path:
        """
        Move failed PDF to failed/YYYYMMDD/.
        """

        today = datetime.now().strftime("%Y%m%d")

        target_dir = FAILED_DIR / today
        target_dir.mkdir(parents=True, exist_ok=True)

        target_file = target_dir / pdf_file.name

        move(str(pdf_file), str(target_file))

        logger.error(
            "Failed: %s (%s)",
            pdf_file.name,
            reason,
        )

        return target_file