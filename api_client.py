import requests

class BaseApiClient:
    def __init__(self, url: str):
        self.url = url
        self.session = requests.Session()

    def _request(self, method: str, path: str, **kwargs):
        url = f"{self.url}{path}"
        response = self.session.request(method, url, **kwargs)
        return response

    def get(self, path: str, params: dict = None):
        return self._request("GET", path, params=params)

    def post(self, path: str, body: dict):
        return self._request("POST", path, json=body)

    def put(self, path: str, body: dict):
        return self._request("PUT", path, json=body)

    def delete(self, path: str):
        return self._request("DELETE", path)

