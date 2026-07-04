"""
Base parser.
"""

from abc import ABC, abstractmethod

from models import SalesOrder


class BaseParser(ABC):

    @abstractmethod
    def parse(self, text: str) -> SalesOrder:
        pass