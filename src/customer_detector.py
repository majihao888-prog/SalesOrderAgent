"""
customer_detector.py
Customer template detector.
"""

from __future__ import annotations

from logger import logger


class CustomerDetector:
    """
    Detect customer by PDF text.
    """

    def __init__(self) -> None:

        # 所有关键词统一转为大写比较
        self.rules = {

            "ATB": [
                "ATB TAMEL",
                "TARNÓW",
                "TARNOW",
            ],

            "WORLDWIDE": [
                "WORLDWIDE ELECTRIC",
                "WORLDWIDE ELECTRIC CORP",
                "WORLDWIDE ELECTRIC CORP. LLC",
            ],

            "WOLONG_AMERICA": [
                "WOLONG ELECTRIC AMERICA",
                "WOLONG ELECTRIC AMERICA LLC",
            ],

            "ABB": [
                "ABB",
                "PURCHASE ORDER",
                "SHIP TO",
            ],

            "SIEMENS": [
                "SIEMENS",
                "SIEMENS AG",
            ],

            "SCHNEIDER": [
                "SCHNEIDER",
                "SCHNEIDER ELECTRIC",
            ],

            "GE": [
                "GENERAL ELECTRIC",
                "GE",
            ],
        }

    def detect(self, text: str) -> str:
        """
        Detect customer name using keyword score.
        """

        text_upper = text.upper()

        best_customer = "UNKNOWN"
        best_score = 0

        for customer, keywords in self.rules.items():

            score = 0

            for keyword in keywords:

                if keyword.upper() in text_upper:
                    score += 1

            logger.debug(
                "Customer %s matched %d keyword(s).",
                customer,
                score,
            )

            if score > best_score:
                best_score = score
                best_customer = customer

        if best_score > 0:
            logger.info(
                "Customer detected: %s (score=%d)",
                best_customer,
                best_score,
            )
            return best_customer

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

    samples = [

        "ATB Tamel Purchase Order",

        "WorldWide Electric Corp. LLC Purchase Order",

        "WOLONG ELECTRIC AMERICA LLC Purchase Order",

        "ABB Purchase Order Ship To",

        "Siemens AG Purchase Order",

        "Schneider Electric Purchase Order",

        "General Electric Purchase Order",
    ]

    for sample in samples:

        print(sample)

        print(detector.detect(sample))

        print("-" * 60)