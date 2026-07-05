"""
Base Parser
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from models import SalesOrder


class BaseParser(ABC):
    """
    Base class for all customer parsers.
    """

    @abstractmethod
    def parse(self, text: str) -> SalesOrder:
        """
        Parse PDF text into SalesOrder.
        """
        raise NotImplementedError