from fastapi import APIRouter
import httpx

router = APIRouter()

@router.get("/{station_id}")
async def air_quality():
    
    r = httpx.get("https://luftdaten.umweltbundesamt.de/api/air-data/v4/stations/json?use=airquality&lang=de")
    print(r.json())
    return r.json()