
import requests
from github_api_cls.consts import HEADERS


class RequestApi:

    @staticmethod
    def get_data_github_api(url) -> list:
        return requests.get(url, headers=HEADERS).json()

