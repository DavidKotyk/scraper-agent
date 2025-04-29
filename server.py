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
    Fetch events near the specified city. All returned items include
    placeholder values ('NA') for missing fields (url, date, description).
    """
    try:
        data = await gather_data(city)
    except Exception:
        # On errors, return empty list
        return []
    # Ensure each item has all expected keys
    for item in data:
        item.setdefault('url', 'NA')
        item.setdefault('date', 'NA')
        item.setdefault('description', 'NA')
    return data

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)