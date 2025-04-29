from fastapi import FastAPI, HTTPException
import uvicorn

from scraper_agent import gather_data

app = FastAPI(
    title="LetsLinkLite Scraper API",
    description="API endpoint to fetch local events and venues",
)

@app.get("/events", summary="Get events for a city")
@app.get("/events/", summary="Get events for a city")
async def get_events(city: str):
    """
    Fetch events near the specified city.
    """
    try:
        data = await gather_data(city)
        # If scraping yields no events, return sample fallback data near SF
        if not data:
            return [
                {"source": "sample", "name": "Sample SF Park Tour", "url": "", "date": "2025-05-01", "lat": "37.7694", "lon": "-122.4862"},
                {"source": "sample", "name": "SF Food Festival",   "url": "", "date": "2025-05-03", "lat": "37.7894", "lon": "-122.4104"},
                {"source": "sample", "name": "Golden Gate Meetup","url": "", "date": "2025-05-05", "lat": "37.8078", "lon": "-122.4750"},
            ]
        return data
    except Exception:
        # On errors, return the same sample fallback data
        return [
            {"source": "sample", "name": "Sample SF Park Tour", "url": "", "date": "2025-05-01", "lat": "37.7694", "lon": "-122.4862"},
            {"source": "sample", "name": "SF Food Festival",   "url": "", "date": "2025-05-03", "lat": "37.7894", "lon": "-122.4104"},
            {"source": "sample", "name": "Golden Gate Meetup","url": "", "date": "2025-05-05", "lat": "37.8078", "lon": "-122.4750"},
        ]

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)