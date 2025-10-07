from pydantic import BaseModel
from typing import List, Optional

class PlaceRequest(BaseModel):
    lat: float
    lng: float
    type: Optional[str] = "cafe"
    radius: int = 5000

class PlaceInfo(BaseModel):
    name: str
    address: Optional[str]
    rating: Optional[float]
    location: dict
    open_now: Optional[bool] = None

class PlacesResponse(BaseModel):
    places: List[PlaceInfo]