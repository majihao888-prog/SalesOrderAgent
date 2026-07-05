"""
Rename PDF Service
"""

from __future__ import annotations

import shutil
from pathlib import Path

from app_config import ARCHIVE_DIR
from models import SalesOrder
from logger import logger


class RenameService:

    def rename(
        self,
        pdf: Path,
        order: SalesOrder,
    ) -> Path:
        """
        Rename and move PDF to archive.

        archive/
            2026/
                ATB/
                    ATB_B72175221.pdf
        """

        # 年份
        year = "UNKNOWN"

        if order.order_date:

            try:
                year = order.order_date.split(".")[-1]
            except Exception:
                pass

        # 客户
        customer = order.customer or "UNKNOWN"

        # PO
        po = order.po_no or pdf.stem

        target_dir = (
            ARCHIVE_DIR
            / year
            / customer
        )

        target_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        target_file = target_dir / f"{customer}_{po}.pdf"

        # 如果重名
        index = 1

        while target_file.exists():

            target_file = (
                target_dir
                / f"{customer}_{po}_{index}.pdf"
            )

            index += 1

        shutil.move(
            str(pdf),
            str(target_file),
        )

        logger.info(
            f"Rename -> {target_file.name}"
        )

        return target_file