"""
"""
from typing import List, Dict

import time
import random
import requests
from requests_middleware.base import Base


class SmartRequests(Base):
    SLEEP_TIME = 30

    def __init__(self, proxies: List[Dict[str, str]], use_proxy: bool) -> None:
        super().__init__(proxies=proxies)
        self.use_proxy = use_proxy
    
    def get(self, url: str, cookies: Dict[str, str]= {}, params: Dict[str, str]= {}, headers: Dict[str, str] = {}, timeout: int = 15, verify: bool = True) -> requests.Response:
        proxy = random.choice(self.proxies)
        try:
            response = requests.get(
                url=url, 
                headers=headers,
                params=params,
                cookies=cookies,
                timeout=timeout,
                verify=verify, 
                proxy=proxy,
            )
            return response
        except Exception as e:
            self.proxy_management[proxy] = time.time()
            raise e