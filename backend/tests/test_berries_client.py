from typing import Dict

import pytest

import pokeclient


@pytest.mark.asyncio
async def test_get_berries():
    async with pokeclient.BerriesClient(url="https://pokeapi.co/api/v2/berry") as client:
        berries = await client.get_berries()
        for task in berries:
            assert isinstance(task, Dict)


@pytest.mark.asyncio
async def test_async_context_manager():
    async with pokeclient.BerriesClient(url="https://pokeapi.co/api/v2/berry") as client:
        assert client is not None

    assert client.http.session.closed
