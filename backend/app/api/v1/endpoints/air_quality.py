from fastapi import APIRouter
import httpx
from core.constants import API_BASE_URL

router = APIRouter()

@router.get("/{station_id}")
async def air_quality(station_id):
    
    params = {
        "date_from": "2025-01-01",
        "time_from": 1,
        "date_to": "2026-04-30",
        "time_to": 23,
        "station": station_id,
        "component": 6,
        "scope": 2,

    }
    r = httpx.get(f"{API_BASE_URL}/measures/json", params=params)
    print(r.json())
    return r.json()