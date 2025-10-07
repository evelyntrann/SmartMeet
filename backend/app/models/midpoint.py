from pydantic import BaseModel
from typing import List, Optional

class Participant(BaseModel):
    name: str
    address: str

class MidpointRequest(BaseModel):
    participants: List[Participant]
    type: str = "cafe"
    mode: str = "driving"

class Place(BaseModel):
    name: str
    address: str
    rating: Optional[float]
    lat: float
    lng: float
    total_time: Optional[float]

class MidpointResponse(BaseModel):
    midpoint: dict
    places: List[Place]
