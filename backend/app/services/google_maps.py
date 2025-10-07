import httpx
from app.core.config import settings

GEOCODE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
DM_URL = "https://maps.googleapis.com/maps/api/distancematrix/json"

async def geocode(address: str):
    params = {"address": address, "key": settings.GOOGLE_API_KEY}
    async with httpx.AsyncClient(timeout=10) as client:
        res = await client.get(GEOCODE_URL, params=params)
    data = res.json()
    if data["status"] != "OK":
        raise ValueError(f"Geocoding failed: {data['status']}")
    return data["results"][0]["geometry"]["location"]

async def distance_matrix(origin: str, destination: str, mode: str):
    DM_URL = "https://maps.googleapis.com/maps/api/distancematrix/json"
    params={
        "origin": origin,
        "destination": destination,
        "mode": mode,
        "key": settings.GOOGLE_API_KEY
    }
    if mode == "driving":
        params["departure_time"] = "now"
    
    async with httpx.AsyncClient(timeout=10) as client:
        r = await client.get(DM_URL, params=params)
    data = r.json() #return as json

    if data["status"] != "OK":
        raise ValueError(f"Distance matrix request failed: {data.get('status')}")
    
    element = data["rows"][0]["elements"][0]
    if element["status"] != "OK":
        raise ValueError(f"Distance matrix element error: {element.get('status')}")
    
    return {
        "distance_text": element["distance"]["text"],
        "distance_value_m": element["distance"]["value"],
        "duration_text": element["duration"]["text"],
        "duration_value_s": element["duration"]["value"]
    }

async def nearby_places(lat: float, lng: float, type: str = "cafe", radius: int = 5000):
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": f"{lat},{lng}",
        "radius": radius,
        "type": type,
        "key": settings.GOOGLE_API_KEY
    }
    async with httpx.AsyncClient(timeout=10) as client:
        res = await client.get(url, params=params)
    data = res.json()

    if data["status"] != "OK":  
        raise ValueError(f"Places request failed: {data.get('status')}")
    
    places = []
    for p in data.get("results", []):
        places.apeend({
            "name": p.get("name"),
            "address": p.get("vicinity"),
            "rating": p.get("rating"),
            "location": p.get("geometry", {}).get("location"),
            "open_now": p.get("opening_hours", {}).get("open_now")
        })
    return places