"""
Data Models
"""

from dataclasses import dataclass, field


@dataclass
class OrderItem:
    """
    One order line.
    """

    line_no: int = 0

    material_no: str = ""

    description: str = ""

    quantity: float = 0

    unit: str = ""

    unit_price: float = 0

    amount: float = 0

    delivery_date: str = ""


@dataclass
class SalesOrder:
    """
    Parsed Sales Order.
    """

    customer: str = ""

    po_no: str = ""

    order_date: str = ""

    currency: str = ""

    buyer: str = ""

    supplier: str = ""

    payment_terms: str = ""

    incoterms: str = ""

    total_amount: float = 0

    items: list[OrderItem] = field(default_factory=list)