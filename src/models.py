"""
models.py
Data models for SalesOrderAgent
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path


@dataclass(slots=True)
class OrderItem:
    """Single sales order item."""

    line_no: int = 0
    material_no: str = ""
    customer_material: str = ""
    description: str = ""

    quantity: float = 0.0
    unit: str = ""

    unit_price: float = 0.0
    amount: float = 0.0

    delivery_date: str = ""


@dataclass(slots=True)
class SalesOrder:
    """Sales order."""

    customer: str = ""

    order_no: str = ""
    po_no: str = ""

    order_date: str = ""
    currency: str = ""

    sold_to: str = ""
    ship_to: str = ""

    pdf_path: Path | None = None

    create_time: datetime = field(default_factory=datetime.now)

    items: list[OrderItem] = field(default_factory=list)

    def add_item(self, item: OrderItem) -> None:
        self.items.append(item)

    @property
    def item_count(self) -> int:
        return len(self.items)

    @property
    def total_qty(self) -> float:
        return sum(i.quantity for i in self.items)

    @property
    def total_amount(self) -> float:
        return sum(i.amount for i in self.items)