import json
from http.client import responses

import requests

class CustomRequester:

    base_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    def __init__(self,session,base_url):
        self.session = session
        self.base_url = base_url
        self.headers = self.base_headers.copy()

    def send_request(self, method, endpoint, data=None, params = None,expected_status=(200, 201)):
        url = f"{self.base_url}{endpoint}"
        response = self.session.request(method,url,json=data,params=params)
        if response.status_code not in expected_status:
            raise Exception(f"Мы получили статус код {response.status_code} и тело ответа {response.text}")
        return response

    def update_session_headers(self,session, **kwargs):
        self.headers.update(kwargs)
        session.headers.update(self.headers)


