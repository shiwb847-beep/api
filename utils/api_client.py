# api_client.py
import requests

from utils.http_logger import log_http_request


class APIClient:
    def __init__(self, base_url=""):
        self.base_url = base_url
        self.session = requests.Session()

    @log_http_request
    def get(self, url, **kwargs):
        """GET请求"""
        full_url = f"{self.base_url}{url}" if self.base_url else url
        return self.session.get(full_url, **kwargs)

    @log_http_request
    def post(self, url, **kwargs):
        """POST请求"""
        full_url = f"{self.base_url}{url}" if self.base_url else url
        return self.session.post(full_url, **kwargs)

    @log_http_request
    def put(self, url, **kwargs):
        """PUT请求"""
        full_url = f"{self.base_url}{url}" if self.base_url else url
        return self.session.put(full_url, **kwargs)

    @log_http_request
    def delete(self, url, **kwargs):
        """DELETE请求"""
        full_url = f"{self.base_url}{url}" if self.base_url else url
        return self.session.delete(full_url, **kwargs)
