"""
SalesOrder Processing Pipeline
"""

from logger import logger
from utils import find_pdf_files

from pdf_reader import PDFReader
from customer_detector import CustomerDetector

from parsers.parser_factory import ParserFactory

from services.rename_service import RenameService
from services.summary_service import SummaryService


class Pipeline:

    def __init__(self):

        self.reader = PDFReader()

        self.detector = CustomerDetector()

        self.renamer = RenameService()

        self.summary = SummaryService()

    def run(self):

        pdfs = find_pdf_files()

        if not pdfs:

            logger.info("No PDF files found.")

            return

        logger.info(f"Found {len(pdfs)} PDF(s).")

        for pdf in pdfs:

            logger.info("=" * 60)

            logger.info(f"Processing : {pdf.name}")

            try:

                # --------------------------------------------------
                # Read PDF
                # --------------------------------------------------

                text = self.reader.read(pdf)

                # --------------------------------------------------
                # Detect Customer
                # --------------------------------------------------

                customer = self.detector.detect(text)

                logger.info(f"Customer : {customer}")

                # --------------------------------------------------
                # Parser
                # --------------------------------------------------

                parser = ParserFactory.create(customer)

                order = parser.parse(text)

                # 防止Parser没有写customer
                if not order.customer:
                    order.customer = customer

                logger.info(
                    f"PO : {order.po_no}"
                )

                logger.info(
                    f"Items : {len(order.items)}"
                )

                # --------------------------------------------------
                # Rename PDF
                # --------------------------------------------------

                new_pdf = self.renamer.rename(
                    pdf,
                    order,
                )

                logger.info(
                    f"Archive : {new_pdf}"
                )

                # --------------------------------------------------
                # Write Summary
                # --------------------------------------------------

                self.summary.append(
                    order,
                    new_pdf,
                )

                logger.info(
                    "Summary Updated."
                )

            except Exception as e:

                logger.exception(e)

                logger.error(
                    f"Failed : {pdf.name}"
                )

        logger.info("=" * 60)

        logger.info("Pipeline Finished.")