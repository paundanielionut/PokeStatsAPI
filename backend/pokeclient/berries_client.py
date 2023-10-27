import asyncio
from typing import Any, Dict

from pokeclient.http_client import HttpClient


class BerriesClient:
    http: HttpClient
    url: str

    def __init__(self, url: str, session=None) -> None:
        self.http = HttpClient(session=session)
        self.url = url

    async def get_berries(self) -> Dict[str, Any]:
        data = await self.http.get(url=self.url)
        tasks = []
        while data['next']:
            for berry in data['results']:
                tasks.append(self.http.get(url=berry['url']))
            data = await self.http.get(url=data['next'])

        berries = await asyncio.gather(*tasks)
        return berries

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.http.close()

    async def __anext__(self):
        return self

