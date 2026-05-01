from fastapi import FastAPI
import logging
from api.v1.endpoints import air_quality
from services import stations_service
app = FastAPI()

app.include_router(air_quality.router, prefix = "/air-quality")

@app.on_event("startup")
async def on_startup():
    await stations_service.load_stations()
