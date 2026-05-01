import httpx
from core.constants import API_BASE_URL

data = None

async def load_stations():
    global data
    r = httpx.get(f"{API_BASE_URL}/stations/json?use=airquality&lang=de")
    data = r.json()



def get_data():
    return data