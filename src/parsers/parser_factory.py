from .atb_parser import ATBParser
from .worldwide_parser import WorldWideParser
from .wolong_america_parser import WolongAmericaParser


class ParserFactory:

    @staticmethod
    def create(customer: str):

        customer = customer.upper()

        parsers = {
            "ATB": ATBParser,
            "WORLDWIDE": WorldWideParser,
            "WOLONG_AMERICA": WolongAmericaParser,
        }

        parser = parsers.get(customer)

        if parser is None:
            raise ValueError(f"No parser for customer: {customer}")

        return parser()