from fastapi import FastAPI
import logging
from api.v1.endpoints import air_quality

app = FastAPI()

app.include_router(air_quality.router, prefix = "/air-quality")

@app.get("/")
async def root():
    return {"text": "Hello world"}