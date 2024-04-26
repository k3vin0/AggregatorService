from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from aggregatorservice.router.news import app as news_router
from aggregatorservice.router.weather import app as weather_router

app = FastAPI()

# Include routers
app.include_router(news_router, prefix="/news")
app.include_router(weather_router, prefix="/weather")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["X-Custom-Header", "Authorization"],
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "aggregatorservice.__main__:app", host="0.0.0.0", port=5007, reload=True
    )
