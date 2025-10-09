import httpx
import os
from app.services.cache import get_cache, set_cache

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
BASE_URL = "https://maps.googleapis.com/maps/api"

# 1️⃣ Geocode API
async def geocode(address: str):
    cache_key = f"geo:{address}"
    cached = await get_cache(cache_key)
    if cached:
        return cached

    async with httpx.AsyncClient() as client:
        res = await client.get(f"{BASE_URL}/geocode/json", params={"address": address, "key": GOOGLE_API_KEY})
        data = res.json()
        if data.get("status") != "OK":
            raise ValueError(f"Geocode failed: {data.get('status')}")

        loc = data["results"][0]["geometry"]["location"]
        await set_cache(cache_key, loc, ttl=86400)  # 1 day cache
        return loc


# 2️⃣ Distance Matrix API
async def distance_matrix(origin: str, destination: str, mode: str = "driving"):
    cache_key = f"dist:{origin}->{destination}:{mode}"
    cached = await get_cache(cache_key)
    if cached:
        return cached

    async with httpx.AsyncClient() as client:
        res = await client.get(f"{BASE_URL}/distancematrix/json", params={
            "origins": origin,
            "destinations": destination,
            "mode": mode,
            "key": GOOGLE_API_KEY
        })
        data = res.json()
        if data.get("status") != "OK":
            raise ValueError(f"Distance matrix failed: {data.get('status')}")

        element = data["rows"][0]["elements"][0]
        result = {
            "origin": origin,
            "destination": destination,
            "distance_text": element["distance"]["text"],
            "distance_value": element["distance"]["value"],
            "duration_text": element["duration"]["text"],
            "duration_value": element["duration"]["value"],
        }

        await set_cache(cache_key, result, ttl=3600)  # 1 hour cache
        return result


# 3️⃣ Places API
async def nearby_places(lat: float, lng: float, place_type: str = "cafe", radius: int = 3000):
    cache_key = f"places:{lat},{lng}:{place_type}:{radius}"
    cached = await get_cache(cache_key)
    if cached:
        return cached

    async with httpx.AsyncClient() as client:
        res = await client.get(f"{BASE_URL}/place/nearbysearch/json", params={
            "location": f"{lat},{lng}",
            "radius": radius,
            "type": place_type,
            "key": GOOGLE_API_KEY
        })
        data = res.json()
        if data.get("status") != "OK":
            raise ValueError(f"Places request failed: {data.get('status')}")

        results = [
            {
                "name": p["name"],
                "address": p.get("vicinity"),
                "rating": p.get("rating"),
                "lat": p["geometry"]["location"]["lat"],
                "lng": p["geometry"]["location"]["lng"]
            }
            for p in data["results"]
        ]

        await set_cache(cache_key, results, ttl=1800)  # 30 min cache
        return result