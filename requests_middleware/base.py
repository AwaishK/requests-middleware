"""
"""
from typing import List


class Base:
    def __init__(self, proxies: List) -> None:
        self.proxies = proxies
        self.proxy_management = {}
