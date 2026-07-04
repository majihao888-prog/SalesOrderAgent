"""
ATB Parser
"""

import re

from models import SalesOrder, OrderItem
from .base_parser import BaseParser


class ATBParser(BaseParser):

    def parse(self, text: str) -> SalesOrder:

        order = SalesOrder()

        order.customer = "ATB"

        # PO
        m = re.search(
            r"Order No\.\s+([A-Z0-9]+)",
            text,
        )

        if m:
            order.po_no = m.group(1)

        # Currency

        m = re.search(
            r"Currency\s+([A-Z]+)",
            text,
        )

        if m:
            order.currency = m.group(1)

        # Date

        m = re.search(
            r"Date\s+(\d+\.\d+\.\d+)",
            text,
        )

        if m:
            order.order_date = m.group(1)

        # Material

        m = re.search(
            r"\d+\s+([A-Z0-9]+)\s+\d",
            text,
        )

        if m:

            item = OrderItem()

            item.material_no = m.group(1)

            order.items.append(item)

        return order