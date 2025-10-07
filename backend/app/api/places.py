from fastapi import APIRouter, HTTPException
from app.models.places import PlaceRequest, PlacesResponse, PlaceInfo
from app.services.google_maps import nearby_places

router = APIRouter(tags=["Places"])

@router.post("/places", response_model=PlacesResponse)
async def get_nearby_places(req: PlaceRequest):
    try:
        places_data = await nearby_places(req.lat, req.lng, req.type, req.radius)
        places = [PlaceInfo(**p) for p in places_data]
        return PlacesResponse(places=places)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
