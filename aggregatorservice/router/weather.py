from http.client import HTTPException
from fastapi import APIRouter
from dotenv import load_dotenv
import httpx
import os

load_dotenv()

app = APIRouter()

api_key = os.getenv("WEATHER_API_KEY")
weather_base_url = os.getenv("WEATHER_BASE_URL_DAILY")


@app.get("/local")
async def get_local_weather(lat: float, lon: float):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                weather_base_url,
                params={
                    "lat": lat,
                    "lon": lon,
                    "appid": api_key,
                },
            )
            data = response.json()
            return data  # You might want to parse this data further depending on your needs
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
