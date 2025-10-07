from fastapi import FastAPI
from app.api import geocode, distance, places, midpoint

app = FastAPI(title="SmartMeet Backend")

app.include_router(geocode.router, prefix="/api")
app.include_router(distance.router, prefix="/api")
app.include_router(places.router, prefix="/api")
app.include_router(midpoint.router, prefix="/api")
