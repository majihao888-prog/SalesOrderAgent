"""
WorldWide Electric Parser

目前采用ATB模板，
后续只需要修改正则即可。
"""

from __future__ import annotations

from .atb_parser import ATBParser


class WorldWideParser(ATBParser):

    def parse(self, text):

        order = super().parse(text)

        order.customer = "WORLDWIDE"

        return order