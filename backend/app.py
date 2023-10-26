import asyncio
import os

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import aiohttp

from statistics import mean, median, variance

from backend.utils import get_frequencies, make_frequency_growth_time_histogram

app = FastAPI()
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

# PokeAPI base URL
POKEAPI_BASE_URL = os.getenv("POKEAPI_BASE_URL")


@app.get('/allBerryStats')
async def get_all_berry_stats():
    # List to store berry names and growth times
    berry_names = []
    growth_times = []

    async with aiohttp.ClientSession() as session:
        # Fetch the initial page of berry data
        response = await session.get(f"{POKEAPI_BASE_URL}berry?offset=0&limit=64")
        tasks = []
        if response.status == 200:
            data = await response.json()
            for berry in data['results']:
                print(berry)
                berry_names.append(berry['name'])
                tasks.append(session.get(berry['url']))

        responses = await asyncio.gather(*tasks)
        for resp in responses:
            berry_data = await resp.json()
            if resp.status == 200:
                growth_time = berry_data['growth_time']
                growth_times.append(int(growth_time))

    min_growth_time = min(growth_times)
    median_growth_time = median(growth_times)
    max_growth_time = max(growth_times)
    variance_growth_time = variance(growth_times)
    mean_growth_time = mean(growth_times)
    frequency_growth_time = get_frequencies(growth_times)

    make_frequency_growth_time_histogram(frequency_growth_time)

    return {
        "berries_names": berry_names,
        "min_growth_time": min_growth_time,
        "median_growth_time": median_growth_time,
        "max_growth_time": max_growth_time,
        "variance_growth_time": variance_growth_time,
        "mean_growth_time": mean_growth_time,
        "frequency_growth_time": frequency_growth_time
    }
