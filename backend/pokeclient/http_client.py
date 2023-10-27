from typing import Any, Dict

from aiohttp import ClientSession


class HttpClient:
    session: ClientSession

    def __init__(self, session=None) -> None:
        self.session = session if session else ClientSession()

    async def get(self, url: str) -> Dict[str, Any]:
        async with self.session.get(url) as response:
            if response.status == 404:
                raise ValueError(f"{url} was not found")
            return await response.json()

    async def close(self) -> None:
        if self.session is not None:
            await self.session.close()

