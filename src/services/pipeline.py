"""
SalesOrder Processing Pipeline
"""

from logger import logger
from utils import find_pdf_files
from pdf_reader import PDFReader
from customer_detector import CustomerDetector


class Pipeline:

    def __init__(self):
        self.reader = PDFReader()
        self.detector = CustomerDetector()

    def run(self):

        pdfs = find_pdf_files()

        if not pdfs:
            logger.info("No PDF files found.")
            return

        for pdf in pdfs:

            logger.info(f"Processing {pdf.name}")

            try:

                text = self.reader.read(pdf)

                customer = self.detector.detect(text)

                logger.info(f"Customer: {customer}")

            except Exception as e:

                logger.exception(e)