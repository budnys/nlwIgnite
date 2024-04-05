from typing import Dict

class HttpRequest:
    def __init__(self, body: Dict = None, query_params: Dict = None) -> None:
        self.body = body
        self.q_params = query_params