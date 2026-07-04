"""
customer_detector.py
Customer template detector.
"""

from __future__ import annotations

from pathlib import Path

from logger import logger


class CustomerDetector:
    """
    Detect customer by PDF text.
    """

    def __init__(self) -> None:
        self.rules = {
            "ABB": [
                "ABB",
                "Purchase Order",
                "Ship To",
            ],
            "SIEMENS": [
                "SIEMENS",
                "Siemens",
            ],
            "SCHNEIDER": [
                "SCHNEIDER",
                "Schneider Electric",
            ],
            "GE": [
                "GENERAL ELECTRIC",
                "GE",
            ],
        }

    def detect(self, text: str) -> str:
        """
        Detect customer name.
        """

        text_upper = text.upper()

        for customer, keywords in self.rules.items():

            matched = 0

            for keyword in keywords:

                if keyword.upper() in text_upper:
                    matched += 1

            if matched > 0:
                logger.info("Customer detected: %s", customer)
                return customer

        logger.warning("Unknown customer.")
        return "UNKNOWN"

    def register(
        self,
        customer: str,
        keywords: list[str],
    ) -> None:
        """
        Register a new customer template.
        """

        self.rules[customer.upper()] = keywords

        logger.info(
            "Register customer template: %s",
            customer,
        )


if __name__ == "__main__":

    detector = CustomerDetector()

    print(
        detector.detect(
            "ABB Purchase Order Ship To Vietnam"
        )
    )