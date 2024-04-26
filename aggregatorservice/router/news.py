from http.client import HTTPException
from fastapi import APIRouter
from dotenv import load_dotenv
import httpx
import os

from aggregatorservice.models.types.types import NewsCategories

load_dotenv()

app = APIRouter()

api_key = os.getenv("NEWS_API_KEY")
top_headline_url = os.getenv("TOP_HEADLINE_URL")


@app.get("/business")
async def get_business_news():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                top_headline_url,
                params={
                    "country": "us",
                    "category": NewsCategories.BUSINESS.value,
                    "apiKey": api_key,
                },
            )
            articles = response.json().get("articles", [])
        return articles
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code)


@app.get("/sports")
async def get_sports_news():
    async with httpx.AsyncClient() as client:
        response = await client.get(
            top_headline_url,
            params={
                "country": "us",
                "category": NewsCategories.SPORTS.value,
                "apiKey": api_key,
            },
        )
        articles = response.json().get("articles", [])
    return articles


@app.get("/technology")
async def get_technology_news():
    async with httpx.AsyncClient() as client:
        response = await client.get(
            top_headline_url,
            params={
                "country": "us",
                "category": NewsCategories.TECHNOLOGY.value,
                "apiKey": api_key,
            },
        )
        articles = response.json().get("articles", [])
    return articles
