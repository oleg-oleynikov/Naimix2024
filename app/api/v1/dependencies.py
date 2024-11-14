from fastapi import APIRouter, Depends
from app.services.cosmogram_service import CosmogramService
from app.repositories.cosmogram_repo import CosmogramRepository
from app.models.cosmogram import CosmogramRead
from datetime import datetime

def get_cosmogram_api_router() -> APIRouter: 

    router = APIRouter()

    @router.post("/cosmogram", response_model=CosmogramRead)
    async def create_cosmogram():
        return 
        
    return router

def get_cosmogram_service() -> CosmogramService:
    cosmogramRepo = CosmogramRepository()
    cosmogramService = CosmogramService(cosmogramRepo)
    return cosmogramService