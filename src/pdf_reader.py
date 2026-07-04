"""
pdf_reader.py
SalesOrderAgent PDF Reader
"""

from __future__ import annotations

from pathlib import Path

from pypdf import PdfReader

from app_config import OUTPUT_DIR
from logger import logger


class PDFReader:

    def __init__(self):

        self.debug_dir = OUTPUT_DIR / "debug"
        self.debug_dir.mkdir(parents=True, exist_ok=True)

    def read(self, pdf: Path) -> str:

        logger.info("Reading PDF: %s", pdf.name)

        reader = PdfReader(str(pdf))

        texts = []

        page_count = len(reader.pages)

        logger.info("Total Pages : %d", page_count)

        for index, page in enumerate(reader.pages, start=1):

            try:

                text = page.extract_text()

                if text:

                    texts.append(text)

                    logger.info(
                        "Page %d : %d chars",
                        index,
                        len(text),
                    )

                else:

                    logger.warning(
                        "Page %d is empty.",
                        index,
                    )

            except Exception as e:

                logger.exception(e)

        result = "\n".join(texts)

        logger.info(
            "Total Characters : %d",
            len(result),
        )

        self.save_debug_text(
            pdf,
            result,
        )

        return result

    def save_debug_text(
        self,
        pdf: Path,
        text: str,
    ) -> None:

        txt = self.debug_dir / f"{pdf.stem}.txt"

        txt.write_text(
            text,
            encoding="utf-8",
        )

        logger.info(
            "Debug text saved: %s",
            txt.name,
        )