from fastapi import APIRouter
from app.models.location import GeocodeRequest, Coordinates
from app.services.google_maps import geocode

router = APIRouter(tags=["Geocode"])

@router.post("/geocode", response_model=Coordinates)
async def geocode_address(req: GeocodeRequest):
    loc = await geocode(req.address)
    return Coordinates(**loc)
