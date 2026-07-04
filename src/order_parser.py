"""
order_parser.py
Parse sales order information from PDF text.
"""

from __future__ import annotations

import re

from logger import logger
from models import OrderItem, SalesOrder


class OrderParser:
    """
    Base parser.

    This version only extracts some common fields.
    Customer-specific parsers will be added later.
    """

    def parse(
        self,
        customer: str,
        text: str,
    ) -> SalesOrder:

        logger.info("Parsing order (%s)...", customer)

        order = SalesOrder()
        order.customer = customer

        order.po_no = self._find_po(text)
        order.currency = self._find_currency(text)

        logger.info("Parse completed.")

        return order

    @staticmethod
    def _find_po(text: str) -> str:

        patterns = [
            r"PO\s*[:#]?\s*([A-Za-z0-9\-]+)",
            r"Purchase\s*Order\s*[:#]?\s*([A-Za-z0-9\-]+)",
            r"P/O\s*[:#]?\s*([A-Za-z0-9\-]+)",
        ]

        for pattern in patterns:

            match = re.search(
                pattern,
                text,
                flags=re.IGNORECASE,
            )

            if match:
                return match.group(1)

        return ""

    @staticmethod
    def _find_currency(text: str) -> str:

        currencies = [
            "USD",
            "EUR",
            "CNY",
            "RMB",
            "VND",
            "JPY",
        ]

        text = text.upper()

        for currency in currencies:
            if currency in text:
                return currency

        return ""

    @staticmethod
    def create_item() -> OrderItem:
        """
        Create an empty order item.
        """
        return OrderItem()


if __name__ == "__main__":

    parser = OrderParser()

    order = parser.parse(
        "ABB",
        """
        Purchase Order: 4500012345
        Currency USD
        """,
    )

    print(order)