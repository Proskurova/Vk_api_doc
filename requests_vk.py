import requests


class RequestsVK:

    def __init__(self, token: str, version: float):
        self.token = token
        self.version = version

    def make_request(self, method: str, params: dict) -> dict:
        params['access_token'] = self.token
        params['v'] = self.version
        response = requests.get('https://api.vk.com/method/' + method, params=params)
        data = response.json()
        return data