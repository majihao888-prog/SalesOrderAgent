"""
Order Summary Service
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

from openpyxl import Workbook, load_workbook

from app_config import OUTPUT_DIR
from logger import logger
from models import SalesOrder


SUMMARY_FILE = OUTPUT_DIR / "OrderSummary.xlsx"


class SummaryService:

    def __init__(self):

        self.file = SUMMARY_FILE

        if not self.file.exists():
            self.create_workbook()

    def create_workbook(self):

        wb = Workbook()

        ws = wb.active
        ws.title = "Orders"

        ws.append([
            "PO",
            "Customer",
            "OrderDate",
            "Currency",
            "PDF",
            "ImportTime",
            "FileHash"
        ])

        item_ws = wb.create_sheet("Items")

        item_ws.append([
            "PO",
            "Line",
            "Material",
            "Description",
            "Qty",
            "Unit",
            "Price",
            "Amount",
            "DeliveryDate"
        ])

        wb.save(self.file)

        logger.info("Create OrderSummary.xlsx")

    def append_order(
        self,
        order: SalesOrder,
        pdf_name: str,
        file_hash: str = "",
    ):

        wb = load_workbook(self.file)

        ws = wb["Orders"]

        ws.append([
            order.po_no,
            order.customer,
            order.order_date,
            order.currency,
            pdf_name,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            file_hash
        ])

        item_ws = wb["Items"]

        for index, item in enumerate(order.items, start=1):

            item_ws.append([
                order.po_no,
                index,
                item.material_no,
                item.description,
                item.quantity,
                item.unit,
                item.unit_price,
                item.amount,
                item.delivery_date
            ])

        wb.save(self.file)

        logger.info(
            "Order %s saved.",
            order.po_no,
        )