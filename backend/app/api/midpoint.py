from fastapi import APIRouter, HTTPException
from app.services.geocode import geocode_address
from app.services.places import find_places
from app.services.distance import get_travel_time
from app.models.midpoint import MidpointRequest, MidpointResponse
import asyncio

router = APIRouter(prefix="/api", tags=["Midpoint"])

@router.post("/midpoint", response_model=MidpointResponse)
async def get_midpoint(data: MidpointRequest):
    try:
        # 1️⃣ Geocode each participant address
        coords = []
        for user in data.participants:
            lat, lng = await geocode_address(user.address)
            coords.append((lat, lng))

        # 2️⃣ Compute midpoint
        lat = sum(c[0] for c in coords) / len(coords)
        lng = sum(c[1] for c in coords) / len(coords)

        # 3️⃣ Find nearby places
        places = await find_places(lat, lng, data.type)

        # 4️⃣ Compute total travel time for each place (concurrently)
        ranked_places = []
        for p in places:
            # run distance lookups concurrently
            tasks = [get_travel_time(c, (p["lat"], p["lng"]), data.mode) for c in coords]
            travel_times = await asyncio.gather(*tasks)
            total_time = sum(travel_times)
            p["total_time"] = total_time
            ranked_places.append(p)

        # 5️⃣ Sort by total travel time
        ranked_places.sort(key=lambda x: x["total_time"])

        # 6️⃣ Return top results
        return {"midpoint": {"lat": lat, "lng": lng}, "places": ranked_places[:5]}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
