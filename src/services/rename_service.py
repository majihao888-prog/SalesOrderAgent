"""
Rename PDF by PO Number
"""

from __future__ import annotations

from pathlib import Path

from logger import logger


class RenameService:

    @staticmethod
    def rename(pdf: Path, po_no: str) -> Path:

        if not po_no:
            logger.warning("PO Number empty.")
            return pdf

        target = pdf.with_name(f"{po_no}.pdf")

        index = 2

        while target.exists():

            target = pdf.with_name(
                f"{po_no}_{index}.pdf"
            )

            index += 1

        pdf.rename(target)

        logger.info(
            "Rename: %s -> %s",
            pdf.name,
            target.name,
        )

        return target