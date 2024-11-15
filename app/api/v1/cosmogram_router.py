from fastapi import APIRouter, Depends
from app.services.cosmogram_service import CosmogramService
from app.models.cosmogram import CosmogramRead
from app.models.cosmogram import CosmogramCreate
from app.api.v1.dependencies import get_cosmogram_service

def get_cosmogram_api_router() -> APIRouter: 

    router = APIRouter()

    @router.post("/cosmogram", response_model=CosmogramRead)
    async def create_cosmogram(cosmogram: CosmogramCreate, cosmogram_service: CosmogramService=Depends(get_cosmogram_service)) -> CosmogramRead:
        cosmogram_read = await cosmogram_service.create_cosmogram(cosmogram)
        return cosmogram_read
        
    return router