from .atb_parser import ATBParser


class ParserFactory:

    @staticmethod
    def create(customer: str):

        customer = customer.upper()

        if customer == "ATB":
            return ATBParser()

        raise ValueError(
            f"No parser for {customer}"
        )