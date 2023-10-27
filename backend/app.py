import asyncio
import os

from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from statistics import mean, median, variance

from pokeclient.berries_client import BerriesClient
from pokeclient.http_client import HttpClient
from utils import get_frequencies, make_frequency_growth_time_histogram

app = FastAPI()
load_dotenv()

templates = Jinja2Templates(directory="templates")

POKEAPI_BASE_URL = os.getenv("BERRIES_URL")


@app.get('/histogram')
async def get_histogram(request: Request):
    return templates.TemplateResponse("frequencyHistogram.html", {"request": request})


@app.get('/allBerryStats')
async def get_all_berry_stats():
    berry_names = []
    growth_times = []

    async with BerriesClient(url=POKEAPI_BASE_URL) as bclient:
        berries = await bclient.get_berries()
        for berry_data in berries:
            berry_names.append(berry_data['name'])
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


folder = os.path.dirname(__file__)
app.mount("/", StaticFiles(directory=folder + "/static"), name="static")
