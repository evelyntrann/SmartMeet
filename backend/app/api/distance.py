from fastapi import APIRouter, HTTPException
from app.models.distance import DistanceRequest, DistanceResponse
from app.services.google_maps import distance_matrix

router = APIRouter(tags=["Distance Matrix"])

@router.post("/distance", response_model=DistanceResponse)
async def get_distance(req: DistanceRequest):
    try:
        result = await distance_matrix(req.origin, req.destination, req.mode)
        return DistanceResponse(**result)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))