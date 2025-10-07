from pydantic import BaseModel

class DistanceRequest(BaseModel):
    origin: str
    destination: str 
    mode: str = "driving"

class DistanceResponse(BaseModel):
    distance_text: str
    distance_value_m: int
    duration_text: str
    duration_value_s: int