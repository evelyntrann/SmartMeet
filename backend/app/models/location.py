from pydantic import BaseModel

class GeocodeRequest(BaseModel):
    address: str

class Coordinates(BaseModel):
    lat: float
    lng: float
