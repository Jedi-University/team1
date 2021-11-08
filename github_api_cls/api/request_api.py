
import requests
import aiohttp
from github_api_cls.consts import HEADERS


class RequestApi:

    @staticmethod
    def get_data_github_api(url):
        return requests.get(url, headers=HEADERS)

    @staticmethod
    async def get_async_data_github_api(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=HEADERS) as response:
                return await response.content.read()
