"""
ATB Parser
"""

from __future__ import annotations

import re

from models import SalesOrder, OrderItem
from .base_parser import BaseParser


class ATBParser(BaseParser):

    def _to_float(self, value: str) -> float:
        """
        Convert European number format.

        Examples
        --------
        27.518,40 -> 27518.40
        96,000 -> 96
        """

        if not value:
            return 0

        value = value.strip()

        # 数量
        if "," in value and "." not in value:
            parts = value.split(",")

            if len(parts[-1]) == 3:
                value = parts[0]

            else:
                value = value.replace(",", ".")

        # 金额
        elif "." in value and "," in value:
            value = value.replace(".", "")
            value = value.replace(",", ".")

        try:
            return float(value)

        except Exception:
            return 0

    def parse(self, text: str) -> SalesOrder:

        order = SalesOrder()

        order.customer = "ATB"

        # ----------------------------
        # PO
        # ----------------------------

        m = re.search(
            r"Order No\.\s+([A-Z0-9]+)",
            text,
            re.IGNORECASE,
        )

        if m:
            order.po_no = m.group(1)

        # ----------------------------
        # Order Date
        # ----------------------------

        m = re.search(
            r"Date\s+(\d+\.\d+\.\d+)",
            text,
            re.IGNORECASE,
        )

        if m:
            order.order_date = m.group(1)

        # ----------------------------
        # Currency
        # ----------------------------

        m = re.search(
            r"Currency\s+([A-Z]{3})",
            text,
            re.IGNORECASE,
        )

        if m:
            order.currency = m.group(1)

        # ----------------------------
        # Total Amount
        # ----------------------------

        m = re.search(
            r"Total Amount\s+[A-Z]+\s+([\d.,]+)",
            text,
            re.IGNORECASE,
        )

        if m:
            order.total_amount = self._to_float(
                m.group(1)
            )

        # ----------------------------
        # Item
        # ----------------------------

        pattern = re.compile(
            r"""
            \d+\s+
            ([A-Z0-9]+)          # Material

            \s+

            ([\d.,]+)            # Qty

            \s+/([A-Z]+)         # Unit

            \s+

            ([\d.,]+)            # Unit Price

            \s+\d+\s+[A-Z]+\s+

            ([\d.,]+)            # Amount

            .*?

            \n

            (.*?)                # Description

            \n

            Delivery\s+date:\s*

            (\d+\.\d+\.\d+)      # Delivery
            """,
            re.VERBOSE | re.DOTALL,
        )

        m = pattern.search(text)

        if m:

            item = OrderItem()

            item.material_no = m.group(1)

            item.quantity = self._to_float(
                m.group(2)
            )

            item.unit = m.group(3)

            item.unit_price = self._to_float(
                m.group(4)
            )

            item.amount = self._to_float(
                m.group(5)
            )

            item.description = m.group(6).strip()

            item.delivery_date = m.group(7)

            order.items.append(item)

        return order