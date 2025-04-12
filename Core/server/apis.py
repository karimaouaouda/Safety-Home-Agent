import abc
import json
from abc import ABC

import requests


def to_json(data: dict):
    return json.dumps(data)


class BaseApi(metaclass=abc.ABCMeta):
    def __init__(self, api_base_url, api_prefix = "/api"):
        self.api_base_url:str = api_base_url
        self.api_url:str = self.api_base_url.strip("/") + '/' + api_prefix.strip("/")


    def post(self, data: dict) -> dict:
        response = requests.post(self.api_base_url, data=data)
        return response.json()

    def get(self, query: dict) -> dict:
        response = requests.get(self.api_base_url, query)
        return response.json()


    def after_response(self):
        pass


class FetchApi(BaseApi):
    def __init__(self, api_base_url='https://www.example.com', api_prefix = "/api"):
        super().__init__(api_base_url, api_prefix)


class NotificationApi(BaseApi):
    def __init__(self, api_base_url='https://www.example.com', api_prefix="/api"):
        super().__init__(api_base_url, api_prefix)

